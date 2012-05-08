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
## ============ GENERATED SUBSCRIPTION CALLBACKS ==================

## Callback for topic setSpeed
def setSpeed_callback(data):
  global gModel

  ## Flatten into tuples
  angular = (data.angular.x, data.angular.y, data.angular.z)
  linear = (data.linear.x, data.linear.y, data.linear.z)

  env = dict()
  env["angular"] = angular
  env["linear"] = linear

  env['angular'] = rdis.safeEval('<angular[0]>', env)
  env['linear'] = rdis.safeEval('<linear[0]>', env)
  
  gModel.callDomainInterface('set_velocity', env)
## ================= GENERATED PUBLISH ACTIONS ==================

## Auto-generated function for publishing ROS Bools.
def publish_hitObject(rdisMsg, pub):
  env = dict()

  ## Generated initializations from model.
  env['distance'] = rdisMsg['distance']

  ## Generated mappings to ROS bool from any domain adapter of RDIS.
  env['data'] = rdis.safeEval('<distance == 0>', env)

  ## Statements above should have initialized env['data']
  pub.publish(Bool( env['data'] ))


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
  rospy.init_node('rdisWanderer', anonymous=True)

  ## AUTO-GENERATED PUBLISH/SUBSCRIBE STATEMENTS.
  ## CREATES LOCAL VARIABLE FOR EACH PUBLISHER.
  rospy.Subscriber('setSpeed',Twist,setSpeed_callback)
  registerPublisher('detect_bump', rospy.Publisher('hitObject', Bool), publish_hitObject)

  while not rospy.is_shutdown():
    ## Lets model know a thread tick has passed. Internal
    ## timers will govern whether or not it is time to call
    ## any periodic interfaces.
    gModel.tick()

    ## Sleep for some amount of time calculated from the
    ## connection.
    rospy.sleep(1.0 / 40.0)

  print "Shutting down."
  gModel.terminate()
  sys.exit(0)

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException as e:
    global gModel
    print "Termination signal received: " + str(e)
    gModel.terminate()
    sys.exit(1)
