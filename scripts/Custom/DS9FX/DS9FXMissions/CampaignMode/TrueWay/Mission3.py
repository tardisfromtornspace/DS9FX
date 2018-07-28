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
pName = MissionIDs.TW3
sName = "Gunships"
sObjectives = "-Return to the Trivas system\n-Find out what is being transported to Empok Nor by who"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission3"
sProgress = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\TrueWay\\Save\\MissionState.py"
pShipType = None


def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 70708.9\n\nCaptain " + str(
        pPlayerName) + ",\nYour report regarding the transport off of Empok Nor is interesting Captain. The Cardassian's abandoned the Trivas system in 2372 because of lack of strategic value, it's unlikely that they would find a need to re-occupy the station. It's more likely that the True Way is using the station as a pick up point. For what? We don't know, but thats what we want you to find out. Go back to the Trivas system and wait for a ship to transport something to the station. If you orbit the fourth planet with shields and weapons offline, you should be able to avoid detection long enough to figure out who and what is visiting Empok Nor."
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)


def MissionInitiate():
    global pShipType
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

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
    pPlayer = MissionLib.GetPlayer()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if (pShip.GetObjID() == pPlayer.GetObjID()):
        Failed()

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

    if pSet.GetName() == "DS9FXTrivas1":
        SetupSet()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons",
                               App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetupSet():
    ShowMessage(
        "We should enter orbit of Trivas 4. We'll need to keep our shields and weapons offline in order to avoid detection.")
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting",
                                            "Trivas 4")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbit", pCondition)
    CreateEmpokNor()


def CreateEmpokNor():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    sShip = "Empok Nor"
    pShip = loadspacehelper.CreateShip(DS9FXShips.MissionStation, pSet, sShip, "Dummy Location")
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


def ShowMessage(s):
    sText = s
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)


def InOrbit(bInOrbit):
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
    message = "I'm detecting a ship en route to this system."
    if (ProbePlayerPowerSettings()):
        message = message + "\n" + "Sir we haven't powered off weapons and shields!"
    ShowMessage(message)
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".WarbirdEntering",
                           App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(10, 35), 0, 0)


def ProbePlayerPowerSettings():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    lLevels = [pPlayer.GetShields(), pPlayer.GetPhaserSystem(), pPlayer.GetTorpedoSystem(),
               pPlayer.GetPulseWeaponSystem()]
    for pSys in lLevels:
        if pSys:
            if pSys.IsOn():
                return 1
    return 0


def WarbirdEntering(pObject, pEvent):
    if ProbePlayerPowerSettings():
        Failed()
        return 0
    ShowMessage("A Romulan Warbird has just entered the system.\nThey are beaming something to the station.")
    CreateWarbird()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".TransportRelated",
                           App.g_kUtopiaModule.GetGameTime() + GetRandomNumber(10, 35), 0, 0)


def Failed():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    FailedTxt()
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
    except:
        pass

    DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
    DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)


def CreateWarbird():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    sShip = "Empok Nor"
    pShip = MissionLib.GetShip(sShip, pSet)
    if not pShip:
        return
    pLocation = pShip.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pShip = loadspacehelper.CreateShip(DS9FXShips.Warbird, pSet, "Warbird", "Dummy Location")
    DS9FXLifeSupportLib.ClearFromGroup("Warbird")
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(250, 50)
    adY = GetRandomNumber(250, 50)
    adZ = GetRandomNumber(250, 50)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()


def TransportRelated(pObject, pEvent):
    ShowMessage(
        "I'm scanning Empok Nor. I'm detecting plasma torpedoes, phaser batteries, and shield generators. We should confiscate the shipment and report this to DS9!")
    from Custom.DS9FX.DS9FXLib import GalaxyCharts
    pInstalled = GalaxyCharts.IsInstalled()
    pSet = MissionLib.GetPlayer().GetContainingSet()
    pShip = MissionLib.GetShip("Warbird", pSet)
    if pInstalled:
        try:
            # Delete the ship if the AI won't work. No time to do it properly.
            pSet.DeleteObjectFromSet("Warbird")
        except:
            pass
    else:
        import Custom.DS9FX.DS9FXAILib.DS9FXFlee
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFlee.CreateAI(pShip))
    pPlayer = MissionLib.GetPlayer()
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pCheck = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 120, pPlayer.GetName(),
                                        "Empok Nor")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InScanningRange", pCheck)


def InScanningRange(bInRange):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
    ShowMessage("I have the weapons and shield generators in the cargo bays, sir.")
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
        SaveProgress()
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
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


def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Save import MissionState
    reload(MissionState)
    id = 4
    if MissionState.OnMission > id:
        i = MissionState.OnMission
    else:
        i = id
    file = nt.open(sProgress, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
    nt.write(file, "OnMission = " + str(i) + "\n")
    nt.write(file, "Ship = " + "'" + pShipType + "'")
    nt.close(file)


def CrewLost():
    Failed()
    RemoveMissionShips()


def RemoveMissionShips():
    ships = ["Empok Nor", "Warbird"]

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
