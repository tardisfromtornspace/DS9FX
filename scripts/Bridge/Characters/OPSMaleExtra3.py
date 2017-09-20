###############################################################################
#	Filename:	MaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador MaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create MaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating MaleExtra3")

	if (pSet.GetObject("MaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

        CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/jurot-head.NIF", None)
	pOPSMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/jurot-head.NIF", 1)
	pOPSMaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/female_bodies/female-redA_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/female_faces/jurot_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSMaleExtra3)

	# Setup the character configuration
	pOPSMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pOPSMaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pOPSMaleExtra3.SetRandomAnimationChance(.75)
	pOPSMaleExtra3.SetBlinkChance(0.1)
	pOPSMaleExtra3.SetCharacterName("MaleExtra3")

	pOPSMaleExtra3.SetHidden(1)

	# Load MaleExtra3's generic sounds
	LoadSounds()

	# Create MaleExtra3's menus
	#import MaleExtra3MenuHandlers
	#MaleExtra3MenuHandlers.CreateMenus(pOPSMaleExtra3)

	pOPSMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pOPSMaleExtra3.GetDatabase(), "MaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating MaleExtra3")
	return pOPSMaleExtra3



###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSMaleExtra3.ClearAnimations()

	# Register animation mappings
	pOPSMaleExtra3.SetAsExtra(1)
	pOPSMaleExtra3.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pOPSMaleExtra3)

	pOPSMaleExtra3.SetLocation("OPSXT02")
#	kDebugObj.Print("Finished configuring MaleExtra3")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSMaleExtra3):
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSMaleExtra3.AddRandomAnimation("Bridge.Characters.OPSMediumAnimations.xtra_interaction_XT02")


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
	# MaleExtra3 has no generic bridge sounds at this time
	#
	pass
