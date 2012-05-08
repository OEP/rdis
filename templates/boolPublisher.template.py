## Auto-generated function for publishing ROS Bools.
def publish_{name}(rdisMsg, pub):
  env = dict()
  
  ## Generated initializations from model.
{initialization}

  ## Generated mappings to ROS bool from any domain adapter of RDIS.
{mappingStatements}

  ## Statements above should have initialized env['data']
  pub.publish(Bool( env['data'] ))
