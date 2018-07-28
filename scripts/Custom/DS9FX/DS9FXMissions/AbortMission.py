# Allows abort mission
# I wish that few things I wrote better in the past but... ah well... no sense in refactoring a mod for an old and dead game :(

import MissionModulePaths
from Custom.DS9FX.DS9FXLifeSupport import HandleMissions


def Abort():
    mission_id = HandleMissions.sMission
    if mission_id != "":
        mission_path = MissionModulePaths.GetMissionModulePath(mission_id)
        if (mission_path != None):
            try:
                mission_module = __import__(mission_path)
                mission_module.CrewLost()
                return 1
            except:
                print 'DS9FX: Failed to abort mission, reasons unknown!'
    return 0
