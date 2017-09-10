import App
import Tactical.LensFlares
import MissionLib
import loadspacehelper
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
        from Custom.DS9FX.DS9FXObjects import Starbase375ShipsAndStations
        Starbase375ShipsAndStations.Create()
	
	pSun = App.Sun_Create(4500.0, 1500, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	Tactical.LensFlares.WhiteLensFlare(pSet, pSun, 1, 0.3, 0.3)
	SunStreak.Create(pSet, "SunStr", 100000.0, "White", "2")