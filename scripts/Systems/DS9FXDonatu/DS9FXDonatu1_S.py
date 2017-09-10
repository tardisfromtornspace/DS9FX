import App
import Tactical.LensFlares
from Custom.DS9FX.DS9FXSunStreak import SunStreak
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def Initialize(pSet):
        pSun = App.Sun_Create(2000.0, 1500, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.YellowLensFlare(pSet, pSun, 1, 0.25, 0.25)
        SunStreak.Create(pSet, "SunStr", 75000.0, "Yellow", "2")

        reload(DS9FXSavedConfig)
        sPath = "data/Models/Environment/DS9FX/"
        if DS9FXSavedConfig.DonatuMapPlanetDetail == 3:
                sPath = sPath + "HighRes/"
        elif DS9FXSavedConfig.DonatuMapPlanetDetail == 2:
                sPath = sPath + "StandardRes/"
        elif DS9FXSavedConfig.DonatuMapPlanetDetail == 1:
                sPath = sPath + "LowRes/"
        else:
                sPath = sPath + "LowestRes/"

        if DS9FXSavedConfig.DonatuPlanets == 1:      
                pPlanet1 = App.Planet_Create(75.0, sPath + "Donatu1.nif")
                pSet.AddObjectToSet(pPlanet1, "Donatu I")
        
                pPlanet1.PlaceObjectByName( "Planet1" )
                pPlanet1.UpdateNodeOnly()
        
                pPlanet2 = App.Planet_Create(90.0, sPath + "Donatu2.nif")
                pSet.AddObjectToSet(pPlanet2, "Donatu II")
        
                pPlanet2.PlaceObjectByName( "Planet2" )
                pPlanet2.UpdateNodeOnly()
        
                pPlanet3 = App.Planet_Create(85.0, sPath + "Donatu3.nif")
                pSet.AddObjectToSet(pPlanet3, "Donatu III")
        
                pPlanet3.PlaceObjectByName( "Planet3" )
                pPlanet3.UpdateNodeOnly()
        
                pPlanet4 = App.Planet_Create(95.0, sPath + "Donatu4.nif")
                pSet.AddObjectToSet(pPlanet4, "Donatu IV")
        
                pPlanet4.PlaceObjectByName( "Planet4" )
                pPlanet4.UpdateNodeOnly()
        
                pPlanet5 = App.Planet_Create(85.0, sPath + "Qonos.nif")
                pSet.AddObjectToSet(pPlanet5, "Donatu V")
        
                pPlanet5.PlaceObjectByName( "Planet5" )
                pPlanet5.UpdateNodeOnly()
        
                pPlanet6 = App.Planet_Create(190.0, sPath + "Donatu6.nif")
                pSet.AddObjectToSet(pPlanet6, "Donatu VI")
        
                pPlanet6.PlaceObjectByName( "Planet6" )
                pPlanet6.UpdateNodeOnly()
        
                pPlanet7 = App.Planet_Create(145.0, sPath + "Donatu7.nif")
                pSet.AddObjectToSet(pPlanet7, "Donatu VII")
        
                pPlanet7.PlaceObjectByName( "Planet7" )
                pPlanet7.UpdateNodeOnly()
        
                if DS9FXSavedConfig.DonatuNanoFX == 1:
                        try:
                                import Custom.NanoFXv2.NanoFX_Lib
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, sPath + "Donatu1.nif", "Class-H")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, sPath + "Donatu2.nif", "Class-K")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, sPath + "Donatu3.nif", "Class-M")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, sPath + "Donatu4.nif", "Class-O")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, sPath + "Qonos.nif", "Class-M")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, sPath + "Donatu6.nif", "Class-H")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, sPath + "Donatu7.nif", "Class-O")
                        except:
                                print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"	