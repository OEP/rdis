#!/usr/bin/env python
import roslib; roslib.load_manifest('rdis')
import rospy

## Imports resolved by rosmake
import time
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist

gLastMessage = 0
gHitObject = False

def detected_timeout():
  global gLastMessage
  now = time.time()
  return now - gLastMessage >= 3

## Called every time we receive a range message.
def hitObject_callback(data):
  global gHitObject
  global gLastMessage
  gLastMessage = time.time()
  gHitObject = gHitObject or data.data
  print "Hit something: ", data.data

## Alias for publishing linear/angular velocity
## as a Twist message.
def publish_setSpeed(pub, linear, angular):
  twistMsg = Twist()
  twistMsg.linear.x = linear
  twistMsg.angular.x = angular
  pub.publish(twistMsg)

def main():
  global gHitObject
  rospy.init_node('wander', anonymous=True)

  ## Send out updates to speed
  ## Listen for updates on colliding with objects.
  pub = rospy.Publisher('setSpeed', Twist)
  rospy.Subscriber('hitObject', Bool, hitObject_callback)

  ## Flag for seeing if we've handled the timeout.
  timeout_handled = False

  ## Time which we started backing up.
  backup_time = 0

  while not rospy.is_shutdown():
    now = time.time()

    if detected_timeout():
      if not timeout_handled:
        print "Timeout. Waiting for message."
        publish_setSpeed(pub, 0, 0)
        timeout_handled = True
    elif now - backup_time < 1 or gHitObject:
      if gHitObject:
        backup_time = time.time()
        publish_setSpeed(pub, -0.1, -0.5)
        gHitObject = False
      timeout_handled = False
    else:
      publish_setSpeed(pub, 0.1, 0.0)
      timeout_handled = False

    rospy.sleep(0.1)

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    pass
