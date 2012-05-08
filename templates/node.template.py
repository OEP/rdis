#!/usr/bin/env python
import roslib; roslib.load_manifest('rdis')
import rospy
import sys
import rdis

from collections import deque

## Imports resolved by rosmake
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist

## RDIS model interpreter.
gModel = None

## Maps topics (string) to ROS publsiher for topic
gPublishers = dict()

## Maps RDIS domain interface name to (topic, generator) tuple
gTopicMap = dict()

## RDIS model callback
def rdisCallback(msg):
  (pub, callback) = getPublisher(msg["name"])
  callback(msg["contents"], pub)

## Named publishers functions
def registerPublisher(name, pub, callback):
  global gPublishers
  gPublishers[name] = (pub, callback)

def getPublisher(name):
  global gPublishers
  return gPublishers[name]

def mapDomainInterface2Topic(interface):
  return 

## AUTO-GENERATED CALLBACKS
{callbackSection}

def main():
  if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " <rdis-file> <serial-port>"
    sys.exit(1)

  print "Starting up RDIS..."
  global gModel
  gModel = rdis.load( sys.argv[1] )
  gModel.setCallback(rdisCallback)
  gModel.startup(port=sys.argv[2])

  ## FIELD FROM NODE NAME IN ROS FORMALISM
  rospy.init_node('{nodeName}', anonymous=True)

  ## AUTO-GENERATED PUBLISH/SUBSCRIBE STATEMENTS.
  ## CREATES LOCAL VARIABLE FOR EACH PUBLISHER.
{initializationSection}

  while not rospy.is_shutdown():
    ## Lets model know a thread tick has passed. Internal
    ## timers will govern whether or not it is time to call
    ## any periodic interfaces.
    gModel.tick()

    ## Sleep for some amount of time calculated from the
    ## connection.
    rospy.sleep(1.0)

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
    global gModel
    gModel.terminate()
    pass
