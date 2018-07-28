# by USS Sovereign: DS9FX v3.0 Mission


# Imports
import App
import loadspacehelper
import MissionLib
import Custom.DS9FX.DS9FXmain
import nt
import string
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXLifeSupportLib, DS9FXMissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Events
ET_ACCEPT = App.UtopiaModule_GetNextEventType()
ET_DECLINE = App.UtopiaModule_GetNextEventType()
ET_BACK = App.UtopiaModule_GetNextEventType()

# Vars
pPane = None
pMainPane = None
Enemies = []
pPaneID = App.NULL_ID
pName = MissionIDs.HM4
sName = "Retake DS9 (Canon)"
sObjectives = "-Defeat 35 enemy ships to takeover DS9\n-Survive the battle"
sBriefing = "Captain, it's time now to return to DS9. We have received word that the Dominion is about to disarm the cloaked minefield we have placed. If this happens the Dominion will be able to receive reinforcements from the Gamma Quadrant. We can't let this happen. You and your ship, the USS Trinculo, are ordered to join the task force. We do no expect the Klingons to join us so you will be on your own. Godspeed Captain."


def Briefing():
    global pMainPane, pPane

    if not pPane == None:
        Decline(None, None)
        return

    pPane = App.TGPane_Create(1.0, 1.0)
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0)
    pMainPane = App.TGPane_Create(0.60, 0.65)
    pPane.AddChild(pMainPane, 0.22, 0.12)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_DECLINE, pMission, __name__ + ".Decline")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")

    CreateEntries(None, None)


def CreateEntries(pObject, pEvent):
    global pMainPane, pPane

    kColor = App.TGColorA()
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)

    pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize",
                                               App.TGString("Mission: Retake DS9 (Canon)"), 0.0, 0.0, None, 1, 0.30,
                                               0.30, kColor)
    pMainPane.AddChild(pIconWindow, 0, 0)

    pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0,
                                                     0.0, None, 1, 0.29, 0.30, kColor)
    pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

    pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0,
                                                   None, 1, 0.60, 0.25, kColor)
    pMainPane.AddChild(pBriefingWindow, 0, 0.31)

    pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0,
                                                 0.0, None, 1, 0.60, 0.08, kColor)
    pMainPane.AddChild(pButtonWindow, 0, 0.57)

    pText = App.TGParagraph_CreateW(App.TGString("-Defeat 35 enemy ships to takeover DS9\n-Survive the battle"),
                                    pObjectivesWindow.GetMaximumInteriorWidth(), None, '',
                                    pObjectivesWindow.GetMaximumInteriorWidth(),
                                    App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pObjectivesWindow.AddChild(pText, 0, 0.01)

    pText = App.TGParagraph_CreateW(App.TGString(
        "Captain, it's time now to return to DS9. We have received word that the Dominion is about to disarm the cloaked minefield we have placed. If this happens the Dominion will be able to receive reinforcements from the Gamma Quadrant. We can't let this happen. You and your ship, the USS Defiant, are ordered to join the task force. We do no expect the Klingons to join us so you will be on your own. Godspeed Captain."),
                                    pBriefingWindow.GetMaximumInteriorWidth(), None, '',
                                    pBriefingWindow.GetMaximumInteriorWidth(),
                                    App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pBriefingWindow.AddChild(pText, 0, 0.01)

    CreateRandomIcon(pIconWindow)

    kNormalColor = App.TGColorA()
    kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
    kHilightedColor = App.TGColorA()
    kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
    kDisabledColor = App.TGColorA()
    kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

    x = 0
    y = 0.01
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_ACCEPT)
    pEvent.SetString("Accepting")
    pButton = App.STRoundedButton_CreateW(App.TGString("Accept Mission"), pEvent, 0.13125, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pButtonWindow.AddChild(pButton, x, y)

    x = 0 + 0.2
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_DECLINE)
    pEvent.SetString("Declining")
    pButton = App.STRoundedButton_CreateW(App.TGString("Decline Mission"), pEvent, 0.13125, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pButtonWindow.AddChild(pButton, x, y)

    x = x + 0.2
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_BACK)
    pEvent.SetString("BackToMissionSelectioMenu")
    pButton = App.STRoundedButton_CreateW(App.TGString("Select Another Mission"), pEvent, 0.13125, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pButtonWindow.AddChild(pButton, x, y)

    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
    pLCARS = pGraphicsMode.GetLcarsString()
    pGlass = App.TGIcon_Create(pLCARS, 120)
    pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight())
    pMainPane.AddChild(pGlass, 0, 0)

    pIconWindow.InteriorChangedSize()
    pIconWindow.Layout()
    pObjectivesWindow.InteriorChangedSize()
    pObjectivesWindow.Layout()
    pBriefingWindow.InteriorChangedSize()
    pBriefingWindow.Layout()
    pButtonWindow.InteriorChangedSize()
    pButtonWindow.Layout()
    pMainPane.Layout()
    pPane.Layout()

    pTop = App.TopWindow_GetTopWindow()
    pTop.ForceTacticalVisible()

    pPane.SetVisible()


def CreateRandomIcon(pWindow):
    from Custom.DS9FX.DS9FXIconManager import IconManager

    IconManager.LoadDS9FX_Icons()

    pIcon = App.TGIcon_Create("DS9FX_Icons", App.SPECIES_UNKNOWN)
    pIcon.Resize(0.26, 0.25)
    pIcon.SetVisible()

    pSelection = GetRandomRate(1)
    pIcon.SetIconNum(pSelection)

    pWindow.AddChild(pIcon, 0.01, 0.01)


def GetRandomRate(iNumber):
    return App.g_kSystemWrapper.GetRandomNumber(16) + iNumber


def Decline(pObject, pEvent):
    global pMainPane, pPane

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
        App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
        App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
    except:
        pass

    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

    App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

    pTCW.DeleteChild(pPane)

    pPane = None

    pMainPane = None

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def Accept(pObject, pEvent):
    global pMainPane, pPane

    DS9FXGlobalEvents.Trigger_DS9FX_Mission_Start(MissionLib.GetPlayer(), pName)

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
        App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
        App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
    except:
        pass

    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

    App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

    pTCW.DeleteChild(pPane)

    pPane = None

    pMainPane = None

    MissionTittle(None, None)

    MissionInitiate(None, None)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ShowMissionMenu(pObject, pEvent):
    Decline(None, None)
    Custom.DS9FX.DS9FXmain.RecallMissionMenu()
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def MissionTittle(pObject, pEvent):
    global pPaneID

    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)
    pSequence.AppendAction(TextSequence(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()


def TextSequence(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)

    pAction = LineAction("Mission: Retake DS9 (Canon)", pPane, 3, 6, 16)
    pSequence.AddAction(pAction, None, 10)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()


def LineAction(sLine, pPane, fPos, duration, fontSize):
    i = string.find(sLine, "Mission:")
    if not i == 0:
        from Custom.DS9FX.DS9FXMissions import MissionStatus
        MissionStatus.AddLOGEntry(sLine)

    fHeight = fPos * 0.0375
    App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
    pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
    return pAction


def MissionInitiate(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    try:
        pSet.DeleteObjectFromSet("USS Excalibur")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS Defiant")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS Oregon")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS_Lakota")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("Deep_Space_9")
    except:
        pass

    SetupPlayer()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons",
                           App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

    ObjectivesPrompt(None, None)

    MissionSetup()

    PlayMissionMovies()


def PlayMissionMovies():
    DS9FXMissionLib.PlayMissionMovies()


def SetupPlayer():
    pShip = DS9FXShips.Defiant

    pPlayer = MissionLib.GetPlayer()
    pPlayerName = pPlayer.GetName()
    pSet = pPlayer.GetContainingSet()
    pSet.DeleteObjectFromSet(pPlayerName)

    loadspacehelper.CreateShip(pShip, pSet, pPlayerName, "RetakePlayerPos")
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

    try:
        bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

        bEnter.SetDisabled()

    except:

        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    try:
        bDock = DS9FXMenuLib.GetSubMenuButton("Dock To DS9", "Helm", "DS9FX", "DS9 Options...")

        bDock.SetDisabled()

    except:

        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    try:

        Custom.DS9FX.DS9FXmain.DisableWarpButton()

    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())


def PlayerExploding(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
    pPlayeName = pPlayer.GetName()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    ShipName = pShip.GetName()

    if (ShipName == pPlayeName):
        FailedTxt(None, None)
        RemoveShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                   __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                   __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def CrewLost():
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt(None, None)
        RemoveShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                   __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                   __name__ + ".ObjectExploding")
        RemoveMissionShips()
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass


def FailedTxt(pObject, pEvent):
    global pPaneID
    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)
    pSequence.AppendAction(Failed(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()


def Failed(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)

    pAction = LineAction("Mission Failed!", pPane, 6, 6, 12)
    pSequence.AddAction(pAction, None, 0)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()


def ReenableAllButtons():
    try:

        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")

        bHail.SetEnabled()

    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    try:
        bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

        bEnter.SetEnabled()

    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    try:
        bDock = DS9FXMenuLib.GetSubMenuButton("Dock To DS9", "Helm", "DS9FX", "DS9 Options...")

        bDock.SetEnabled()

    except:

        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

    try:
        Custom.DS9FX.DS9FXmain.RestoreWarpButton()

    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."


def ObjectivesPrompt(pObject, pEvent):
    global pPaneID

    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)
    pSequence.AppendAction(ObjectivesSequence(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()


def ObjectivesSequence(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)

    pAction = LineAction("This is it Captain!\nLet's go down in history!", pPane, 6, 10, 12)
    pSequence.AddAction(pAction, None, 10)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()


def MissionSetup():
    global Enemies

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    Enemies = ["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8", "Enemy 9",
               "Enemy 10", "Enemy 11", "Enemy 12", "Enemy 13", "Enemy 14", "Enemy 15", "Enemy 16", "Enemy 17",
               "Enemy 18", "Enemy 19", "Enemy 20", "Enemy 21", "Enemy 22", "Enemy 23", "Enemy 24", "Enemy 25",
               "Enemy 26", "Enemy 27", "Enemy 28", "Enemy 29", "Enemy 30", "Enemy 31", "Enemy 32", "Enemy 33",
               "Enemy 34", "Enemy 35"]

    SpawnShips()

    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                      __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                      __name__ + ".ObjectExploding")


def SpawnShips():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    loadspacehelper.CreateShip(DS9FXShips.Akira, pSet, "USS Argus", "FriendlyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("USS Argus")
    pMission.GetFriendlyGroup().AddName("USS Argus")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship1 = MissionLib.GetShip("USS Argus", pSet)

    pship1 = App.ShipClass_Cast(ship1)

    pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

    loadspacehelper.CreateShip(DS9FXShips.Excelsior, pSet, "USS Iconia", "FriendlyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("USS Iconia")
    pMission.GetFriendlyGroup().AddName("USS Iconia")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship2 = MissionLib.GetShip("USS Iconia", pSet)

    pship2 = App.ShipClass_Cast(ship2)

    pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

    loadspacehelper.CreateShip(DS9FXShips.Nebula, pSet, "USS Rotterdam", "FriendlyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("USS Rotterdam")
    pMission.GetFriendlyGroup().AddName("USS Rotterdam")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship3 = MissionLib.GetShip("USS Rotterdam", pSet)

    pship3 = App.ShipClass_Cast(ship3)

    pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))

    loadspacehelper.CreateShip(DS9FXShips.Miranda, pSet, "USS Monaco", "FriendlyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("USS Monaco")
    pMission.GetFriendlyGroup().AddName("USS Monaco")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship4 = MissionLib.GetShip("USS Monaco", pSet)

    pship4 = App.ShipClass_Cast(ship4)

    pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))

    loadspacehelper.CreateShip(DS9FXShips.Miranda, pSet, "USS Rapid", "FriendlyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("USS Rapid")
    pMission.GetFriendlyGroup().AddName("USS Rapid")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship5 = MissionLib.GetShip("USS Rapid", pSet)

    pship5 = App.ShipClass_Cast(ship5)

    pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship5))

    Att1 = "Enemy 1"
    pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att1, "EnemyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att1)
    pMission.GetEnemyGroup().AddName(Att1)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker1 = MissionLib.GetShip("Enemy 1", pSet)

    pAttacker1 = App.ShipClass_Cast(Attacker1)

    pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

    Att2 = "Enemy 2"
    pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att2, "EnemyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att2)
    pMission.GetEnemyGroup().AddName(Att2)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker2 = MissionLib.GetShip("Enemy 2", pSet)

    pAttacker2 = App.ShipClass_Cast(Attacker2)

    pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

    Att3 = "Enemy 3"
    pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att3, "EnemyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att3)
    pMission.GetEnemyGroup().AddName(Att3)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker3 = MissionLib.GetShip("Enemy 3", pSet)

    pAttacker3 = App.ShipClass_Cast(Attacker3)

    pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

    Att4 = "Enemy 4"
    pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "EnemyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att4)
    pMission.GetEnemyGroup().AddName(Att4)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker4 = MissionLib.GetShip("Enemy 4", pSet)

    pAttacker4 = App.ShipClass_Cast(Attacker4)

    pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

    Att5 = "Enemy 5"
    pAtt5 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att5, "EnemyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att5)
    pMission.GetEnemyGroup().AddName(Att5)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker5 = MissionLib.GetShip("Enemy 5", pSet)

    pAttacker5 = App.ShipClass_Cast(Attacker5)

    pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

    Att6 = "Enemy 6"
    pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att6, "EnemyPos6")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att6)
    pMission.GetEnemyGroup().AddName(Att6)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker6 = MissionLib.GetShip("Enemy 6", pSet)

    pAttacker6 = App.ShipClass_Cast(Attacker6)

    pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

    Att7 = "Enemy 7"
    pAtt7 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att7, "EnemyPos7")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att7)
    pMission.GetEnemyGroup().AddName(Att7)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker7 = MissionLib.GetShip("Enemy 7", pSet)

    pAttacker7 = App.ShipClass_Cast(Attacker7)

    pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


# Next wave of enemy ships coming in. The best way to simulate BIG battles in BC!
def SpawnSecondWave():
    # Get some values
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    Att1 = "Enemy 8"
    pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att1, "EnemyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att1)
    pMission.GetEnemyGroup().AddName(Att1)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker1 = MissionLib.GetShip("Enemy 8", pSet)

    pAttacker1 = App.ShipClass_Cast(Attacker1)

    pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

    Att2 = "Enemy 9"
    pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att2, "EnemyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att2)
    pMission.GetEnemyGroup().AddName(Att2)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker2 = MissionLib.GetShip("Enemy 9", pSet)

    pAttacker2 = App.ShipClass_Cast(Attacker2)

    pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

    Att3 = "Enemy 10"
    pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att3, "EnemyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att3)
    pMission.GetEnemyGroup().AddName(Att3)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker3 = MissionLib.GetShip("Enemy 10", pSet)

    pAttacker3 = App.ShipClass_Cast(Attacker3)

    pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

    Att4 = "Enemy 11"
    pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "EnemyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att4)
    pMission.GetEnemyGroup().AddName(Att4)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker4 = MissionLib.GetShip("Enemy 11", pSet)

    pAttacker4 = App.ShipClass_Cast(Attacker4)

    pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

    Att5 = "Enemy 12"
    pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "EnemyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att5)
    pMission.GetEnemyGroup().AddName(Att5)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker5 = MissionLib.GetShip("Enemy 12", pSet)

    pAttacker5 = App.ShipClass_Cast(Attacker5)

    pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

    Att6 = "Enemy 13"
    pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att6, "EnemyPos6")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att6)
    pMission.GetEnemyGroup().AddName(Att6)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker6 = MissionLib.GetShip("Enemy 13", pSet)

    pAttacker6 = App.ShipClass_Cast(Attacker6)

    pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

    Att7 = "Enemy 14"
    pAtt7 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att7, "EnemyPos7")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att7)
    pMission.GetEnemyGroup().AddName(Att7)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker7 = MissionLib.GetShip("Enemy 14", pSet)

    pAttacker7 = App.ShipClass_Cast(Attacker7)

    pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


# 3rd wave
def SpawnThirdWave():
    # Get some values
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    Att1 = "Enemy 15"
    pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att1, "EnemyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att1)
    pMission.GetEnemyGroup().AddName(Att1)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker1 = MissionLib.GetShip("Enemy 15", pSet)

    pAttacker1 = App.ShipClass_Cast(Attacker1)

    pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

    Att2 = "Enemy 16"
    pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att2, "EnemyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att2)
    pMission.GetEnemyGroup().AddName(Att2)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker2 = MissionLib.GetShip("Enemy 16", pSet)

    pAttacker2 = App.ShipClass_Cast(Attacker2)

    pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

    Att3 = "Enemy 17"
    pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att3, "EnemyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att3)
    pMission.GetEnemyGroup().AddName(Att3)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker3 = MissionLib.GetShip("Enemy 17", pSet)

    pAttacker3 = App.ShipClass_Cast(Attacker3)

    pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

    Att4 = "Enemy 18"
    pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "EnemyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att4)
    pMission.GetEnemyGroup().AddName(Att4)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker4 = MissionLib.GetShip("Enemy 18", pSet)

    pAttacker4 = App.ShipClass_Cast(Attacker4)

    pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

    Att5 = "Enemy 19"
    pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att5, "EnemyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att5)
    pMission.GetEnemyGroup().AddName(Att5)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker5 = MissionLib.GetShip("Enemy 19", pSet)

    pAttacker5 = App.ShipClass_Cast(Attacker5)

    pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

    Att6 = "Enemy 20"
    pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att6, "EnemyPos6")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att6)
    pMission.GetEnemyGroup().AddName(Att6)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker6 = MissionLib.GetShip("Enemy 20", pSet)

    pAttacker6 = App.ShipClass_Cast(Attacker6)

    pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

    Att7 = "Enemy 21"
    pAtt7 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att7, "EnemyPos7")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att7)
    pMission.GetEnemyGroup().AddName(Att7)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker7 = MissionLib.GetShip("Enemy 21", pSet)

    pAttacker7 = App.ShipClass_Cast(Attacker7)

    pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


def SpawnFourthWave():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    Att1 = "Enemy 22"
    pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att1, "EnemyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att1)
    pMission.GetEnemyGroup().AddName(Att1)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker1 = MissionLib.GetShip("Enemy 22", pSet)

    pAttacker1 = App.ShipClass_Cast(Attacker1)

    pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

    Att2 = "Enemy 23"
    pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att2, "EnemyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att2)
    pMission.GetEnemyGroup().AddName(Att2)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker2 = MissionLib.GetShip("Enemy 23", pSet)

    pAttacker2 = App.ShipClass_Cast(Attacker2)

    pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

    Att3 = "Enemy 24"
    pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att3, "EnemyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att3)
    pMission.GetEnemyGroup().AddName(Att3)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker3 = MissionLib.GetShip("Enemy 24", pSet)

    pAttacker3 = App.ShipClass_Cast(Attacker3)

    pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

    Att4 = "Enemy 25"
    pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "EnemyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att4)
    pMission.GetEnemyGroup().AddName(Att4)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker4 = MissionLib.GetShip("Enemy 25", pSet)

    pAttacker4 = App.ShipClass_Cast(Attacker4)

    pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

    Att5 = "Enemy 26"
    pAtt5 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att5, "EnemyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att5)
    pMission.GetEnemyGroup().AddName(Att5)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker5 = MissionLib.GetShip("Enemy 26", pSet)

    pAttacker5 = App.ShipClass_Cast(Attacker5)

    pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

    Att6 = "Enemy 27"
    pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att6, "EnemyPos6")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att6)
    pMission.GetEnemyGroup().AddName(Att6)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker6 = MissionLib.GetShip("Enemy 27", pSet)

    pAttacker6 = App.ShipClass_Cast(Attacker6)

    pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

    Att7 = "Enemy 28"
    pAtt7 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att7, "EnemyPos7")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att7)
    pMission.GetEnemyGroup().AddName(Att7)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker7 = MissionLib.GetShip("Enemy 28", pSet)

    pAttacker7 = App.ShipClass_Cast(Attacker7)

    pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


def SpawnFifthWave():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    Att1 = "Enemy 29"
    pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att1, "EnemyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att1)
    pMission.GetEnemyGroup().AddName(Att1)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker1 = MissionLib.GetShip("Enemy 29", pSet)

    pAttacker1 = App.ShipClass_Cast(Attacker1)

    pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

    Att2 = "Enemy 30"
    pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att2, "EnemyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att2)
    pMission.GetEnemyGroup().AddName(Att2)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker2 = MissionLib.GetShip("Enemy 30", pSet)

    pAttacker2 = App.ShipClass_Cast(Attacker2)

    pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

    Att3 = "Enemy 31"
    pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att3, "EnemyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att3)
    pMission.GetEnemyGroup().AddName(Att3)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker3 = MissionLib.GetShip("Enemy 31", pSet)

    pAttacker3 = App.ShipClass_Cast(Attacker3)

    pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

    Att4 = "Enemy 32"
    pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "EnemyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att4)
    pMission.GetEnemyGroup().AddName(Att4)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker4 = MissionLib.GetShip("Enemy 32", pSet)

    pAttacker4 = App.ShipClass_Cast(Attacker4)

    pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

    Att5 = "Enemy 33"
    pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "EnemyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att5)
    pMission.GetEnemyGroup().AddName(Att5)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker5 = MissionLib.GetShip("Enemy 33", pSet)

    pAttacker5 = App.ShipClass_Cast(Attacker5)

    pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

    Att6 = "Enemy 34"
    pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att6, "EnemyPos6")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att6)
    pMission.GetEnemyGroup().AddName(Att6)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker6 = MissionLib.GetShip("Enemy 34", pSet)

    pAttacker6 = App.ShipClass_Cast(Attacker6)

    pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

    Att7 = "Enemy 35"
    pAtt7 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att7, "EnemyPos7")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(Att7)
    pMission.GetEnemyGroup().AddName(Att7)

    import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

    Attacker7 = MissionLib.GetShip("Enemy 35", pSet)

    pAttacker7 = App.ShipClass_Cast(Attacker7)

    pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


def KlingonArrival():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKV Ykir", "FriendlyPos1")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("IKV Ykir")
    pMission.GetFriendlyGroup().AddName("IKV Ykir")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship1 = MissionLib.GetShip("IKV Ykir", pSet)

    pship1 = App.ShipClass_Cast(ship1)

    pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

    loadspacehelper.CreateShip(DS9FXShips.Ktinga, pSet, "IKV Nawrya", "FriendlyPos2")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("IKS Nawrya")
    pMission.GetFriendlyGroup().AddName("IKV Nawrya")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship2 = MissionLib.GetShip("IKV Nawrya", pSet)

    pship2 = App.ShipClass_Cast(ship2)

    pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

    loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKV Tumultuous", "FriendlyPos3")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("IKV Tumultuous")
    pMission.GetFriendlyGroup().AddName("IKV Tumultuous")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship3 = MissionLib.GetShip("IKV Tumultuous", pSet)

    pship3 = App.ShipClass_Cast(ship3)

    pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))

    loadspacehelper.CreateShip(DS9FXShips.Vorcha, pSet, "IKV Hunter", "FriendlyPos4")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("IKV Hunter")
    pMission.GetFriendlyGroup().AddName("IKV Hunter")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship4 = MissionLib.GetShip("IKV Hunter", pSet)

    pship4 = App.ShipClass_Cast(ship4)

    pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))

    loadspacehelper.CreateShip(DS9FXShips.Vorcha, pSet, "IKV Invincible", "FriendlyPos5")

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup("IKV Invincible")
    pMission.GetFriendlyGroup().AddName("IKV Invincible")

    import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

    ship5 = MissionLib.GetShip("IKV Invincible", pSet)

    pship5 = App.ShipClass_Cast(ship5)

    pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship5))


def ObjectExploding(pObject, pEvent):
    global Enemies

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    ShipName = pShip.GetName()

    if (ShipName in Enemies):
        Enemies.remove(ShipName)

        if (len(Enemies) == 28):
            SpawnSecondWave()

        elif (len(Enemies) == 21):
            SpawnThirdWave()

        elif (len(Enemies) == 16):
            KlingonsPrompt(None, None)
            KlingonArrival()

        elif (len(Enemies) == 14):
            SpawnFourthWave()

        elif (len(Enemies) == 7):
            SpawnFifthWave()

        elif (len(Enemies) == 0):
            from Custom.DS9FX.DS9FXObjects import DS9Ships
            DS9Ships.DS9SetShips()

            from Custom.DS9FX.DS9FXObjects import DS9Stations
            DS9Stations.DS9SetStations()

            ReenableAllButtons()

            RemoveShips()

            MissionWin(None, None)

            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission,
                                                       __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission,
                                                       __name__ + ".ObjectExploding")

            DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def KlingonsPrompt(pObject, pEvent):
    global pPaneID

    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)
    pSequence.AppendAction(KlingonsSequence(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()


def KlingonsSequence(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)

    pAction = LineAction("The Klingons, Sir!\nThey have arrived!!!", pPane, 6, 10, 12)
    pSequence.AddAction(pAction, None, 10)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()


def MissionWin(pObject, pEvent):
    global pPaneID

    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)
    pSequence.AppendAction(WinSequence(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()


def WinSequence(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime(1)

    pAction = LineAction("DS9 is ours once again!\n\nTime to celebrate!", pPane, 6, 10, 12)
    pSequence.AddAction(pAction, None, 10)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()

    DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)


def RemoveShips():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()

    try:
        pSet.DeleteObjectFromSet("USS Argus")
    except:
        pass
    try:
        pSet.DeleteObjectFromSet("USS Iconia")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS Rotterdam")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS Monaco")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("USS Rapid")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("IKV Ykir")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("IKV Nawrya")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("IKV Tumultuous")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("IKV Hunter")
    except:
        pass

    try:
        pSet.DeleteObjectFromSet("IKV Invincible")
    except:
        pass


def Quit():
    global pMainPane, pPane

    if not pPane == None:

        try:
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
            App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
            App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
        except:
            pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None


def KillPane(pAction):
    global pPaneID

    pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
    App.g_kRootWindow.DeleteChild(pPane)

    pPaneID = App.NULL_ID

    return 0


def RemoveMissionShips():
    ships = ["USS Argus", "USS Iconia", "USS Rotterdam", "USS Monaco", "USS Rapid", "IKV Ykir", "IKV Nawrya",
             "IKV Hunter", "IKV Invincible"]
    for i in range(1, 36):
        ships.append("Enemy " + str(i))

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
