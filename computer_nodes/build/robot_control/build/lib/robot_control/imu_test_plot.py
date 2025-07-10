import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
from collections import deque
import threading
import sys

class IMULivePlot(Node):
    def __init__(self, topic='/test_plot_imu', buf_size=200):
        super().__init__('imu_live_plot_pyqtgraph')
        self.buf_size = buf_size

        self.ax_buf = deque(maxlen=buf_size)
        self.ay_buf = deque(maxlen=buf_size)
        self.az_buf = deque(maxlen=buf_size)
        self.lock = threading.Lock()

        self.create_subscription(Imu, topic, self.imu_callback, 200)

        # PyQtGraph setup
        self.app = QtWidgets.QApplication(sys.argv)
        self.win = pg.GraphicsLayoutWidget(title="IMU Live Acceleration")
        self.win.resize(800, 500)
        self.plot = self.win.addPlot(title="Linear Acceleration (mm/s²)")
        self.plot.addLegend()
        self.plot.setYRange(-10, 10)
        self.plot.setLabel('bottom', 'Samples (most recent on right)')

        self.curve_x = self.plot.plot(pen=pg.mkPen('r', width=2), name='accel X')
        self.curve_y = self.plot.plot(pen=pg.mkPen('g', width=2), name='accel Y')
        self.curve_z = self.plot.plot(pen=pg.mkPen('b', width=2), name='accel Z')

        # Timer for periodic updates
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(int(1000 / 24))  # 10 Hz update rate

    def imu_callback(self, msg: Imu):
        # with self.lock:
        self.ax_buf.append(msg.angular_velocity.x)
        self.ay_buf.append(msg.angular_velocity.y)
        self.az_buf.append(msg.angular_velocity.z)

    def update_plot(self):
        with self.lock:
            xs = list(range(len(self.ax_buf)))
            self.curve_x.setData(xs, list(self.ax_buf))
            self.curve_y.setData(xs, list(self.ay_buf))
            self.curve_z.setData(xs, list(self.az_buf))

    def run(self):
        self.app.aboutToQuit.connect(self.shutdown_ros)
        self.win.show()
        sys.exit(self.app.exec())

    def shutdown_ros(self):
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = IMULivePlot()

    # Run rclpy spinning in a background thread
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(node)
    thread = threading.Thread(target=executor.spin, daemon=True)
    thread.start()

    # Start PyQtGraph event loop in the main thread
    node.run()

    # No need to shutdown again; already handled
    thread.join()


if __name__ == '__main__':
    main()
