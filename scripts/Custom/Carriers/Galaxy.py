#####  Created by:
#####  Bridge Commander Universal Tool


Carrier = __import__('ftb.Carrier')
class Galaxy(Carrier.Carrier):
   def __init__(self, pShip):
               Carrier.Carrier.__init__(self, pShip)
               LauncherGroup = __import__('ftb.LauncherGroup')


               group = LauncherGroup.LauncherGroup()
               LauncherManager = __import__('ftb.LauncherManager')


               launcher1 = LauncherManager.GetLauncher('Shuttle Bay 1', pShip)
               group.AddLauncher('Shuttle Bay 1', launcher1)


               launcher2 = LauncherManager.GetLauncher('Shuttle Bay 2', pShip)
               group.AddLauncher('Shuttle Bay 2', launcher2)


               launcher3 = LauncherManager.GetLauncher('Shuttle Bay 3', pShip)
               group.AddLauncher('Shuttle Bay 3', launcher3)


               launcher1.AddLaunchable('DS9FXDanubemkI', 'ftb.friendlyAI', 3)


               launcher2.AddLaunchable('Shuttle', 'ftb.friendlyAI', 4)


               launcher3.AddLaunchable('Shuttle', 'ftb.friendlyAI', 4)


               self.AddLauncher('Group 1', group)


   def GetMaxShuttles(self):
               return 11


ShipManager = __import__('ftb.ShipManager')
ShipManager.RegisterShipClass('Galaxy', Galaxy)
