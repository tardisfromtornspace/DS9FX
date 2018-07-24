# Creates starbase stations and ships

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib, DisableLocalForces
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


def Create():
    pModule = __import__("Systems.DS9FXStarbase375.DS9FXStarbase3751")
    pSet = pModule.GetSet()

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.FederationSide == 1:
        if (DS9FXSavedConfig.Starbase375Starbase == 1):
            Name = "Starbase 375"
            pDS9 = loadspacehelper.CreateShip(DS9FXShips.FedStarbase, pSet, Name, "Starbase 375 Location")
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            DS9FXLifeSupportLib.ClearFromGroup(Name)
            pMission.GetFriendlyGroup().AddName(Name)
            import Custom.DS9FX.DS9FXAILib.DS9FXDS9AI
            pObj = MissionLib.GetShip(Name, pSet)
            pObj = App.ShipClass_Cast(pObj)
            pObj.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXDS9AI.CreateAI(pObj))

            if not DisableLocalForces.ShouldEnforceLocalForces():
                Name = "USS Centaur"
                pExcal = loadspacehelper.CreateShip(DS9FXShips.Centaur, pSet, Name, "Centaur Location")
                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Name)
                pMission.GetFriendlyGroup().AddName(Name)
                import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI
                pObj = MissionLib.GetShip(Name, pSet)
                pObj = App.ShipClass_Cast(pObj)
                pObj.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pObj))
    else:
        if (DS9FXSavedConfig.Starbase375Starbase == 1):
            Name = "Starbase 375"
            loadspacehelper.CreateShip(DS9FXShips.FedStarbase, pSet, Name, "Starbase 375 Location")
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            DS9FXLifeSupportLib.ClearFromGroup(Name)
            pMission.GetEnemyGroup().AddName(Name)
            import Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI
            pObj = MissionLib.GetShip(Name, pSet)
            pObj = App.ShipClass_Cast(pObj)
            pObj.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI.CreateAI(pObj))

            if not DisableLocalForces.ShouldEnforceLocalForces():
                Name = "USS Centaur"
                pExcal = loadspacehelper.CreateShip(DS9FXShips.Centaur, pSet, Name, "Centaur Location")
                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Name)
                pMission.GetFriendlyGroup().AddName(Name)
                import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
                pObj = MissionLib.GetShip(Name, pSet)
                pObj = App.ShipClass_Cast(pObj)
                pObj.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pObj))
