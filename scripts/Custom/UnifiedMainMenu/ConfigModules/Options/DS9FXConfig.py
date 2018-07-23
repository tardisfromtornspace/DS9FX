"""
This file is used to control DS9FX Configuration.

by USS Sovereign
"""

# Imports
import App
import string
import nt
from Custom.DS9FX.DS9FXSoundManager import SoundManager
from Custom.DS9FX.DS9FXConfigurations import DS9FXHighConfig, DS9FXHighestConfig, DS9FXLowConfig, DS9FXLowestConfig, \
    DS9FXMedConfig
from Custom.DS9FX.DS9FXConfigurations.TempConfig import DS9FXUnsavedConfig
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Config directory paths
sPath = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\DS9FXSavedConfig.py"
sUnsavedPath = "scripts\\Custom\\DS9FX\\DS9FXConfigurations\\TempConfig\\DS9FXUnsavedConfig.py"

# Events
ET_STATE_BUTTON = App.UtopiaModule_GetNextEventType()
ET_ONOFF_BUTTON = App.UtopiaModule_GetNextEventType()

# Timer properties
ET_TIMER_EVENT = App.UtopiaModule_GetNextEventType()
idTimer = App.NULL_ID

# Intro movies properties
dIntro = {0: ["DS9FX Intro", "DS9FXintro.bik"], 1: ["DS9FX Trailer", "DS9FXTrailer.bik"],
          2: ["Xtended Intro", "DS9FXXtendedIntro.bik"],
          3: ["Xtended 1.1", "DS9FXXtendedIntro2.bik"], 4: ["Random", "Random"]}

# Config properties
lSettings = ['ExcaliburSelection', 'DefiantSelection', 'OregonSelection', 'LakotaSelection',
             'DS9Selection', 'Bugship1Selection', 'Bugship2Selection', 'Bugship3Selection',
             'WormholeSelection', 'VideoSelection', 'ModelPreloadingSelection', 'RandomEnemyFleetAttacks',
             'DomIS', 'DS9Music', 'WormholeMusic', 'GammaMusic', 'RandomDomStrength', 'FederationSide',
             'DominionSide', 'CometSelection', 'DS9Planets', 'DS9NanoFX', 'GammaPlanets', 'GammaNanoFX',
             'DominionTimeSpan', 'CometAlphaTrail', 'CometAlphaTrailTexture', 'DebugMode', 'DS9MapPlanetDetail',
             'GammaMapPlanetDetail', 'InsideWormholeBackgroundTexture', 'InsideWormholeModel', 'StabilizeBC',
             'IntroVid', 'CompletionVid', 'AutoMutatorBackup', 'IntroMovieSel', 'BadlandsBackground', 'BadlandsVortex',
             'BadlandsMusic', 'BadlandsBackground2Res', 'BadlandsVortexVariant', 'LifeSupport', 'ExitGameDebugMode',
             'LifeSupportCrewLabels', 'KillRandomFleetsDuringMission', 'NanoFXExplosionFix', 'ExitGameFix',
             'TransporterFix', 'LifeSupportCombatEffectiveness', 'BadlandsDamageFX', 'KaremmaPlanets',
             'KaremmaNanoFX', 'KaremmaMapPlanetDetail', 'KaremmaDreadnought1', 'KaremmaDreadnought2',
             'KaremmaMusic', 'DosiPlanets', 'DosiNanoFX', 'DosiMapPlanetDetail', 'DosiMusic',
             'YaderaPlanets', 'YaderaNanoFX', 'YaderaMapPlanetDetail', 'YaderaMusic', 'NewBajorPlanets',
             'NewBajorNanoFX', 'NewBajorMapPlanetDetail', 'NewBajorMajestic', 'NewBajorBonchune', 'NewBajorMusic',
             'GaiaPlanets', 'GaiaNanoFX', 'GaiaMapPlanetDetail', 'GaiaMusic', 'KurrillPlanets', 'KurrillNanoFX',
             'KurrillMapPlanetDetail', 'KurrillShip1', 'KurrillShip2', 'KurrillShip3', 'KurrillShip4', 'KurrillShip5',
             'KurrillMusic', 'TrialusPlanets', 'TrialusNanoFX', 'TrialusMapPlanetDetail', 'TrialusMusic',
             'TRogoranPlanets', 'TRogoranNanoFX', 'TRogoranMapPlanetDetail', 'TRogoranMusic', 'VandrosPlanets',
             'VandrosNanoFX', 'VandrosMapPlanetDetail', 'VandrosMusic', 'FoundersPlanets', 'FoundersNanoFX',
             'FoundersMapPlanetDetail', 'FoundersShip1', 'FoundersShip2', 'FoundersShip3', 'FoundersShip4',
             'FoundersReinforcements', 'FoundersMusic', 'InstantConfigSave', 'NoDamageThroughShields',
             'EasterEggs', 'AIBoardings', 'QonosPlanets', 'QonosNanoFX', 'QonosMapPlanetDetail', 'QonosShip1',
             'QonosShip2', 'QonosShip3', 'QonosMusic', 'BadlandsBrightness', 'ChintokaPlanets', 'ChintokaNanoFX',
             'ChintokaMapPlanetDetail', 'ChintokaMusic', 'SunStreaks', 'VelaMusic', 'CardassiaPlanets',
             'CardassiaNanoFX',
             'CardassiaMapPlanetDetail', 'CardassiaMusic', 'CardassiaShip1', 'CardassiaShip2', 'CardassiaShip3',
             'CardassiaShip4', 'CardassiaShip5', 'TrivasPlanets', 'TrivasNanoFX', 'TrivasMapPlanetDetail',
             'TrivasMusic',
             'KlingonSide', 'CardassianSide', 'SeptimusPlanets', 'SeptimusNanoFX', 'SeptimusMapPlanetDetail',
             'SeptimusMusic',
             'DonatuPlanets', 'DonatuNanoFX', 'DonatuMapPlanetDetail', 'DonatuMusic', 'PelosaPlanets', 'PelosaNanoFX',
             'PelosaMapPlanetDetail', 'PelosaMusic', 'Starbase375Centaur', 'Starbase375Starbase', 'Starbase375Music',
             'MaxRandShips', 'DisableLocalForces']
dSettings = {}
for s in lSettings:
    dSettings[str(s)] = str(s)

# Button properties
dButtons = {}

# Register UMM Menu sounds
SoundManager.RegisterDS9FXUMMSounds()


# Functions
def GetName():
    return "DS9FX"


def CreateMenu(pOptionPane, pContentPanel, bGameEnded=0):
    global dButtons

    CorrectConfig()

    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.RemoveHandlerForInstance(ET_STATE_BUTTON, __name__ + ".HandleStateButton")
    pOptionsWindow.RemoveHandlerForInstance(ET_ONOFF_BUTTON, __name__ + ".HandleOnOffButton")

    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_STATE_BUTTON, __name__ + ".HandleStateButton")
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ONOFF_BUTTON, __name__ + ".HandleOnOffButton")

    CreateDS9FXSides(pOptionPane, pContentPanel)
    CreateDS9MapRelated(pOptionPane, pContentPanel)
    CreateGammaMapRelated(pOptionPane, pContentPanel)
    CreateWormholeMapRelated(pOptionPane, pContentPanel)
    CreateBadlandsMapRelated(pOptionPane, pContentPanel)
    CreateChintokaMapRelated(pOptionPane, pContentPanel)
    CreateCardassiaMapRelated(pOptionPane, pContentPanel)
    CreateDonatuMapRelated(pOptionPane, pContentPanel)
    CreateDosiMapRelated(pOptionPane, pContentPanel)
    CreateFoundersMapRelated(pOptionPane, pContentPanel)
    CreateGaiaMapRelated(pOptionPane, pContentPanel)
    CreateKaremmaMapRelated(pOptionPane, pContentPanel)
    CreateKurrillMapRelated(pOptionPane, pContentPanel)
    CreateNewBajorMapRelated(pOptionPane, pContentPanel)
    CreatePelosaMapRelated(pOptionPane, pContentPanel)
    CreateTRogoranMapRelated(pOptionPane, pContentPanel)
    CreateTrialusMapRelated(pOptionPane, pContentPanel)
    CreateTrivasMapRelated(pOptionPane, pContentPanel)
    CreateVandrosMapRelated(pOptionPane, pContentPanel)
    CreateVelaMapRelated(pOptionPane, pContentPanel)
    CreateQonosMapRelated(pOptionPane, pContentPanel)
    CreateSeptimusMapRelated(pOptionPane, pContentPanel)
    CreateStarbase375MapRelated(pOptionPane, pContentPanel)
    CreateYaderaMapRelated(pOptionPane, pContentPanel)
    CreateMiscOptions(pOptionPane, pContentPanel)
    CreateSaveConfig(pOptionPane, pContentPanel)
    CreateExtras(pOptionPane, pContentPanel)

    dButtons['44'] = CreateButton("DS9FX Credits", pContentPanel, pOptionPane, pContentPanel,
                                  __name__ + ".DS9FXCredits")

    CheckShownOptions()

    return App.TGPane_Create(0, 0)


def CreateDS9FXSides(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("DS9FX Ship\Station Sides")
    pContentPanel.AddChild(pMainMenu)

    pFederation = App.STCharacterMenu_Create("Federation")
    pMainMenu.AddChild(pFederation)

    pDominion = App.STCharacterMenu_Create("Dominion")
    pMainMenu.AddChild(pDominion)

    pKling = App.STCharacterMenu_Create("Klingon")
    pMainMenu.AddChild(pKling)

    pCard = App.STCharacterMenu_Create("Cardassian")
    pMainMenu.AddChild(pCard)

    dButtons['FederationSide'] = CreateStateButton(App.TGString("Ships\Stations: "), "FederationSide",
                                      [App.TGString("Enemy"), App.TGString("Friendly")],
                                      DS9FXUnsavedConfig.FederationSide)
    pFederation.AddChild(dButtons['FederationSide'])

    dButtons['DominionSide'] = CreateStateButton(App.TGString("Ships\Stations: "), "DominionSide",
                                      [App.TGString("Enemy"), App.TGString("Friendly")],
                                      DS9FXUnsavedConfig.DominionSide)
    pDominion.AddChild(dButtons['DominionSide'])

    dButtons['KlingonSide'] = CreateStateButton(App.TGString("Ships\Stations: "), "KlingonSide",
                                        [App.TGString("Enemy"), App.TGString("Friendly")],
                                        DS9FXUnsavedConfig.KlingonSide)
    pKling.AddChild(dButtons['KlingonSide'])

    dButtons['CardassianSide'] = CreateStateButton(App.TGString("Ships\Stations: "), "CardassianSide",
                                        [App.TGString("Enemy"), App.TGString("Friendly")],
                                        DS9FXUnsavedConfig.CardassianSide)
    pCard.AddChild(dButtons['CardassianSide'])

    return pMainMenu


def CreateDS9MapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("DS9 Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pDS9Planets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pDS9Planets)

    pDS9Ships = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pDS9Ships)

    pDS9Objects = App.STCharacterMenu_Create("Stations")
    pMainMenu.AddChild(pDS9Objects)

    pCometAlpha = App.STCharacterMenu_Create("Comet Alpha")
    pMainMenu.AddChild(pCometAlpha)

    pDS9Music = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pDS9Music)

    pDS9RndFleet = App.STCharacterMenu_Create("Random Fleets")
    pMainMenu.AddChild(pDS9RndFleet)

    dButtons['KlingonSide'] = CreateStateButton(App.TGString("Planets: "), "DS9Planets",
                                      [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9Planets)
    pDS9Planets.AddChild(dButtons['KlingonSide'])

    dButtons['DS9NanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "DS9NanoFX",
                                      [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9NanoFX)
    pDS9Planets.AddChild(dButtons['DS9NanoFX'])

    dButtons['DS9MapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "DS9MapPlanetDetail",
                                      [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                       App.TGString("High")], DS9FXUnsavedConfig.DS9MapPlanetDetail)
    pDS9Planets.AddChild(dButtons['DS9MapPlanetDetail'])

    dButtons['Bugship1Selection'] = CreateStateButton(App.TGString("USS Excalibur: "), "ExcaliburSelection",
                                      [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.ExcaliburSelection)
    pDS9Ships.AddChild(dButtons['Bugship1Selection'])

    dButtons['DefiantSelection'] = CreateStateButton(App.TGString("USS Defiant: "), "DefiantSelection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DefiantSelection)
    pDS9Ships.AddChild(dButtons['DefiantSelection'])

    dButtons['OregonSelection'] = CreateStateButton(App.TGString("USS Oregon: "), "OregonSelection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.OregonSelection)
    pDS9Ships.AddChild(dButtons['OregonSelection'])

    dButtons['LakotaSelection'] = CreateStateButton(App.TGString("USS Lakota: "), "LakotaSelection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.LakotaSelection)
    pDS9Ships.AddChild(dButtons['LakotaSelection'])

    dButtons['DS9Selection'] = CreateStateButton(App.TGString("Deep Space 9: "), "DS9Selection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9Selection)
    pDS9Objects.AddChild(dButtons['DS9Selection'])

    dButtons['CometSelection'] = CreateStateButton(App.TGString("Comet Alpha: "), "CometSelection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CometSelection)
    pCometAlpha.AddChild(dButtons['CometSelection'])

    dButtons['CometAlphaTrail'] = CreateStateButton(App.TGString("Trail Style: "), "CometAlphaTrail",
                                       [App.TGString("Plasma"), App.TGString("Comet")],
                                       DS9FXUnsavedConfig.CometAlphaTrail)
    pCometAlpha.AddChild(dButtons['CometAlphaTrail'])

    dButtons['CometAlphaTrailTexture'] = CreateStateButton(App.TGString("Trail Color: "), "CometAlphaTrailTexture",
                                       [App.TGString("Blue"), App.TGString("White")],
                                       DS9FXUnsavedConfig.CometAlphaTrailTexture)
    pCometAlpha.AddChild(dButtons['CometAlphaTrailTexture'])

    dButtons['DS9MusicSelection'] = CreateButton("Selection:  None", pDS9Music, pOptionPane, pContentPanel,
                                  __name__ + ".DS9MusicSelection", EventInt=0)

    if DS9FXUnsavedConfig.DS9Music == 1:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.DS9Music == 2:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.DS9Music == 3:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.DS9Music == 4:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Off"))

    dButtons['RandomEnemyFleetAttacks'] = CreateStateButton(App.TGString("Attacks\Assists: "), "RandomEnemyFleetAttacks",
                                       [App.TGString("Off"), App.TGString("On")],
                                       DS9FXUnsavedConfig.RandomEnemyFleetAttacks)
    pDS9RndFleet.AddChild(dButtons['RandomEnemyFleetAttacks'])

    dButtons['RandomDomStrength'] = CreateStateButton(App.TGString("Strength: "), "RandomDomStrength",
                                       [App.TGString("Weak"), App.TGString("Medium"), App.TGString("Strong"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.RandomDomStrength)
    pDS9RndFleet.AddChild(dButtons['RandomDomStrength'])

    dButtons['DominionTimeSpan'] = CreateStateButton(App.TGString("Timespan: "), "DominionTimeSpan",
                                       [App.TGString("2-4 mins"), App.TGString("4-6 mins"), App.TGString("6-8 mins"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.DominionTimeSpan)
    pDS9RndFleet.AddChild(dButtons['DominionTimeSpan'])

    dButtons['KillRandomFleetsDuringMission'] = CreateStateButton(App.TGString("Turn Off During Missions: "), "KillRandomFleetsDuringMission",
                                       [App.TGString("No"), App.TGString("Yes")],
                                       DS9FXUnsavedConfig.KillRandomFleetsDuringMission)
    pDS9RndFleet.AddChild(dButtons['KillRandomFleetsDuringMission'])

    dButtons['MaxRandShips'] = CreateStateButton(App.TGString("Max Number Of Enemies: "), "MaxRandShips",
                                        [App.TGString("2"), App.TGString("4")], DS9FXUnsavedConfig.MaxRandShips)
    pDS9RndFleet.AddChild(dButtons['MaxRandShips'])

    return pMainMenu


def CreateGammaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Gamma Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pGammaPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pGammaPlanets)

    pGammaShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pGammaShips)

    pGammaMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pGammaMusic)

    pGammaTech = App.STCharacterMenu_Create("Dominion Techs")
    pMainMenu.AddChild(pGammaTech)

    dButtons['ExcaliburSelection'] = CreateStateButton(App.TGString("Planets: "), "GammaPlanets",
                                      [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.GammaPlanets)
    pGammaPlanets.AddChild(dButtons['ExcaliburSelection'])

    dButtons['GammaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "GammaNanoFX",
                                      [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.GammaNanoFX)
    pGammaPlanets.AddChild(dButtons['GammaNanoFX'])

    dButtons['GammaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "GammaMapPlanetDetail",
                                      [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                       App.TGString("High")], DS9FXUnsavedConfig.GammaMapPlanetDetail)
    pGammaPlanets.AddChild(dButtons['GammaMapPlanetDetail'])

    dButtons['CometAlphaTrail'] = CreateStateButton(App.TGString("Bugship 1: "), "Bugship1Selection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship1Selection)
    pGammaShips.AddChild(dButtons['CometAlphaTrail'])

    dButtons['Bugship2Selection'] = CreateStateButton(App.TGString("Bugship 2: "), "Bugship2Selection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship2Selection)
    pGammaShips.AddChild(dButtons['Bugship2Selection'])

    dButtons['Bugship3Selection'] = CreateStateButton(App.TGString("Bugship 3: "), "Bugship3Selection",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship3Selection)
    pGammaShips.AddChild(dButtons['Bugship3Selection'])

    dButtons['GammaMusic'] = CreateStateButton(App.TGString("Selection: "), "GammaMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.GammaMusic)
    pGammaMusic.AddChild(dButtons['GammaMusic'])

    dButtons['DomIS'] = CreateOnOffButton(App.TGString("Intensive Scan: "), "DomIS", DS9FXUnsavedConfig.DomIS)
    pGammaTech.AddChild(dButtons['DomIS'])

    return pMainMenu


def CreateWormholeMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Wormhole Related Options")
    pContentPanel.AddChild(pMainMenu)

    pWormholeExterior = App.STCharacterMenu_Create("Exterior")
    pMainMenu.AddChild(pWormholeExterior)

    pWormholeInterior = App.STCharacterMenu_Create("Interior")
    pMainMenu.AddChild(pWormholeInterior)

    pWormholeMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pWormholeMusic)

    dButtons['WormholeSelection'] = CreateButton("Model: None", pWormholeExterior, pOptionPane, pContentPanel,
                                  __name__ + ".SelectModel", EventInt=0)

    if DS9FXUnsavedConfig.WormholeSelection == 1:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  2"))

    elif DS9FXUnsavedConfig.WormholeSelection == 2:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  3"))

    elif DS9FXUnsavedConfig.WormholeSelection == 3:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  4"))

    elif DS9FXUnsavedConfig.WormholeSelection == 4:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  5"))

    elif DS9FXUnsavedConfig.WormholeSelection == 5:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  6"))

    elif DS9FXUnsavedConfig.WormholeSelection == 6:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  7"))

    elif DS9FXUnsavedConfig.WormholeSelection == 7:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  8"))

    else:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  1"))

    dButtons['InsideWormholeBackgroundTexture'] = CreateButton("Background:  None", pWormholeInterior, pOptionPane, pContentPanel,
                                  __name__ + ".InsideWormholeBack", EventInt=0)

    if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 1:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Red"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 2:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Chrome"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 3:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Dark Blue"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 4:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Water Blue"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 5:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Weird"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 6:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  None"))

    else:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Blue"))

    dButtons['InsideWormholeModel'] = CreateButton("Variant:  None", pWormholeInterior, pOptionPane, pContentPanel,
                                  __name__ + ".InsideWormholeModels", EventInt=0)

    if DS9FXUnsavedConfig.InsideWormholeModel == 1:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Yellow"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 2:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Red Dawn"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 3:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Slipstream"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 4:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Blackhole"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 5:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  DS9 Series Rev."))

    else:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  DS9 Series"))

    dButtons['VideoSelection'] = CreateOnOffButton(App.TGString("Video Sequence: "), "VideoSelection",
                                       DS9FXUnsavedConfig.VideoSelection)
    pWormholeInterior.AddChild(dButtons['VideoSelection'])

    dButtons['WormholeMusic'] = CreateStateButton(App.TGString("Selection: "), "WormholeMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.WormholeMusic)
    pWormholeMusic.AddChild(dButtons['WormholeMusic'])

    return pMainMenu


def CreateBadlandsMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Badlands Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pBadlandsBackground = App.STCharacterMenu_Create("Backgrounds")
    pMainMenu.AddChild(pBadlandsBackground)

    pBadlandsStorms = App.STCharacterMenu_Create("Plasma Storms")
    pMainMenu.AddChild(pBadlandsStorms)

    pBadlandsMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pBadlandsMusic)

    dButtons['BadlandsBrightness'] = CreateStateButton(App.TGString("Enhanced Brightness: "), "BadlandsBrightness",
                                        [App.TGString("Off"), App.TGString("On")],
                                        DS9FXUnsavedConfig.BadlandsBrightness)
    pBadlandsBackground.AddChild(dButtons['BadlandsBrightness'])

    dButtons['BadlandsBackground'] = CreateStateButton(App.TGString("Set Background: "), "BadlandsBackground",
                                       [App.TGString("Model"), App.TGString("Model 2"), App.TGString("Model 3"),
                                        App.TGString("Texture")], DS9FXUnsavedConfig.BadlandsBackground)
    pBadlandsBackground.AddChild(dButtons['BadlandsBackground'])

    dButtons['BadlandsBackground2Res'] = CreateStateButton(App.TGString("Model 2 Detail: "), "BadlandsBackground2Res",
                                       [App.TGString("Low"), App.TGString("Med"), App.TGString("High")],
                                       DS9FXUnsavedConfig.BadlandsBackground2Res)
    pBadlandsBackground.AddChild(dButtons['BadlandsBackground2Res'])

    dButtons['BadlandsVortex'] = CreateStateButton(App.TGString("Count: "), "BadlandsVortex",
                                       [App.TGString("None"), App.TGString("Low"), App.TGString("Med"),
                                        App.TGString("High")], DS9FXUnsavedConfig.BadlandsVortex)
    pBadlandsStorms.AddChild(dButtons['BadlandsVortex'])

    dButtons['BadlandsVortexVariant'] = CreateStateButton(App.TGString("Variant: "), "BadlandsVortexVariant",
                                       [App.TGString("Default"), App.TGString("Alternate")],
                                       DS9FXUnsavedConfig.BadlandsVortexVariant)
    pBadlandsStorms.AddChild(dButtons['BadlandsVortexVariant'])

    dButtons['BadlandsDamageFX'] = CreateStateButton(App.TGString("Damage FX: "), "BadlandsDamageFX",
                                       [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.BadlandsDamageFX)
    pBadlandsStorms.AddChild(dButtons['BadlandsDamageFX'])

    dButtons['BadlandsMusic'] = CreateStateButton(App.TGString("Selection: "), "BadlandsMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.BadlandsMusic)
    pBadlandsMusic.AddChild(dButtons['BadlandsMusic'])

    return pMainMenu


def CreateKaremmaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Karemma Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['KaremmaPlanets'] = CreateStateButton(App.TGString("Planets: "), "KaremmaPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KaremmaPlanets)
    pPlanets.AddChild(dButtons['KaremmaPlanets'])

    dButtons['KaremmaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "KaremmaNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KaremmaNanoFX)
    pPlanets.AddChild(dButtons['KaremmaNanoFX'])

    dButtons['KaremmaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "KaremmaMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.KaremmaMapPlanetDetail)
    pPlanets.AddChild(dButtons['KaremmaMapPlanetDetail'])

    dButtons['KaremmaDreadnought1'] = CreateStateButton(App.TGString("Dreadnought 1: "), "KaremmaDreadnought1",
                                       [App.TGString("No"), App.TGString("Yes")],
                                       DS9FXUnsavedConfig.KaremmaDreadnought1)
    pShips.AddChild(dButtons['KaremmaDreadnought1'])

    dButtons['KaremmaDreadnought2'] = CreateStateButton(App.TGString("Dreadnought 2: "), "KaremmaDreadnought2",
                                       [App.TGString("No"), App.TGString("Yes")],
                                       DS9FXUnsavedConfig.KaremmaDreadnought2)
    pShips.AddChild(dButtons['KaremmaDreadnought2'])

    dButtons['KaremmaMusic'] = CreateStateButton(App.TGString("Selection: "), "KaremmaMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.KaremmaMusic)
    pMusic.AddChild(dButtons['KaremmaMusic'])

    return pMainMenu


def CreateDosiMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Dosi Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['DosiPlanets'] = CreateStateButton(App.TGString("Planets: "), "DosiPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DosiPlanets)
    pPlanets.AddChild(dButtons['DosiPlanets'])

    dButtons['DosiNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "DosiNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DosiNanoFX)
    pPlanets.AddChild(dButtons['DosiNanoFX'])

    dButtons['DosiMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "DosiMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.DosiMapPlanetDetail)
    pPlanets.AddChild(dButtons['DosiMapPlanetDetail'])

    dButtons['DosiMusic'] = CreateStateButton(App.TGString("Selection: "), "DosiMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.DosiMusic)
    pMusic.AddChild(dButtons['DosiMusic'])

    return pMainMenu


def CreateYaderaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Yadera Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['YaderaPlanets'] = CreateStateButton(App.TGString("Planets: "), "YaderaPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.YaderaPlanets)
    pPlanets.AddChild(dButtons['YaderaPlanets'])

    dButtons['YaderaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "YaderaNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.YaderaNanoFX)
    pPlanets.AddChild(dButtons['YaderaNanoFX'])

    dButtons['YaderaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "YaderaMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.YaderaMapPlanetDetail)
    pPlanets.AddChild(dButtons['YaderaMapPlanetDetail'])

    dButtons['YaderaMusic'] = CreateStateButton(App.TGString("Selection: "), "YaderaMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.YaderaMusic)
    pMusic.AddChild(dButtons['YaderaMusic'])

    return pMainMenu


def CreateNewBajorMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("New Bajor Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['NewBajorPlanets'] = CreateStateButton(App.TGString("Planets: "), "NewBajorPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.NewBajorPlanets)
    pPlanets.AddChild(dButtons['NewBajorPlanets'])

    dButtons['NewBajorNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "NewBajorNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.NewBajorNanoFX)
    pPlanets.AddChild(dButtons['NewBajorNanoFX'])

    dButtons['NewBajorMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "NewBajorMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.NewBajorMapPlanetDetail)
    pPlanets.AddChild(dButtons['NewBajorMapPlanetDetail'])

    dButtons['NewBajorMajestic'] = CreateStateButton(App.TGString("USS Majestic: "), "NewBajorMajestic",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.NewBajorMajestic)
    pShips.AddChild(dButtons['NewBajorMajestic'])

    dButtons['NewBajorBonchune'] = CreateStateButton(App.TGString("USS Bonchune: "), "NewBajorBonchune",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.NewBajorBonchune)
    pShips.AddChild(dButtons['NewBajorBonchune'])

    dButtons['NewBajorMusic'] = CreateStateButton(App.TGString("Selection: "), "NewBajorMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.NewBajorMusic)
    pMusic.AddChild(dButtons['NewBajorMusic'])

    return pMainMenu


def CreateGaiaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Gaia Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['85'] = CreateStateButton(App.TGString("Planets: "), "GaiaPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.GaiaPlanets)
    pPlanets.AddChild(dButtons['85'])

    dButtons['86'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "GaiaNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.GaiaNanoFX)
    pPlanets.AddChild(dButtons['86'])

    dButtons['87'] = CreateStateButton(App.TGString("Detail: "), "GaiaMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.GaiaMapPlanetDetail)
    pPlanets.AddChild(dButtons['87'])

    dButtons['GaiaMusic'] = CreateStateButton(App.TGString("Selection: "), "GaiaMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.GaiaMusic)
    pMusic.AddChild(dButtons['GaiaMusic'])

    return pMainMenu


def CreateKurrillMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Kurill Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['KurrillPlanets'] = CreateStateButton(App.TGString("Planets: "), "KurrillPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillPlanets)
    pPlanets.AddChild(dButtons['KurrillPlanets'])

    dButtons['KurrillNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "KurrillNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillNanoFX)
    pPlanets.AddChild(dButtons['KurrillNanoFX'])

    dButtons['91'] = CreateStateButton(App.TGString("Detail: "), "KurrillMapPlanetDetail",
                                       [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                        App.TGString("High")], DS9FXUnsavedConfig.KurrillMapPlanetDetail)
    pPlanets.AddChild(dButtons['91'])

    dButtons['KurrillShip1'] = CreateStateButton(App.TGString("Bugship 1: "), "KurrillShip1",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillShip1)
    pShips.AddChild(dButtons['KurrillShip1'])

    dButtons['KurrillShip2'] = CreateStateButton(App.TGString("Bugship 2: "), "KurrillShip2",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillShip2)
    pShips.AddChild(dButtons['KurrillShip2'])

    dButtons['KurrillShip3'] = CreateStateButton(App.TGString("Bugship 3: "), "KurrillShip3",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillShip3)
    pShips.AddChild(dButtons['KurrillShip3'])

    dButtons['KurrillShip4'] = CreateStateButton(App.TGString("Bugship 4: "), "KurrillShip4",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillShip4)
    pShips.AddChild(dButtons['KurrillShip4'])

    dButtons['KurrillShip5'] = CreateStateButton(App.TGString("Dreadnought: "), "KurrillShip5",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.KurrillShip5)
    pShips.AddChild(dButtons['KurrillShip5'])

    dButtons['KurrillMusic'] = CreateStateButton(App.TGString("Selection: "), "KurrillMusic",
                                       [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                        App.TGString("Random")], DS9FXUnsavedConfig.KurrillMusic)
    pMusic.AddChild(dButtons['KurrillMusic'])

    return pMainMenu


def CreateTrialusMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Trialus Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['TrialusPlanets'] = CreateStateButton(App.TGString("Planets: "), "TrialusPlanets",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TrialusPlanets)
    pPlanets.AddChild(dButtons['TrialusPlanets'])

    dButtons['TrialusNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "TrialusNanoFX",
                                       [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TrialusNanoFX)
    pPlanets.AddChild(dButtons['TrialusNanoFX'])

    dButtons['TrialusMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "TrialusMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.TrialusMapPlanetDetail)
    pPlanets.AddChild(dButtons['TrialusMapPlanetDetail'])

    dButtons['TrialusMusic'] = CreateStateButton(App.TGString("Selection: "), "TrialusMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.TrialusMusic)
    pMusic.AddChild(dButtons['TrialusMusic'])

    return pMainMenu


def CreateTRogoranMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("T-Rogoran Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['TRogoranPlanets'] = CreateStateButton(App.TGString("Planets: "), "TRogoranPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TRogoranPlanets)
    pPlanets.AddChild(dButtons['TRogoranPlanets'])

    dButtons['TRogoranNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "TRogoranNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TRogoranNanoFX)
    pPlanets.AddChild(dButtons['TRogoranNanoFX'])

    dButtons['TRogoranMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "TRogoranMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.TRogoranMapPlanetDetail)
    pPlanets.AddChild(dButtons['TRogoranMapPlanetDetail'])

    dButtons['TRogoranMusic'] = CreateStateButton(App.TGString("Selection: "), "TRogoranMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.TRogoranMusic)
    pMusic.AddChild(dButtons['TRogoranMusic'])

    return pMainMenu


def CreateVandrosMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Vandros Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['VandrosPlanets'] = CreateStateButton(App.TGString("Planets: "), "VandrosPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.VandrosPlanets)
    pPlanets.AddChild(dButtons['VandrosPlanets'])

    dButtons['VandrosNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "VandrosNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.VandrosNanoFX)
    pPlanets.AddChild(dButtons['VandrosNanoFX'])

    dButtons['VandrosMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "VandrosMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.VandrosMapPlanetDetail)
    pPlanets.AddChild(dButtons['VandrosMapPlanetDetail'])

    dButtons['VandrosMusic'] = CreateStateButton(App.TGString("Selection: "), "VandrosMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.VandrosMusic)
    pMusic.AddChild(dButtons['VandrosMusic'])

    return pMainMenu


def CreateFoundersMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Founders Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['FoundersPlanets'] = CreateStateButton(App.TGString("Planets: "), "FoundersPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersPlanets)
    pPlanets.AddChild(dButtons['FoundersPlanets'])

    dButtons['FoundersNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "FoundersNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersNanoFX)
    pPlanets.AddChild(dButtons['FoundersNanoFX'])

    dButtons['FoundersMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "FoundersMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.FoundersMapPlanetDetail)
    pPlanets.AddChild(dButtons['FoundersMapPlanetDetail'])

    dButtons['FoundersShip1'] = CreateStateButton(App.TGString("Dreadnought: "), "FoundersShip1",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersShip1)
    pShips.AddChild(dButtons['FoundersShip1'])

    dButtons['FoundersShip2'] = CreateStateButton(App.TGString("Bugship 1: "), "FoundersShip2",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersShip2)
    pShips.AddChild(dButtons['FoundersShip2'])

    dButtons['FoundersShip3'] = CreateStateButton(App.TGString("Bugship 2: "), "FoundersShip3",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersShip3)
    pShips.AddChild(dButtons['FoundersShip3'])

    dButtons['FoundersShip4'] = CreateStateButton(App.TGString("Bugship 3: "), "FoundersShip4",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.FoundersShip4)
    pShips.AddChild(dButtons['FoundersShip4'])

    dButtons['FoundersReinforcements'] = CreateStateButton(App.TGString("Reinforcements: "), "FoundersReinforcements",
                                        [App.TGString("No"), App.TGString("Yes")],
                                        DS9FXUnsavedConfig.FoundersReinforcements)
    pShips.AddChild(dButtons['FoundersReinforcements'])

    dButtons['FoundersReinforcements'] = CreateButton("Selection:  None", pMusic, pOptionPane, pContentPanel,
                                   __name__ + ".FoundersMusicSelection", EventInt=0)

    if DS9FXUnsavedConfig.FoundersMusic == 1:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.FoundersMusic == 2:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.FoundersMusic == 3:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.FoundersMusic == 4:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Off"))

    return pMainMenu


def CreateQonosMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Qo'nos Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['QonosPlanets'] = CreateStateButton(App.TGString("Planets: "), "QonosPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.QonosPlanets)
    pPlanets.AddChild(dButtons['QonosPlanets'])

    dButtons['QonosNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "QonosNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.QonosNanoFX)
    pPlanets.AddChild(dButtons['QonosNanoFX'])

    dButtons['QonosMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "QonosMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.QonosMapPlanetDetail)
    pPlanets.AddChild(dButtons['QonosMapPlanetDetail'])

    dButtons['QonosShip1'] = CreateStateButton(App.TGString("IKS K'mpec: "), "QonosShip1",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.QonosShip1)
    pShips.AddChild(dButtons['QonosShip1'])

    dButtons['QonosShip2'] = CreateStateButton(App.TGString("IKS Amar: "), "QonosShip2",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.QonosShip2)
    pShips.AddChild(dButtons['QonosShip2'])

    dButtons['QonosShip3'] = CreateStateButton(App.TGString("IKS Ki'Tang: "), "QonosShip3",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.QonosShip3)
    pShips.AddChild(dButtons['QonosShip3'])

    dButtons['FoundersReinforcements'] = CreateButton("Selection:  None", pMusic, pOptionPane, pContentPanel,
                                   __name__ + ".QonosMusicSelection", EventInt=0)

    if DS9FXUnsavedConfig.QonosMusic == 1:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.QonosMusic == 2:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.QonosMusic == 3:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.QonosMusic == 4:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Off"))

    return pMainMenu


def CreateChintokaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Chin'toka Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['ChintokaPlanets'] = CreateStateButton(App.TGString("Planets: "), "ChintokaPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.ChintokaPlanets)
    pPlanets.AddChild(dButtons['ChintokaPlanets'])

    dButtons['ChintokaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "ChintokaNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.ChintokaNanoFX)
    pPlanets.AddChild(dButtons['ChintokaNanoFX'])

    dButtons['ChintokaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "ChintokaMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.ChintokaMapPlanetDetail)
    pPlanets.AddChild(dButtons['ChintokaMapPlanetDetail'])

    dButtons['ChintokaMusic'] = CreateStateButton(App.TGString("Selection: "), "ChintokaMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.ChintokaMusic)
    pMusic.AddChild(dButtons['ChintokaMusic'])

    return pMainMenu


def CreateVelaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Vela Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['VelaMusic'] = CreateStateButton(App.TGString("Selection: "), "VelaMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.VelaMusic)
    pMusic.AddChild(dButtons['VelaMusic'])

    return pMainMenu


def CreateCardassiaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Cardassia Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pShips = App.STCharacterMenu_Create("Ships")
    pMainMenu.AddChild(pShips)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['CardassiaPlanets'] = CreateStateButton(App.TGString("Planets: "), "CardassiaPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaPlanets)
    pPlanets.AddChild(dButtons['CardassiaPlanets'])

    dButtons['CardassiaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "CardassiaNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaNanoFX)
    pPlanets.AddChild(dButtons['CardassiaNanoFX'])

    dButtons['CardassiaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "CardassiaMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.CardassiaMapPlanetDetail)
    pPlanets.AddChild(dButtons['CardassiaMapPlanetDetail'])

    dButtons['CardassiaShip1'] = CreateStateButton(App.TGString("Hutet 1: "), "CardassiaShip1",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaShip1)
    pShips.AddChild(dButtons['CardassiaShip1'])

    dButtons['CardassiaShip2'] = CreateStateButton(App.TGString("Keldon 1: "), "CardassiaShip2",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaShip2)
    pShips.AddChild(dButtons['CardassiaShip2'])

    dButtons['CardassiaShip3'] = CreateStateButton(App.TGString("Keldon 2: "), "CardassiaShip3",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaShip3)
    pShips.AddChild(dButtons['CardassiaShip3'])

    dButtons['CardassiaShip4'] = CreateStateButton(App.TGString("Galor 1: "), "CardassiaShip4",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaShip4)
    pShips.AddChild(dButtons['CardassiaShip4'])

    dButtons['CardassiaShip5'] = CreateStateButton(App.TGString("Galor 2: "), "CardassiaShip5",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CardassiaShip5)
    pShips.AddChild(dButtons['CardassiaShip5'])

    dButtons['CardassiaMusic'] = CreateStateButton(App.TGString("Selection: "), "CardassiaMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.CardassiaMusic)
    pMusic.AddChild(dButtons['CardassiaMusic'])

    return pMainMenu


def CreateTrivasMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Trivas Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['TrivasPlanets'] = CreateStateButton(App.TGString("Planets: "), "TrivasPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TrivasPlanets)
    pPlanets.AddChild(dButtons['TrivasPlanets'])

    dButtons['TrivasNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "TrivasNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.TrivasNanoFX)
    pPlanets.AddChild(dButtons['TrivasNanoFX'])

    dButtons['TrivasMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "TrivasMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.TrivasMapPlanetDetail)
    pPlanets.AddChild(dButtons['TrivasMapPlanetDetail'])

    dButtons['TrivasMusic'] = CreateStateButton(App.TGString("Selection: "), "TrivasMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.TrivasMusic)
    pMusic.AddChild(dButtons['TrivasMusic'])

    return pMainMenu


def CreateSeptimusMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Septimus Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['SeptimusPlanets'] = CreateStateButton(App.TGString("Planets: "), "SeptimusPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.SeptimusPlanets)
    pPlanets.AddChild(dButtons['SeptimusPlanets'])

    dButtons['SeptimusNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "SeptimusNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.SeptimusNanoFX)
    pPlanets.AddChild(dButtons['SeptimusNanoFX'])

    dButtons['SeptimusMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "SeptimusMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.SeptimusMapPlanetDetail)
    pPlanets.AddChild(dButtons['SeptimusMapPlanetDetail'])

    dButtons['SeptimusMusic'] = CreateStateButton(App.TGString("Selection: "), "SeptimusMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.SeptimusMusic)
    pMusic.AddChild(dButtons['SeptimusMusic'])

    return pMainMenu


def CreatePelosaMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Pelosa Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['PelosaPlanets'] = CreateStateButton(App.TGString("Planets: "), "PelosaPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.PelosaPlanets)
    pPlanets.AddChild(dButtons['PelosaPlanets'])

    dButtons['PelosaNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "PelosaNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.PelosaNanoFX)
    pPlanets.AddChild(dButtons['PelosaNanoFX'])

    dButtons['PelosaMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "PelosaMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.PelosaMapPlanetDetail)
    pPlanets.AddChild(dButtons['PelosaMapPlanetDetail'])

    dButtons['PelosaMusic'] = CreateStateButton(App.TGString("Selection: "), "PelosaMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.PelosaMusic)
    pMusic.AddChild(dButtons['PelosaMusic'])

    return pMainMenu


def CreateDonatuMapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Donatu Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pPlanets = App.STCharacterMenu_Create("Planets")
    pMainMenu.AddChild(pPlanets)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['DonatuPlanets'] = CreateStateButton(App.TGString("Planets: "), "DonatuPlanets",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DonatuPlanets)
    pPlanets.AddChild(dButtons['DonatuPlanets'])

    dButtons['DonatuNanoFX'] = CreateStateButton(App.TGString("NanoFX Atmospheres: "), "DonatuNanoFX",
                                        [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DonatuNanoFX)
    pPlanets.AddChild(dButtons['DonatuNanoFX'])

    dButtons['DonatuMapPlanetDetail'] = CreateStateButton(App.TGString("Detail: "), "DonatuMapPlanetDetail",
                                        [App.TGString("Lowest"), App.TGString("Low"), App.TGString("Standard"),
                                         App.TGString("High")], DS9FXUnsavedConfig.DonatuMapPlanetDetail)
    pPlanets.AddChild(dButtons['DonatuMapPlanetDetail'])

    dButtons['DonatuMusic'] = CreateStateButton(App.TGString("Selection: "), "DonatuMusic",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.DonatuMusic)
    pMusic.AddChild(dButtons['DonatuMusic'])

    return pMainMenu


def CreateStarbase375MapRelated(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Starbase 375 Map Related Options")
    pContentPanel.AddChild(pMainMenu)

    pObjects = App.STCharacterMenu_Create("Stations/Ships")
    pMainMenu.AddChild(pObjects)

    pMusic = App.STCharacterMenu_Create("Music")
    pMainMenu.AddChild(pMusic)

    dButtons['Starbase375Starbase'] = CreateStateButton(App.TGString("Starbase 375: "), "Starbase375Starbase",
                                        [App.TGString("No"), App.TGString("Yes")],
                                        DS9FXUnsavedConfig.Starbase375Starbase)
    pObjects.AddChild(dButtons['Starbase375Starbase'])

    dButtons['Starbase375Centaur'] = CreateStateButton(App.TGString("USS Centaur: "), "Starbase375Centaur",
                                        [App.TGString("No"), App.TGString("Yes")],
                                        DS9FXUnsavedConfig.Starbase375Centaur)
    pObjects.AddChild(dButtons['Starbase375Centaur'])

    dButtons['Starbase375Music'] = CreateStateButton(App.TGString("Selection: "), "Starbase375Music",
                                        [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"),
                                         App.TGString("Random")], DS9FXUnsavedConfig.Starbase375Music)
    pMusic.AddChild(dButtons['Starbase375Music'])

    return pMainMenu


def CreateMiscOptions(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Misc Options")
    pContentPanel.AddChild(pMainMenu)

    pMiscOptions = App.STCharacterMenu_Create("Other DS9FX Options")
    pMainMenu.AddChild(pMiscOptions)

    pConsoleDumps = App.STCharacterMenu_Create("Create Console Dumps")
    pMainMenu.AddChild(pConsoleDumps)

    pBCPerfomance = App.STCharacterMenu_Create("BC Performance")
    pMainMenu.AddChild(pBCPerfomance)

    pMovieRelated = App.STCharacterMenu_Create("Mission Videos")
    pMainMenu.AddChild(pMovieRelated)

    pMovieOverrides = App.STCharacterMenu_Create("Movie Overrides")
    pMainMenu.AddChild(pMovieOverrides)

    pLifeSupport = App.STCharacterMenu_Create("Life Support")
    pMainMenu.AddChild(pLifeSupport)

    pSuns = App.STCharacterMenu_Create("Suns")
    pMainMenu.AddChild(pSuns)

    pGameFixes = App.STCharacterMenu_Create("Game Fixes")
    pMainMenu.AddChild(pGameFixes)

    pMutatorFix = App.STCharacterMenu_Create("Mutator Functions")
    pMainMenu.AddChild(pMutatorFix)

    dButtons['DebugMode'] = CreateOnOffButton(App.TGString("Via Keyboard Shortcut: "), "DebugMode",
                                       DS9FXUnsavedConfig.DebugMode)
    pConsoleDumps.AddChild(dButtons['DebugMode'])

    dButtons['DisableLocalForces'] = CreateOnOffButton(App.TGString("Disable Local Forces In Missions: "), "DisableLocalForces",
                                       DS9FXUnsavedConfig.DisableLocalForces)
    pMiscOptions.AddChild(dButtons['DisableLocalForces'])

    dButtons['ExitGameDebugMode'] = CreateOnOffButton(App.TGString("On Exit To Windows: "), "ExitGameDebugMode",
                                       DS9FXUnsavedConfig.ExitGameDebugMode)
    pConsoleDumps.AddChild(dButtons['ExitGameDebugMode'])

    dButtons['StabilizeBC'] = CreateOnOffButton(App.TGString("Memory Cleaning: "), "StabilizeBC", DS9FXUnsavedConfig.StabilizeBC)
    pBCPerfomance.AddChild(dButtons['StabilizeBC'])

    dButtons['ModelPreloadingSelection'] = CreateOnOffButton(App.TGString("Model Preloading (DS9FX): "), "ModelPreloadingSelection",
                                       DS9FXUnsavedConfig.ModelPreloadingSelection)
    pBCPerfomance.AddChild(dButtons['ModelPreloadingSelection'])

    dButtons['IntroVid'] = CreateOnOffButton(App.TGString("Intro: "), "IntroVid", DS9FXUnsavedConfig.IntroVid)
    pMovieRelated.AddChild(dButtons['IntroVid'])

    dButtons['CompletionVid'] = CreateOnOffButton(App.TGString("Completion: "), "CompletionVid", DS9FXUnsavedConfig.CompletionVid)
    pMovieRelated.AddChild(dButtons['CompletionVid'])

    dButtons['IntroOverride'] = CreateButton("Intro Override:  None", pMovieOverrides, pOptionPane, pContentPanel,
                                  __name__ + ".SetIntroOverride", EventInt=0)
    for k, v in dIntro.items():
        if (v[1] == DS9FXUnsavedConfig.IntroMovieSel):
            dButtons['IntroOverride'].SetName(App.TGString("Intro Override:  " + v[0]))
            break

    dButtons['NoDamageThroughShields'] = CreateStateButton(App.TGString("No Dmg Through Shields: "), "NoDamageThroughShields",
                                        [App.TGString("Off"), App.TGString("On")],
                                        DS9FXUnsavedConfig.NoDamageThroughShields)
    pLifeSupport.AddChild(dButtons['NoDamageThroughShields'])

    dButtons['LifeSupport'] = CreateStateButton(App.TGString("Life Support: "), "LifeSupport",
                                       [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.LifeSupport)
    pLifeSupport.AddChild(dButtons['LifeSupport'])

    dButtons['LifeSupportCrewLabels'] = CreateStateButton(App.TGString("Crew Counter Labels: "), "LifeSupportCrewLabels",
                                       [App.TGString("Off"), App.TGString("On")],
                                       DS9FXUnsavedConfig.LifeSupportCrewLabels)
    pLifeSupport.AddChild(dButtons['LifeSupportCrewLabels'])

    dButtons['LifeSupportCombatEffectiveness'] = CreateStateButton(App.TGString("Combat Effectiveness: "), "LifeSupportCombatEffectiveness",
                                       [App.TGString("Off"), App.TGString("On")],
                                       DS9FXUnsavedConfig.LifeSupportCombatEffectiveness)
    pLifeSupport.AddChild(dButtons['LifeSupportCombatEffectiveness'])

    dButtons['AIBoardings'] = CreateStateButton(App.TGString("AI Boarding Parties: "), "AIBoardings",
                                        [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.AIBoardings)
    pLifeSupport.AddChild(dButtons['AIBoardings'])

    dButtons['SunStreaks'] = CreateStateButton(App.TGString("Sun Streaks: "), "SunStreaks",
                                        [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.SunStreaks)
    pSuns.AddChild(dButtons['SunStreaks'])

    dButtons['NanoFXExplosionFix'] = CreateStateButton(App.TGString("NanoFX Explosion Fix: "), "NanoFXExplosionFix",
                                       [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.NanoFXExplosionFix)
    pGameFixes.AddChild(dButtons['NanoFXExplosionFix'])

    dButtons['ExitGameFix'] = CreateStateButton(App.TGString("Exit Mission Fix: "), "ExitGameFix",
                                       [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.ExitGameFix)
    pGameFixes.AddChild(dButtons['ExitGameFix'])

    dButtons['TransporterFix'] = CreateStateButton(App.TGString("Transporter Fix: "), "TransporterFix",
                                       [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.TransporterFix)
    pGameFixes.AddChild(dButtons['TransporterFix'])

    dButtons['AutoMutatorBackup'] = CreateOnOffButton(App.TGString("Auto Mutator Backup: "), "AutoMutatorBackup",
                                       DS9FXUnsavedConfig.AutoMutatorBackup)
    pMutatorFix.AddChild(dButtons['AutoMutatorBackup'])

    dButtons['SaveFdtnConfig'] = CreateButton("Create Mutator Backup", pMutatorFix, pOptionPane, pContentPanel,
                                  __name__ + ".SaveFdtnConfig", EventInt=0)
    dButtons['RestoreFdtnConfig'] = CreateButton("Restore Mutator Backup", pMutatorFix, pOptionPane, pContentPanel,
                                  __name__ + ".RestoreFdtnConfig", EventInt=0)
    dButtons['EnableAllMutators'] = CreateButton("Enable All Mutators", pMutatorFix, pOptionPane, pContentPanel,
                                  __name__ + ".EnableAllMutators", EventInt=0)
    dButtons['DisableAllMutators'] = CreateButton("Disable All Mutators", pMutatorFix, pOptionPane, pContentPanel,
                                  __name__ + ".DisableAllMutators", EventInt=0)

    return pMainMenu


def CreateSaveConfig(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("DS9FX Configuration Options")
    pContentPanel.AddChild(pMainMenu)

    pAutoConfig = App.STCharacterMenu_Create("Auto Configuration")
    pMainMenu.AddChild(pAutoConfig)

    pSaveConfig = App.STCharacterMenu_Create("Save Configuration")
    pMainMenu.AddChild(pSaveConfig)

    pRefreshConfig = App.STCharacterMenu_Create("Refresh Configuration")
    pMainMenu.AddChild(pRefreshConfig)

    pPresetConfig = App.STCharacterMenu_Create("Preset Configuration")
    pMainMenu.AddChild(pPresetConfig)

    dButtons['InstantConfigSave'] = CreateOnOffButton(App.TGString("Auto Apply Settings: "), "InstantConfigSave",
                                        DS9FXUnsavedConfig.InstantConfigSave)
    pAutoConfig.AddChild(dButtons['InstantConfigSave'])

    dButtons['SaveConfig'] = CreateButton("Apply New Settings", pSaveConfig, pOptionPane, pContentPanel,
                                  __name__ + ".SaveConfig", EventInt=0)
    dButtons['RefreshConfig'] = CreateButton("Refresh Settings", pRefreshConfig, pOptionPane, pContentPanel,
                                  __name__ + ".RefreshConfig", EventInt=0)
    dButtons['HighestSettings'] = CreateButton("Highest Settings", pPresetConfig, pOptionPane, pContentPanel,
                                  __name__ + ".HighestSettings", EventInt=0)
    dButtons['HighSettings'] = CreateButton("High Settings", pPresetConfig, pOptionPane, pContentPanel,
                                   __name__ + ".HighSettings", EventInt=0)
    dButtons['MediumSettings'] = CreateButton("Medium Settings", pPresetConfig, pOptionPane, pContentPanel,
                                   __name__ + ".MediumSettings", EventInt=0)
    dButtons['LowSettings'] = CreateButton("Low Settings", pPresetConfig, pOptionPane, pContentPanel, __name__ + ".LowSettings",
                                   EventInt=0)
    dButtons['LowestSettings'] = CreateButton("Lowest Settings", pPresetConfig, pOptionPane, pContentPanel,
                                   __name__ + ".LowestSettings", EventInt=0)

    return pMainMenu


def CreateExtras(pOptionPane, pContentPanel):
    global dButtons

    pMainMenu = App.STCharacterMenu_Create("Extras\Tutorials")
    pContentPanel.AddChild(pMainMenu)

    dButtons['ExtraVid1'] = CreateButton("Completion Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid1",
                                  EventInt=0)
    dButtons['ExtraVid7'] = CreateButton("Xtended Completion Video", pMainMenu, pOptionPane, pContentPanel,
                                  __name__ + ".ExtraVid7", EventInt=0)
    dButtons['ExtraVid8'] = CreateButton("Xtended 1.1 Completion Video", pMainMenu, pOptionPane, pContentPanel,
                                   __name__ + ".ExtraVid8", EventInt=0)
    dButtons['ExtraVid2'] = CreateButton("Intro Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid2",
                                  EventInt=0)
    dButtons['ExtraVid6'] = CreateButton("Xtended Intro Video", pMainMenu, pOptionPane, pContentPanel,
                                   __name__ + ".ExtraVid6", EventInt=0)
    dButtons['ExtraVid9'] = CreateButton("Xtended 1.1 Intro Video", pMainMenu, pOptionPane, pContentPanel,
                                   __name__ + ".ExtraVid9", EventInt=0)
    dButtons['ExtraVid5'] = CreateButton("Trailer Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid5",
                                  EventInt=0)
    dButtons['ExtraVid3'] = CreateButton("Wormhole Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid3",
                                  EventInt=0)
    dButtons['ExtraVid4'] = CreateButton("Tutorial Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid4",
                                  EventInt=0)

    return pMainMenu


def SaveFdtnConfig(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
    FoundationMutatorFix.SaveBackup()


def RestoreFdtnConfig(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
    FoundationMutatorFix.RestoreFoundationSettings()

    import MainMenu.mainmenu
    MainMenu.mainmenu.SwitchMiddlePane("Configure")


def EnableAllMutators(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXLib import FoundationMutatorActivation
    FoundationMutatorActivation.EnableMutators()

    import MainMenu.mainmenu
    MainMenu.mainmenu.SwitchMiddlePane("Configure")


def DisableAllMutators(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXLib import FoundationMutatorActivation
    FoundationMutatorActivation.DisableMutators()

    import MainMenu.mainmenu
    MainMenu.mainmenu.SwitchMiddlePane("Configure")


def ExtraVid1(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasCompletionVid
    DS9FXExtrasCompletionVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid2(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasIntroVid
    DS9FXExtrasIntroVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid3(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasWormholeVid
    DS9FXExtrasWormholeVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid4(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasTutorialVid
    DS9FXExtrasTutorialVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid5(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasTrailerVid
    DS9FXExtrasTrailerVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid6(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasXtendedIntroVid
    DS9FXExtrasXtendedIntroVid.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid7(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasCompletionVid2
    DS9FXExtrasCompletionVid2.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid8(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasCompletionVid3
    DS9FXExtrasCompletionVid3.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def ExtraVid9(pObject, pEvent):
    PlayButtonClickedSound()

    from Custom.DS9FX.DS9FXVids import DS9FXExtrasXtendedIntroVid2
    DS9FXExtrasXtendedIntroVid2.PlayMovieSeq()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def DS9FXCredits(pObject, pEvent):
    PlayCreditsButtonClickedSound()

    from Custom.DS9FX.DS9FXPrompts import DS9FXCreditsPrompt
    DS9FXCreditsPrompt.Prompt()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SelectModel(pObject, pEvent):
    DS9FXUnsavedConfig.WormholeSelection = DS9FXUnsavedConfig.WormholeSelection + 1

    if DS9FXUnsavedConfig.WormholeSelection >= 8:
        DS9FXUnsavedConfig.WormholeSelection = 0

    SetModelConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetModelConfig():
    global dButtons

    if DS9FXUnsavedConfig.WormholeSelection == 1:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  2"))

    elif DS9FXUnsavedConfig.WormholeSelection == 2:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  3"))

    elif DS9FXUnsavedConfig.WormholeSelection == 3:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  4"))

    elif DS9FXUnsavedConfig.WormholeSelection == 4:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  5"))

    elif DS9FXUnsavedConfig.WormholeSelection == 5:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  6"))

    elif DS9FXUnsavedConfig.WormholeSelection == 6:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  7"))

    elif DS9FXUnsavedConfig.WormholeSelection == 7:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  8"))

    else:
        dButtons['WormholeSelection'].SetName(App.TGString("Model:  1"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def InsideWormholeBack(pObject, pEvent):
    DS9FXUnsavedConfig.InsideWormholeBackgroundTexture = DS9FXUnsavedConfig.InsideWormholeBackgroundTexture + 1

    if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture >= 7:
        DS9FXUnsavedConfig.InsideWormholeBackgroundTexture = 0

    SetWormholeBackConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetWormholeBackConfig():
    global dButtons

    if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 1:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Red"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 2:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Chrome"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 3:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Dark Blue"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 4:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Water Blue"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 5:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Weird"))

    elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 6:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  None"))

    else:
        dButtons['InsideWormholeBackgroundTexture'].SetName(App.TGString("Background:  Blue"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def InsideWormholeModels(pObject, pEvent):
    DS9FXUnsavedConfig.InsideWormholeModel = DS9FXUnsavedConfig.InsideWormholeModel + 1

    if DS9FXUnsavedConfig.InsideWormholeModel >= 6:
        DS9FXUnsavedConfig.InsideWormholeModel = 0

    SetWormholeModelConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetWormholeModelConfig():
    global dButtons

    if DS9FXUnsavedConfig.InsideWormholeModel == 1:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Yellow"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 2:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Red Dawn"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 3:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Slipstream"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 4:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  Blackhole"))

    elif DS9FXUnsavedConfig.InsideWormholeModel == 5:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  DS9 Series Rev."))

    else:
        dButtons['InsideWormholeModel'].SetName(App.TGString("Variant:  DS9 Series"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def DS9MusicSelection(pObject, pEvent):
    DS9FXUnsavedConfig.DS9Music = DS9FXUnsavedConfig.DS9Music + 1

    if DS9FXUnsavedConfig.DS9Music >= 5:
        DS9FXUnsavedConfig.DS9Music = 0

    SetDS9MusicSelectionConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetDS9MusicSelectionConfig():
    global dButtons

    if DS9FXUnsavedConfig.DS9Music == 1:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.DS9Music == 2:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.DS9Music == 3:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.DS9Music == 4:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['DS9MusicSelection'].SetName(App.TGString("Selection:  Off"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def FoundersMusicSelection(pObject, pEvent):
    DS9FXUnsavedConfig.FoundersMusic = DS9FXUnsavedConfig.FoundersMusic + 1

    if DS9FXUnsavedConfig.FoundersMusic >= 5:
        DS9FXUnsavedConfig.FoundersMusic = 0

    SetFoundersMusicSelectionConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetFoundersMusicSelectionConfig():
    global dButtons

    if DS9FXUnsavedConfig.FoundersMusic == 1:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.FoundersMusic == 2:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.FoundersMusic == 3:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.FoundersMusic == 4:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Off"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def QonosMusicSelection(pObject, pEvent):
    DS9FXUnsavedConfig.QonosMusic = DS9FXUnsavedConfig.QonosMusic + 1

    if DS9FXUnsavedConfig.QonosMusic >= 5:
        DS9FXUnsavedConfig.QonosMusic = 0

    SetQonosMusicSelectionConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetQonosMusicSelectionConfig():
    global dButtons

    if DS9FXUnsavedConfig.QonosMusic == 1:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 1"))

    elif DS9FXUnsavedConfig.QonosMusic == 2:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 2"))

    elif DS9FXUnsavedConfig.QonosMusic == 3:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Music 3"))

    elif DS9FXUnsavedConfig.QonosMusic == 4:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Random"))

    else:
        dButtons['FoundersReinforcements'].SetName(App.TGString("Selection:  Off"))

    App.g_kSoundManager.StopSound("DS9FXClicked")

    SaveTempConfig()


def SetIntroOverride(pObject, pEvent):
    global dButtons

    for k, v in dIntro.items():
        iCounter = k + 1
        if (v[1] == DS9FXUnsavedConfig.IntroMovieSel):
            break

    val = len(dIntro.keys()) - 1  # fuck python 1.5
    if (iCounter > val):
        iCounter = 0

    dButtons['IntroOverride'].SetName(App.TGString("Intro Override:  " + dIntro[iCounter][0]))
    DS9FXUnsavedConfig.IntroMovieSel = dIntro[iCounter][1]
    App.g_kSoundManager.StopSound("DS9FXClicked")
    SaveTempConfig()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def SetEasterEggs(bState):
    DS9FXUnsavedConfig.EasterEggs = bState
    DS9FXConfigsManager(DS9FXUnsavedConfig, sUnsavedPath, DS9FXUnsavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=1)
    DS9FXConfigsManager(DS9FXUnsavedConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=1)


def SetMirrorUniverse(bFed, bDom):
    DS9FXUnsavedConfig.FederationSide = bFed
    DS9FXUnsavedConfig.DominionSide = bDom
    DS9FXConfigsManager(DS9FXUnsavedConfig, sUnsavedPath, DS9FXUnsavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=1)
    DS9FXConfigsManager(DS9FXUnsavedConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=1)


def HandleStateButton(pObject, pEvent):
    DS9FXUnsavedConfig.__dict__[pEvent.GetCString()] = App.STToggle_Cast(pEvent.GetSource()).GetState()
    App.g_kSoundManager.StopSound("DS9FXClicked")
    SaveTempConfig()
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def HandleOnOffButton(pObject, pEvent):
    DS9FXUnsavedConfig.__dict__[pEvent.GetCString()] = App.STToggle_Cast(pEvent.GetSource()).GetState()
    App.g_kSoundManager.StopSound("DS9FXClicked")
    SaveTempConfig()
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def CreateStateButton(pName, sVar, lStates, iState):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    kArgs = [pName, iState]
    kEvents = []
    for kStateName in lStates:
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_STATE_BUTTON)
        pEvent.SetDestination(pOptionsWindow)
        pEvent.SetString(sVar)

        kArgs.append(kStateName)
        kArgs.append(pEvent)
        kEvents.append(pEvent)
    kMenuButton = apply(App.STToggle_CreateW, kArgs)
    for pEvent in kEvents:
        pEvent.SetSource(kMenuButton)

    return kMenuButton


def CreateOnOffButton(pName, sVar, iState):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOffEvent = App.TGStringEvent_Create()
    pOnEvent = App.TGStringEvent_Create()
    pOffEvent.SetString(sVar)
    pOnEvent.SetString(sVar)
    pOffEvent.SetEventType(ET_ONOFF_BUTTON)
    pOnEvent.SetEventType(ET_ONOFF_BUTTON)
    pOffEvent.SetDestination(pOptionsWindow)
    pOnEvent.SetDestination(pOptionsWindow)

    pMenuButton = App.STToggle_CreateW(pName, iState, App.TGString("Off"), pOnEvent, App.TGString("On"), pOffEvent)
    pOffEvent.SetSource(pMenuButton)
    pOnEvent.SetSource(pMenuButton)

    return pMenuButton


def CreateButton(sButtonName, pMenu, pOptionPane, pContentPanel, sFunction, EventInt=0):
    ET_EVENT = App.UtopiaModule_GetNextEventType()

    pOptionPane.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_EVENT)
    pEvent.SetDestination(pOptionPane)
    pEvent.SetString(sButtonName)

    pButton = App.STButton_Create(sButtonName, pEvent)
    pButton.SetChosen(0)

    pEvent.SetSource(pButton)
    pMenu.AddChild(pButton)

    return pButton


def PlayButtonClickedSound():
    App.g_kSoundManager.PlaySound("DS9FXClicked")


def PlayConfigSavedSound():
    App.g_kSoundManager.PlaySound("DS9FXSaved")


def PlayCreditsButtonClickedSound():
    App.g_kSoundManager.PlaySound("DS9FXClicked2")


def SaveTempConfig():
    DS9FXConfigsManager(DS9FXUnsavedConfig, sUnsavedPath, DS9FXUnsavedConfig, bDisableButtons=1, bPlaySound=1,
                        bPlayConfigSound=0, bStartTimer=1, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=0)
    if DS9FXSavedConfig.InstantConfigSave == 1:
        DS9FXConfigsManager(DS9FXUnsavedConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0,
                            bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                            bBackupMutators=0, bSilentMutatorBackup=1)


def DisableMyButtons():
    global dButtons

    for k in dButtons.keys():
        dButtons[k].SetDisabled()


def KillTimerInstance():
    global idTimer
    App.g_kRealtimeTimerManager.DeleteTimer(idTimer)
    idTimer = App.NULL_ID


def ResetButtons(pObject, pEvent):
    global dButtons

    # Fixes a game crash if the user promptly switches tabs after selection
    import MainMenu.mainmenu
    m = MainMenu.mainmenu
    if m.g_kCurrentMiddlePane != 4:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    for k in dButtons.keys():
        dButtons[k].SetEnabled()

    CheckShownOptions()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)


def RefreshConfig(pObject, pEvent):
    DS9FXConfigsManager(DS9FXSavedConfig, sUnsavedPath, DS9FXUnsavedConfig, bDisableButtons=0, bPlaySound=1,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=1, bHackUMM=1, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=0)


def SaveConfig(pObject, pEvent):
    DS9FXConfigsManager(DS9FXUnsavedConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=1, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=1,
                        bBackupMutators=1, bSilentMutatorBackup=0)


def CorrectConfig():
    DS9FXConfigsManager(DS9FXSavedConfig, sUnsavedPath, DS9FXUnsavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=0)


def HighestSettings(pObject, pEvent):
    DS9FXConfigsManager(DS9FXHighestConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0,
                        bPlayConfigSound=0, bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0,
                        bBackupMutators=0, bSilentMutatorBackup=0)
    RefreshConfig(None, None)


def HighSettings(pObject, pEvent):
    DS9FXConfigsManager(DS9FXHighConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0, bPlayConfigSound=0,
                        bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0, bBackupMutators=0,
                        bSilentMutatorBackup=0)
    RefreshConfig(None, None)


def MediumSettings(pObject, pEvent):
    DS9FXConfigsManager(DS9FXMedConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0, bPlayConfigSound=0,
                        bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0, bBackupMutators=0,
                        bSilentMutatorBackup=0)
    RefreshConfig(None, None)


def LowSettings(pObject, pEvent):
    DS9FXConfigsManager(DS9FXLowConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0, bPlayConfigSound=0,
                        bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0, bBackupMutators=0,
                        bSilentMutatorBackup=0)
    RefreshConfig(None, None)


def LowestSettings(pObject, pEvent):
    DS9FXConfigsManager(DS9FXLowestConfig, sPath, DS9FXSavedConfig, bDisableButtons=0, bPlaySound=0, bPlayConfigSound=0,
                        bStartTimer=0, bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0, bBackupMutators=0,
                        bSilentMutatorBackup=0)
    RefreshConfig(None, None)


def CheckShownOptions():
    global dButtons

    bMenu25 = None
    bMenu28 = None
    bMenu29 = None

    if DS9FXUnsavedConfig.DS9Planets == 1:
        if not dButtons['DS9NanoFX'].IsEnabled():
            dButtons['DS9NanoFX'].SetEnabled()
        if not dButtons['DS9MapPlanetDetail'].IsEnabled():
            dButtons['DS9MapPlanetDetail'].SetEnabled()
    else:
        if dButtons['DS9NanoFX'].IsEnabled():
            dButtons['DS9NanoFX'].SetDisabled()
        if dButtons['DS9MapPlanetDetail'].IsEnabled():
            dButtons['DS9MapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.GammaPlanets == 1:
        if not dButtons['GammaNanoFX'].IsEnabled():
            dButtons['GammaNanoFX'].SetEnabled()
        if not dButtons['GammaMapPlanetDetail'].IsEnabled():
            dButtons['GammaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['GammaNanoFX'].IsEnabled():
            dButtons['GammaNanoFX'].SetDisabled()
        if dButtons['GammaMapPlanetDetail'].IsEnabled():
            dButtons['GammaMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.CometSelection == 1:
        if not dButtons['CometAlphaTrail'].IsEnabled():
            dButtons['CometAlphaTrail'].SetEnabled()
        if not dButtons['CometAlphaTrailTexture'].IsEnabled():
            dButtons['CometAlphaTrailTexture'].SetEnabled()
    else:
        if dButtons['CometAlphaTrail'].IsEnabled():
            dButtons['CometAlphaTrail'].SetDisabled()
        if dButtons['CometAlphaTrailTexture'].IsEnabled():
            dButtons['CometAlphaTrailTexture'].SetDisabled()

    if DS9FXUnsavedConfig.RandomEnemyFleetAttacks == 1:
        if not dButtons['RandomDomStrength'].IsEnabled():
            dButtons['RandomDomStrength'].SetEnabled()
        if not dButtons['DominionTimeSpan'].IsEnabled():
            dButtons['DominionTimeSpan'].SetEnabled()
        if not dButtons['KillRandomFleetsDuringMission'].IsEnabled():
            dButtons['KillRandomFleetsDuringMission'].SetEnabled()
        if not dButtons['MaxRandShips'].IsEnabled():
            dButtons['MaxRandShips'].SetEnabled()
    else:
        if dButtons['RandomDomStrength'].IsEnabled():
            dButtons['RandomDomStrength'].SetDisabled()
        if dButtons['DominionTimeSpan'].IsEnabled():
            dButtons['DominionTimeSpan'].SetDisabled()
        if dButtons['KillRandomFleetsDuringMission'].IsEnabled():
            dButtons['KillRandomFleetsDuringMission'].SetDisabled()
        if dButtons['MaxRandShips'].IsEnabled():
            dButtons['MaxRandShips'].SetDisabled()

    if DS9FXUnsavedConfig.FederationSide == 1:
        if not dButtons['IntroVid'].IsEnabled():
            bMenu28 = 1
            dButtons['IntroVid'].SetEnabled()
        if not dButtons['CompletionVid'].IsEnabled():
            bMenu29 = 1
            dButtons['CompletionVid'].SetEnabled()
    else:
        if dButtons['IntroVid'].IsEnabled():
            bMenu28 = 0
            dButtons['IntroVid'].SetDisabled()
        if dButtons['CompletionVid'].IsEnabled():
            bMenu29 = 0
            dButtons['CompletionVid'].SetDisabled()

    if DS9FXUnsavedConfig.DominionSide == 1:
        if dButtons['DomIS'].IsEnabled():
            bMenu25 = 0
            dButtons['DomIS'].SetDisabled()
        if dButtons['IntroVid'].IsEnabled():
            if not bMenu28 == 1 or bMenu28 == None:
                dButtons['IntroVid'].SetDisabled()
        if dButtons['CompletionVid'].IsEnabled():
            if not bMenu29 == 1 or bMenu29 == None:
                dButtons['CompletionVid'].SetDisabled()
    else:
        if not dButtons['DomIS'].IsEnabled():
            bMenu25 = 1
            dButtons['DomIS'].SetEnabled()
        if not dButtons['IntroVid'].IsEnabled():
            if not bMenu28 == 0 or bMenu28 == None:
                dButtons['IntroVid'].SetEnabled()
        if not dButtons['IntroVid'].IsEnabled():
            if not bMenu29 == 0 or bMenu29 == None:
                dButtons['CompletionVid'].SetEnabled()

    if (DS9FXUnsavedConfig.Bugship1Selection == 0) and (DS9FXUnsavedConfig.Bugship2Selection == 0) and (
            DS9FXUnsavedConfig.Bugship3Selection == 0):
        if dButtons['DomIS'].IsEnabled():
            if not bMenu25 == 1 or bMenu25 == None:
                dButtons['DomIS'].SetDisabled()
    else:
        if not dButtons['DomIS'].IsEnabled():
            if not bMenu25 == 0 or bMenu25 == None:
                dButtons['DomIS'].SetEnabled()

    if DS9FXUnsavedConfig.BadlandsBackground == 1:
        if not dButtons['BadlandsBackground2Res'].IsEnabled():
            dButtons['BadlandsBackground2Res'].SetEnabled()
    else:
        if dButtons['BadlandsBackground2Res'].IsEnabled():
            dButtons['BadlandsBackground2Res'].SetDisabled()

    if DS9FXUnsavedConfig.BadlandsVortex == 0:
        if dButtons['BadlandsVortexVariant'].IsEnabled():
            dButtons['BadlandsVortexVariant'].SetDisabled()
        if dButtons['BadlandsDamageFX'].IsEnabled():
            dButtons['BadlandsDamageFX'].SetDisabled()
    else:
        if not dButtons['BadlandsVortexVariant'].IsEnabled():
            dButtons['BadlandsVortexVariant'].SetEnabled()
        if not dButtons['BadlandsDamageFX'].IsEnabled():
            dButtons['BadlandsDamageFX'].SetEnabled()

    if DS9FXUnsavedConfig.LifeSupport == 0:
        if dButtons['LifeSupportCrewLabels'].IsEnabled():
            dButtons['LifeSupportCrewLabels'].SetDisabled()
        if dButtons['LifeSupportCombatEffectiveness'].IsEnabled():
            dButtons['LifeSupportCombatEffectiveness'].SetDisabled()
        if dButtons['AIBoardings'].IsEnabled():
            dButtons['AIBoardings'].SetDisabled()
    else:
        if not dButtons['LifeSupportCrewLabels'].IsEnabled():
            dButtons['LifeSupportCrewLabels'].SetEnabled()
        if not dButtons['LifeSupportCombatEffectiveness'].IsEnabled():
            dButtons['LifeSupportCombatEffectiveness'].SetEnabled()
        if not dButtons['AIBoardings'].IsEnabled():
            dButtons['AIBoardings'].SetEnabled()

    if DS9FXUnsavedConfig.KaremmaPlanets == 1:
        if not dButtons['KaremmaNanoFX'].IsEnabled():
            dButtons['KaremmaNanoFX'].SetEnabled()
        if not dButtons['KaremmaMapPlanetDetail'].IsEnabled():
            dButtons['KaremmaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['KaremmaNanoFX'].IsEnabled():
            dButtons['KaremmaNanoFX'].SetDisabled()
        if dButtons['KaremmaMapPlanetDetail'].IsEnabled():
            dButtons['KaremmaMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.DosiPlanets == 1:
        if not dButtons['DosiNanoFX'].IsEnabled():
            dButtons['DosiNanoFX'].SetEnabled()
        if not dButtons['DosiMapPlanetDetail'].IsEnabled():
            dButtons['DosiMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['DosiNanoFX'].IsEnabled():
            dButtons['DosiNanoFX'].SetDisabled()
        if dButtons['DosiMapPlanetDetail'].IsEnabled():
            dButtons['DosiMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.YaderaPlanets == 1:
        if not dButtons['YaderaNanoFX'].IsEnabled():
            dButtons['YaderaNanoFX'].SetEnabled()
        if not dButtons['YaderaMapPlanetDetail'].IsEnabled():
            dButtons['YaderaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['YaderaNanoFX'].IsEnabled():
            dButtons['YaderaNanoFX'].SetDisabled()
        if dButtons['YaderaMapPlanetDetail'].IsEnabled():
            dButtons['YaderaMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.NewBajorPlanets == 1:
        if not dButtons['NewBajorNanoFX'].IsEnabled():
            dButtons['NewBajorNanoFX'].SetEnabled()
        if not dButtons['NewBajorMapPlanetDetail'].IsEnabled():
            dButtons['NewBajorMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['NewBajorNanoFX'].IsEnabled():
            dButtons['NewBajorNanoFX'].SetDisabled()
        if dButtons['NewBajorMapPlanetDetail'].IsEnabled():
            dButtons['NewBajorMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.GaiaPlanets == 1:
        if not dButtons['86'].IsEnabled():
            dButtons['86'].SetEnabled()
        if not dButtons['87'].IsEnabled():
            dButtons['87'].SetEnabled()
    else:
        if dButtons['86'].IsEnabled():
            dButtons['86'].SetDisabled()
        if dButtons['87'].IsEnabled():
            dButtons['87'].SetDisabled()

    if DS9FXUnsavedConfig.KurrillPlanets == 1:
        if not dButtons['KurrillNanoFX'].IsEnabled():
            dButtons['KurrillNanoFX'].SetEnabled()
        if not dButtons['91'].IsEnabled():
            dButtons['91'].SetEnabled()
    else:
        if dButtons['KurrillNanoFX'].IsEnabled():
            dButtons['KurrillNanoFX'].SetDisabled()
        if dButtons['91'].IsEnabled():
            dButtons['91'].SetDisabled()

    if DS9FXUnsavedConfig.TrialusPlanets == 1:
        if not dButtons['TrialusNanoFX'].IsEnabled():
            dButtons['TrialusNanoFX'].SetEnabled()
        if not dButtons['TrialusMapPlanetDetail'].IsEnabled():
            dButtons['TrialusMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['TrialusNanoFX'].IsEnabled():
            dButtons['TrialusNanoFX'].SetDisabled()
        if dButtons['TrialusMapPlanetDetail'].IsEnabled():
            dButtons['TrialusMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.TRogoranPlanets == 1:
        if not dButtons['TRogoranNanoFX'].IsEnabled():
            dButtons['TRogoranNanoFX'].SetEnabled()
        if not dButtons['TRogoranMapPlanetDetail'].IsEnabled():
            dButtons['TRogoranMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['TRogoranNanoFX'].IsEnabled():
            dButtons['TRogoranNanoFX'].SetDisabled()
        if dButtons['TRogoranMapPlanetDetail'].IsEnabled():
            dButtons['TRogoranMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.VandrosPlanets == 1:
        if not dButtons['VandrosNanoFX'].IsEnabled():
            dButtons['VandrosNanoFX'].SetEnabled()
        if not dButtons['VandrosMapPlanetDetail'].IsEnabled():
            dButtons['VandrosMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['VandrosNanoFX'].IsEnabled():
            dButtons['VandrosNanoFX'].SetDisabled()
        if dButtons['VandrosMapPlanetDetail'].IsEnabled():
            dButtons['VandrosMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.FoundersPlanets == 1:
        if not dButtons['FoundersNanoFX'].IsEnabled():
            dButtons['FoundersNanoFX'].SetEnabled()
        if not dButtons['FoundersMapPlanetDetail'].IsEnabled():
            dButtons['FoundersMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['FoundersNanoFX'].IsEnabled():
            dButtons['FoundersNanoFX'].SetDisabled()
        if dButtons['FoundersMapPlanetDetail'].IsEnabled():
            dButtons['FoundersMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.QonosPlanets == 1:
        if not dButtons['QonosNanoFX'].IsEnabled():
            dButtons['QonosNanoFX'].SetEnabled()
        if not dButtons['QonosMapPlanetDetail'].IsEnabled():
            dButtons['QonosMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['QonosNanoFX'].IsEnabled():
            dButtons['QonosNanoFX'].SetDisabled()
        if dButtons['QonosMapPlanetDetail'].IsEnabled():
            dButtons['QonosMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.ChintokaPlanets == 1:
        if not dButtons['ChintokaNanoFX'].IsEnabled():
            dButtons['ChintokaNanoFX'].SetEnabled()
        if not dButtons['ChintokaMapPlanetDetail'].IsEnabled():
            dButtons['ChintokaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['ChintokaNanoFX'].IsEnabled():
            dButtons['ChintokaNanoFX'].SetDisabled()
        if dButtons['ChintokaMapPlanetDetail'].IsEnabled():
            dButtons['ChintokaMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.CardassiaPlanets == 1:
        if not dButtons['CardassiaNanoFX'].IsEnabled():
            dButtons['CardassiaNanoFX'].SetEnabled()
        if not dButtons['CardassiaMapPlanetDetail'].IsEnabled():
            dButtons['CardassiaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['CardassiaNanoFX'].IsEnabled():
            dButtons['CardassiaNanoFX'].SetDisabled()
        if dButtons['CardassiaMapPlanetDetail'].IsEnabled():
            dButtons['CardassiaMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.TrivasPlanets == 1:
        if not dButtons['TrivasNanoFX'].IsEnabled():
            dButtons['TrivasNanoFX'].SetEnabled()
        if not dButtons['TrivasMapPlanetDetail'].IsEnabled():
            dButtons['TrivasMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['TrivasNanoFX'].IsEnabled():
            dButtons['TrivasNanoFX'].SetDisabled()
        if dButtons['TrivasMapPlanetDetail'].IsEnabled():
            dButtons['TrivasMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.SeptimusPlanets == 1:
        if not dButtons['SeptimusNanoFX'].IsEnabled():
            dButtons['SeptimusNanoFX'].SetEnabled()
        if not dButtons['SeptimusMapPlanetDetail'].IsEnabled():
            dButtons['SeptimusMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['SeptimusNanoFX'].IsEnabled():
            dButtons['SeptimusNanoFX'].SetDisabled()
        if dButtons['SeptimusMapPlanetDetail'].IsEnabled():
            dButtons['SeptimusMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.DonatuPlanets == 1:
        if not dButtons['DonatuNanoFX'].IsEnabled():
            dButtons['DonatuNanoFX'].SetEnabled()
        if not dButtons['DonatuMapPlanetDetail'].IsEnabled():
            dButtons['DonatuMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['DonatuNanoFX'].IsEnabled():
            dButtons['DonatuNanoFX'].SetDisabled()
        if dButtons['DonatuMapPlanetDetail'].IsEnabled():
            dButtons['DonatuMapPlanetDetail'].SetDisabled()

    if DS9FXUnsavedConfig.PelosaPlanets == 1:
        if not dButtons['PelosaNanoFX'].IsEnabled():
            dButtons['PelosaNanoFX'].SetEnabled()
        if not dButtons['PelosaMapPlanetDetail'].IsEnabled():
            dButtons['PelosaMapPlanetDetail'].SetEnabled()
    else:
        if dButtons['PelosaNanoFX'].IsEnabled():
            dButtons['PelosaNanoFX'].SetDisabled()
        if dButtons['PelosaMapPlanetDetail'].IsEnabled():
            dButtons['PelosaMapPlanetDetail'].SetDisabled()


def DS9FXConfigsManager(pModule, strPath, pToReload, bDisableButtons=0, bPlaySound=0, bPlayConfigSound=0, bStartTimer=0,
                        bCheckShownOptions=0, bHackUMM=0, bShowPrompt=0, bBackupMutators=0, bSilentMutatorBackup=0):
    if bDisableButtons:
        DisableMyButtons()

    rExcaliburSelection = pModule.ExcaliburSelection
    rDefiantSelection = pModule.DefiantSelection
    rOregonSelection = pModule.OregonSelection
    rLakotaSelection = pModule.LakotaSelection
    rDS9Selection = pModule.DS9Selection
    rBugship1Selection = pModule.Bugship1Selection
    rBugship2Selection = pModule.Bugship2Selection
    rBugship3Selection = pModule.Bugship3Selection
    rWormholeSelection = pModule.WormholeSelection
    rVideoSelection = pModule.VideoSelection
    rModelPreloadingSelection = pModule.ModelPreloadingSelection
    rRandomEnemyFleetAttacks = pModule.RandomEnemyFleetAttacks
    rDomIS = pModule.DomIS
    rDS9Music = pModule.DS9Music
    rWormholeMusic = pModule.WormholeMusic
    rGammaMusic = pModule.GammaMusic
    rRandomDomStrength = pModule.RandomDomStrength
    rFederationSide = pModule.FederationSide
    rDominionSide = pModule.DominionSide
    rCometSelection = pModule.CometSelection
    rDS9Planets = pModule.DS9Planets
    rDS9NanoFX = pModule.DS9NanoFX
    rGammaPlanets = pModule.GammaPlanets
    rGammaNanoFX = pModule.GammaNanoFX
    rDominionTimeSpan = pModule.DominionTimeSpan
    rCometAlphaTrail = pModule.CometAlphaTrail
    rCometAlphaTrailTexture = pModule.CometAlphaTrailTexture
    rDebugMode = pModule.DebugMode
    rDS9MapPlanetDetail = pModule.DS9MapPlanetDetail
    rGammaMapPlanetDetail = pModule.GammaMapPlanetDetail
    rInsideWormholeBackgroundTexture = pModule.InsideWormholeBackgroundTexture
    rInsideWormholeModel = pModule.InsideWormholeModel
    rStabilizeBC = pModule.StabilizeBC
    rIntroVid = pModule.IntroVid
    rCompletionVid = pModule.CompletionVid
    rAutoMutatorBackup = pModule.AutoMutatorBackup
    rIntroMovieSel = pModule.IntroMovieSel
    rBadlandsBackground = pModule.BadlandsBackground
    rBadlandsVortex = pModule.BadlandsVortex
    rBadlandsMusic = pModule.BadlandsMusic
    rBadlandsBackground2Res = pModule.BadlandsBackground2Res
    rBadlandsVortexVariant = pModule.BadlandsVortexVariant
    rLifeSupport = pModule.LifeSupport
    rExitGameDebugMode = pModule.ExitGameDebugMode
    rLifeSupportCrewLabels = pModule.LifeSupportCrewLabels
    rKillRandomFleetsDuringMission = pModule.KillRandomFleetsDuringMission
    rNanoFXExplosionFix = pModule.NanoFXExplosionFix
    rExitGameFix = pModule.ExitGameFix
    rTransporterFix = pModule.TransporterFix
    rLifeSupportCombatEffectiveness = pModule.LifeSupportCombatEffectiveness
    rBadlandsDamageFX = pModule.BadlandsDamageFX
    rKaremmaPlanets = pModule.KaremmaPlanets
    rKaremmaNanoFX = pModule.KaremmaNanoFX
    rKaremmaMapPlanetDetail = pModule.KaremmaMapPlanetDetail
    rKaremmaDreadnought1 = pModule.KaremmaDreadnought1
    rKaremmaDreadnought2 = pModule.KaremmaDreadnought2
    rKaremmaMusic = pModule.KaremmaMusic
    rDosiPlanets = pModule.DosiPlanets
    rDosiNanoFX = pModule.DosiNanoFX
    rDosiMapPlanetDetail = pModule.DosiMapPlanetDetail
    rDosiMusic = pModule.DosiMusic
    rYaderaPlanets = pModule.YaderaPlanets
    rYaderaNanoFX = pModule.YaderaNanoFX
    rYaderaMapPlanetDetail = pModule.YaderaMapPlanetDetail
    rYaderaMusic = pModule.YaderaMusic
    rNewBajorPlanets = pModule.NewBajorPlanets
    rNewBajorNanoFX = pModule.NewBajorNanoFX
    rNewBajorMapPlanetDetail = pModule.NewBajorMapPlanetDetail
    rNewBajorMajestic = pModule.NewBajorMajestic
    rNewBajorBonchune = pModule.NewBajorBonchune
    rNewBajorMusic = pModule.NewBajorMusic
    rGaiaPlanets = pModule.GaiaPlanets
    rGaiaNanoFX = pModule.GaiaNanoFX
    rGaiaMapPlanetDetail = pModule.GaiaMapPlanetDetail
    rGaiaMusic = pModule.GaiaMusic
    rKurrillPlanets = pModule.KurrillPlanets
    rKurrillNanoFX = pModule.KurrillNanoFX
    rKurrillMapPlanetDetail = pModule.KurrillMapPlanetDetail
    rKurrillShip1 = pModule.KurrillShip1
    rKurrillShip2 = pModule.KurrillShip2
    rKurrillShip3 = pModule.KurrillShip3
    rKurrillShip4 = pModule.KurrillShip4
    rKurrillShip5 = pModule.KurrillShip5
    rKurrillMusic = pModule.KurrillMusic
    rTrialusPlanets = pModule.TrialusPlanets
    rTrialusNanoFX = pModule.TrialusNanoFX
    rTrialusMapPlanetDetail = pModule.TrialusMapPlanetDetail
    rTrialusMusic = pModule.TrialusMusic
    rTRogoranPlanets = pModule.TRogoranPlanets
    rTRogoranNanoFX = pModule.TRogoranNanoFX
    rTRogoranMapPlanetDetail = pModule.TRogoranMapPlanetDetail
    rTRogoranMusic = pModule.TRogoranMusic
    rVandrosPlanets = pModule.VandrosPlanets
    rVandrosNanoFX = pModule.VandrosNanoFX
    rVandrosMapPlanetDetail = pModule.VandrosMapPlanetDetail
    rVandrosMusic = pModule.VandrosMusic
    rFoundersPlanets = pModule.FoundersPlanets
    rFoundersNanoFX = pModule.FoundersNanoFX
    rFoundersMapPlanetDetail = pModule.FoundersMapPlanetDetail
    rFoundersShip1 = pModule.FoundersShip1
    rFoundersShip2 = pModule.FoundersShip2
    rFoundersShip3 = pModule.FoundersShip3
    rFoundersShip4 = pModule.FoundersShip4
    rFoundersReinforcements = pModule.FoundersReinforcements
    rFoundersMusic = pModule.FoundersMusic
    rInstantConfigSave = pModule.InstantConfigSave
    rNoDamageThroughShields = pModule.NoDamageThroughShields
    rEasterEggs = pModule.EasterEggs
    rAIBoardings = pModule.AIBoardings
    rQonosPlanets = pModule.QonosPlanets
    rQonosNanoFX = pModule.QonosNanoFX
    rQonosMapPlanetDetail = pModule.QonosMapPlanetDetail
    rQonosShip1 = pModule.QonosShip1
    rQonosShip2 = pModule.QonosShip2
    rQonosShip3 = pModule.QonosShip3
    rQonosMusic = pModule.QonosMusic
    rBadlandsBrightness = pModule.BadlandsBrightness
    rChintokaPlanets = pModule.ChintokaPlanets
    rChintokaNanoFX = pModule.ChintokaNanoFX
    rChintokaMapPlanetDetail = pModule.ChintokaMapPlanetDetail
    rChintokaMusic = pModule.ChintokaMusic
    rSunStreaks = pModule.SunStreaks
    rVelaMusic = pModule.VelaMusic
    rCardassiaPlanets = pModule.CardassiaPlanets
    rCardassiaNanoFX = pModule.CardassiaNanoFX
    rCardassiaMapPlanetDetail = pModule.CardassiaMapPlanetDetail
    rCardassiaMusic = pModule.CardassiaMusic
    rCardassiaShip1 = pModule.CardassiaShip1
    rCardassiaShip2 = pModule.CardassiaShip2
    rCardassiaShip3 = pModule.CardassiaShip3
    rCardassiaShip4 = pModule.CardassiaShip4
    rCardassiaShip5 = pModule.CardassiaShip5
    rTrivasPlanets = pModule.TrivasPlanets
    rTrivasNanoFX = pModule.TrivasNanoFX
    rTrivasMapPlanetDetail = pModule.TrivasMapPlanetDetail
    rTrivasMusic = pModule.TrivasMusic
    rKlingonSide = pModule.KlingonSide
    rCardassianSide = pModule.CardassianSide
    rSeptimusPlanets = pModule.SeptimusPlanets
    rSeptimusNanoFX = pModule.SeptimusNanoFX
    rSeptimusMapPlanetDetail = pModule.SeptimusMapPlanetDetail
    rSeptimusMusic = pModule.SeptimusMusic
    rDonatuPlanets = pModule.DonatuPlanets
    rDonatuNanoFX = pModule.DonatuNanoFX
    rDonatuMapPlanetDetail = pModule.DonatuMapPlanetDetail
    rDonatuMusic = pModule.DonatuMusic
    rPelosaPlanets = pModule.PelosaPlanets
    rPelosaNanoFX = pModule.PelosaNanoFX
    rPelosaMapPlanetDetail = pModule.PelosaMapPlanetDetail
    rPelosaMusic = pModule.PelosaMusic
    rStarbase375Centaur = pModule.Starbase375Centaur
    rStarbase375Starbase = pModule.Starbase375Starbase
    rStarbase375Music = pModule.Starbase375Music
    rRandFleetNumber = pModule.MaxRandShips
    rDisableLocalForces = pModule.DisableLocalForces

    file = nt.open(strPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
    nt.write(file, "##### DS9FX Xtended Settings" + "\n" +
             "\n" + str(dSettings["ExcaliburSelection"]) + " = " + str(rExcaliburSelection) +
             "\n" + str(dSettings["DefiantSelection"]) + " = " + str(rDefiantSelection) +
             "\n" + str(dSettings["OregonSelection"]) + " = " + str(rOregonSelection) +
             "\n" + str(dSettings["LakotaSelection"]) + " = " + str(rLakotaSelection) +
             "\n" + str(dSettings["DS9Selection"]) + " = " + str(rDS9Selection) +
             "\n" + str(dSettings["Bugship1Selection"]) + " = " + str(rBugship1Selection) +
             "\n" + str(dSettings["Bugship2Selection"]) + " = " + str(rBugship2Selection) +
             "\n" + str(dSettings["Bugship3Selection"]) + " = " + str(rBugship3Selection) +
             "\n" + str(dSettings["WormholeSelection"]) + " = " + str(rWormholeSelection) +
             "\n" + str(dSettings["VideoSelection"]) + " = " + str(rVideoSelection) +
             "\n" + str(dSettings["ModelPreloadingSelection"]) + " = " + str(rModelPreloadingSelection) +
             "\n" + str(dSettings["RandomEnemyFleetAttacks"]) + " = " + str(rRandomEnemyFleetAttacks) +
             "\n" + str(dSettings["DomIS"]) + " = " + str(rDomIS) +
             "\n" + str(dSettings["DS9Music"]) + " = " + str(rDS9Music) +
             "\n" + str(dSettings["WormholeMusic"]) + " = " + str(rWormholeMusic) +
             "\n" + str(dSettings["GammaMusic"]) + " = " + str(rGammaMusic) +
             "\n" + str(dSettings["RandomDomStrength"]) + " = " + str(rRandomDomStrength) +
             "\n" + str(dSettings["FederationSide"]) + " = " + str(rFederationSide) +
             "\n" + str(dSettings["DominionSide"]) + " = " + str(rDominionSide) +
             "\n" + str(dSettings["CometSelection"]) + " = " + str(rCometSelection) +
             "\n" + str(dSettings["DS9Planets"]) + " = " + str(rDS9Planets) +
             "\n" + str(dSettings["DS9NanoFX"]) + " = " + str(rDS9NanoFX) +
             "\n" + str(dSettings["GammaPlanets"]) + " = " + str(rGammaPlanets) +
             "\n" + str(dSettings["GammaNanoFX"]) + " = " + str(rGammaNanoFX) +
             "\n" + str(dSettings["DominionTimeSpan"]) + " = " + str(rDominionTimeSpan) +
             "\n" + str(dSettings["CometAlphaTrail"]) + " = " + str(rCometAlphaTrail) +
             "\n" + str(dSettings["CometAlphaTrailTexture"]) + " = " + str(rCometAlphaTrailTexture) +
             "\n" + str(dSettings["DebugMode"]) + " = " + str(rDebugMode) +
             "\n" + str(dSettings["DS9MapPlanetDetail"]) + " = " + str(rDS9MapPlanetDetail) +
             "\n" + str(dSettings["GammaMapPlanetDetail"]) + " = " + str(rGammaMapPlanetDetail) +
             "\n" + str(dSettings["InsideWormholeBackgroundTexture"]) + " = " + str(rInsideWormholeBackgroundTexture) +
             "\n" + str(dSettings["InsideWormholeModel"]) + " = " + str(rInsideWormholeModel) +
             "\n" + str(dSettings["StabilizeBC"]) + " = " + str(rStabilizeBC) +
             "\n" + str(dSettings["IntroVid"]) + " = " + str(rIntroVid) +
             "\n" + str(dSettings["CompletionVid"]) + " = " + str(rCompletionVid) +
             "\n" + str(dSettings["AutoMutatorBackup"]) + " = " + str(rAutoMutatorBackup) +
             "\n" + str(dSettings["IntroMovieSel"]) + " = " + "'" + str(rIntroMovieSel) + "'" +
             "\n" + str(dSettings["BadlandsBackground"]) + " = " + str(rBadlandsBackground) +
             "\n" + str(dSettings["BadlandsVortex"]) + " = " + str(rBadlandsVortex) +
             "\n" + str(dSettings["BadlandsMusic"]) + " = " + str(rBadlandsMusic) +
             "\n" + str(dSettings["BadlandsBackground2Res"]) + " = " + str(rBadlandsBackground2Res) +
             "\n" + str(dSettings["BadlandsVortexVariant"]) + " = " + str(rBadlandsVortexVariant) +
             "\n" + str(dSettings["LifeSupport"]) + " = " + str(rLifeSupport) +
             "\n" + str(dSettings["ExitGameDebugMode"]) + " = " + str(rExitGameDebugMode) +
             "\n" + str(dSettings["LifeSupportCrewLabels"]) + " = " + str(rLifeSupportCrewLabels) +
             "\n" + str(dSettings["KillRandomFleetsDuringMission"]) + " = " + str(rKillRandomFleetsDuringMission) +
             "\n" + str(dSettings["NanoFXExplosionFix"]) + " = " + str(rNanoFXExplosionFix) +
             "\n" + str(dSettings["ExitGameFix"]) + " = " + str(rExitGameFix) +
             "\n" + str(dSettings["TransporterFix"]) + " = " + str(rTransporterFix) +
             "\n" + str(dSettings["LifeSupportCombatEffectiveness"]) + " = " + str(rLifeSupportCombatEffectiveness) +
             "\n" + str(dSettings["BadlandsDamageFX"]) + " = " + str(rBadlandsDamageFX) +
             "\n" + str(dSettings["KaremmaPlanets"]) + " = " + str(rKaremmaPlanets) +
             "\n" + str(dSettings["KaremmaNanoFX"]) + " = " + str(rKaremmaNanoFX) +
             "\n" + str(dSettings["KaremmaMapPlanetDetail"]) + " = " + str(rKaremmaMapPlanetDetail) +
             "\n" + str(dSettings["KaremmaDreadnought1"]) + " = " + str(rKaremmaDreadnought1) +
             "\n" + str(dSettings["KaremmaDreadnought2"]) + " = " + str(rKaremmaDreadnought2) +
             "\n" + str(dSettings["KaremmaMusic"]) + " = " + str(rKaremmaMusic) +
             "\n" + str(dSettings["DosiPlanets"]) + " = " + str(rDosiPlanets) +
             "\n" + str(dSettings["DosiNanoFX"]) + " = " + str(rDosiNanoFX) +
             "\n" + str(dSettings["DosiMapPlanetDetail"]) + " = " + str(rDosiMapPlanetDetail) +
             "\n" + str(dSettings["DosiMusic"]) + " = " + str(rDosiMusic) +
             "\n" + str(dSettings["YaderaPlanets"]) + " = " + str(rYaderaPlanets) +
             "\n" + str(dSettings["YaderaNanoFX"]) + " = " + str(rYaderaNanoFX) +
             "\n" + str(dSettings["YaderaMapPlanetDetail"]) + " = " + str(rYaderaMapPlanetDetail) +
             "\n" + str(dSettings["YaderaMusic"]) + " = " + str(rYaderaMusic) +
             "\n" + str(dSettings["NewBajorPlanets"]) + " = " + str(rNewBajorPlanets) +
             "\n" + str(dSettings["NewBajorNanoFX"]) + " = " + str(rNewBajorNanoFX) +
             "\n" + str(dSettings["NewBajorMapPlanetDetail"]) + " = " + str(rNewBajorMapPlanetDetail) +
             "\n" + str(dSettings["NewBajorMajestic"]) + " = " + str(rNewBajorMajestic) +
             "\n" + str(dSettings["NewBajorBonchune"]) + " = " + str(rNewBajorBonchune) +
             "\n" + str(dSettings["NewBajorMusic"]) + " = " + str(rNewBajorMusic) +
             "\n" + str(dSettings["GaiaPlanets"]) + " = " + str(rGaiaPlanets) +
             "\n" + str(dSettings["GaiaNanoFX"]) + " = " + str(rGaiaNanoFX) +
             "\n" + str(dSettings["GaiaMapPlanetDetail"]) + " = " + str(rGaiaMapPlanetDetail) +
             "\n" + str(dSettings["GaiaMusic"]) + " = " + str(rGaiaMusic) +
             "\n" + str(dSettings["KurrillPlanets"]) + " = " + str(rKurrillPlanets) +
             "\n" + str(dSettings["KurrillNanoFX"]) + " = " + str(rKurrillNanoFX) +
             "\n" + str(dSettings["KurrillMapPlanetDetail"]) + " = " + str(rKurrillMapPlanetDetail) +
             "\n" + str(dSettings["KurrillShip1"]) + " = " + str(rKurrillShip1) +
             "\n" + str(dSettings["KurrillShip2"]) + " = " + str(rKurrillShip2) +
             "\n" + str(dSettings["KurrillShip3"]) + " = " + str(rKurrillShip3) +
             "\n" + str(dSettings["KurrillShip4"]) + " = " + str(rKurrillShip4) +
             "\n" + str(dSettings["KurrillShip5"]) + " = " + str(rKurrillShip5) +
             "\n" + str(dSettings["KurrillMusic"]) + " = " + str(rKurrillMusic) +
             "\n" + str(dSettings["TrialusPlanets"]) + " = " + str(rTrialusPlanets) +
             "\n" + str(dSettings["TrialusNanoFX"]) + " = " + str(rTrialusNanoFX) +
             "\n" + str(dSettings["TrialusMapPlanetDetail"]) + " = " + str(rTrialusMapPlanetDetail) +
             "\n" + str(dSettings["TrialusMusic"]) + " = " + str(rTrialusMusic) +
             "\n" + str(dSettings["TRogoranPlanets"]) + " = " + str(rTRogoranPlanets) +
             "\n" + str(dSettings["TRogoranNanoFX"]) + " = " + str(rTRogoranNanoFX) +
             "\n" + str(dSettings["TRogoranMapPlanetDetail"]) + " = " + str(rTRogoranMapPlanetDetail) +
             "\n" + str(dSettings["TRogoranMusic"]) + " = " + str(rTRogoranMusic) +
             "\n" + str(dSettings["VandrosPlanets"]) + " = " + str(rVandrosPlanets) +
             "\n" + str(dSettings["VandrosNanoFX"]) + " = " + str(rVandrosNanoFX) +
             "\n" + str(dSettings["VandrosMapPlanetDetail"]) + " = " + str(rVandrosMapPlanetDetail) +
             "\n" + str(dSettings["VandrosMusic"]) + " = " + str(rVandrosMusic) +
             "\n" + str(dSettings["FoundersPlanets"]) + " = " + str(rFoundersPlanets) +
             "\n" + str(dSettings["FoundersNanoFX"]) + " = " + str(rFoundersNanoFX) +
             "\n" + str(dSettings["FoundersMapPlanetDetail"]) + " = " + str(rFoundersMapPlanetDetail) +
             "\n" + str(dSettings["FoundersShip1"]) + " = " + str(rFoundersShip1) +
             "\n" + str(dSettings["FoundersShip2"]) + " = " + str(rFoundersShip2) +
             "\n" + str(dSettings["FoundersShip3"]) + " = " + str(rFoundersShip3) +
             "\n" + str(dSettings["FoundersShip4"]) + " = " + str(rFoundersShip4) +
             "\n" + str(dSettings["FoundersReinforcements"]) + " = " + str(rFoundersReinforcements) +
             "\n" + str(dSettings["FoundersMusic"]) + " = " + str(rFoundersMusic) +
             "\n" + str(dSettings["InstantConfigSave"]) + " = " + str(rInstantConfigSave) +
             "\n" + str(dSettings["NoDamageThroughShields"]) + " = " + str(rNoDamageThroughShields) +
             "\n" + str(dSettings["EasterEggs"]) + " = " + str(rEasterEggs) +
             "\n" + str(dSettings["AIBoardings"]) + " = " + str(rAIBoardings) +
             "\n" + str(dSettings["QonosPlanets"]) + " = " + str(rQonosPlanets) +
             "\n" + str(dSettings["QonosNanoFX"]) + " = " + str(rQonosNanoFX) +
             "\n" + str(dSettings["QonosMapPlanetDetail"]) + " = " + str(rQonosMapPlanetDetail) +
             "\n" + str(dSettings["QonosShip1"]) + " = " + str(rQonosShip1) +
             "\n" + str(dSettings["QonosShip2"]) + " = " + str(rQonosShip2) +
             "\n" + str(dSettings["QonosShip3"]) + " = " + str(rQonosShip3) +
             "\n" + str(dSettings["QonosMusic"]) + " = " + str(rQonosMusic) +
             "\n" + str(dSettings["BadlandsBrightness"]) + " = " + str(rBadlandsBrightness) +
             "\n" + str(dSettings["ChintokaPlanets"]) + " = " + str(rChintokaPlanets) +
             "\n" + str(dSettings["ChintokaNanoFX"]) + " = " + str(rChintokaNanoFX) +
             "\n" + str(dSettings["ChintokaMapPlanetDetail"]) + " = " + str(rChintokaMapPlanetDetail) +
             "\n" + str(dSettings["ChintokaMusic"]) + " = " + str(rChintokaMusic) +
             "\n" + str(dSettings["SunStreaks"]) + " = " + str(rSunStreaks) +
             "\n" + str(dSettings["VelaMusic"]) + " = " + str(rVelaMusic) +
             "\n" + str(dSettings["CardassiaPlanets"]) + " = " + str(rCardassiaPlanets) +
             "\n" + str(dSettings["CardassiaNanoFX"]) + " = " + str(rCardassiaNanoFX) +
             "\n" + str(dSettings["CardassiaMapPlanetDetail"]) + " = " + str(rCardassiaMapPlanetDetail) +
             "\n" + str(dSettings["CardassiaMusic"]) + " = " + str(rCardassiaMusic) +
             "\n" + str(dSettings["CardassiaShip1"]) + " = " + str(rCardassiaShip1) +
             "\n" + str(dSettings["CardassiaShip2"]) + " = " + str(rCardassiaShip2) +
             "\n" + str(dSettings["CardassiaShip3"]) + " = " + str(rCardassiaShip3) +
             "\n" + str(dSettings["CardassiaShip4"]) + " = " + str(rCardassiaShip4) +
             "\n" + str(dSettings["CardassiaShip5"]) + " = " + str(rCardassiaShip5) +
             "\n" + str(dSettings["TrivasPlanets"]) + " = " + str(rTrivasPlanets) +
             "\n" + str(dSettings["TrivasNanoFX"]) + " = " + str(rTrivasNanoFX) +
             "\n" + str(dSettings["TrivasMapPlanetDetail"]) + " = " + str(rTrivasMapPlanetDetail) +
             "\n" + str(dSettings["TrivasMusic"]) + " = " + str(rTrivasMusic) +
             "\n" + str(dSettings["KlingonSide"]) + " = " + str(rKlingonSide) +
             "\n" + str(dSettings["CardassianSide"]) + " = " + str(rCardassianSide) +
             "\n" + str(dSettings["SeptimusPlanets"]) + " = " + str(rSeptimusPlanets) +
             "\n" + str(dSettings["SeptimusNanoFX"]) + " = " + str(rSeptimusNanoFX) +
             "\n" + str(dSettings["SeptimusMapPlanetDetail"]) + " = " + str(rSeptimusMapPlanetDetail) +
             "\n" + str(dSettings["SeptimusMusic"]) + " = " + str(rSeptimusMusic) +
             "\n" + str(dSettings["DonatuPlanets"]) + " = " + str(rDonatuPlanets) +
             "\n" + str(dSettings["DonatuNanoFX"]) + " = " + str(rDonatuNanoFX) +
             "\n" + str(dSettings["DonatuMapPlanetDetail"]) + " = " + str(rDonatuMapPlanetDetail) +
             "\n" + str(dSettings["DonatuMusic"]) + " = " + str(rDonatuMusic) +
             "\n" + str(dSettings["PelosaPlanets"]) + " = " + str(rPelosaPlanets) +
             "\n" + str(dSettings["PelosaNanoFX"]) + " = " + str(rPelosaNanoFX) +
             "\n" + str(dSettings["PelosaMapPlanetDetail"]) + " = " + str(rPelosaMapPlanetDetail) +
             "\n" + str(dSettings["PelosaMusic"]) + " = " + str(rPelosaMusic) +
             "\n" + str(dSettings["Starbase375Centaur"]) + " = " + str(rStarbase375Centaur) +
             "\n" + str(dSettings["Starbase375Starbase"]) + " = " + str(rStarbase375Starbase) +
             "\n" + str(dSettings["Starbase375Music"]) + " = " + str(rStarbase375Music) +
             "\n" + str(dSettings["MaxRandShips"]) + " = " + str(rRandFleetNumber) +
             "\n" + str(dSettings["DisableLocalForces"]) + " = " + str(rDisableLocalForces) +
             "\n")
    nt.close(file)

    reload(pToReload)

    if bPlaySound:
        PlayButtonClickedSound()

    if bPlayConfigSound:
        PlayConfigSavedSound()

    if bStartTimer:
        KillTimerInstance()
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_TIMER_EVENT, __name__ + ".ResetButtons")

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_TIMER_EVENT)
        pEvent.SetDestination(pOptionsWindow)

        pTimer = App.TGTimer_Create()
        pTimer.SetEvent(pEvent)
        pTimer.SetTimerStart(App.g_kUtopiaModule.GetRealTime() + 1.0)
        pTimer.SetDelay(0.0)
        pTimer.SetDuration(0.0)

        global idTimer
        idTimer = pTimer.GetObjID()

        App.g_kRealtimeTimerManager.AddTimer(pTimer)

    if bHackUMM:
        import MainMenu.mainmenu
        MainMenu.mainmenu.SwitchMiddlePane("Configure")

    if bBackupMutators:
        checkAutoMutatorBackup = DS9FXSavedConfig.AutoMutatorBackup

        if checkAutoMutatorBackup == 1:
            from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
            FoundationMutatorFix.SaveBackup(bSilent=1)  # bSilent as in show on the console

    if bSilentMutatorBackup:
        checkAutoMutatorBackup = DS9FXSavedConfig.AutoMutatorBackup

        if checkAutoMutatorBackup == 1:
            from Custom.DS9FX.DS9FXLib import FoundationMutatorFix
            FoundationMutatorFix.SaveBackup()

    if bShowPrompt:
        from Custom.DS9FX.DS9FXPrompts import DS9FXPrompt
        DS9FXPrompt.Prompt()

    if bCheckShownOptions:
        CheckShownOptions()
