import App

# Here's how the lens flares work...
#
# pLensFlare = App.LensFlare_Create(pSet)
#
# Creates the lens flare object for a particular set
#
# pLensFlare.SetSource(pObject, iDirection)	
#
# Sets the light source orientation
# pObject is the object or backdrop that the light is attached to
# you could also fetch a light by name from the set for example.
# the second parameter is to help with the orientation that different objects have
# basically, use 1 if using a placement or object, and 0 if using a backdrop or light
#
# fSize1 is the size of the main flare
# fSize2 determines the size of the secondary flares
#
# Add the flares.
# Each of the flares are built from wedges, you can think of them as pies,
#  1- The number of wedges for that flare.
#  2- The name of the texture to use.
#  3- The position: 0 is at the source, 1 is at the center of the screen, 2 is as far as 0 on the opposite side, etc
#  4- The size of the flare
#  5&6 are optional parameters that make the flare shift or wobble a bit. This is good for flares on a sun
#  5- (optional) the frequency
#  6- (optional) the amplitude
#     				  1   2                         3     4    (5)  (6)
# pLensFlare.AddFlare(15, "data/textures/rays.tga", 0.0,  0.2, 3.0, 1.0)
# pLensFlare.AddFlare( 6,  "data/textures/redorange.tga", 0.5,  0.1)
# pLensFlare.AddFlare(18, "data/textures/redorange.tga", 1.0,  0.1)
# pLensFlare.AddFlare(15, "data/textures/redorange.tga", 2.0,  0.1)
# when done adding flares, this builds the actual geometry, etc, etc
# pLensFlare.Build()

###############################################################################
#	MakeLensFlare()
#	
#	Helper function for making Lens Flares
#	
#	Args:	pSet 		- the Set the Lens Flare goes in
#			pObject		- the object (or backdrop) the Flare is attached to
#			bFromObject	- 1 = Object, 0 = Backdrop
#			fSize1		- The size of the primary flare
#			fSize2		- Determines the size of secondary flares
#			sTexture1	- The texture for the primary flare
#			sTexture2	- The texture for the secondary flare
#			sTexture3	- The texture for the tertiary flare
#			sTexture4	- The texture for the quaternary flare
#
#	Return:	none
###############################################################################
def MakeLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0, 
                  sTexture1 = None, sTexture2 = None, sTexture3 = None, sTexture4 = None):

        if (pObject == None) or (pSet == None): 
                return

        # Setting up lens flare textures if they were not passed in
        if (sTexture1 == None):
                sTexture1 = "data/textures/rays.tga"
        if (sTexture2 == None):
                sTexture2 = "data/textures/whitelines.tga"
        if (sTexture3 == None):
                sTexture3 = "data/textures/whiteloop.tga"
        if (sTexture4 == None):
                sTexture4 = "data/textures/white2.tga"

        iDirection = 1
        if (bFromObject):
                iDirection = 6

        if not fSize1:
                # Size values not set
                if (bFromObject):
                        # Adjust direction and size lens flare based on the size of the object

                        fRadius = pObject.GetRadius() / 2

                        if (fRadius >= 6000):
                                fSize1 = 0.6

                        elif (fRadius >= 5000):
                                fSize1 = 0.5

                        elif (fRadius >= 4000):
                                fSize1 = 0.4

                        elif (fRadius >= 3000):
                                fSize1 = 0.3

                        elif (fRadius >= 2000):
                                fSize1 = 0.2

                        elif (fRadius >= 1000):
                                fSize1 = 0.1

                        else:
                                fSize1 = 0.05

                else:
                        # Use defaults for Backdrop
                        fSize1 = 0.3

        pLensFlare = App.LensFlare_Create(pSet)
        pLensFlare.SetSource(pObject, iDirection)
        pLensFlare.AddFlare(6, sTexture1, 0.0,	fSize1 * .67, .5, .1)
        pLensFlare.AddFlare(30, "data/textures/RainbowLoop.tga", 0.4, fSize1 * 0.1)
        pLensFlare.AddFlare(30, sTexture3, 0.5,	fSize1 * .0225)
        pLensFlare.AddFlare(30, sTexture4, 0.8,	fSize1 * .0167)
#	pLensFlare.AddFlare(30, "data/textures/redorangelines.tga", 0.5, fSize1 * .125)
        pLensFlare.AddFlare(30, sTexture2, 1.1,	fSize1 * .03)
#	pLensFlare.AddFlare(30, "data/textures/redorange.tga", .65,	fSize1 * .0167)
#	pLensFlare.AddFlare( 6, "data/textures/rays.tga", .75,	fSize1 * .00167)
        pLensFlare.AddFlare( 6, sTexture1, 1.4,	fSize1 * .1)
#	pLensFlare.AddFlare(30, "data/textures/white2.tga", 0.95,	fSize1 * .0833)
        pLensFlare.AddFlare(30, sTexture4, 1.8, fSize1 * .0325)
#	pLensFlare.AddFlare(30, "data/textures/lightblue.tga", 1.05, fSize1 * .05)
#	pLensFlare.AddFlare(30, sTexture2, 2.4, fSize1 * .0167)
#	pLensFlare.AddFlare(30, "data/textures/yellowloop.tga", 1.2,	fSize1 * .00167)
        pLensFlare.AddFlare(30, sTexture3, 2.1, fSize1 * .1)
        pLensFlare.AddFlare(5, sTexture2, 3.0, fSize1 * .0167)
        pLensFlare.AddFlare(5, sTexture2, 3.5, fSize1 * .0267)
        pLensFlare.AddFlare(5, sTexture2, 4.0, fSize1 * .0167)
        pLensFlare.Build()


#
# RedOrangeLensFlare() - Helper function for making a RedOrange Lens Flare
#

def RedOrangeFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return RedOrangeLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def RedOrangeLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/raysredorange.tga", "data/textures/redorangelines.tga", "data/textures/redorangeloop.tga", "data/textures/redorange.tga")

#
# YellowLensFlare() - Helper function for making a Yellow Lens Flare
#

def YellowFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return YellowLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def YellowLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/raysyellow.tga", "data/textures/yellowlines.tga", "data/textures/yellowloop.tga", "data/textures/yellow.tga")


#
# BlueLensFlare() - Helper function for making a Blue Lens Flare
#	

def BlueFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return BlueLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def BlueLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        iDirection = 1
        if (bFromObject):
                iDirection = 6

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/rayslightblue.tga", "data/textures/lightbluelines.tga", "data/textures/lightblueloop.tga", "data/textures/lightblue.tga")

#
# WhiteLensFlare() - Helper function for making a White Lens Flare
#

def WhiteFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return WhiteLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def WhiteLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/rays.tga", "data/textures/whitelines.tga", "data/textures/whiteloop.tga", "data/textures/white2.tga")

#
# DimBlueFlares() - Helper function for making a Dim Blue Lens Flare for distant stars
#	

def DimBlueFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return DimBlueLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def DimBlueLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        iDirection = 1
        if (bFromObject):
                iDirection = 6

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/raysdimblue.tga", "data/textures/dimbluelines1.tga", "data/textures/dimblueloop.tga", "data/textures/dimblue1.tga")

#
# BlackFlares() - Helper function for making Black Flares for Neutron Stars
#	

def BlackFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return BlackLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def BlackLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        iDirection = 1
        if (bFromObject):
                iDirection = 6

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/raysblack.tga", "data/textures/blacklines.tga", "data/textures/Blackloop.tga", "data/textures/Blackloop.tga")

#
# PurpleFlares() - Helper function for making a Dim Purple Lens Flare for distant stars
#	

def PurpleFlares(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        return PurpleLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0)

def PurpleLensFlare(pSet, pObject, bFromObject = 1, fSize1 = 0, fSize2 = 0):
        if (pObject == None) or (pSet == None): 
                return

        iDirection = 1
        if (bFromObject):
                iDirection = 6

        MakeLensFlare (pSet, pObject, bFromObject, fSize1, fSize2, 
                       "data/textures/rayspurple.tga", "data/textures/dimpurplelines1.tga", "data/textures/dimpurpleloop.tga", "data/textures/dimpurple1.tga")

