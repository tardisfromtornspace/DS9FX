import App
import Tactical.LensFlares
from Custom.DS9FX.DS9FXSunStreak import SunStreak
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def Initialize(pSet):
        pSun = App.Sun_Create(4000.00, 4000.0, 4000.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.YellowLensFlare(pSet, pSun, 1, 0.5, 0.5)
        SunStreak.Create(pSet, "SunStr", 50000.0, "Yellow", "8")

        reload(DS9FXSavedConfig)
        sPath = "data/Models/Environment/DS9FX/"
        if DS9FXSavedConfig.SeptimusMapPlanetDetail == 3:
                sPath = sPath + "HighRes/"
        elif DS9FXSavedConfig.SeptimusMapPlanetDetail == 2:
                sPath = sPath + "StandardRes/"
        elif DS9FXSavedConfig.SeptimusMapPlanetDetail == 1:
                sPath = sPath + "LowRes/"
        else:
                sPath = sPath + "LowestRes/"

        if DS9FXSavedConfig.SeptimusPlanets == 1:         
                pSeptimus1 = App.Planet_Create(75.0, sPath + "Septimus1.nif")
                pSet.AddObjectToSet(pSeptimus1, "Septimus I")

                pSeptimus1.PlaceObjectByName( "Septimus 1" )
                pSeptimus1.UpdateNodeOnly()

                pSeptimus2 = App.Planet_Create(105.0, sPath + "Septimus2.nif")
                pSet.AddObjectToSet(pSeptimus2, "Septimus II")

                pSeptimus2.PlaceObjectByName( "Septimus 2" )
                pSeptimus2.UpdateNodeOnly()

                pSeptimus3 = App.Planet_Create(85.0, sPath + "Septimus3.nif")
                pSet.AddObjectToSet(pSeptimus3, "Septimus III")

                pSeptimus3.PlaceObjectByName( "Septimus 3" )
                pSeptimus3.UpdateNodeOnly()

                pSeptimus4 = App.Planet_Create(120.0, sPath + "Septimus4.nif")
                pSet.AddObjectToSet(pSeptimus4, "Septimus IV")

                pSeptimus4.PlaceObjectByName( "Septimus 4" )
                pSeptimus4.UpdateNodeOnly()

                pSeptimus5 = App.Planet_Create(60.0, sPath + "Septimus5.nif")
                pSet.AddObjectToSet(pSeptimus5, "Septimus V")

                pSeptimus5.PlaceObjectByName( "Septimus 5" )
                pSeptimus5.UpdateNodeOnly()

                pSeptimus6 = App.Planet_Create(240.0, sPath + "Septimus6.nif")
                pSet.AddObjectToSet(pSeptimus6, "Septimus VI")

                pSeptimus6.PlaceObjectByName( "Septimus 6" )
                pSeptimus6.UpdateNodeOnly()

                if DS9FXSavedConfig.SeptimusNanoFX == 1:
                        try:
                                import Custom.NanoFXv2.NanoFX_Lib
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus1, sPath + "Septimus1.nif", "Class-H")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus2, sPath + "Septimus2.nif", "Class-K")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus3, sPath + "Septimus3.nif", "Class-M")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus4, sPath + "Septimus4.nif", "Class-O")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus5, sPath + "Septimus5.nif", "Class-K")
                                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSeptimus6, sPath + "Septimus6.nif", "Class-H")
                        except:
                                print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"  