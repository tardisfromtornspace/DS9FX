# Handles enable\disable local forces

import App
import MissionLib
from Custom.DS9FX import DS9FXmain
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

ships = ["Attacker 1", "Attacker 2", "Attacker 3", "Attacker 4", "Attacker 5",
         "USS Excalibur", "USS Defiant", "USS Oregon", "USS_Lakota", "Verde", "Guadiana", "Lankin",
         "Maroni", "Kuban", "Paraguay", "Tigris", "Dreadnought", "Bugship 1", "Bugship 2", "Bugship 3",
         "Bugship Patrol 1", "Bugship Patrol 2",
         "Bugship Patrol 3", "Bugship Patrol 4",
         "Bugship Patrol 5", "Bugship Patrol 6", "Bugship Patrol 7", "Bugship Patrol 8", "Bugship Patrol 9",
         "Bugship Patrol 10", "Bugship Patrol 11", "Dreadnought 1", "Dreadnought 2", "Bugship 1", "Bugship 2",
         "Bugship 3", "Bugship 4", "Dreadnought", "USS Majestic", "USS Bonchune", "Bugship 1", "Bugship 2", "Bugship 3",
         "IKS K'mpec", "IKS Amar", "IKS Ki'Tang", "Hutet 1", "Keldon 1", "Keldon 2", "Galor 1", "Galor 2"]


def DisableForces():
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.DisableLocalForces == 0:
        return

    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "DisableDelay")
    # 10 second delay, to ensure it's executed last
    pSequence.AddAction(pAction, None, 10)
    pSequence.Play()


def DisableDelay(pAction):
    player = MissionLib.GetPlayer()
    if not player:
        return 0

    set = player.GetContainingSet()
    if not set:
        return 0

    name = set.GetName()
    if not name:
        return 0

    for s in ships:
        try:
            set.DeleteObjectFromSet(s)
        except:
            pass

    return 1


def EnableForces():
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.DisableLocalForces == 0:
        return

    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "EnableDelay")
    # 10 second delay, to ensure it's executed last
    pSequence.AddAction(pAction, None, 10)
    pSequence.Play()


def EnableDelay(pAction):
    player = MissionLib.GetPlayer()
    if not player:
        return 0

    set = player.GetContainingSet()
    if not set:
        return 0

    name = set.GetName()
    if not name:
        return 0

    DS9FXmain.CreateDS9FXShips()

    return 1
