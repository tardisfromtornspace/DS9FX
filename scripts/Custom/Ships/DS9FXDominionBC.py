import App
import Foundation

abbrev = "DS9FXDominionBC"
iconName = "DS9FXDominionWarship"
longName = "Warship"
shipFile = "DS9FXDominionBC"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXDominionBC = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXDominionBC.SubMenu = "Dominion Ships"
Foundation.ShipDef.DS9FXDominionBC.fMaxWarp = 9.8 + 0.0001
Foundation.ShipDef.DS9FXDominionBC.fCruiseWarp = 9.6 + 0.0001
Foundation.ShipDef.DS9FXDominionBC.fCrew = 2500

Foundation.ShipDef.DS9FXDominionBC.desc = "------- DESCRIPTION -------\nThe Jem\'Hadar battlecruiser is the Dominion\'s large capital ship, similar in size to a Galaxy class starship, used for fleet engagements  and a command ship for high ranking Vorta.  It provides the Dominion with a much stronger ship as opposed to the aging attack fighter.  Equipped with Polaron Beams and Cannons, it can deliver quite a punch to a ship.  Able to inflict major damage on enemies, several  Starfleet ships would be required to take a battlecruiser down.\n\n------- TACTICS -------\nThis ship is slow, but has a powerful weapons array.  It has full coverage on all sides, so there is no use in try to outmaneuver, or get  out of range of their Polaron Beams, as they will most likely get you anyways.  Try to go for their Ventral side, as that is its weak  point.  Make full use of its Polaron Beams, to cut your enemy ship\'s hull. \n\n------- SHIP STATS -------\n\nHull Rating: 18000\n\nShield Rating:\n     Fore - 12500 @ 10chg\n     Aft - 12500 @ 10chg\n     Dorsal - 12500 @ 10chg\n     Ventral - 12500 @ 10chg\n     Port - 12500 @ 10chg\n     Starboard - 12500 @ 10chg\n\nImpulse Engines\n     Max Speed - 8\n     Max Accel - 1.9\n     Max Ang Velocity - 0.4\n     Max Ang Accel - 0.3\n\nWarp Engines:\n     Max Warp - 9.8\n     Max Cruise Warp - 9.6\n\nCrew Complement - 2500\n\n------- SHIP WEAPONS -------\n\nEnforced Polaron Beams:\n   4xF 2xA 2xD 2xV 2xP 2xS\n     Max Chg - 0.5	\n     Max Dmg - 1500\n     Min Firing Chg - 0.5\n     Rechg Rate - 2\n     Max Damage Distance - 100\n\nPolaron Cannons:\n   4xF 2xA\n     Max Chg - 1\n     Max Dmg - 250\n     Min Firing Chg - 1\n     Rechg Rate - 0.25\n     Cooldown Time - 1.6\n\nTorpedoes:\n    4xF 4xA\n     Poleron - 400\n     Reload Delay - 40\n\n------- SHIP PROPERTIES -------\n\nHull:\n     Max Condition - 18000\n     Repair Complexity - 1\n     Disabled Percentage - 0 \n\nLife Support System:\n     Max Condition - 17000\n     Repair Complexity - 1\n     Disabled Percentage -  0.1\n\nPolaron Beam Emitters:\n     Max Condition - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n\nPolaron Beam System:\n     Max Condition - 9000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n     Normal Power/Sec - 750\n\nPolaron Cannons:\n     Max Condition - 1600\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n\nPolaron Cannon System:\n     Max Condition - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n     Normal Power/Sec - 150\n\nRepair System:\n     Max Condition - 3000\n     Repair Complexity - 3\n     Disabled Percentage - 0 \n     Maximum Repair Points - 100 \n     Repair Teams - 1\n\nSensor Array:\n     Max Condition - 10000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 100 \n     Max # of Probes - 10\n     Sensor Base Range - 4500\n\nShield Generator:\n     Max Condition - 17000\n     Repair Complexity - 1\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 600\n\nTorpedo Bays:\n   2xF 2xA\n     Max Condition - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n\nTorpedo System:\n     Max Condition - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0 \n\nWarp Core:\n     Max Condition - 15000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Power Output/Sec - 2000\n     Main Battery Limit - 700000\n     Backup Battery Limit - 350000\n     Main Conduit Capacity - 2350\n     Backup Battery Capacity - 1150\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 8000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 300\n\n   Main Impulse:\n     Max Condition - 12000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25 \n \nWarp Engines:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n\n   Port Warp:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n\n   Star Warp:\n     Max Condition - 10000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n\n   Warp Enhancer 1:\n     Max Condition - 4500\n     Repair Complexity - 6\n     Disabled Percentage - 0.25\n\n   Warp Enhancer 2:\n     Max Condition - 4500\n     Repair Complexity - 6\n     Disabled Percentage - 0.25"

if menuGroup:           Foundation.ShipDef.DS9FXDominionBC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXDominionBC.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
