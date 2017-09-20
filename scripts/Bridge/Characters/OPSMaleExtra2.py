###############################################################################
#	Filename:	MaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador MaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create MaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating MaleExtra2")

	if (pSet.GetObject("MaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-cadet01-head.NIF", None)
	pOPSMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-cadet01-head.NIF")
	pOPSMaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-blueD_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/cadet-male01A_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSMaleExtra2)

	# Setup the character configuration
	pOPSMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pOPSMaleExtra2.SetGender(App.CharacterClass.MALE)
	pOPSMaleExtra2.SetRandomAnimationChance(.75)
	pOPSMaleExtra2.SetBlinkChance(0.1)
	pOPSMaleExtra2.SetCharacterName("MaleExtra2")

	pOPSMaleExtra2.SetHidden(1)

	# Load MaleExtra2's generic sounds
	LoadSounds()

	# Create MaleExtra2's menus
	#import MaleExtra2MenuHandlers
	#MaleExtra2MenuHandlers.CreateMenus(pOPSMaleExtra2)

	pOPSMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pOPSMaleExtra2.GetDatabase(), "MaleExtra2NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating MaleExtra2")
	return pOPSMaleExtra2



###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSMaleExtra2):
#	kDebugObj.Print("Configuring MaleExtra2 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSMaleExtra2.ClearAnimations()

	# Register animation mappings

	pOPSMaleExtra2.SetAsExtra(1)
	pOPSMaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pOPSMaleExtra2)

	pOPSMaleExtra2.SetLocation("OPSXT01")
#	kDebugObj.Print("Finished configuring MaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSMaleExtra2):
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSMaleExtra2.AddRandomAnimation
("Bridge.Characters.OPSMediumAnimations.xtra_interaction_XT01")

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
	# MaleExtra2 has no generic bridge sounds at this time
	#
	pass
