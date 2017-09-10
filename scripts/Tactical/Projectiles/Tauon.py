import App
def Create(pTorp):
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.700000, 0.600000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.600000, 0.600000, 0.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.55) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.225)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Borg Super Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Tauon")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.1

def GetLifetime():
	return 10.0
