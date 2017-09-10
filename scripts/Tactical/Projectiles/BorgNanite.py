import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(149.0 / 255.0, 198.0 / 255.0, 76.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.3,		
					0.5)
	pTorp.SetDamage(2500.0)
	pTorp.SetDamageRadiusFactor(0.175)
	pTorp.SetGuidanceLifetime(10.0)
	pTorp.SetMaxAngularAccel(3.0)
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("Nanite Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Nanite")
