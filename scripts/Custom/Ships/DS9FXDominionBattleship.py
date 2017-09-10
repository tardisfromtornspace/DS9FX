import App
import Foundation


abbrev = "DS9FXDominionBattleship"
iconName = "DS9FXDominionBattleship"
longName = "Battleship"
shipFile = "DS9FXDominionBattleship"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"
Foundation.ShipDef.DS9FXDominionBattleship = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DS9FXDominionBattleship.desc = "The Jem\'Hadar battleship is a type of warship introduced in the Alpha Quadrant midway through the Dominion War in 2374.\n\nInitial observations of the prototype vessel, conducted by the USS Valiant using sensor probes, indicated that the battleship was twice the size of a Galaxy-class starship and three times as powerful.\n\nWeapons:\n13 Phased Polaron Beams\n15 Polaron Cannons\n4 Torpedo Launchers\n\nShield Rating:\n20F, 20A, 20D, 20V, 20P, 20S\n\nHull Rating:\n35"
Foundation.ShipDef.DS9FXDominionBattleship.SubMenu = "Dominion Ships"
Foundation.ShipDef.DS9FXDominionBattleship.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.DS9FXDominionBattleship.fCruiseWarp = 9.2 + 0.0001
Foundation.ShipDef.DS9FXDominionBattleship.fCrew = 3500


if menuGroup:           Foundation.ShipDef.DS9FXDominionBattleship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXDominionBattleship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
