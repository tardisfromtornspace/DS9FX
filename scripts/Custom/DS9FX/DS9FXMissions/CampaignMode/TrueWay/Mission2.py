# Xtended Mission

# by Sov

import App
import MissionLib
import loadspacehelper
import nt
import string
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict

pPlayerName = ""
pName = MissionIDs.TW2
sName = "On the Border"
sObjectives = "-Patrol the Chin'toka system\n-Patrol the Septimus system\n-Patrol the Trivas system"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission2"
sProgress = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\TrueWay\\Save\\MissionState.py"
pShipType = None
iProgress = 0


def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 70698.4\n\nCaptain " + str(
        pPlayerName) + ",\nGul Madred, the suspected leader of the True Way, has denied any involvement in the hijacking of the Vrenak. Although we find this hard to believe, we do not have enough evidence to prove otherwise. Never the less, we believe it is necessary to make our presence known to the True Way. We want you to patrol Cardassian space and ensure that everything is status quo."
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)


def MissionInitiate():
    global pShipType, iProgress
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)
    iProgress = 0

    SetupPlayer()

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons",
                           App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")


def SetupPlayer():
    from Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Save import MissionState
    reload(MissionState)
    pShip = MissionState.Ship
    pPlayer = MissionLib.GetPlayer()
    pPlayerName = pPlayer.GetName()
    pSet = pPlayer.GetContainingSet()
    pSet.DeleteObjectFromSet(pPlayerName)
    loadspacehelper.CreateShip(pShip, pSet, pPlayerName, "Player Start")
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(pPlayerName)
    pMission.GetFriendlyGroup().AddName(pPlayerName)
    GetPlayer = MissionLib.GetShip(pPlayerName, pSet)
    pGame = App.Game_GetCurrentGame()
    pGame.SetPlayer(GetPlayer)


def DisableDS9FXMenuButtons(pObject, pEvent):
    try:
        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
        bHail.SetDisabled()
    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."


def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat


def PlayerExploding(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if (pShip.GetObjID() == pPlayer.GetObjID()):
        FailedTxt()
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
        except:
            pass

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def FailedTxt():
    sText = "Mission Failed!"
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)


def MissionHandler(pObject, pEvent):
    global iProgress
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if pSet.GetName() == "DS9FXChintoka1":
        iProgress = 1
        HandleMissionDetails()
    elif pSet.GetName() == "DS9FXSeptimus1":
        iProgress = 2
        HandleMissionDetails()
    elif pSet.GetName() == "DS9FXTrivas1":
        iProgress = 3
        HandleMissionDetails()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons",
                               App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def HandleMissionDetails():
    global iProgress
    if iProgress == 1:
        ShowMessage("Scanning system...")
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanOver",
                               App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(40, 35), 0, 0)
    elif iProgress == 2:
        ShowMessage("Scanning system...")
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanOver",
                               App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(35, 35), 0, 0)
    elif iProgress == 3:
        PopulateSystem()
        ShowMessage("Scanning system...")
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanOver",
                               App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(30, 35), 0, 0)


def ShowMessage(s):
    sText = s
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)


def ScanOver(pObj, pEvent):
    global iProgress
    if iProgress == 1:
        ShowMessage("Nothing unusual detected sir.\nI recommend we proceed to our next objective.")
    if iProgress == 2:
        ShowMessage("I'm detecting only routine minning missions.\nI recommend we move on sir.")
    if iProgress == 3:
        ShowMessage("I'm detecting a Galor Class vessel near the Empok Nor...")
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RunAway",
                               App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(20, 30), 0, 0)


def PopulateSystem():
    lShips = ["Galor", "Empok Nor"]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    for s in lShips:
        sShip = s
        if sShip == lShips[len(lShips) - 1]:
            pShip = loadspacehelper.CreateShip(DS9FXShips.MissionStation, pSet, sShip, "Dummy Location")
        else:
            pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1000, 17000)
        adY = GetRandomNumber(1000, 17000)
        adZ = GetRandomNumber(1000, 17000)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveCrew",
                           App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)


def RemoveCrew(pObj, pEvent):
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    pDerelict = MissionLib.GetShip("Empok Nor", pSet)
    if not pDerelict:
        return
    LifeSupport_dict.dCrew[pDerelict.GetObjID()] = 0
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pDerelict)


def RunAway(pObj, pEvent):
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pShip = MissionLib.GetShip("Galor", pSet)
    pShip = App.ShipClass_Cast(pShip)

    from Custom.DS9FX.DS9FXLib import GalaxyCharts
    pInstalled = GalaxyCharts.IsInstalled()

    if pInstalled:
        try:
            # Delete the ship if the AI won't work. No time to do it properly.
            pSet.DeleteObjectFromSet("Galor")
        except:
            pass
    else:
        import Custom.DS9FX.DS9FXAILib.DS9FXFlee
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFlee.CreateAI(pShip))

    ShowMessage(
        "Galor just warped out sir, I cannot track them...\nMaybe we should scan Empok Nor.\nWe need to be in 50 km range first.")

    pCheck = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 120, pPlayer.GetName(),
                                        "Empok Nor")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InScanningRange", pCheck)


def InScanningRange(bInRange):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
    ShowMessage(
        "Nothing unusual on the station, but according to these readings something\nwas beamed off Empok Nor a few minutes ago.\n\nWe should return to DS9 and report this.")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")


def MissionEnd(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if pSet.GetName() == "DeepSpace91":
        CompletedTxt()
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveShips",
                               App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        SaveProgress()
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
        except:
            pass

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def CompletedTxt():
    sText = "Mission Completed!"
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)


def RemoveShips(pObject, pEvent):
    pTrivas = __import__("Systems.DS9FXTrivas.DS9FXTrivas1")
    pTrivas = pTrivas.GetSet()
    try:
        pTrivas.DeleteObjectFromSet("Empok Nor")
    except:
        pass


def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Save import MissionState
    reload(MissionState)
    id = 3
    if MissionState.OnMission > id:
        i = MissionState.OnMission
    else:
        i = id
    file = nt.open(sProgress, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
    nt.write(file, "OnMission = " + str(i) + "\n")
    nt.write(file, "Ship = " + "'" + pShipType + "'")
    nt.close(file)


def CrewLost():
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
        RemoveMissionShips()
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass


def RemoveMissionShips():
    ships = ["Galor", "Empok Nor"]

    player = MissionLib.GetPlayer()
    if not player:
        return 0

    set = player.GetContainingSet()
    if not set:
        return 0

    set_name = set.GetName()
    if not set_name:
        return 0

    for ship in ships:
        try:
            set.DeleteObjectFromSet(ship)
        except:
            pass

    return 1
