# If you lose the original ship, the mission is over

# by Sov

import App
import MissionLib
from Custom.DS9FX.DS9FXMissions import MissionModulePaths

sMission = ""

def MissionName(pObject, pEvent):
    global sMission

    try:
        s = pEvent.GetCString()
    except:
        return

    sMission = s

def ResetMission():
    global sMission
    sMission = ""

def MissionFailureCheck(pObject, pEvent):
    global sMission

    if sMission == "":
        return

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        return
            
    sPath = MissionModulePaths.GetMissionModulePath(sMission)
    if (sPath != None):
        try:
            pModule = __import__(sPath)
            pModule.CrewLost()
        except:
            print 'DS9FX: Failed to reset crew after a mission failure. Please report this error to BCS-TNG.'
            