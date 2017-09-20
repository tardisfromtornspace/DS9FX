import Foundation

Foundation.BridgeDef('DS9 Ops', 'DS9Ops', dict = { 	
    'modes': [ Foundation.MutatorDef.Stock ],
	'locations': {
		'OPSHelm':	[ 'data/animations/OPS_stand_h_m.nif', 'OPS_stand_h_m' ],
		'OPSTactical':	[ 'data/animations/OPS_stand_t_l.nif', 'OPS_stand_t_l' ],
		'OPSCommander':[ 'data/animations/OPS_stand_c_m.nif', 'OPS_stand_c_m' ],
		'OPSScience':	[ 'data/animations/OPS_stand_S_S.nif', 'OPS_stand_s_s' ],
		'OPSEngineer':	[ 'data/animations/OPS_stand_e_s.nif', 'OPS_stand_e_s' ],
		'OPSGuest':	[ 'data/animations/OPS_stand_X_m.nif', 'OPS_stand_X_m' ],
		'OPSL2M':	[ 'data/animations/OPS_L2toG1_M.nif', 'OPS_L2toG1_M'],
		'OPSG1M':	[ 'data/animations/OPS_G1toL2_M.nif', 'OPS_G1toL2_M'],
		'OPSXT01':	[ 'data/animations/OPS_seated_XT01.NIF', 'OPS_seated_XT01'],
		'OPSXT02':	[ 'data/animations/OPS_seated_XT02.NIF', 'OPS_seated_XT02'], 
	}, 
    'bridgeSound': 	{
			"LiftDoor": {"volume": 1.0,"file": "sfx/DS9Ops/Door.wav", "group": "BridgeGeneric"},
		"AmbBridge": {"volume": 1.0,"file": "sfx/DS9Ops/Ambience.wav", "group": "BridgeGeneric"},
		"RedAlertSound": {"volume": 1.0,"file": "sfx/DS9Ops/redalert.wav", "group": "BridgeGeneric"},
		"YellowAlertSound": {"volume": 1.0,"file": "sfx/DS9Ops/yellowalert.wav", "group": "BridgeGeneric"},
			"GreenAlertSound": {"volume": 1.0,"file": "sfx/DS9Ops/greenalert.wav", "group": "BridgeGeneric"},
			"ViewOn": {"volume": 1.0,"file": "sfx/DS9Ops/ViewscreenOn.wav", "group": "BridgeGeneric"},
			"ViewOff": {"volume": 1.0,"file": "sfx/DS9Ops/ViewscreenOff.wav", "group": "BridgeGeneric"}
			},
    "LoadingScreen": "data/Icons/LoadingScreens/SovereignLoading.tga",
})
