###############################################################################
#	Filename:	MaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador MaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create MaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating MaleExtra1")

	if (pSet.GetObject("MaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-head04.NIF", None)
	pOPSMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../SPModCrews/starfleet/starfleet-male-SF-base-hand01.NIF", CharacterPaths.g_pcHeadNIFPath + "../SPModCrews/starfleet/male-head04.NIF")
	pOPSMaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../SPModCrews/starfleet/male_bodies/male-blueD_body.tga", CharacterPaths.g_pcHeadTexPath + "../SPModCrews/starfleet/male_faces/male04_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pOPSMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pOPSMaleExtra1)

	# Setup the character configuration
	pOPSMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pOPSMaleExtra1.SetGender(App.CharacterClass.MALE)
	pOPSMaleExtra1.SetRandomAnimationChance(.75)
	pOPSMaleExtra1.SetBlinkChance(0.1)
	pOPSMaleExtra1.SetCharacterName("MaleExtra1")

	pOPSMaleExtra1.SetHidden(1)

	# Load MaleExtra1's generic sounds
	LoadSounds()

	# Create MaleExtra1's menus
	#import MaleExtra1MenuHandlers
	#MaleExtra1MenuHandlers.CreateMenus(pOPSMaleExtra1)

	pOPSMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pOPSMaleExtra1.GetDatabase(), "MaleExtra1NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating MaleExtra1")
	return pOPSMaleExtra1




###############################################################################
#	ConfigureForOps()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pOPSMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOps(pOPSMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	pOPSMaleExtra1.ClearAnimations()

	# Register animation mappings
	pOPSMaleExtra1.AddAnimation("OPSL2MToG", "Bridge.Characters.OPSMediumAnimations.OPSL2ToG1")
	pOPSMaleExtra1.AddAnimation("OPSG1MToL", "Bridge.Characters.OPSMediumAnimations.OPSG1ToL2")
	pOPSMaleExtra1.AddAnimation("StandingEBG1M", "Bridge.Characters.CommonAnimations.Standing")
	pOPSMaleExtra1.SetStanding(1)

	# Hit animations
	pOPSMaleExtra1.AddAnimation("EBG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pOPSMaleExtra1.AddAnimation("EBG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pOPSMaleExtra1.AddAnimation("EBG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pOPSMaleExtra1.AddAnimation("EBG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pOPSMaleExtra1.SetAsExtra(1)
	pOPSMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pOPSMaleExtra1)

	pOPSMaleExtra1.SetLocation("OPSL2M")
#	kDebugObj.Print("Finished configuring MaleExtra1")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pOPSMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pOPSMaleExtra1):
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pOPSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# MaleExtra1 has no generic bridge sounds at this time
	#
	pass
