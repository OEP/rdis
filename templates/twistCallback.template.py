## Callback for topic {name}
def {name}_callback(data):
  global gModel

  ## Flatten into tuples
  angular = (data.angular.x, data.angular.y, data.angular.z)
  linear = (data.linear.x, data.linear.y, data.linear.z)

  env = dict()
  env["angular"] = angular
  env["linear"] = linear

{toRdis}
  
  gModel.callDomainInterface('{domainInterface}', env)
