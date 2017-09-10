# by USS Sovereign, Wormhole Cone cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'WormholeConeVar1_1'
iconName = 'WormholeConeVar1_1'
longName = 'WormholeConeVar1_1'
shipFile = 'WormholeConeVar1_1' 
species = App.SPECIES_GALAXY

# Ship foundation def
Foundation.ShipDef.WormholeConeVar1_1 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.WormholeConeVar1_1.desc = "The Bajoran wormhole is the only stable wormhole currently known to exist in the galaxy. The terminus nearest to the Federation is located in the Denorios belt in the Bajor system, and crosses some 70,000 light years to the Idran system in the Gamma Quadrant.\n\nThe wormhole is also the home of extra-dimensional beings who are worshipped by the Bajorans as the Prophets, and therefore is also sometimes referred to as the Celestial Temple. The wormhole is also known as \"the anomaly\" by the Jem'Hadar.\n\nBajoran historical records indicate that the wormhole has most likely been in existence for at least the past 10,000 years. In that period of time, nine Orbs have appeared on or near Bajor, and are revered as active links between the Bajoran people and their gods.\n\nThere were several unexplained incidents that are now attributed to the wormhole, although it remained undiscovered until the 24th century. In the 22nd century, Kai Taluno's ship was disabled inside the Denorios belt for several days, and Taluno reported that \"the heavens opened up and nearly swallowed the ship.\" Also, in 2337, an unknown, unpiloted alien ship appeared in the Belt, with a shapeshifting being on board (later named Odo).\n\nBecause the Denorios belt was generally avoided by all interplanetary traffic, the wormhole remained undiscovered until 2369, shortly after the end of the Cardassian Occupation of Bajor. When Starfleet took over operation of the station, Commander Benjamin Sisko and science officer Jadzia Dax investigated the many reported anomalies in the Belt aboard the USS Rio Grande, and became the official discoverers of the wormhole. Shortly thereafter, starbase Deep Space 9 was relocated to a position near the Bajor terminus of the wormhole. \n\nThere is no full understanding of the scientific principles that allow the wormhole to remain stable. Much information, however, has been gained through observation in the past decade. Highly elevated levels of neutrinos are commonly detected prior to the appearance of the wormhole's event horizon, and as a vessel traverses the passage. It is believed that verteron nodes play a large part in keeping the wormhole stable. \n\nIn 2371, Starfleet initiated a joint scientific project with the Bajoran and Cardassian governments to establish a trans-wormhole subspace communications relay to make it possible for ships in the Gamma Quadrant to contact home, as well as to provide early warning of any Dominion attack. The mission was complicated by a warning from Bajoran Vedek Yarka, who cited Trakor's Third Prophecy about the potential destruction of the Celestial Temple. This prophecy was unexpectedly validated soon after with the approach of a previously-unknown, long-period comet. This comet was infused with silithium, which had the potential to permanently destabilize the wormhole if it interacted with the verteron particles in the passage. Unable to alter the comet's trajectory, a shuttlepod from the USS Defiant used a deflector shield to prevent the comet's material from contaminating the wormhole. During the transit, trace amounts of silithium inadvertently leaked through the shield. However, the small amounts did not destablize the wormhole, but instead created a subspace filament inside the wormhole that allowed normal communication between the quadrants.\n\nThe wormhole had an enormous impact on interstellar politics in the Alpha Quadrant. In the first two years, many races eagerly sent explorers and freighters through the wormhole to open relations with new trading partners, and to establish new colonies. However, the wormhole also brought the powers of the Alpha Quadrant into contact with the Dominion, a powerful government that controlled a large swath of territory in the Gamma Quadrant.\n\nIn 2373, Starfleet was forced to blockade the wormhole with self-replicating mines in order to prevent a growing Dominion invasion of the Alpha Quadrant. Although DS9 was subsequently lost to the Dominion in an attack, the minefield was successfully planted, preventing further Dominion ships from departing it. Although the minefield was eventually destroyed during the Federation attempt to retake Deep Space 9, thanks to Sisko appealing to the Prophets themselves for aid, the Dominion fleet currently passing through the wormhole was destroyed by the Prophets, who protected the wormhole from Dominion incursion for the entire Dominion War.\n\nLater that year, Sisko was willing to let the Prophets bring about the Reckoning as they had saved the Alpha and Beta Quadrants by destroying the Dominion fleet. They were also blocking any additional enemy ships from coming through.\n\nThe wormhole was apparently destroyed in late 2374, when Dukat, acting as a conduit for the exiled Pah-wraiths, attacked the Orb of Contemplation which was then housed on Deep Space 9. Following Dukat's attack, all of the Orbs went dark, and the wormhole itself disappeared. Dukat's aim was to force the Prophets out and make the wormhole passable again.\n\nThe disappearance of the wormhole and the apparent loss of contact with their deities caused great consternation and fear among the Bajorans, as well as the rise of the Cult of the Pah-wraiths. The wormhole remained closed for the next three months, until Benjamin Sisko, acting as the Emissary of the Prophets, discovered the Orb of the Emissary on Tyree in early 2375. Sisko's discovery of the previously-unknown tenth Orb signaled the re-opening of the wormhole.\n\nLater that year, Dukat told Damar that he had no regrets in failing to reopen the wormhole by killing the Prophets. \n\nJake watched the wormhole, where his father now was, opening from the Promenade after Captain Sisko's encounter with Dukat in the Fire Caves."

Foundation.ShipDef.WormholeConeVar1_1.fCrew = "Off"

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

