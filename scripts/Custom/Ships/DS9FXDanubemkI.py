import App
import Foundation

abbrev = "DS9FXDanubemkI"
iconName = "DS9FXDanubemkI"
longName = "Danube Mk I"
shipFile = "DS9FXDanubemkI"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXDanubemkI = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXDanubemkI.SubMenu = "Federation Ships"
Foundation.ShipDef.DS9FXDanubemkI.SubSubMenu = "Danube"
Foundation.ShipDef.DS9FXDanubemkI.fMaxWarp = 5.7 + 0.0001
Foundation.ShipDef.DS9FXDanubemkI.fCruiseWarp = 5 + 0.0001
Foundation.ShipDef.DS9FXDanubemkI.fCrew = 4

Foundation.ShipDef.DS9FXDanubemkI.desc = "------- DESCRIPTION -------\nThe Danube class resembles a large shuttlecraft and are informally called \"runabouts\". They are multi-role vessels used for short-range  movement of personnel and supplies. They have a cockpit that incorporates a short range two-person transporter. The midsection was a detachable  module which could be used for different missions. Assigned to large starships and deep space outposts, including starbases like Deep Space  Nine, runabouts allow for the operation of local exploratory and diplomatic missions around their assigned region without the need for calling  in or diverting a larger starship. Observed Danube class runabouts are named after rivers on Earth.\n\n------- TACTICS -------\nAs would be expected, a vessel of this size does not pose a great threat when isolated. However, in packs of three or more, or supporting  larger starships, they can prove effective as combat support vessels. When attacking Danube Class vessels, a successful torpedo strike should  be enough to knock out its shield vector allowing phasers to destroy the hull.\n\n------- SHIP STATS -------\n\nHull Rating: 3500\n\nShield Rating:\n     Fore - 4000 @ 4chg\n     Aft - 4000 @ 4chg\n     Dorsal - 4000 @ 4chg\n     Ventral - 4000 @ 4chg\n     Port - 4000 @ 4chg\n     Starboard - 4000 @ 4chg\n\nImpulse Engines:\n     Max Speed - 9.5\n     Max Accel - 3.9\n     Max Ang Velocity - 1 \n     Max Ang Accel - 1\n\nWarp Engines:\n     Max Warp - 5.7\n     Max Cruise Warp - 5\n\nCrew Complement: 4\n\n------- SHIP WEAPONS -------\n\nPhasers:\n   2xF 2xA 1xP 1xS \n     Max Chg - 0.75\n     Max Dmg - 500\n     Min Firing Chg - 0.75 \n     Rechg Rate - 1\n     Max Damage Distance - 100 \n\nTorpedoes:\n   2xF\n     Photon Type 6 - 16\n     Reload Delay - 30\n\n------- SYSTEMS STATS -------\n\nHull:\n     Max Condition - 3500\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.1\n\nPhaser Arrays:\n     Max Condition - 300\n     Repair Complexity - 1  \n     Disabled Percentage - 0.5  \n\nPhaser System:\n     Max Condition - 1200\n     Repair Complexity - 1 \n     Disabled Percentage - 0.5  \n     Normal Power/Sec - 50\n\nRepair System:\n     Max Condition - 800\n     Repair Complexity - 4 \n     Disabled Percentage - 0.5 \n     Maximum Repair Points - 1\n     Repair Teams - 1\n\nSensor Array:\n     Max Condition - 600\n     Repair Complexity - 3 \n     Disabled Percentage - 0.5\n     Normal Power/Sec - 50\n     Max # of Probes - 0\n     Sensor Base Range - 1500\n\nShield Generator:\n     Max Condition - 800\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 75\n\nTorpedo Bays:\n   2xF\n     Max Condition - 400\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\nTorpedo System:\n     Max Condition - 1000\n     Repair Complexity - 1\n     Disabled Percentage - 0.5 \n     Normal Power/Sec - 50\n\nWarp Core:\n     Max Condition - 1000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25 \n     Power Output/Sec - 300\n     Main Battery Limit - 30000\n     Backup Battery Limit - 3000\n     Main Conduit Capacity - 400\n     Backup Battery Capacity - 50\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 1000\n     Repair Complexity - 2\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 50\n\n   Port Impulse:\n     Max Condition - 600\n     Repair Complexity - 1 \n     Disabled Percentage - 0.5 \n\n   Star Impulse:\n     Max Condition - 600\n     Repair Complexity - 1  \n     Disabled Percentage - 0.5 \n\nWarp Engines:\n     Max Condition - 1600\n     Repair Complexity - 1\n     Disabled Percentage - 0.5 \n\n   Port Warp:\n     Max Condition - 500\n     Repair Complexity - 1 \n     Disabled Percentage - 0.5 \n\n   Star Warp:\n     Max Condition - 500\n     Repair Complexity - 1 \n     Disabled Percentage - 0.5 "

if menuGroup:           Foundation.ShipDef.DS9FXDanubemkI.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXDanubemkI.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
