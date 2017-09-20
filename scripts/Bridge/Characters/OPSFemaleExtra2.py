###############################################################################
#	Filename:	FemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador FemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create FemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating FemaleExtra2")

	if (pSet.GetObject("FemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head02.NIF", None)
	pOPSFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/female-cadet-head02.NIF")
	pOPSFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-blue_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/female03_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFemaleExtra2)

	# Setup the character configuration
	pOPSFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pOPSFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pOPSFemaleExtra2.SetRandomAnimationChance(.75)
	pOPSFemaleExtra2.SetBlinkChance(0.1)
	pOPSFemaleExtra2.SetCharacterName("FemaleExtra2")

	pOPSFemaleExtra2.SetHidden(1)

	# Load FemaleExtra2's generic sounds
	LoadSounds()

	# Create FemaleExtra2's menus
	#import FemaleExtra2MenuHandlers
	#FemaleExtra2MenuHandlers.CreateMenus(pOPSFemaleExtra2)

	pOPSFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pOPSFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFemaleExtra2.SetLocation("")

#	kDebugObj.Print("Finished creating FemaleExtra2")
	return pOPSFemaleExtra2



###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSFemaleExtra2):
#	kDebugObj.Print("Configuring FemaleExtra2 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pOPSFemaleExtra2.SetAsExtra(1)
	pOPSFemaleExtra2.SetHidden(0)


	# Add common animations.
	AddCommonAnimations(pOPSFemaleExtra2)

	pOPSFemaleExtra2.SetLocation("OPSXT01")
#	kDebugObj.Print("Finished configuring FemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSFemaleExtra2):
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSFemaleExtra2.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.xtra_interaction_XT01")


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
	# FemaleExtra2 has no generic bridge sounds at this time
	#
	pass
