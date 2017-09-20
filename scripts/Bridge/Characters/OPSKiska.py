###############################################################################
#	Filename:	Kiska.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Kiska Lomar, Helm, and configures animations
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Kiska by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Kiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head03.NIF", None)
	pOPSKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head03.NIF", 1)
	pOPSKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-yellow_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")

	pOPSKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSKiska)

	# Setup the character configuration
	pOPSKiska.SetSize(App.CharacterClass.MEDIUM)
	pOPSKiska.SetGender(App.CharacterClass.FEMALE)
	pOPSKiska.SetStanding(0)
	pOPSKiska.SetRandomAnimationChance(0.75)
	pOPSKiska.SetBlinkChance(0.1)
	pOPSKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pOPSKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.SetBlinkStages(3)

	pOPSKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female03C_head.tga")
	pOPSKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pOPSKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pOPSKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Kiska")
	return pOPSKiska


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
	pOPSKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pOPSKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pOPSKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#



###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSKiska):
#	kDebugObj.Print("Configuring Kiska for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSKiska.ClearAnimations()

	# Register animation mappings
	pOPSKiska.AddAnimation("EBL1MToH", "Bridge.Characters.OPSMediumAnimations.EBMoveFromL1ToH")
	pOPSKiska.AddAnimation("EBHelmToL1", "Bridge.Characters.OPSMediumAnimations.EBMoveFromHToL1")
	pOPSKiska.AddAnimation("EBHelmTurnCaptain", "Bridge.Characters.OPSMediumAnimations.EBTurnAtHTowardsCaptain")
	pOPSKiska.AddAnimation("EBHelmBackCaptain", "Bridge.Characters.OPSMediumAnimations.EBTurnBackAtHFromCaptain")

	pOPSKiska.AddAnimation("EBHelmTurnC", "Bridge.Characters.OPSMediumAnimations.EBHTalkC")
	pOPSKiska.AddAnimation("EBHelmBackC", "Bridge.Characters.OPSMediumAnimations.EBHTalkFinC")
	pOPSKiska.AddAnimation("EBHelmTurnE", "Bridge.Characters.OPSMediumAnimations.EBHTalkE")
	pOPSKiska.AddAnimation("EBHelmBackE", "Bridge.Characters.OPSMediumAnimations.EBHTalkFinE")
	pOPSKiska.AddAnimation("EBHelmTurnS", "Bridge.Characters.OPSMediumAnimations.EBHTalkS")
	pOPSKiska.AddAnimation("EBHelmBackS", "Bridge.Characters.OPSMediumAnimations.EBHTalkFinS")
	pOPSKiska.AddAnimation("EBHelmTurnT", "Bridge.Characters.OPSMediumAnimations.EBHTalkT")
	pOPSKiska.AddAnimation("EBHelmBackT", "Bridge.Characters.OPSMediumAnimations.EBHTalkFinT")

	pOPSKiska.AddAnimation("EBHelmTurnX", "Bridge.Characters.OPSMediumAnimations.EBHTalkE")
	pOPSKiska.AddAnimation("EBHelmBackX", "Bridge.Characters.OPSMediumAnimations.EBHTalkFinE")

	pOPSKiska.AddAnimation("EBHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pOPSKiska.AddAnimation("EBHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pOPSKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Interaction
	pOPSKiska.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pOPSKiska.AddAnimation("PushingButtons", "Bridge.Characters.OPSMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pOPSKiska.AddAnimation("EBHelmHit", "Bridge.Characters.MediumAnimations.HHit")
	#pOPSKiska.AddAnimation("EBHelmHitHard", "Bridge.Characters.MediumAnimations.HHitHard")
	pOPSKiska.AddAnimation("EBHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pOPSKiska.AddAnimation("EBHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pOPSKiska)

	pOPSKiska.SetLocation("OPSHelm")
	pOPSKiska.AddPositionZoom("OPSHelm", 0.5, "Helm")
	pOPSKiska.SetLookAtAdj(0, 0, 70)
#	kDebugObj.Print("Finished configuring Kiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSKiska):
	# Interaction with their environment
	pOPSKiska.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pOPSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
	lSoundList =	[	"KiskaSir1",	# Click Response
						"KiskaSir2",
						"KiskaSir3",
						"KiskaSir4",
						"KiskaSir5",
						
						"KiskaYes1",	# Order Confirmation
						"KiskaYes2",
						"KiskaYes3",
						"KiskaYes4",

						"gh075",	# Course laid in
						"gh081",	# Intercept course plotted

						"HailOpen1",
						"HailOpen2",
						"NotResponding1",
						"NotResponding2",
						"OnScreen",

						"CollisionAlert1",
						"CollisionAlert2",
						"CollisionAlert3",
						"CollisionAlert4",
						"CollisionAlert5",
						"CollisionAlert6",
						"CollisionAlert7",
						"CollisionAlert10",

						"IncomingMsg1",
						"IncomingMsg2",
						"IncomingMsg3",
						"IncomingMsg4",
						"IncomingMsg5",
						"IncomingMsg6",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
