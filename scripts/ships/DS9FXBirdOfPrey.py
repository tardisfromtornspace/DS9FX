import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/DS9FX/BirdOfPrey/Birdofprey.nif",
		"FilenameMed": "data/Models/Ships/DS9FX/BirdOfPrey/BirdofpreyMed.nif",
		"FilenameLow": "data/Models/Ships/DS9FX/BirdOfPrey/BirdofpreyLow.nif",
		"Name": "DS9FXBirdOfPrey",
		"HardpointFile": "DS9FXBirdOfPrey",
		"Species": Multiplayer.SpeciesToShip.BIRDOFPREY
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  40.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 100.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 500.0, 15.0, 30.0, 400, 900, "_glow", None, "_specular")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)

def GetPulseModule(pulsenum):
	if (pulsenum==1):
		return 'Tactical.Projectiles.PulseDisruptor'
	if (pulsenum==2):
		return 'Tactical.Projectiles.AdvPulseDisruptor'
	return 'End'

def GetPulseName(pulsenum):
	if (pulsenum==1):
		return 'Cannon: Std'
	if (pulsenum==2):
		return 'Cannon: Adv'
	return 'No Name'

def GetArmorRatio():
	return 0.4