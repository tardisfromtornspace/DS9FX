import App
import Foundation

abbrev = "DS9FXD7Ktinga"
iconName = "DS9FXD7Ktinga"
longName = "D7 K't'inga"
shipFile = "DS9FXD7Ktinga"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXD7Ktinga = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXD7Ktinga.SubMenu = "Klingon Ships"
Foundation.ShipDef.DS9FXD7Ktinga.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.DS9FXD7Ktinga.fCruiseWarp = 8.7 + 0.0001
Foundation.ShipDef.DS9FXD7Ktinga.fCrew = 800

Foundation.ShipDef.DS9FXD7Ktinga.desc = "------- DESCRIPTION -------\nThe Klingon K\'t\'inga class is the successor to the D-7 class. First introduced in the late 23rd century, the K\'t\'inga class has remained in service for decades through the late 24th century (even longer than the Bird Of Prey) where they fought in the Dominion War; a testament to the worthiness of the design. With marked improvements, these warships received constant upgrades and refits to keep it current, and saw continuous use as front-line and border patrol ships throughout the Second Klingon-Federation War and the Dominion War of the early-2370s. They were not always the ship of choice for all missions, however, as more agile craft like the Klingon Bird-of-Prey were better suited for some tasks.  However, the K\'t\'inga is one of the only Klingon Vessels adaptable to exploratory and research use as well. The vessel serves many diplomatic functions and is a reliable light escort ship.\n\n------- TACTICS -------\nThe K\'t\'inga class does have its pros and cons. When attacking this ship, target its shields and hull, since it is an outdated vessel. When attacking with this ship, use combinations of torpedoes and disruptors in one violent volley to maximize damage dealt to your enemy.\n\n------- SHIP STATS -------\n\nHull Rating: 10000\n\nShield Rating:\n     Fore - 8000 @ 12chg\n     Aft - 8000 @ 12chg\n     Dorsal - 8000 @ 12chg\n     Ventral - 8000 @ 12chg\n     Port - 8000 @ 12chg\n     Starboard - 8000 @ 12chg\n\nImpulse Engines:\n     Max Speed - 7.75\n     Max Accel - 3.9\n     Max Ang Velocity - 0.5\n     Max Ang Accel - 0.5\n\nWarp Engines:\n     Max Warp - 9.6\n     Max Cruise Warp - 8.7\n\nCrew Complement: 800\n\n------- SHIP WEAPONS -------\n\nDisruptor Cannons:\n   2xF 2xA\n     Max Chg - 5\n     Max Dmg - 300\n     Min Firing Chg - 2\n     Rechg Rate - 2\n     Cooldown Time - 0.5\n\nDisruptor Beams:\n   1xF 1xA\n     Max Chg - 0.6\n     Max Dmg - 1500\n     Min Firing Chg - 0.6\n     Rechg Rate - 1\n     Max Damage Distance - 70\n\nTorpedoes: \n   4xF 2xA\n     Klingon Photon - 200\n     Reload Delay - 35\n\n------- SHIP PROPERTIES -------\n\nCloaking System:\n     Max Condition - 1600\n     Repair Complexity - 6\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 300\n\nDisruptor Beam Emitters:\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n\nDisruptor Beam System:\n     Max Condition System - 2900 \n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 5\n\nDisruptor Cannons:\n     Max Condition - 600\n     Repair Complexity - 1\n     Disabled Percentage - 0.25   \n\nDisruptor Cannon System:\n     Max Condition - 600\n     Repair Complexity - 9\n     Disabled Percentage - 0.75 \n     Normal Power/Sec - 70\n\nHull:\n     Max Condition - 10000\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 9520\n     Repair Complexity - 1\n     Disabled Percentage - 0.1\n\nRepair System:\n     Max Condition - 800\n     Repair Complexity - 1 \n     Disabled Percentage - 0.1\n     Maximum Repair Points - 35\n     Repair Teams - 4\n\nSensor Array:\n     Max Condition - 6000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 50\n     Max # of Probes - 10\n     Sensor Base Range - 2000\n\nShield Generator:\n     Max Condition - 5000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 180\n\nTorpedo Bays:\n   1xF 1xA\n     Max Condition - 4000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n\nTorpedo System:\n     Max Condition - 4500\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 50\n\nTractor Beam Emitters:\n   1xF 1xA\n     Max Condition - 1200\n     Repair Complexity - 7\n     Disabled Percentage - 0.75\n\nTractor Beam System:\n     Max Condition - 2400\n     Repair Complexity - 7\n     Disabled Percentage - 0.75\n     Normal Power/Sec - 700\n\nWarp Core:\n     Max Condition - 5000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Power Output/Sec - 670\n     Main Battery Limit - 80000\n     Backup Battery Limit - 40000\n     Main Conduit Capacity - 670\n     Backup Battery Capacity - 70\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 2400\n     Repair Complexity - 2\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 50\n\n   Port Impulse:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25 \n\n   Star Impulse:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25 \n\nWarp Engines:\n     Max Condition - 3200\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n\n   Port Warp:\n     Max Condition - 1600\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n\n   Star Warp:\n     Max Condition - 1600\n     Repair Complexity - 3\n     Disabled Percentage - 0.25"

if menuGroup:           Foundation.ShipDef.DS9FXD7Ktinga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXD7Ktinga.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
