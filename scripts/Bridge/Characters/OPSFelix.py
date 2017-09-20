###############################################################################
#	Filename:	Felix.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Felix Savali, tactical officer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Felix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Felix")
	
	if (pSet.GetObject("Tactical") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Tactical")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-munro-head.NIF", None)
	pOPSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-munro-head.NIF")
	pOPSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-redC_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")

	pOPSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFelix)

	# Set up character configuration
	pOPSFelix.SetSize(App.CharacterClass.MEDIUM)
	pOPSFelix.SetGender(App.CharacterClass.MALE)
	pOPSFelix.SetStanding(0)
	pOPSFelix.SetRandomAnimationChance(0.75)
	pOPSFelix.SetBlinkChance(0.1)
	pOPSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pOPSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pOPSFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.SetBlinkStages(3)

	pOPSFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")
	pOPSFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pOPSFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pOPSFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pOPSFelix

###############################################################################
#	CreateCharacterNoSounds()
#
#	Create Felix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoSounds(pSet):
#	kDebugObj.Print("Creating Felix")
	
	import Bridge.TacticalMenuHandlers
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pOPSFelix)

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-munro-head.NIF", None)
	pOPSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-munro-head.NIF")
	pOPSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-redC_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/riker_head.tga")

	pOPSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFelix)

	# Set up character configuration
	pOPSFelix.SetSize(App.CharacterClass.LARGE)
	pOPSFelix.SetGender(App.CharacterClass.MALE)
	pOPSFelix.SetStanding(0)
	pOPSFelix.SetHidden(1)
	pOPSFelix.SetRandomAnimationChance(0.75)
	pOPSFelix.SetBlinkChance(0.1)
	pOPSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pOPSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pOPSFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pOPSFelix


###############################################################################
#	CreateCharacterNoMenu()
#
#	Create Felix by building his character and placing him on the passed in set.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoMenu(pSet):
#	kDebugObj.Print("Creating Felix")
	
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pOPSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pOPSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGoldC_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pOPSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFelix)

	# Set up character configuration
	pOPSFelix.SetSize(App.CharacterClass.LARGE)
	pOPSFelix.SetGender(App.CharacterClass.MALE)
	pOPSFelix.SetStanding(0)
	pOPSFelix.SetHidden(1)
	pOPSFelix.SetRandomAnimationChance(0.75)
	pOPSFelix.SetBlinkChance(0.1)
	pOPSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pOPSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pOPSFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pOPSFelix


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	# Get our character object
	pOPSFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pOPSFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pOPSFelix)



###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSFelix):
#	kDebugObj.Print("Configuring Felix for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSFelix.ClearAnimations()

	# Register animation mappings
	pOPSFelix.AddAnimation("SeatedEBTactical", "Bridge.Characters.CommonAnimations.SeatedL")
	pOPSFelix.AddAnimation("EBL1LToT", "Bridge.Characters.OPSLargeAnimations.EBMoveFromL1ToT")
	pOPSFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.OPSLargeAnimations.EBMoveFromTToL1")



	# Breathing
	pOPSFelix.AddAnimation("EBTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction


	# So the mission builders can force the call


	# Hit animations		
	#pOPSFelix.AddAnimation("EBTacticalHit", "Bridge.Characters.LargeAnimations.THit")
	#pOPSFelix.AddAnimation("EBTacticalHitHard", "Bridge.Characters.LargeAnimations.THitHard")
	pOPSFelix.AddAnimation("EBTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pOPSFelix.AddAnimation("EBTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pOPSFelix)

	pOPSFelix.SetLocation("OPSTactical")
	pOPSFelix.SetStanding(1)
	pOPSFelix.AddPositionZoom("OPSTactical", 0.5, "Tactical")
	pOPSFelix.SetLookAtAdj(5, 0, 65)
#	kDebugObj.Print("Finished configuring Felix")



###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSFelix):
	pOPSFelix.AddRandomAnimation("Bridge.Characters.OPSLargeAnimations.TLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)
	pOPSFelix.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.EB_interaction_tac")

	pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.StandingConsole")
	pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pOPSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pOPSFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pOPSFelix):
	pOPSFelix = App.CharacterClass_Cast(pOPSFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pOPSFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pOPSFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pOPSFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pOPSFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	pOPSFelix.ClearAnimations()

	# Register animation mappings
	pOPSFelix.SetStanding(1)
	pOPSFelix.SetHidden(0)
	pOPSFelix.SetLocation("SovereignSeated")
	AddCommonAnimations(pOPSFelix)

#	kDebugObj.Print("Finished configuring Felix")

###############################################################################
#	LoadSounds
#	
#	Precache Felix's typical voice lines, so they don't hitch the
#	game when they try to play.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	# Loop through all of Felix's voice lines that we want to preload, and load them.
	for sLine in g_lsFelixLines:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

#
# A list of the voice lines we want preloaded for Felix.
#
g_lsFelixLines = (
	"AttackStatus_EvadingTorps1",
	"AttackStatus_FallingBack1",
	"AttackStatus_LiningUpFront1",
	"AttackStatus_MovingIn1",
	"AttackStatus_RearTorpRun1",
	"AttackStatus_SweepingPhasers1",
	"BadTarget1",
	"BadTarget2",
	"Disengaging",
	"DontShootTac",
	"EvasiveManuvers", # Sumbody furgot to spel this rite.
	"FelixEnDes",
	"FelixNothingToAdd",
	"FelixNothingToAdd2",
	"FelixNothingToAdd3",
	"FelixSir1",
	"FelixSir2",
	"FelixSir3",
	"FelixSir4",
	"FelixSir5",
	"FelixYes1",
	"FelixYes2",
	"FelixYes3",
	"FelixYes4",
	"ForeShieldsOffline",
	"Incoming1",
	"Incoming2",
	"Incoming3",
	"Incoming4",
	"Incoming5",
	"Incoming6",
	"LoadingPhoton",
	"LoadingQuantum",
	"LoadingTorps",
	"NeedPower",
	"OutOfPhotons",
	"OutOfQuantums",
	"OutOfType",
	"TacticalManuver", # This wun to.
	"gt001",
	"gt002",
	"gt007",
	"gt029",
	"gt030",
	"gt037",
	"gt038",
	"gt212",
	"gt213",
	)
