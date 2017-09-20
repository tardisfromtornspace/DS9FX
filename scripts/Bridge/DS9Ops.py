##############################################################################
#	Filename:	DS9Ops.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	This contains the code to create and configure the DS9Ops bridge.
#	It is only called by LoadBridge.Initialize("DS9Ops"), so don't
#	call these functions directly
#
#	Created:	9/12/00 -	DLitwin
#	Modified:	9/11/17	-	Blackrook32
###############################################################################
import App

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

###############################################################################
#	CreateBridgeModel()
#
#	Create the DS9Ops bridge model, viewscreen and main camera, attaching them
#	to the Set passed in.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def CreateBridgeModel(pBridgeSet):
    iDetail = App.g_kImageManager.GetImageDetail()
    pcDetail = [ "Low/", "Medium/", "High/" ]
    pcEnvPath = "data/Models/Sets/DS9Ops/" + pcDetail[iDetail]

    # Pre-load the Bridge model and viewscreen
    App.g_kModelManager.LoadModel("data/Models/Sets/DS9Ops/DS9Ops.NIF", None, pcEnvPath)
    App.g_kModelManager.LoadModel("data/Models/Sets/DS9Ops/OpsViewScreen.NIF", None, pcEnvPath)

    # Load the viewscreen and set it up specially with SetViewScreen()
    pViewScreen = App.ViewScreenObject_Create("data/Models/Sets/DS9Ops/OpsViewScreen.NIF")
    pBridgeSet.SetViewScreen(pViewScreen, "viewscreen")

    # Setup bridge object
    pBridgeObject = App.BridgeObjectClass_Create("data/Models/Sets/DS9Ops/DS9Ops.NIF")
    pBridgeSet.AddObjectToSet(pBridgeObject, "bridge")
    pBridgeObject.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
    pBridgeObject.SetAngleAxisRotation(0.000000, 1.000000, 0.000000, 0.000000)

    # setup hardpoints for dbridge.
    pPropertySet = pBridgeObject.GetPropertySet()
    import Bridge.DS9OpsProperties
    App.g_kModelPropertyManager.ClearLocalTemplates()
    reload(Bridge.DS9OpsProperties)
    Bridge.DS9OpsProperties.LoadPropertySet(pPropertySet)

    # Create camera
    lPos = GetBaseCameraPosition()
    pCamera = App.ZoomCameraObjectClass_Create(lPos[0], lPos[1], lPos[2], 1.570796, -0.000665, -0.087559, 0.996159, "maincamera")
    pCamera.SetMinZoom(0.66)
    pCamera.SetMaxZoom(1.2)
    pCamera.SetZoomTime(0.375)
    pBridgeSet.AddCameraToSet(pCamera, "maincamera")
    pCamera.Update( App.g_kUtopiaModule.GetGameTime() )
    App.g_kVarManager.SetFloatVariable("global", "fZoomTuneState", 0)

    # Load Sovereign bridge specific sounds
    LoadSounds()

    App.g_kModelPropertyManager.ClearLocalTemplates()

###############################################################################
#	GetBaseCameraPosition
#	
#	Get the normal camera position for this bridge.
#	
#	Args:	None
#	
#	Return:	A tuple with the (x,y,z) location for the base camera position.
###############################################################################
def GetBaseCameraPosition():
    return (-43, 170, 105)

###############################################################################
#	AdjustCameraPositionForBridge
#	
#	Adjust the position of the camera, based on the horizontal
#	angle it's facing, based on the bridge that it's on.
#	
#	Args:	fHorizAngle
#	
#	Return:	The adjusted camera position.
###############################################################################
def AdjustCameraPositionForBridge(pCamera, fHorizAngle):
    vLocation = App.TGPoint3()
    apply(vLocation.SetXYZ, GetBaseCameraPosition())
    return vLocation

###############################################################################
#	ConfigureCharacters()
#
#	Configure the bridge crew to the set, which adds bridge specific animations
#	to them.
#
#	Args:	pBridgeSet	- The Bridge set
#
#	Return:	none
###############################################################################
def ConfigureCharacters(pBridgeSet):
    # Configure bridge characters to our bridge
    import Bridge.Characters.OPSFelix
    import Bridge.Characters.OPSKiska
    import Bridge.Characters.OPSSaffi
    import Bridge.Characters.OPSMiguel
    import Bridge.Characters.OPSBrex


    import Bridge.Characters.OPSFemaleExtra1
    import Bridge.Characters.OPSFemaleExtra2
    import Bridge.Characters.OPSFemaleExtra3
    import Bridge.Characters.OPSMaleExtra1
    import Bridge.Characters.OPSMaleExtra2
    import Bridge.Characters.OPSMaleExtra3


    pOPSFelix = App.CharacterClass_Cast(pBridgeSet.GetObject("Tactical"))
    pOPSKiska = App.CharacterClass_Cast(pBridgeSet.GetObject("Helm"))
    pOPSSaffi = App.CharacterClass_Cast(pBridgeSet.GetObject("XO"))
    pOPSMiguel = App.CharacterClass_Cast(pBridgeSet.GetObject("Science"))
    pOPSBrex = App.CharacterClass_Cast(pBridgeSet.GetObject("Engineer"))

    pOPSFemaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSFemaleExtra1"))
    pOPSFemaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSFemaleExtra2"))
    pOPSFemaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSFemaleExtra3"))

    pOPSMaleExtra1 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSMaleExtra1"))
    pOPSMaleExtra2 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSMaleExtra2"))
    pOPSMaleExtra3 = App.CharacterClass_Cast(pBridgeSet.GetObject("OPSMaleExtra3"))



    Bridge.Characters.OPSFelix.ConfigureForOps(pOPSFelix)
    Bridge.Characters.OPSKiska.ConfigureForOps(pOPSKiska)
    Bridge.Characters.OPSSaffi.ConfigureForOps(pOPSSaffi)
    Bridge.Characters.OPSMiguel.ConfigureForOps(pOPSMiguel)
    Bridge.Characters.OPSBrex.ConfigureForOps(pOPSBrex)




    pOPSFelix.SetStanding(1)


    if (pOPSFemaleExtra1):
        Bridge.Characters.OPSFemaleExtra1.ConfigureForOps(pOPSFemaleExtra1)
    if (pOPSFemaleExtra2):
        Bridge.Characters.OPSFemaleExtra2.ConfigureForOps(pOPSFemaleExtra2)
    if (pOPSFemaleExtra3):
        Bridge.Characters.OPSFemaleExtra3.ConfigureForOps(pOPSFemaleExtra3)
    if (pOPSMaleExtra1):
        Bridge.Characters.OPSMaleExtra1.ConfigureForOps(pOPSMaleExtra1)
    if (pOPSMaleExtra2):
        Bridge.Characters.OPSMaleExtra2.ConfigureForOps(pOPSMaleExtra2)
    if (pOPSMaleExtra3):
        Bridge.Characters.OPSMaleExtra3.ConfigureForOps(pOPSMaleExtra3)


    pCamera = App.ZoomCameraObjectClass_GetObject(pBridgeSet, "maincamera")
    pCamera.SetTranslateXYZ(-43, 170, 105)


###############################################################################
#	LoadSounds()
#
#	Load any Sovereign bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():

#	debug("Loading Sovereign door sound")

    pGame = App.Game_GetCurrentGame()
    pGame.LoadSoundInGroup("sfx/door.wav", "LiftDoor", "BridgeGeneric")


###############################################################################
#	UnloadSounds()
#
#	Unload any Sovereign bridge specific sounds
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadSounds():
    App.g_kSoundManager.DeleteSound("LiftDoor")


###############################################################################
#	PreloadAnimations()
#
#	Load any Sovereign bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def PreloadAnimations ():
    kAM = App.g_kAnimationManager

    kAM.LoadAnimation ("data/animations/OPS_Door_L1.nif", "OPS_Door_L1")
    kAM.LoadAnimation ("data/animations/OPS_Door_L2.nif", "OPS_Door_L2")

    # Small animations
    # Science Movement
    kAM.LoadAnimation ("data/animations/OPS_stand_s_s.nif", "OPS_stand_s_s")
    kAM.LoadAnimation ("data/animations/OPS_seated_s_s.nif", "OPS_seated_s_s")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_s.nif", "OPS_face_capt_s")
    kAM.LoadAnimation ("data/animations/OPS_chair_s_face_capt.nif", "OPS_chair_s_face_capt")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_s_reverse.nif", "OPS_face_capt_s_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_s_face_capt_reverse.nif", "OPS_chair_s_face_capt_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_S_in.nif", "OPS_chair_S_in")

    # Science Console Slides and Button Pushes
    kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_A.nif", "EB_S_pushing_buttons_seated_A")
    kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_B.nif", "EB_S_pushing_buttons_seated_B")
    kAM.LoadAnimation ("data/animations/EB_S_pushing_buttons_seated_C.nif", "EB_S_pushing_buttons_seated_C")

    # Science Talking to other stations

    # Engineer Movement
    kAM.LoadAnimation ("data/animations/OPS_stand_e_s.nif", "OPS_stand_e_s")
    kAM.LoadAnimation ("data/animations/OPS_seated_e_s.nif", "OPS_seated_e_s")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_e.nif", "OPS_face_capt_e")
    kAM.LoadAnimation ("data/animations/OPS_chair_e_face_capt.nif", "OPS_chair_e_face_capt")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_e_reverse.nif", "OPS_face_capt_e_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_e_face_capt_reverse.nif", "OPS_chair_e_face_capt_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_E_in.nif", "OPS_chair_E_in")

    # Engineer Console Slides and Button Pushes
    kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_A.nif", "EB_E_pushing_buttons_seated_A")
    kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_B.nif", "EB_E_pushing_buttons_seated_B")
    kAM.LoadAnimation ("data/animations/EB_E_pushing_buttons_seated_C.nif", "EB_E_pushing_buttons_seated_C")

    # Engineer Talking to other stations

    # 
    # medium animations
    # Helm Movement
    kAM.LoadAnimation ("data/animations/OPS_stand_h_m.nif", "OPS_stand_h_m")
    kAM.LoadAnimation ("data/animations/OPS_seated_h_m.nif", "OPS_seated_h_m")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_h.nif", "OPS_face_capt_h")
    kAM.LoadAnimation ("data/animations/OPS_chair_H_face_capt.nif", "OPS_chair_H_face_capt")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_h_reverse.nif", "OPS_face_capt_h_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_H_face_capt_reverse.nif", "OPS_chair_H_face_capt_reverse")
    kAM.LoadAnimation ("data/animations/OPS_hit_h.nif", "OPS_hit_h")


    # Helm Console Slides and Button Pushes
    kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_A.nif", "EB_H_console_slide_A")
    kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_B.nif", "EB_H_console_slide_B")
    kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_C.nif", "EB_H_console_slide_C")
    kAM.LoadAnimation ("data/animations/EB_H_Console_Slide_D.nif", "EB_H_console_slide_D")

    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_A.nif", "EB_H_pushing_buttons_A")
    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_B.nif", "EB_H_pushing_buttons_B")
    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_C.nif", "EB_H_pushing_buttons_C")
    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_D.nif", "EB_H_pushing_buttons_D")
    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_E.nif", "EB_H_pushing_buttons_E")
    kAM.LoadAnimation ("data/animations/EB_H_pushing_buttons_F.nif", "EB_H_pushing_buttons_F")

    # Helm Talking to other stations
    kAM.LoadAnimation ("data/animations/EB_H_Talk_to_C_M.nif", "EB_H_Talk_to_C_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_to_E_M.nif", "EB_H_Talk_to_E_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_to_S_M.nif", "EB_H_Talk_to_S_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_to_T_M.nif", "EB_H_Talk_to_T_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_C_M.nif", "EB_H_Talk_fin_C_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_E_M.nif", "EB_H_Talk_fin_E_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_S_M.nif", "EB_H_Talk_fin_S_M")
    kAM.LoadAnimation ("data/animations/EB_H_Talk_fin_T_M.nif", "EB_H_Talk_fin_T_M")

    # XO Movement
    kAM.LoadAnimation ("data/animations/OPS_seated_c_m.nif", "OPS_seated_c_m")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_c1.nif", "OPS_face_capt_c1")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_c.nif", "OPS_face_capt_c")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_C_reverse.nif", "OPS_face_capt_C_reverse")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_c1_reverse.nif", "OPS_face_capt_c1_reverse")
    kAM.LoadAnimation ("data/animations/OPS_hit_c.nif", "OPS_hit_c")

    # XO Console Slides and Button Pushes
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_A.nif", "EB_C_pushing_buttons_A")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_B.nif", "EB_C_pushing_buttons_B")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_C.nif", "EB_C_pushing_buttons_C")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_D.nif", "EB_C_pushing_buttons_D")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_E.nif", "EB_C_pushing_buttons_E")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_F.nif", "EB_C_pushing_buttons_F")
    kAM.LoadAnimation ("data/animations/EB_C_pushing_buttons_G.nif", "EB_C_pushing_buttons_G")

    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_A.nif", "EB_X_pushing_buttons_A")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_B.nif", "EB_X_pushing_buttons_B")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_C.nif", "EB_X_pushing_buttons_C")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_D.nif", "EB_X_pushing_buttons_D")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_E.nif", "EB_X_pushing_buttons_E")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_F.nif", "EB_X_pushing_buttons_F")
    kAM.LoadAnimation ("data/animations/EB_X_pushing_buttons_G.nif", "EB_X_pushing_buttons_G")

    # XO Talking to other stations
    kAM.LoadAnimation ("data/animations/EB_C_Talk_E_M.nif", "EB_C_Talk_E_M")
    kAM.LoadAnimation ("data/animations/EB_C_Talk_G2_M.nif", "EB_C_Talk_G2_M")
    kAM.LoadAnimation ("data/animations/EB_C_Talk_G3_M.nif", "EB_C_Talk_G3_M")
    kAM.LoadAnimation ("data/animations/EB_C_Talk_TH_M.nif", "EB_C_Talk_TH_M")
    kAM.LoadAnimation ("data/animations/EB_C_Talk_S_M.nif", "EB_C_Talk_S_M")




    # Guest Animations
    kAM.LoadAnimation ("data/animations/OPS_L1toX_M.nif", "OPS_L1toX_M")
    kAM.LoadAnimation ("data/animations/OPS_stand_X_m.nif", "OPS_stand_X_m")
    kAM.LoadAnimation ("data/animations/OPS_seated_X_m.nif", "OPS_seated_X_m")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_X.nif", "OPS_face_capt_X")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_X_reverse.nif", "OPS_face_capt_X_reverse")
    kAM.LoadAnimation ("data/animations/OPS_hit_x.nif", "OPS_hit_x")
    kAM.LoadAnimation ("data/animations/OPS_seated_Capt.nif", "OPS_seated_Capt")


    # Extras
    kAM.LoadAnimation ("data/animations/OPS_L1toG3_S.nif", "OPS_L1toG3_S")
    kAM.LoadAnimation ("data/animations/OPS_L1toG3_M.nif", "OPS_L1toG3_M")
    kAM.LoadAnimation ("data/animations/OPS_L1toG3_L.nif", "OPS_L1toG3_L")

    kAM.LoadAnimation ("data/animations/OPS_L2toG1_S.nif", "OPS_L2toG1_S")
    kAM.LoadAnimation ("data/animations/OPS_L2toG1_M.nif", "OPS_L2toG1_M")
    kAM.LoadAnimation ("data/animations/OPS_L2toG1_L.nif", "OPS_L2toG1_L")

    kAM.LoadAnimation ("data/animations/OPS_L2toG2_S.nif", "OPS_L2toG2_S")
    kAM.LoadAnimation ("data/animations/OPS_L2toG2_M.nif", "OPS_L2toG2_M")
    kAM.LoadAnimation ("data/animations/OPS_L2toG2_L.nif", "OPS_L2toG2_L")

    kAM.LoadAnimation ("data/animations/OPS_G1toL2_S.nif", "OPS_G1toL2_S")
    kAM.LoadAnimation ("data/animations/OPS_G1toL2_M.nif", "OPS_G1toL2_M")
    kAM.LoadAnimation ("data/animations/OPS_G1toL2_L.nif", "OPS_G1toL2_L")
    
    kAM.LoadAnimation ("data/animations/OPS_G2toL2_S.nif", "OPS_G2toL2_S")
    kAM.LoadAnimation ("data/animations/OPS_G2toL2_M.nif", "OPS_G2toL2_M")
    kAM.LoadAnimation ("data/animations/OPS_G2toL2_L.nif", "OPS_G2toL2_L")
    
    kAM.LoadAnimation ("data/animations/OPS_G3toL1_S.nif", "OPS_G3toL1_S")
    kAM.LoadAnimation ("data/animations/OPS_G3toL1_M.nif", "OPS_G3toL1_M")
    kAM.LoadAnimation ("data/animations/OPS_G3toL1_L.nif", "OPS_G3toL1_L")

    kAM.LoadAnimation ("data/animations/OPS_seated_XT01.nif", "OPS_seated_XT01")
    kAM.LoadAnimation ("data/animations/OPS_seated_XT02.nif", "OPS_seated_XT02")
    kAM.LoadAnimation ("data/animations/xtra_interaction_XT01.nif", "xtra_interaction_XT01")
    kAM.LoadAnimation ("data/animations/xtra_interaction_XT02.nif", "xtra_interaction_XT02")


    # Large animations
    # Tactical Movement
    kAM.LoadAnimation ("data/animations/OPS_stand_t_l.nif", "OPS_stand_t_l")
    kAM.LoadAnimation ("data/animations/OPS_seated_t_l.nif", "OPS_seated_t_l")
    kAM.LoadAnimation ("data/animations/OPS_TtoL1_L.nif", "OPS_TtoL1_L")
    kAM.LoadAnimation ("data/animations/OPS_L1toT_L.nif", "OPS_L1toT_L")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_t.nif", "OPS_face_capt_t")
    kAM.LoadAnimation ("data/animations/OPS_chair_T_face_capt.nif", "OPS_chair_T_face_capt")
    kAM.LoadAnimation ("data/animations/OPS_face_capt_t_reverse.nif", "OPS_face_capt_t_reverse")
    kAM.LoadAnimation ("data/animations/OPS_chair_T_face_capt_reverse.nif", "OPS_chair_T_face_capt_reverse")
    kAM.LoadAnimation ("data/animations/OPS_hit_t.nif", "OPS_hit_t")

    # Tactical Console Slides and Button Pushes
    kAM.LoadAnimation ("data/animations/EB_interaction_tac.nif", "EB_interaction_tac")

    # Tactical Talking to other stations
    kAM.LoadAnimation ("data/animations/EB_T_Talk_to_H_L.nif", "EB_T_Talk_to_H_L")
    kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G2_L.nif", "EB_T_Talk_to_G2_L")
    kAM.LoadAnimation ("data/animations/EB_T_Talk_to_G3_L.nif", "EB_T_Talk_to_G3_L")

    kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_H_L.nif", "EB_T_Talk_fin_H_L")
    kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G2_L.nif", "EB_T_Talk_fin_G2_L")
    kAM.LoadAnimation ("data/animations/EB_T_Talk_fin_G3_L.nif", "EB_T_Talk_fin_G3_L")

    return

###############################################################################
#	UnloadAnimations()
#
#	Unload any Sovereign bridge specific animations that are common
#
#	Args:	none
#
#	Return:	none
###############################################################################
def UnloadAnimations ():
    kAM = App.g_kAnimationManager

    kAM.FreeAnimation("OPS_Door_L1")
    kAM.FreeAnimation("OPS_Door_L2")

    # Small animations
    # Science Movement
    kAM.FreeAnimation("OPS_stand_s_s")
    kAM.FreeAnimation("OPS_seated_s_s")
    kAM.FreeAnimation("OPS_face_capt_s")
    kAM.FreeAnimation("OPS_chair_s_face_capt")
    kAM.FreeAnimation("OPS_face_capt_s_reverse")
    kAM.FreeAnimation("OPS_chair_s_face_capt_reverse")
    kAM.FreeAnimation("OPS_chair_S_in")

    # Science Console Slides and Button Pushes
    kAM.FreeAnimation("EB_S_pushing_buttons_seated_A")
    kAM.FreeAnimation("EB_S_pushing_buttons_seated_B")
    kAM.FreeAnimation("EB_S_pushing_buttons_seated_C")

    # Science Talking to other stations

    # Engineer Movement
    kAM.FreeAnimation("OPS_stand_e_s")
    kAM.FreeAnimation("OPS_seated_e_s")
    kAM.FreeAnimation("OPS_face_capt_e")
    kAM.FreeAnimation("OPS_chair_e_face_capt")
    kAM.FreeAnimation("OPS_face_capt_e_reverse")
    kAM.FreeAnimation("OPS_chair_e_face_capt_reverse")
    kAM.FreeAnimation("OPS_chair_E_in")

    # Engineer Console Slides and Button Pushes
    kAM.FreeAnimation("EB_E_pushing_buttons_seated_A")
    kAM.FreeAnimation("EB_E_pushing_buttons_seated_B")
    kAM.FreeAnimation("EB_E_pushing_buttons_seated_C")

    # Engineer Talking to other stations

    # medium animations
    # Helm Movement
    kAM.FreeAnimation("OPS_stand_h_m")
    kAM.FreeAnimation("OPS_seated_h_m")
    kAM.FreeAnimation("OPS_face_capt_h")
    kAM.FreeAnimation("OPS_chair_H_face_capt")
    kAM.FreeAnimation("OPS_face_capt_h_reverse")
    kAM.FreeAnimation("OPS_chair_H_face_capt_reverse")
    kAM.FreeAnimation("OPS_hit_h")

    # Helm Console Slides and Button Pushes
    kAM.FreeAnimation("EB_H_console_slide_A")
    kAM.FreeAnimation("EB_H_console_slide_B")
    kAM.FreeAnimation("EB_H_console_slide_C")
    kAM.FreeAnimation("EB_H_console_slide_D")

    kAM.FreeAnimation("EB_H_pushing_buttons_A")
    kAM.FreeAnimation("EB_H_pushing_buttons_B")
    kAM.FreeAnimation("EB_H_pushing_buttons_C")
    kAM.FreeAnimation("EB_H_pushing_buttons_D")
    kAM.FreeAnimation("EB_H_pushing_buttons_E")
    kAM.FreeAnimation("EB_H_pushing_buttons_F")

    # Helm Talking to other stations
    kAM.FreeAnimation("EB_H_Talk_to_C_M")
    kAM.FreeAnimation("EB_H_Talk_to_E_M")
    kAM.FreeAnimation("EB_H_Talk_to_S_M")
    kAM.FreeAnimation("EB_H_Talk_to_T_M")
    kAM.FreeAnimation("EB_H_Talk_fin_C_M")
    kAM.FreeAnimation("EB_H_Talk_fin_E_M")
    kAM.FreeAnimation("EB_H_Talk_fin_S_M")
    kAM.FreeAnimation("EB_H_Talk_fin_T_M")

    # XO Movement
    kAM.FreeAnimation("OPS_seated_c_m")
    kAM.FreeAnimation("OPS_face_capt_c1")
    kAM.FreeAnimation("OPS_face_capt_c")
    kAM.FreeAnimation("OPS_face_capt_C_reverse")
    kAM.FreeAnimation("OPS_face_capt_c1_reverse")
    kAM.FreeAnimation("OPS_hit_c")

    # XO Console Slides and Button Pushes
    kAM.FreeAnimation("EB_C_pushing_buttons_A")
    kAM.FreeAnimation("EB_C_pushing_buttons_B")
    kAM.FreeAnimation("EB_C_pushing_buttons_C")
    kAM.FreeAnimation("EB_C_pushing_buttons_D")
    kAM.FreeAnimation("EB_C_pushing_buttons_E")
    kAM.FreeAnimation("EB_C_pushing_buttons_F")
    kAM.FreeAnimation("EB_C_pushing_buttons_G")

    # XO Talking to other stations
    kAM.FreeAnimation("EB_C_Talk_E_M")
    kAM.FreeAnimation("EB_C_Talk_H_M")
    kAM.FreeAnimation("EB_C_Talk_T_M")
    kAM.FreeAnimation("EB_C_Talk_S_M")



    # Guest Animations
    kAM.FreeAnimation("OPS_L1toX_M")
    kAM.FreeAnimation("OPS_seated_X_m")
    kAM.FreeAnimation("OPS_stand_X_m")
    kAM.FreeAnimation("OPS_face_capt_X")
    kAM.FreeAnimation("OPS_face_capt_X_reverse")
    kAM.FreeAnimation("OPS_hit_x")
    kAM.FreeAnimation("OPS_seated_Capt")

    kAM.FreeAnimation("EB_X_pushing_buttons_A")
    kAM.FreeAnimation("EB_X_pushing_buttons_B")
    kAM.FreeAnimation("EB_X_pushing_buttons_C")
    kAM.FreeAnimation("EB_X_pushing_buttons_D")
    kAM.FreeAnimation("EB_X_pushing_buttons_E")
    kAM.FreeAnimation("EB_X_pushing_buttons_F")
    kAM.FreeAnimation("EB_X_pushing_buttons_G")

    # Extras
    kAM.FreeAnimation("OPS_L1toG3_S")
    kAM.FreeAnimation("OPS_L1toG3_M")
    kAM.FreeAnimation("OPS_L1toG3_L")

    kAM.FreeAnimation("OPS_L2toG1_S")
    kAM.FreeAnimation("OPS_L2toG1_M")
    kAM.FreeAnimation("OPS_L2toG1_L")

    kAM.FreeAnimation("OPS_L2toG2_S")
    kAM.FreeAnimation("OPS_L2toG2_M")
    kAM.FreeAnimation("OPS_L2toG2_L")

    kAM.FreeAnimation("OPS_G1toL2_S")
    kAM.FreeAnimation("OPS_G1toL2_M")
    kAM.FreeAnimation("OPS_G1toL2_L")
    
    kAM.FreeAnimation("OPS_G2toL2_S")
    kAM.FreeAnimation("OPS_G2toL2_M")
    kAM.FreeAnimation("OPS_G2toL2_L")
    
    kAM.FreeAnimation("OPS_G3toL1_S")
    kAM.FreeAnimation("OPS_G3toL1_M")
    kAM.FreeAnimation("OPS_G3toL1_L")

    kAM.FreeAnimation("OPS_seated_XT01")
    kAM.FreeAnimation("OPS_seated_XT02")
    kAM.FreeAnimation("xtra_interaction_XT01")
    kAM.FreeAnimation("xtra_interaction_XT02")


    # Large animations
    # Tactical Movement
    kAM.FreeAnimation("OPS_stand_t_l")
    kAM.FreeAnimation("OPS_seated_t_l")
    kAM.FreeAnimation ("OPS_TtoL1_L")
    kAM.FreeAnimation ("OPS_L1toT_L")
    kAM.FreeAnimation("OPS_face_capt_t")
    kAM.FreeAnimation("OPS_chair_T_face_capt")
    kAM.FreeAnimation("OPS_face_capt_t_reverse")
    kAM.FreeAnimation("OPS_chair_T_face_capt_reverse")
    kAM.FreeAnimation("OPS_hit_t")


    # Tactical Console Slides and Button Pushes
    kAM.FreeAnimation("EB_interaction_tac")

    # Tactical Talking to other stations
    kAM.FreeAnimation("EB_T_Talk_to_H_L")
    kAM.FreeAnimation("EB_T_Talk_to_G2_L")
    kAM.FreeAnimation("EB_T_Talk_to_G3_L")

    kAM.FreeAnimation("EB_T_Talk_fin_H_L")
    kAM.FreeAnimation("EB_T_Talk_fin_G2_L")
    kAM.FreeAnimation("EB_T_Talk_fin_G3_L")

    return
