import App
import Multiplayer.SpeciesToShip

def GetShipStats():
    kShipStats = {'FilenameHigh': 'data/Models/Ships/DS9FX/Nebula/Nebula.nif', 'FilenameMed': 'data/Models/Ships/Ds9FX/Nebula/NebulaMed.nif', 'FilenameLow': 'data/Models/Ships/DS9FX/Nebula/NebulaLow.nif', 'Name': 'DS9FXNebula', 'HardpointFile': 'DS9FXNebula', 'Species': Multiplayer.SpeciesToShip.NEBULA}
    return kShipStats


def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats['Name'])):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 50.0, 15.0, 15.0, 400, 900, '_glow', None, "_spec")
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 150.0, 15.0, 15.0, 400, 900, '_glow', None, "_spec")
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 1000.0, 15.0, 30.0, 400, 900, '_glow', None, "_spec")
        pLODModel.SetTextureSharePath('data/Models/SharedTextures/FedShips')
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()


def PreLoadModel():
    LoadModel(1)