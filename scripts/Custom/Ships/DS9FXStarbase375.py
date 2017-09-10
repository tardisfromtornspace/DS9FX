import App
import Foundation


abbrev = "DS9FXStarbase375"
iconName = "DS9FXStarbase375"
longName = "Starbase 375"
shipFile = "DS9FXStarbase375"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = ""
Foundation.ShipDef.DS9FXStarbase375 = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DS9FXStarbase375.desc = "Starbase 375 is a Federation space station located near the Cardassian border. During the Dominion War, this station served as a front line command post for Federation Alliance forces until Deep Space 9 was retaken during Operation Return.\n\nWeapons:\n12 Type XI Phaser Banks\n6 Torpedo Launchers\n\nShield Rating:\n30F, 30A, 30D, 30V, 30P, 30S\n\nHull Rating:\n75"
Foundation.ShipDef.DS9FXStarbase375.SubMenu = "Federation Bases"
Foundation.ShipDef.DS9FXStarbase375.fCrew = 800


if menuGroup:           Foundation.ShipDef.DS9FXStarbase375.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXStarbase375.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
