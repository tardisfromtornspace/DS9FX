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
pName = MissionIDs.TW4
sName = "Payback"
sObjectives = "-Return to the Trivas system\n-Intercept the next weapons shipment and take the Romulan commander into custody"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission4"
sProgress = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\TrueWay\\Save\\MissionState.py"
pShipType = None
dEnemies = {}


def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 70722.4\n\nCaptain " + str(
        pPlayerName) + ",\nGiven the factonalized nature of the Romulan Empire since the destruction of their homeworld six years ago it is difficult to assign accountability to the Empire for providing these weapons to the True Way. Our only option is to return to Empok Nor and arrest the provider of the next shipment. I'm sure another one will be sent shortly considering that the True Way did not receive this one. The USS McKinley and the USS Thunderchild will accompany you in case something goes wrong. Good luck Captain!"
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)


def MissionInitiate():
    global pShipType, dEnemies
    dEnemies = {"Warbird 1": "Warbird",
                "Warbird 2": "Warbird",
                "Warbird 3": "Warbird",
                "Keldon 1": "Keldon",
                "Keldon 2": "Keldon",
                "Keldon 3": "Keldon",
                "Keldon 4": "Keldon",
                "Keldon 5": "Keldon"}

    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    SetupPlayer()
    SetupShips()

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


def SetupShips():
    lFriendlies = ["USS McKinley", "USS Thunderchild"]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI
    for s in lFriendlies:
        sShip = s
        if sShip == lFriendlies[0]:
            pShip = loadspacehelper.CreateShip(DS9FXShips.Sovereign, pSet, sShip, "FriendlyPos1")
        else:
            pShip = loadspacehelper.CreateShip(DS9FXShips.Akira, pSet, sShip, "FriendlyPos1")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet)
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(500, 100)
        adY = GetRandomNumber(500, 100)
        adZ = GetRandomNumber(500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()


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
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        SetupSet()
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons",
                               App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetupSet():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    ShowMessage(
        "It's a trap! They were expecting us!\nWe cannot allow the Cardassians to escape with this weapons shipment!")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                      __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                      __name__ + ".ObjectExploding")
    CreateEmpokNor()
    CreateEnemies()


def ShowMessage(s, i=12):
    sText = s
    iPos = 6
    iFont = 12
    iDur = i
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)


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


def CreateEnemies():
    global dEnemies
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
    for k, v in dEnemies.items():
        sShip = k
        if v == "Warbird":
            pShip = loadspacehelper.CreateShip(DS9FXShips.Warbird, pSet, sShip, "Dummy Location")
        else:
            pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetEnemyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet)
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
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


def ObjectExploding(pObject, pEvent):
    global dEnemies
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return
    if (pShip.GetName() == "Empok Nor"):
        Failed()

    if (dEnemies.has_key(pShip.GetName())):
        del dEnemies[pShip.GetName()]

    if (len(dEnemies) == 0):
        ShowMessage("All enemy ships have been destroyed. We should get in range of Empok Nor to scan it")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pCheck = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 120, pPlayer.GetName(),
                                            "Empok Nor")
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbit", pCheck)
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                   __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                   __name__ + ".ObjectExploding")

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def InOrbit(bInOrbit):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
    ShowMessage(
        "I'm scanning Empok Nor. I'm not detecting anything. There is nothing in the enemy wreckage either. I don't think the shipment arrived here.\n\nWe should return to DS9 for further instructions.",
        20)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")


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
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                   __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                   __name__ + ".ObjectExploding")
    except:
        pass

    DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
    DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)


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
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveShips",
                               App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InScanningRange")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                       __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                       __name__ + ".ObjectExploding")
        except:
            pass

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def RemoveShips(pObject, pEvent):
    lFriendlies = ["USS McKinley", "USS Thunderchild"]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    for s in lFriendlies:
        try:
            pSet.DeleteObjectFromSet(s)
        except:
            pass


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
    id = 5
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
    ships = ["USS McKinley", "USS Thunderchild", "Empok Nor", "Warbird 1", "Warbird 2", "Warbird 3", "Keldon 1",
             "Keldon 2", "Keldon 3", "Keldon 4", "Keldon 5"]

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
