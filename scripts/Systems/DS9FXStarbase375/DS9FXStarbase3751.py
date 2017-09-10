import App

def Initialize():
        # Create the set ("DS9FXStarbase3751")
        pSet = App.SetClass_Create()
        App.g_kSetManager.AddSet(pSet, "DS9FXStarbase3751")

        # Save the name of the region file that's creating the set.
        pSet.SetRegionModule("Systems.DS9FXStarbase375.DS9FXStarbase3751")

        # Activate the proximity manager for our set.
        pSet.SetProximityManagerActive(1)

        # Load the placements and backdrops for this set.
        LoadPlacements("DS9FXStarbase3751")
        LoadBackdrops(pSet)

        #Load and place the grid.
        pGrid = App.GridClass_Create()
        pSet.AddObjectToSet(pGrid, "grid")
        pGrid.SetHidden(1)

        # Create static objects for this set:
        # If you want to create static objects for this region, make a
        # "DS9FXStarbase3751_S.py" file with an Initialize function that creates them.
        try:
                import DS9FXStarbase3751_S
                DS9FXStarbase3751_S.Initialize(pSet)
        except ImportError:
                # Couldn't find the file.  That's ok.  Do nothing...
                pass

        # Done.

def GetSetName():
        return "DS9FXStarbase3751"

def GetSet():
        return App.g_kSetManager.GetSet("DS9FXStarbase3751")

def Terminate():
        App.g_kSetManager.DeleteSet("DS9FXStarbase3751")

def LoadPlacements(sSetName):
        # Light position "Ambient Light"
        kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigAmbientLight(0.643137, 0.843137, 0.956863, 0.274510)
        kThis.Update(0)
        kThis = None
        # End position "Ambient Light"

        # Light position "Directional Light"
        kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-4200.000000, -360000.000000, -3000.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.076971, 0.995795, 0.049676)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.006766, -0.050345, 0.998709)
        kThis.AlignToVectors(kForward, kUp)
        kThis.ConfigDirectionalLight(0.764706, 0.949020, 1.000000, 1.000000)
        kThis.Update(0)
        kThis = None
        # End position "Directional Light"

        # Position "Sun"
        kThis = App.Waypoint_Create("Sun", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-4200.000000, -360000.000000, -3000.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Sun"

        # Position "SunStr"
        kThis = App.Waypoint_Create("SunStr", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetTranslateXYZ(-4200.000000, -370000.000000, -3000.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "SunStr"

        # Position "Player Start"
        kThis = App.Waypoint_Create("Player Start", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.000000, 0.000000, 1.000000)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Player Start"

        # Position "Starbase 375 Location"
        kThis = App.Waypoint_Create("Starbase 375 Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-43.960209, 447.588837, -51.575943)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.150231, 0.000000, 0.988651)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Starbase 375 Location"

        # Position "Centaur Location"
        kThis = App.Waypoint_Create("Centaur Location", sSetName, None)
        kThis.SetStatic(1)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(145.000000, 550.000000, 100.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.000000, 1.000000, 0.000000)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.150231, 0.000000, 0.988651)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetSpeed(25.000000)
        kThis.Update(0)
        kThis = None
        # End position "Centaur Location"

import App

def LoadBackdrops(pSet):

        #Draw order is implicit. First object gets drawn first

        # Star Sphere "Backdrop stars"
        kThis = App.StarSphere_Create()
        kThis.SetName("Backdrop stars")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(0.185766, 0.947862, -0.258937)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.049823, 0.254099, 0.965894)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/sovstars.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(1.000000)
        kThis.SetVerticalSpan(1.000000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(22.000000)
        kThis.SetTextureVTile(11.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop stars")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop stars"

        # Backdrop Sphere "Backdrop Starbase375_1"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Starbase375_1")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.799987, 0.000499, -0.005087)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.005087, -0.000011, 0.699987)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Starbase375_1.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.252500)
        kThis.SetVerticalSpan(0.505000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop back1")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Starbase375_1"

        # Backdrop Sphere "Backdrop Starbase375_2"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Starbase375_2")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(1.0, -0.5, 0.2)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Starbase375_2.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.302500)
        kThis.SetVerticalSpan(0.605000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Starbase375_2")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Starbase375_2"

        # Backdrop Sphere "Backdrop Starbase375_3"
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Starbase375_3")
        kThis.SetTranslateXYZ(0.000000, 1.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(1.0, 2.5, 0.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 1.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/Starbase375_2.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.700000)
        kThis.SetVerticalSpan(0.700000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Starbase375_3")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere "Backdrop Starbase375_3"