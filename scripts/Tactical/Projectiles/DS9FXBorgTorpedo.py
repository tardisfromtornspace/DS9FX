import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/Borgtorp.tga', kCoreColor, 0.6, 1.0, 'data/Textures/Tactical/Borgtorp.tga', kGlowColor, 4.0, 1.8, 3.3, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 12, 1.7, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'DS9FXBorg Torpedo'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Gravimetric'


def GetDamage():
    return 1500.0


def GetGuidanceLifetime():
    return 6.0


def GetMaxAngularAccel():
    return 0.10




try:
	import FoundationTech
	import ftb.Tech.EMPProjectile
	oFire = ftb.Tech.EMPProjectile.EMPProjectileDef('EMP Projectile', {
	'nPercentage':			10,
	'nChance':			10,
})
	FoundationTech.dYields[__name__] = oFire
except:
	import sys
	et = sys.exc_info()
	error = str(et[0])+": "+str(et[1])
	print "ERROR at script: " + __name__ +", details -> "+error
