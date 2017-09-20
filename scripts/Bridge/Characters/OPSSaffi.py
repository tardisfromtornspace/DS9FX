###############################################################################
#	Filename:	Saffi.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Commander Alexander Munro, XO, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
#     Revised:    7/29/07 -   Blackrook32 / 3rd Era Productions
###############################################################################

import App
import CharacterPaths

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print

###############################################################################
#	CreateCharacter()
#
#	Create Saffi by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	debug("Creating Saffi")

	if (pSet.GetObject("XO") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("XO")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-head01.NIF", None)
	pOPSSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-head01.NIF", 1)
	pOPSSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-redB_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/female01_head.tga")

	pOPSSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSSaffi)

	# Setup the character configuration
	pOPSSaffi.SetSize(App.CharacterClass.MEDIUM)
	pOPSSaffi.SetGender(App.CharacterClass.FEMALE)
	pOPSSaffi.SetRandomAnimationChance(.75)
	pOPSSaffi.SetBlinkChance(0.1)
	pOPSSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pOPSSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.SetBlinkStages(3)

	pOPSSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "..\SPModCrews\starfleet\female_faces/female01_head.tga")
	pOPSSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pOPSSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pOPSSaffi


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
	# Get our character object
	pOPSSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pOPSSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pOPSSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#


###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSSaffi):
#	debug("Configuring Saffi for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSSaffi.ClearAnimations()

	# Register animation mappings
	pOPSSaffi.AddAnimation("SeatedEBCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("StandingEBCommander1", "Bridge.Characters.CommonAnimations.Standing")
	pOPSSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.OPSMediumAnimations.EBMoveFromL1ToC")
	pOPSSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.OPSMediumAnimations.EBMoveFromCToL1")
	pOPSSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.OPSMediumAnimations.EBMoveFromCToC1")
	pOPSSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.OPSMediumAnimations.EBMoveFromC1ToC")
	pOPSSaffi.AddAnimation("EBCommanderTurnCaptain", "Bridge.Characters.OPSMediumAnimations.EBTurnAtCTowardsCaptain")
	pOPSSaffi.AddAnimation("EBCommander1TurnCaptain", "Bridge.Characters.CommonAnimations.LookLeft")
#	pOPSSaffi.AddAnimation("EBCommander1TurnCaptain", "Bridge.Characters.MediumAnimations.EBTurnAtC1TowardsCaptain")
	pOPSSaffi.AddAnimation("EBCommanderBackCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommander1BackCaptain", "Bridge.Characters.CommonAnimations.Standing")
#	pOPSSaffi.AddAnimation("EBCommander1BackCaptain", "Bridge.Characters.MediumAnimations.EBTurnBackAtC1FromCaptain")

	pOPSSaffi.AddAnimation("EBCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pOPSSaffi.AddAnimation("EBCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pOPSSaffi.AddAnimation("EBCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.Standing")

	pOPSSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.OPSMediumAnimations.EBCTalkE")
	pOPSSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.OPSMediumAnimations.EBCTalkH")
	pOPSSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.OPSMediumAnimations.EBCTalkT")
	pOPSSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.OPSMediumAnimations.EBCTalkS")
	pOPSSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pOPSSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.OPSMediumAnimations.EBCTalkE")
	pOPSSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pOPSSaffi.AddAnimation("EBCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pOPSSaffi.AddAnimation("EBCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pOPSSaffi.AddAnimation("EBCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pOPSSaffi.AddAnimation("EBCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.EBCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pOPSSaffi.AddAnimation("PushingButtons", "Bridge.Characters.OPSMediumAnimations.EBCConsoleInteraction")

	# Hit animations
	#pOPSSaffi.AddAnimation("EBCommanderHit", "Bridge.Characters.MediumAnimations.CHit")
	#pOPSSaffi.AddAnimation("EBCommanderHitHard", "Bridge.Characters.MediumAnimations.CHitHard")
	#pOPSSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pOPSSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pOPSSaffi.AddAnimation("EBCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pOPSSaffi.AddAnimation("EBCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pOPSSaffi)

	pOPSSaffi.SetLocation("OPSCommander")
	pOPSSaffi.AddPositionZoom("OPSCommander", 0.8)
#	debug("Finished configuring Saffi")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSSaffi):
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pOPSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

###############################################################################
#	LoadSounds
#	
#	Load any of Saffi's general or spontaneous sounds, so they don't
#	hitch the game when they're played.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	
	#
	# Build a list of sound to load
	#
	lSoundList =	[
		# Yes?
		"gf001",
		"gf002",

		# Report.
		"gf020",

		# Alert lines.
		"GreenAlert",
		"GreenAlert2",
		"GreenAlert3",
		"YellowAlert",
		"YellowAlert3",
		"YellowAlert2",
		"RedAlert",
		"RedAlert2",

		# Contacting starfleet.
		"gl004",
		"gl005",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
