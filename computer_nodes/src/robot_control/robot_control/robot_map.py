import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header
import numpy as np

class robot_map(Node):
    def __init__(self):
        super().__init__('map_publisher_node')
        
        # Publisher for the map
        self.map_publisher = self.create_publisher(OccupancyGrid, 'map', 10)

        # Timer to publish the map at a regular interval
        self.timer = self.create_timer(1.0, self.publish_map)

        # Create a simple 10x10 grid map (for demonstration purposes)
        self.grid_size = 10
        self.resolution = 0.1  # 10 cm per cell
        
        # Initialize the map
        self.map_data = np.zeros((self.grid_size, self.grid_size), dtype=int)  # Free map
        self.map_data[3:6, 3:6] = 100  # Add an obstacle in the middle
        
        # Create the OccupancyGrid message
        self.occupancy_grid = OccupancyGrid()

    def publish_map(self):
        # Set the header for the map
        self.occupancy_grid.header = Header()
        self.occupancy_grid.header.stamp = self.get_clock().now().to_msg()
        self.occupancy_grid.header.frame_id = 'map'
        
        # Set map metadata
        self.occupancy_grid.info.width = self.grid_size
        self.occupancy_grid.info.height = self.grid_size
        self.occupancy_grid.info.resolution = self.resolution
        self.occupancy_grid.info.origin.position.x = 0.0
        self.occupancy_grid.info.origin.position.y = 0.0
        self.occupancy_grid.info.origin.position.z = 0.0
        self.occupancy_grid.info.origin.orientation.x = 0.0
        self.occupancy_grid.info.origin.orientation.y = 0.0
        self.occupancy_grid.info.origin.orientation.z = 0.0
        self.occupancy_grid.info.origin.orientation.w = 1.0

        # Flatten the 2D array into a 1D array for the OccupancyGrid message
        self.occupancy_grid.data = self.map_data.flatten().tolist()

        # Publish the map
        self.map_publisher.publish(self.occupancy_grid)
        self.get_logger().info('Publishing map')

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
