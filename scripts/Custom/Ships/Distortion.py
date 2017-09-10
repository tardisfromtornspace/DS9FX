# by Wowbagger

import Foundation
import App

abbrev = 'Distortion'
iconName = 'Distortion'
longName = 'Distortion'
shipFile = 'Distortion' 
species = App.SPECIES_PROBE

Foundation.ShipDef.Distortion = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.Distortion.desc = "A subspace distortion or subspace disturbance is a distortion of normal spatial fabric, subspace fabric is vulnerable to distortions when a mass is placed within subspace. This effect is similar to the effect of gravity, however due to the properties of subspace the mass is somewhat lighter and the effect is slightly different."

Foundation.ShipDef.Distortion.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

