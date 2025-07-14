import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid, Odometry
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header

import numpy
from collections import deque

node_name = 'robot_map'
map_frame_id = 'map'
map_topic_name = 'robot_2d_map'
odom_topic_name = 'odom_output'
point_cloud_topic_name = 'processed_pointcloud'
map_publish_interval = 1 / 10
queue_size = 200

# m
map_size = 10
resolution = 0.01


angular_speed_limit = numpy.pi / 2

map_queue_size = 10

map_cleaning_interval = 1 / 5
marp_marking_interval = 1 / 2

intensity_sensitivity = 1000
intensity_max = 1000

marker_threshold = 500

cleaning_factor_1 = 0.8
marker_factor_1 = 1.5

map_count = int(map_size / resolution)
class robot_map(Node):
    def __init__(self):
        super().__init__(node_name)
        
        self.grid_count = map_count
        self.resolution = resolution  
        self.origin = int(self.grid_count / 2)

        self.generating_output = False
        
        self.occupancy_grid = OccupancyGrid()
        self.recent_odom = Odometry() 

        # Initialize the map
        map_data = numpy.zeros((self.grid_count, self.grid_count))
        self.sum_map = map_data

        self.odom_subscribtion = self.create_subscription(
            Odometry,
            odom_topic_name,
            self.handle_odom,
            queue_size
        )

        self.odom_subscribtion = self.create_subscription(
            PointCloud2,
            point_cloud_topic_name,
            self.draw_map,
            queue_size
        )
        
        # Publisher for the map
        self.map_publisher = self.create_publisher(
            OccupancyGrid,
            map_topic_name,
            queue_size
        )

        # Timer to publish the map at a regular interval
        self.map_publish_timer = self.create_timer(
            map_publish_interval, 
            self.publish_map
        )

        self.cleaner_timer = self.create_timer(
            map_cleaning_interval,
            self.clean_map
        )

        # self.marker_timer = self.create_timer(
        #     marp_marking_interval,
        #     self.mark_map
        # )


    def handle_odom(self, msg: Odometry):
        self.recent_odom = msg


    def draw_map(self, msg: PointCloud2):
        # self.clean_map()
        if True:
            next_map  = numpy.zeros((map_count, map_count)) 

            # Get the 3D points from the PointCloud2 message
            points = list(point_cloud2.read_points(msg, field_names=['x','y','z', 'intensity'], skip_nans=True))
            # Loop over all points
            for point in points:
                x, y, z, v= point
                # Convert from world coordinates to grid coordinates
                if -map_count / 2 < x < map_count / 2 and -map_count / 2 < y < map_count / 2:
                    grid_x = int(x / resolution) + self.origin 
                    grid_y = int(y / resolution) + self.origin
                    next_map[grid_y, grid_x] = min(int(100 * v) * intensity_sensitivity, 100)  # 100 = Occupied cell 
            
            # print(numpy.sum(self.sum_map[self.origin - 10:self.origin + 10, self.origin - 10:self.origin + 10]))
            self.sum_map += next_map
            self.sum_map[self.sum_map < 0] = 0
            self.sum_map[self.sum_map > 1000] = 1000

            # self.sum_map[self.sum_map > 10000] = 10000

            # print(numpy.sum(self.sum_map[self.origin - 10:self.origin + 10, self.origin - 10:self.origin + 10]))

            # print('-----')


    def clean_map(self):
        self.sum_map *= cleaning_factor_1
        self.mark_map()

    def mark_map(self):
        self.sum_map[self.sum_map > marker_threshold] *= marker_factor_1

    def __generate_output_map(self)-> numpy.ndarray: 
        # print(self.sum_map.max())
        output_map = numpy.zeros((self.grid_count, self.grid_count))

        max_value = self.sum_map.max()
        if max_value > 0:
            output_map = self.sum_map / max_value * 100
        return output_map.astype(int)


    def publish_map(self):
        output_map = self.__generate_output_map() 

        # Set the header for the map
        self.occupancy_grid.header = Header()
        self.occupancy_grid.header.stamp = self.get_clock().now().to_msg()
        self.occupancy_grid.header.frame_id = map_frame_id        
        # Set map metadata
        self.occupancy_grid.info.width = self.grid_count
        self.occupancy_grid.info.height = self.grid_count
        self.occupancy_grid.info.resolution = self.resolution
        self.occupancy_grid.info.origin.position.x = - map_size / 2
        self.occupancy_grid.info.origin.position.y = - map_size / 2
        self.occupancy_grid.info.origin.position.z = 0.0
        self.occupancy_grid.info.origin.orientation.x = 0.0
        self.occupancy_grid.info.origin.orientation.y = 0.0
        self.occupancy_grid.info.origin.orientation.z = 0.0
        self.occupancy_grid.info.origin.orientation.w = 1.0

        # Flatten the 2D array into a 1D array for the OccupancyGrid message
        self.occupancy_grid.data = output_map.flatten().tolist()

        # Publish the map
        self.map_publisher.publish(self.occupancy_grid)
        # self.get_logger().info('Publishing map')

def main(args=None):
    rclpy.init(args=args)
    node = robot_map()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
