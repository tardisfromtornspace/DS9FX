import App

def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 216.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(244.0 / 255.0, 193.0 / 255.0, 66.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 85.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.03,
					1.2,	 
					"scripts/Custom/DurandalHP/Textures/FTBpoltorp02.tga", 
					kGlowColor,
					2.0,	
					0.25,	 
					0.27,	
					"scripts/Custom/DurandalHP/Textures/Dur_TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.07,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.27)
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
	return("Micro Photon")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Photon")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.20

def GetLifetime():
	return 30.0
	
def GetFlashColor():
	return (25.0, 25.0, 50.0)
