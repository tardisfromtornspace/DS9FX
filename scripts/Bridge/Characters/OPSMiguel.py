###############################################################################
#	Filename:	Miguel.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Lieutenant Austin Chang, science, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Miguel by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Miguel")

	if (pSet.GetObject("Science") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Science")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-cadet01-head.NIF", None)
	pOPSMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-cadet01-head.NIF")
	pOPSMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-yellowC_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")

	pOPSMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSMiguel)

	# Setup the character configuration
	pOPSMiguel.SetSize(App.CharacterClass.MEDIUM)
	pOPSMiguel.SetGender(App.CharacterClass.MALE)
	pOPSMiguel.SetRandomAnimationChance(.75)
	pOPSMiguel.SetBlinkChance(0.1)
	pOPSMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pOPSMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.SetBlinkStages(3)

	pOPSMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/miguel_head.tga")
	pOPSMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pOPSMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pOPSMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pOPSMiguel


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
	pOPSMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pOPSMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pOPSMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#


###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSMiguel):
#	kDebugObj.Print("Configuring Miguel for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSMiguel.ClearAnimations()

	# Register animation mappings
	pOPSMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.OPSSmallAnimations.EBMoveFromL1ToS")
	pOPSMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.OPSSmallAnimations.EBMoveFromSToL1")
	pOPSMiguel.AddAnimation("EBScienceTurnCaptain", "Bridge.Characters.OPSSmallAnimations.EBTurnAtSTowardsCaptain")
	pOPSMiguel.AddAnimation("EBScienceBackCaptain", "Bridge.Characters.OPSSmallAnimations.EBTurnBackAtSFromCaptain")

	pOPSMiguel.AddAnimation("EBScienceTurnC", "Bridge.Characters.OPSSmallAnimations.EBSTalkC")
	pOPSMiguel.AddAnimation("EBScienceBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSMiguel.AddAnimation("EBScienceTurnH", "Bridge.Characters.OPSSmallAnimations.EBSTalkH")
	pOPSMiguel.AddAnimation("EBScienceBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSMiguel.AddAnimation("EBScienceTurnE", "Bridge.Characters.OPSSmallAnimations.EBSTalkE")
	pOPSMiguel.AddAnimation("EBScienceBackE", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSMiguel.AddAnimation("EBScienceTurnT", "Bridge.Characters.OPSSmallAnimations.EBSTalkT")
	pOPSMiguel.AddAnimation("EBScienceBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pOPSMiguel.AddAnimation("EBScienceTurnX", "Bridge.Characters.OPSSmallAnimations.EBSTalkE")
	pOPSMiguel.AddAnimation("EBScienceBackX", "Bridge.Characters.CommonAnimations.SeatedS")

	pOPSMiguel.AddAnimation("EBScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pOPSMiguel.AddAnimation("EBScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pOPSMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.OPSSmallAnimations.EBMoveFromSToS1")
	pOPSMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.OPSSmallAnimations.EBMoveFromS1ToS")
	pOPSMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.OPSSmallAnimations.EBMoveFromSToS2")
	pOPSMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.OPSSmallAnimations.EBMoveFromS2ToS")
	pOPSMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.OPSSmallAnimations.EBMoveFromS1ToS2")
	pOPSMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.OPSSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pOPSMiguel.AddAnimation("EBScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pOPSMiguel.AddAnimation("EBScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.OPSSmallAnimations.EBSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pOPSMiguel.AddAnimation("PushingButtons", "Bridge.Characters.OPSSmallAnimations.EBSConsoleInteraction")

	# Hit animations
	pOPSMiguel.AddAnimation("EBScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pOPSMiguel.AddAnimation("EBScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pOPSMiguel.AddAnimation("EBScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pOPSMiguel.AddAnimation("EBScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pOPSMiguel)

	# Miguel sits on the Sovereign bridge
	pOPSMiguel.SetStanding(0)
	pOPSMiguel.SetLocation("OPSScience")
	pOPSMiguel.AddPositionZoom("OPSScience", 0.5)
	pOPSMiguel.AddPositionZoom("OPSScience1", 0.5)
	pOPSMiguel.AddPositionZoom("OPSScience2", 0.6)
#	kDebugObj.Print("Finished configuring Miguel")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSMiguel):
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.OPSSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
	# Like a function pointer (GetFile() is the same as pDatabase.GetFilename())
	GetFile = pDatabase.GetFilename	# do this for horizontal space savings

	#
	# Build a list of sound to load
	#
	kSoundList =	[	"MiguelSir1",		# Click Response
						"MiguelSir2",
						"MiguelSir3",
						"MiguelSir4",
						"MiguelSir5",

						"MiguelYes1",		# Order Confirmation
						"MiguelYes2",
						"MiguelYes3",
						"MiguelYes4",

						# Scanning lines.
						"MiguelScan",
						"gs038",
						"gs039",
						"gs040",
						"gs041",

						# Launching a probe.
						"gs030",

						# Spontaneous shield callouts.
						"TargetFrontShieldFailed",
						"TargetFrontShieldDraining",
						"TargetRearShieldFailed",
						"TargetRearShieldDraining",
						"TargetLeftShieldFailed",
						"TargetLeftShieldDraining",
						"TargetRightShieldFailed",
						"TargetRightShieldDraining",
						"TargetTopShieldFailed",
						"TargetTopShieldDraining",
						"TargetBottomShieldFailed",
						"TargetBottomShieldDraining",

						# Spontaneous target system callouts..
						"TargetHull05",
						"TargetHull10",
						"TargetHull15",
						"TargetHull20",
						"TargetHull25",
						"TargetHull50",
						"TargetHull75",

						"TargetPhasersDisabled",
						"TargetShieldsDisabled",
						"TargetSensorsDisabled",
						"TargetTorpedoesDisabled",
						"TargetTractorDisabled",
						"TargetImpulseDisabled",
						"TargetWarpDisabled",

						"TargetPhasersDestroyed",
						"TargetShieldsDestroyed",
						"TargetSensorsDestroyed",
						"TargetTorpedoesDestroyed",
						"TargetTractorDestroyed",
						"TargetImpulseDestroyed",
						"TargetWarpDestroyed",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for i in range(len(kSoundList)):
		pGame.LoadDatabaseSoundInGroup(pDatabase, kSoundList[i], "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
