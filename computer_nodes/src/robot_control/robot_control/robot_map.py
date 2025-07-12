import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid, Odometry
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header
import numpy

node_name = 'robot_map'
map_frame_id = 'map'
map_topic_name = 'robot_2d_map'
odom_topic_name = 'odom_output'
point_cloud_topic_name = 'processed_pointcloud'
map_publish_interval = 1 / 20
queue_size = 200

# m
map_size = 10
resolution = 0.01
intensity_sensitivity = 5

# m/s 
angular_speed_limit = 0

map_count = int(map_size / resolution)
class robot_map(Node):
    def __init__(self):
        super().__init__(node_name)

        self.recent_odom = Odometry() 

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
        self.timer = self.create_timer(
            map_publish_interval, 
            self.publish_map
        )

        # Create a simple 10x10 grid map (for demonstration purposes)
        self.grid_count = map_count
        self.resolution = resolution  # 10 cm per cell
        self.origin = int(self.grid_count / 2)
        
        # Initialize the map
        self.map_data = numpy.zeros((self.grid_count, self.grid_count), dtype=int)  # Free map
        # self.map_data[3:6, 3:6] = 100  # Add an obstacle in the middle
        
        # Create the OccupancyGrid message
        self.occupancy_grid = OccupancyGrid()

        self.map_data[self.origin, self.origin] = 100

    def handle_odom(self, msg: Odometry):
        self.recent_odom = msg

    def draw_map(self, msg: PointCloud2):
        if self.recent_odom.twist.twist.angular.z <= angular_speed_limit: 
            # Get the 3D points from the PointCloud2 message
            points = list(point_cloud2.read_points(msg, field_names=['x','y','z', 'intensity'], skip_nans=True))
            # Loop over all points
            for point in points:
                x, y, z, v= point
                # Convert from world coordinates to grid coordinates
                if -map_count < x < map_count and -map_count < y < map_count:
                    grid_x = int(x / resolution) + self.origin 
                    grid_y = int(y / resolution) + self.origin
                    # print(v)
                    # print(grid_x, grid_y) 
                    self.map_data[grid_y, grid_x] = min(int(100 * v) * intensity_sensitivity, 100)  # 100 = Occupied cell 

    def publish_map(self):
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
        self.occupancy_grid.data = self.map_data.flatten().tolist()

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
