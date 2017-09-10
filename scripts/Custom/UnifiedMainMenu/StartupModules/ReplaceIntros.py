"""
This replaces the default intros which an install has

by USS Sovereign
"""

from Custom.DS9FX.DS9FXLib import DS9FXOpeningMovie

def GetName():    
    return "DS9FX: Replace Intro Movies"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    return None

def StartUp():
    DS9FXOpeningMovie.StartUp()

