import App
import Foundation

abbrev = "DS9FXLakota"
iconName = "DS9FXLakota"
longName = "Lakota"
shipFile = "DS9FXLakota"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"
Foundation.ShipDef.DS9FXLakota = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.DS9FXLakota.SubMenu = "Federation Ships"
Foundation.ShipDef.DS9FXLakota.SubSubMenu = "Excelsior"
Foundation.ShipDef.DS9FXLakota.fMaxWarp = 9.4 + 0.0001
Foundation.ShipDef.DS9FXLakota.fCruiseWarp = 9 + 0.0001
Foundation.ShipDef.DS9FXLakota.fCrew = 750
Foundation.ShipDef.DS9FXLakota.dTechs = {
   "Fed Ablative Armor": {"Plates": ["Saucer Armor","Aft Armor","Engineering Armor"]}
}

Foundation.ShipDef.DS9FXLakota.desc = "------- DESCRIPTION -------\nThe USS Lakota is an upgraded Excelsior class ship.  It is equipped with ablative armor as well as a compliment of quantum torpedos.  Commanded by Capt. Benteen during the Changeling invasion scare on Earth in 2372, it ferried Sisko, Jake and Odo there from DS9 and later became an accessory to Admiral Leyton\'s martial law plot.  Before suffering 24 dead in the ill-fated attack on the Defiant, it was used to relay transporters when the worldwide power grid went out on Earth; despite the outage, every Starfleet officer on the planet could be called by relay communicator and transporter within 12 hours.  It was in for a weapons and warp drive refit during the weeks it was at Earth, when it received quantum torpedoes.\n\n------- TACTICS -------\nTake advantage of the Quantum Torpedoes the Lakota has as they provide quite a punch.  When attacking it remember to avoid those same Quantums and remember that the Lakota is a greatly enhanced Excelsior with similar advantages and weaknesses.\n\n------- SHIP STATS -------\n\nAblative Armor Rating: 7500\n\nHull Rating: 15000\n\nShield Rating:\n     Fore - 15000 @ 10chg\n     Aft - 15000 @ 10chg\n     Dorsal - 15000 @ 10chg\n     Ventral - 15000 @ 10chg\n     Port - 15000 @ 10chg\n     Starboard - 15000 @ 10chg\n\nImpulse Engines:\n     Max Speed - 9\n     Max Accel - 3.9\n     Max Ang Velocity - 0.25\n     Max Ang Accel - 0.25\n\nWarp Engines:\n     Max Warp - 9.4\n     Max Cruise Warp - 9\n\nCrew Complement: 750\n\n------- SHIP WEAPONS -------\n\nPhasers:\n   6xD 5xV 2xA\n     Max Chg - 1\n     Max Dmg - 700\n     Min Firing Chg - 1 \n     Rechg Rate - 1\n     Max Damage Distance - 100\n\nTorpedoes:\n   6xF 4xA\n     Quantum Type 2 - 40\n     Photon Type 6 - 120\n     Reload Delay - 30\n\n------- SYSTEMS STATS -------\n\nAblative Armor:\n     Max Condition - 7500\n     Repair Complexity - 10\n     Disabled Percentage - 0.5\n\nHull:\n     Max Condition - 15000\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 190000\n     Repair Complexity - 5\n     Disabled Percentage - 0.1\n\nPhaser Arrays:\n     Max Condition - 1000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n\nPhaser System:\n     Max Condition - 4000\n     Repair Complexity - 4 \n     Disabled Percentage - 0.5  \n     Normal Power/Sec - 230  \n\nRepair System:\n     Max Condition - 5000\n     Repair Complexity - 4 \n     Disabled Percentage - 0.65  \n     Maximum Repair Points - 75\n     Repair Teams - 4\n\nSensor Array:\n     Max Condition - 6000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 160\n     Max # of Probes - 8\n     Sensor Base Range - 3850 \n\nShield Generator:\n     Max Condition - 9000\n     Repair Complexity - 2\n     Disabled Percentage - 0.5 \n     Normal Power/Sec - 600\n\nTorpedo Bays:\n   2xF 2xA\n     Max Condition - 2500\n     Repair Complexity - 3\n     Disabled Percentage - 0.75 \n\nTorpedo System:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.75\n     Normal Power/Sec - 130\n\nTractor Beam Emitters:\n   1xF 1xA   \n     Max Condition - 1500\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n\nTractor Beam System:\n     Max Condition - 1500\n     Repair Complexity - 7\n     Disabled Percentage - 0.75\n     Normal Power/Sec - 600\n\nWarp Core:\n     Max Condition - 9000\n     Repair Complexity - 2\n     Disabled Percentage - 0.3\n     Power Output/Sec - 1700\n     Main Battery Limit - 130000\n     Backup Battery Limit - 45000\n     Main Conduit Capacity - 1500\n     Backup Battery Capacity - 160\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n     Normal Power/Sec - 120\n\n   Port Impulse:\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n\n   Star Impulse:\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25  \n\n   Port Impulse 2:\n     Max Condition - 2200\n     Repair Complexity - 1\n     Disabled Percentage - 0.25 \n\n   Star Impulse 2:\n     Max Condition - 2200\n     Repair Complexity - 1\n     Disabled Percentage - 0.25  \n\nWarp Engines:\n     Max Condition - 5000\n     Repair Complexity - 3\n     Disabled Percentage - 0.5\n\n   Port Warp:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n\n   Star Warp:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25"
Foundation.ShipDef.DS9FXLakota.SubMenu = "Federation Ships"

if menuGroup:           Foundation.ShipDef.DS9FXLakota.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXLakota.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
