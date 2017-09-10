import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(149.0 / 255.0, 198.0 / 255.0, 76.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.1,		
					0.5)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.40)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("BorgNanites")

def GetPowerCost():
	return(33.0)

def GetName():
	return("BorgNanites")

def GetDamage():
	return 700.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 6.0
