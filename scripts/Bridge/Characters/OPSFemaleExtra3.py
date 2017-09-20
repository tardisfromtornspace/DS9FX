###############################################################################
#	Filename:	FemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador FemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create FemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating FemaleExtra3")

	if (pSet.GetObject("FemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/jurot-head.NIF", None)
	pOPSFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/jurot-head.NIF", 1)
	pOPSFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-redA_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/jurot_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSFemaleExtra3)

	# Setup the character configuration
	pOPSFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pOPSFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pOPSFemaleExtra3.SetRandomAnimationChance(.75)
	pOPSFemaleExtra3.SetBlinkChance(0.1)
	pOPSFemaleExtra3.SetCharacterName("FemaleExtra3")

	pOPSFemaleExtra3.SetHidden(1)

	# Load FemaleExtra3's generic sounds
	LoadSounds()

	# Create FemaleExtra3's menus
	#import FemaleExtra3MenuHandlers
	#FemaleExtra3MenuHandlers.CreateMenus(pOPSFemaleExtra3)

	pOPSFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pOPSFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pOPSFemaleExtra3.SetLocation("")

#	kDebugObj.Print("Finished creating FemaleExtra3")
	return pOPSFemaleExtra3


###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSFemaleExtra3):
#	kDebugObj.Print("Configuring FemaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSFemaleExtra3.ClearAnimations()

	# Register animation mappings
	pOPSFemaleExtra3.SetAsExtra(1)
	pOPSFemaleExtra3.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pOPSFemaleExtra3)

	pOPSFemaleExtra3.SetLocation("OPSXT02")
#	kDebugObj.Print("Finished configuring FemaleExtra3")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSFemaleExtra3):
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSFemaleExtra3.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.xtra_interaction_XT02")



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
	# FemaleExtra3 has no generic bridge sounds at this time
	#
	pass
