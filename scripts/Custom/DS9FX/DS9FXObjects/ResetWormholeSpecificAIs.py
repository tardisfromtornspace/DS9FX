# Resets Wormhole Specific AIs

import MissionLib
import DS9Ships
import DS9Stations
import GammaShips

def ResetAllAIs():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0
    lReset = [DS9Ships, DS9Stations, GammaShips]
    for m in lReset:
        m.ResetAI(pSet)
