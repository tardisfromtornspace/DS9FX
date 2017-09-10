import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {'FilenameHigh': 'data/Models/Ships/DS9FX/Danube/danube.NIF', 'FilenameMed': 'data/Models/Ships/DS9FX/Danube/danube.NIF', 'FilenameLow': 'data/Models/ships/DS9FX/Danube/danube.NIF', 'Name': 'DS9FXDanubemkII', 'HardpointFile': 'DS9FXDanubemkII', 'Species': Multiplayer.SpeciesToShip.SHUTTLE}
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats['Name'])):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 200.0, 2.0, 2.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 400.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 800.0, 15.0, 30.0, 400, 900, '_glow', None, None)
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)