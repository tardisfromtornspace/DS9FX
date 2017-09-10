###############################################################################
#	Filename:	PhaseQuantum.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	1/8/04 -	Durandal
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(254.0 / 255.0, 76.0 / 255.0, 250.0 / 255.0, 1.0)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(253.0 / 255.0, 238.0 / 255.0, 134.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(143.0 / 255.0, 167.0 / 255.0, 255.0 / 255.0, 1.0)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.07,
					1.2,	 
					"scripts/Custom/DurandalHP/Textures/FTBpoltorp02.tga", 
					kGlowColor,
					2.0,	
					0.6,	 
					0.7,	
					"scripts/Custom/DurandalHP/Textures/Dur_TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.35,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Phase Quantum")

def GetDamage():
	return 2250.0

def GetGuidanceLifetime():
	return 17.0

def GetMaxAngularAccel():
	return 0.19

def GetLifetime():
	return 20.0
