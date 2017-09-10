"""
Since UMM now by default comes with DS9FX Xtended, why not add a little something for the mutators which annoys me BTW,
The Foundation Mutator Fix works but why not automate it. This simple script will show how actually UMM is wonderful :)
And no more deactivation of Mutators when you exit the game, add new ships or whatever...

by USS Sovereign
"""

import App
import MainMenu.mainmenu
from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def GetName():
    # We need to load the trigger when the config menu loads
    pWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)
    # Tsk, tsk... forgot to remove any previous instances
    App.g_kEventManager.RemoveBroadcastHandler(MainMenu.mainmenu.ET_CONFIGURE_MUTATOR, pWindow, __name__ + ".HandleMutatorSelections")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(MainMenu.mainmenu.ET_CONFIGURE_MUTATOR, pWindow, __name__ + ".HandleMutatorSelections")
    
    return "DS9FX: Autoload Mutator Fix"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    return None

def StartUp():
    FoundationMutatorFix.RestoreFoundationSettings()

def HandleMutatorSelections(pObject, pEvent):
    # Check if we're supposed to track the user
    reload(DS9FXSavedConfig)
    iSetting = DS9FXSavedConfig.AutoMutatorBackup
    if iSetting == 1:
        FoundationMutatorFix.SaveBackup(bSilent = 0) # bSilent as in no prints
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)
