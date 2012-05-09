# _ ros2rdis_GG_exec.py ____________________________________________________________________________
# ros2rdis : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from publishTwist2outputDiffSpeedee_GG_rule import *
from publishBoolean2domainOutputRange_GG_rule import *
from subscribeTwist2interfaceDiffSpeede_GG_rule import *
class ros2rdis_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [publishTwist2outputDiffSpeedee_GG_rule(parent) , publishBoolean2domainOutputRange_GG_rule(parent) , subscribeTwist2interfaceDiffSpeede_GG_rule(parent)])
   def initialAction(self, graph):
      pass

   def finalAction(self, graph):
      pass

importedModules = ['publishTwist2outputDiffSpeedee_GG_rule', 'publishBoolean2domainOutputRange_GG_rule', 'subscribeTwist2interfaceDiffSpeede_GG_rule']

