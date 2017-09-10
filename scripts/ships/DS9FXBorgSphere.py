import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/DS9FX/BorgSphere/BorgSphere.nif",
		"FilenameMed": "data/Models/Ships/DS9FX/BorgSphere/BorgSphere.nif",
		"FilenameLow": "data/Models/Ships/DS9FX/BorgSphere/BorgSphere.nif",
		"Name": "DS9FXBorgSphere",
		"HardpointFile": "DS9FXBorgSphere",
		"Species": Multiplayer.SpeciesToShip.WARBIRD,
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
		# ***FIXME: Not all 3 levels of detail need OBB trees.  PickLeafSize should be 0 for the unused ones.
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  1250.0, 50.0, 50.0, 400, 900, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameMed"],  10,  2500.0, 100.0, 100.0, 400, 900, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameLow"],  10,  5000.0, 200.0, 200.0, 400, 900, "_glow", None, None)
		
#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
