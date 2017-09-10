import App
import Tactical.LensFlares
from Custom.DS9FX.DS9FXSunStreak import SunStreak
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def Initialize(pSet):
        pSun1 = App.Sun_Create(5000.0, 2500, 500, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun1, "Sun1")

        pSun1.PlaceObjectByName( "Sun1" )
        pSun1.UpdateNodeOnly()

        Tactical.LensFlares.BlueLensFlare(pSet, pSun1, 1, 0.35, 0.35)
        SunStreak.Create(pSet, "SunStr1", 75000.0, "DarkBlue", "4")

        pSun2 = App.Sun_Create(5000.0, 2500, 500, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun2, "Sun2")

        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()

        Tactical.LensFlares.BlueLensFlare(pSet, pSun2, 1, 0.25, 0.25)
        SunStreak.Create(pSet, "SunStr2", 75000.0, "DarkBlue", "4")

        reload(DS9FXSavedConfig)
        sPath = "data/Models/Environment/DS9FX/"
        if DS9FXSavedConfig.PelosaMapPlanetDetail == 3:
                sPath = sPath + "HighRes/"
        elif DS9FXSavedConfig.PelosaMapPlanetDetail == 2:
                sPath = sPath + "StandardRes/"
        elif DS9FXSavedConfig.PelosaMapPlanetDetail == 1:
                sPath = sPath + "LowRes/"
        else:
                sPath = sPath + "LowestRes/"	

        if DS9FXSavedConfig.PelosaPlanets == 1:
                pPelosa1 = App.Planet_Create(90.0, sPath + "Chintoka5.nif")
                pSet.AddObjectToSet(pPelosa1, "Pelosa I")
        
                pPelosa1.PlaceObjectByName( "Planet1" )
                pPelosa1.UpdateNodeOnly()
        
                pPelosa2 = App.Planet_Create(75.0, sPath + "Planet002.nif")
                pSet.AddObjectToSet(pPelosa2, "Pelosa II")
        
                pPelosa2.PlaceObjectByName( "Planet2" )
                pPelosa2.UpdateNodeOnly()
        
                pPelosa3 = App.Planet_Create(180.0, sPath + "Gamma1High.nif")
                pSet.AddObjectToSet(pPelosa3, "Pelosa III")
        
                pPelosa3.PlaceObjectByName( "Planet3" )
                pPelosa3.UpdateNodeOnly()
        
                pPelosa4 = App.Planet_Create(180.0, sPath + "Donatu6.nif")
                pSet.AddObjectToSet(pPelosa4, "Pelosa IV")
        
                pPelosa4.PlaceObjectByName( "Planet4" )
                pPelosa4.UpdateNodeOnly()
        
                pPelosa5 = App.Planet_Create(100.0, sPath + "Planet004.nif")
                pSet.AddObjectToSet(pPelosa5, "Pelosa V")
        
                pPelosa5.PlaceObjectByName( "Planet5" )
                pPelosa5.UpdateNodeOnly()
        
                if DS9FXSavedConfig.PelosaNanoFX == 1:
                        try:
                                import Custom.NanoFXv2.NanoFX_Lib
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPelosa1, sPath + "Chintoka5.nif", "Class-H")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPelosa2, sPath + "Planet002.nif", "Class-K")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPelosa3, sPath + "Gamma1High.nif", "Class-O")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPelosa4, sPath + "Donatu6.nif", "Class-O")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPelosa5, sPath + "Planet004.nif", "Class-K")
                        except:
                                print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 	