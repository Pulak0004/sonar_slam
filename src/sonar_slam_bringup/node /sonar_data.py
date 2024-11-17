import rospy
from sensor_msgs.msg import Range, LaserScan

def callback(data):
    pub = rospy.Publisher('scan', LaserScan, queue_size=10)
    scan = LaserScan()
    scan.header.stamp = rospy.Time.now()
    scan.header.frame_id = 'sonar_sensor'
    scan.angle_min = -1.57
    scan.angle_max = 1.57
    scan.angle_increment = 3.14 / data.range
    scan.time_increment = 0.1
    scan.range_min = 0.0
    scan.range_max = 10.0
    scan.ranges = [data.range]
    pub.publish(scan)

def listener():
    rospy.init_node('sonar_to_laserscan', anonymous=True)
    rospy.Subscriber("sonar_data", Range, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()