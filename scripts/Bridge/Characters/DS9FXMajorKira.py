# by USS Sovereign register and make a new character in game :P
# MajorKira v2.1, thanks to BlackRook of course :)
# MajorKira v.3.0 Update by Blackrook32, 10/14/12

# Imports
import App
import CharacterPaths

#kDebugObj = App.CPyDebug()


# Create character
def CreateCharacter(pSet):

        # Register Kira
	if (pSet.GetObject("Kira") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Kira")))

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "../Excalibur/starfleet/bajoran_militia_fem/burgondy/starfleet-base-female.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "../Excalibur/starfleet/bajoran_militia_fem/burgondy/female-cadet-head01.NIF", None)
	pKira = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "../Excalibur/starfleet/bajoran_militia_fem/burgondy/starfleet-base-female.nif", CharacterPaths.g_pcHeadNIFPath + "../Excalibur/starfleet/bajoran_militia_fem/burgondy/female-cadet-head01.NIF", 1)
	pKira.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../Excalibur/starfleet/female_bodies/female-bajoran_body.tga", CharacterPaths.g_pcHeadTexPath + "../Excalibur/starfleet/female_faces/kira_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pKira, "Kira")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pKira)
	
	# Setup the character configuration
	pKira.SetSize(App.CharacterClass.MEDIUM)
	pKira.SetGender(App.CharacterClass.FEMALE)
	pKira.SetStanding(1)
	pKira.SetRandomAnimationChance(.01)
	pKira.SetBlinkChance(0.1)

	pKira.SetCharacterName("Kira")
	pKira.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Configure for the Generic bridge
	import Guest
	Guest.ConfigureForGeneric(pKira)

	pKira.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.SetBlinkStages(3)

	pKira.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "..\Excalibur\starfleet\female_faces\kira_head.tga")
	pKira.SetAnimatedSpeaking(1)

	pKira.AddAnimation("CardassianSeated01", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pKira.AddAnimation("CardassianSeated01", __name__ + ".Breathing")

	pKira.SetLocation("CardassianStationSeated")

	return pKira




def Breathing(pCharacter):
	kAM = App.g_kAnimationManager
	kAM.LoadAnimation ("data/animations/CardassianSeated01.nif", "CardassianStationSeated")
	pCharacter = App.CharacterClass_Cast(pCharacter)
	pSequence = App.TGSequence_Create()
	pAnimNode = pCharacter.GetAnimNode()
	pAction = App.TGAnimAction_Create(pAnimNode, "CardassianStationSeated", 0, 0)
	pSequence.AddAction(pAction)
	return pSequence
