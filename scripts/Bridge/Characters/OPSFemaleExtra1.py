###############################################################################
#	Filename:	FemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador FemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create FemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating FemaleExtra1")

	if (pSet.GetObject("FemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head01.NIF", None)
	pOPSFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head01.NIF")
	pOPSFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-yellow_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/cadet-female01B_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFemaleExtra1)

	# Setup the character configuration
	pOPSFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pOPSFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pOPSFemaleExtra1.SetRandomAnimationChance(.75)
	pOPSFemaleExtra1.SetBlinkChance(0.1)
	pOPSFemaleExtra1.SetCharacterName("FemaleExtra1")

	pOPSFemaleExtra1.SetHidden(1)

	# Load FemaleExtra1's generic sounds
	LoadSounds()

	# Create FemaleExtra1's menus
	#import FemaleExtra1MenuHandlers
	#FemaleExtra1MenuHandlers.CreateMenus(pOPSFemaleExtra1)

	pOPSFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pOPSFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFemaleExtra1.SetLocation("")

#	kDebugObj.Print("Finished creating FemaleExtra1")
	return pOPSFemaleExtra1

###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSFemaleExtra1):
#	kDebugObj.Print("Configuring FemaleExtra1 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pOPSFemaleExtra1.AddAnimation("OPSL2MToG", "Bridge.Characters.OPSMediumAnimations.OPSL2ToG1")
	pOPSFemaleExtra1.AddAnimation("OPSG1MToL", "Bridge.Characters.OPSMediumAnimations.OPSG1ToL2")
	pOPSFemaleExtra1.AddAnimation("StandingEBG1M", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFemaleExtra1.SetStanding(1)

	# Hit animations
	pOPSFemaleExtra1.AddAnimation("EBG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pOPSFemaleExtra1.AddAnimation("EBG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pOPSFemaleExtra1.AddAnimation("EBG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pOPSFemaleExtra1.AddAnimation("EBG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pOPSFemaleExtra1.SetAsExtra(1)
	pOPSFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pOPSFemaleExtra1)

	pOPSFemaleExtra1.SetLocation("OPSL2M")
#	kDebugObj.Print("Finished configuring FemaleExtra1")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSFemaleExtra1):
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pOPSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	#
	# FemaleExtra1 has no generic bridge sounds at this time
	#
	pass
