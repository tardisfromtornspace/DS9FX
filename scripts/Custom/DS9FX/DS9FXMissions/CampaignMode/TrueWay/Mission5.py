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
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

pPlayerName = ""
pName = MissionIDs.TW5
sName = "The Battle of Septimus"
sObjectives = "-Go to the Septimus system\n-Destroy Gul Madred's fleet"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission5"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\TrueWay\\Save\\MissionState.py"
pShipType = None
dEnemies = {}

def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 70752.9\n\nCaptain " + str(pPlayerName) + ",\nStarfleet Intelligence has learned that the last weapons shipment was delivered directly to the Septimus system. In addition to the Jem'Hadar security detail Gul Madred has hired to protect his mining operations, we believe there are several Keldon and Galor-class warships in the system preparing to overthrow the Detapa Council and restore military rule to the Cardassian Union. Captain, it is up to you to see that this does not happen! If the Central Command is restored to power, Cardassia Prime may never recover from its Dominion War losses and the Federation will be drawn to the brink of war, something we cannot afford given the situation with the Klingon Empire. You are to take a task force to the Septimus system and eliminate Gul Madred's invasion fleet. Gods speed Captain!"
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def MissionInitiate():
    global pShipType, dEnemies
    dEnemies = {"Keldon 1" : "Keldon", 
                "Keldon 2" : "Keldon", 
                "Keldon 3" : "Keldon", 
                "Keldon 4" : "Keldon",
                "Fighter 1" : "Fighter",
                "Fighter 2" : "Fighter",
                "Fighter 3" : "Fighter",
                "Fighter 4" : "Fighter",
                "Fighter 5" : "Fighter"}
    
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    SetupPlayer()
    SetupShips()

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
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
    SetupFriendlyShips("USS Kennedy", DS9FXShips.Galaxy)
    SetupFriendlyShips("USS Venice", DS9FXShips.Akira)
    SetupFriendlyShips("USS Monitor", DS9FXShips.Defiant)

def SetupFriendlyShips(shipName, shipType):
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI
    pShip = loadspacehelper.CreateShip(shipType, pSet, shipName, "FriendlyPos1")
    DS9FXLifeSupportLib.ClearFromGroup(shipName)
    pMission.GetFriendlyGroup().AddName(shipName)
    pShip = MissionLib.GetShip(shipName, pSet) 
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
    sText = "Mission Failed at the very end of the campaign!"
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

    if pSet.GetName() == "DS9FXSeptimus1":   
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        SetupSet()        
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)       
        
def SetupSet():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()    
    ShowMessage("I'm reading the enemy task force on long range sensors. The fleet is ready to engage.")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")         
    CreateEnemies()          
    
def ShowMessage(s, i = 12):
    sText = s
    iPos = 6
    iFont = 12
    iDur = i
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)     
    
def CreateEnemies():
    global dEnemies
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
    for k,v in dEnemies.items():
        sShip = k
        if v == "Fighter":
            pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
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
        
    if (dEnemies.has_key(pShip.GetName())):
        del dEnemies[pShip.GetName()]
        
    if (len(dEnemies) == 0):
        ShowMessage("We did it! I don't think the True Way will try to\noverthrow the Detapa Council again any time soon.\nWe should return to DS9.")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)        
        
def Failed():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()    
    FailedTxt()
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")        
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")         
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
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveShips", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".PlayMovie", App.g_kUtopiaModule.GetGameTime() + 25, 0, 0)
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")        
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")         
        except:
            pass

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)    
        
def RemoveShips(pObject, pEvent):    
    lFriendlies = ["USS Kennedy", "USS Venice", "USS Monitor"]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    for s in lFriendlies:
        try:
            pSet.DeleteObjectFromSet(s)
        except:
            pass          
        
def CompletedTxt():
    sText = "Campaign Completed!"
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
    id = 6
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
    
def PlayMovie(pObject, pEvent):
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.CompletionVid != 1:
        return 0    
    pPlayer = MissionLib.GetPlayer()
    pPlayer.SetTarget(None)
    from Custom.DS9FX.DS9FXVids import DS9FXCompletionVideo3
    DS9FXCompletionVideo3.PlayMovieSeq()    
