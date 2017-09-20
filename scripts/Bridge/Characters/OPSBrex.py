###############################################################################
#	Filename:	Brex.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Brex, the Engineer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import Bridge.BridgeUtils
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Brex by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Brex")

	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-Brex-base-hand06.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-chell-head.NIF", None)
	pOPSBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-Brex-base-hand06.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-chell-head.NIF")
	pOPSBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-yellowC_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")

	pOPSBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSBrex)

	# Setup the character configuration
	pOPSBrex.SetSize(App.CharacterClass.MEDIUM)
	pOPSBrex.SetGender(App.CharacterClass.MALE)
	pOPSBrex.SetRandomAnimationChance(.75)
	pOPSBrex.SetBlinkChance(0.1)

	pOPSBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pOPSBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.SetBlinkStages(3)

	pOPSBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/chell-head.tga")
	pOPSBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pOPSBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pOPSBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pOPSBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pOPSBrex


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship (ShipClass object)
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	pOPSBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pOPSBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pOPSBrex)

	# Set up the status events that we need - Shield and Hull
	# Other events (repairs, subsystem reports) are generated elsewhere
	pShieldWatcher = pShip.GetShields().GetShieldWatcher(6)
	pHullWatcher = pShip.GetHull().GetCombinedPercentageWatcher()

	lWatchers = (
		( pShieldWatcher,	App.ET_TACTICAL_SHIELD_LEVEL_CHANGE ),
		( pHullWatcher,		App.ET_TACTICAL_HULL_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75 )

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)

	lWatchers = (
		( pShip.GetShields().GetShieldWatcher(0), App.ET_TACTICAL_SHIELD_0_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(1), App.ET_TACTICAL_SHIELD_1_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(2), App.ET_TACTICAL_SHIELD_2_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(3), App.ET_TACTICAL_SHIELD_3_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(4), App.ET_TACTICAL_SHIELD_4_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(5), App.ET_TACTICAL_SHIELD_5_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.5)

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)




###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSBrex):
#	kDebugObj.Print("Configuring Brex for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSBrex.ClearAnimations()

	# Register animation mappings
	pOPSBrex.AddAnimation("SeatedEBEngineer", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pOPSBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pOPSBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pOPSBrex.AddAnimation("EBEngineerTurnCaptain", "Bridge.Characters.OPSSmallAnimations.EBTurnAtETowardsCaptain")
	pOPSBrex.AddAnimation("EBEngineerBackCaptain", "Bridge.Characters.OPSSmallAnimations.EBTurnBackAtEFromCaptain")
	pOPSBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.OPSSmallAnimations.EBMoveFromE1ToE")
	pOPSBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.OPSSmallAnimations.EBMoveFromEToE1")
	pOPSBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.OPSSmallAnimations.EBMoveFromE2ToE")
	pOPSBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.OPSSmallAnimations.EBMoveFromEToE2")
	pOPSBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.OPSSmallAnimations.EBMoveFromE1ToE2")
	pOPSBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.OPSSmallAnimations.EBMoveFromE2ToE1")

	pOPSBrex.AddAnimation("EBEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pOPSBrex.AddAnimation("EBEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pOPSBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.OPSSmallAnimations.EBETalkC")
	pOPSBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.OPSSmallAnimations.EBETalkH")
	pOPSBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.OPSSmallAnimations.EBETalkS")
	pOPSBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.OPSSmallAnimations.EBETalkT")
	pOPSBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pOPSBrex.AddAnimation("EBEngineerTurnX", "Bridge.Characters.OPSSmallAnimations.EBTurnAtETowardsCaptain")
	pOPSBrex.AddAnimation("EBEngineerBackX", "Bridge.Characters.OPSSmallAnimations.EBTurnBackAtEFromCaptain")

	# Breathing
	pOPSBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pOPSBrex.AddRandomAnimation("Bridge.Characters.OPSSmallAnimations.EBEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pOPSBrex.AddAnimation("PushingButtons", "Bridge.Characters.OPSSmallAnimations.EBEConsoleInteraction")

	# Hit animations


	# Add common animations.
	AddCommonAnimations(pOPSBrex)

	# Brex sits on the Sovereign bridge
	pOPSBrex.SetStanding(0)
	pOPSBrex.SetLocation("OPSEngineer")
	pOPSBrex.AddPositionZoom("OPSEngineer", 0.5)
	pOPSBrex.AddPositionZoom("OPSEngineer1", 0.5)
	pOPSBrex.AddPositionZoom("OPSEngineer2", 0.6)
#	kDebugObj.Print("Finished configuring Brex")


###############################################################################
#	ConfigureForEngineering()
#
#	Configure ourselves for the Engineering partial set
#
#	Args:	pOPSBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEngineering(pOPSBrex):
#	kDebugObj.Print("Configuring Brex for engineering")

	pOPSBrex = App.CharacterClass_Cast(pOPSBrex)
	if pOPSBrex:
		# Clear out any old animations from another configuration
		pOPSBrex.ClearAnimations()

		# Register animation mappings

		pOPSBrex.SetLocation("SovereignEngSeated")
		AddCommonAnimations(pOPSBrex)

#		kDebugObj.Print("Finished configuring Brex")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSBrex):
	pOPSBrex.AddRandomAnimation("Bridge.Characters.OPSSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pOPSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


###############################################################################
#	LoadSounds()
#
#	Load generic bridge sounds for this character
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	#
	# Build a list of sound to load
	#
	kSoundList =	[	"BrexSir1",		# Click Response
						"BrexSir2",
						"BrexSir3",
						"BrexSir4",
						"BrexSir5",

						"BrexYes1",		# Order Confirmation
						"BrexYes2",
						"BrexYes3",
						"BrexYes4",

						"BrexTransfer",	# Transferring Power
						"MainPowerDraining",

						"FrontShieldDraining",
						"FrontShieldFailed",
						"RearShieldDraining",
						"RearShieldFailed",
						"TopShieldDraining",
						"TopShieldFailed",
						"BottomShieldDraining",
						"BottomShieldFailed",
						"LeftShieldDraining",
						"LeftShieldFailed",
						"RightShieldDraining",
						"RightShieldFailed",
						"PhasersDisabled",
						"PhasersDestroyed",
						"ShieldsDisabled",
						"ShieldsDestroyed",
						"SensorsDisabled",
						"SensorsDestroyed",
						"TorpedoesDisabled",
						"TorpedoesDestroyed",
						"TractorDisabled",
						"TractorDestroyed",
						"ImpulseDisabled",
						"ImpulseDestroyed",
						"WarpDisabled",
						"WarpDestroyed",
						"PowerDisabled",
						"OutOfTorpedoes",
						"Hull05",
						"Hull10",
						"Hull15",
						"Hull20",
						"Hull25",
						"Hull50",
						"Hull75",
						"MultipleShieldsOffline",
						"Shields05",
						"Shields10",
						"Shields15",
						"Shields20",
						"Shields25",
						"Shields50",
						"Shields75",
						"ShieldsFailed"
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for i in range(len(kSoundList)):
		pGame.LoadDatabaseSoundInGroup(pDatabase, kSoundList[i], "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

###############################################################################
#	MoveFromEToL1 & MoveFromL1ToE
#	
#	Functions that turn the "Contact Engineering" button on and off
#	
#	Args:	self		- the character that called these
#	
#	Return:	pSequence	- returned by the real functions
###############################################################################
def MoveFromEToL1(self):
	import Bridge.Characters.OPSSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.OPSSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pOPSBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pOPSBrex
	bSuccess = pEngineering.AddObjectToSet(pOPSBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def EnableContactEngineeringButton(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(1)

	return 0
	
def MoveFromL1ToE(self):
	import Bridge.Characters.OPSSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.OPSSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.OPSSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pOPSBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pOPSBrex
	bSuccess = pBridge.AddObjectToSet(pOPSBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	import Bridge.Characters.OPSSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.OPSSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	import Bridge.Characters.OPSSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.OPSSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.OPSSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pOPSBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pOPSBrex
	bSuccess = pBridge.AddObjectToSet(pOPSBrex, "Engineer")
	assert bSuccess

	return 0
