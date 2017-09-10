# MissionModulePaths for objectives

import MissionIDs

dItems = {MissionIDs.BSM1 : "Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish.Mission1",
        MissionIDs.BSM2 : "Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish.Mission2",
        MissionIDs.BSM3 : "Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish.Mission3",
        MissionIDs.BSM4 : "Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish.Mission4",
        MissionIDs.BSM5 : "Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish.Mission5",
        MissionIDs.HM1 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission1",
        MissionIDs.HM2 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission2",
        MissionIDs.HM3 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission3",
        MissionIDs.HM4 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission4",
        MissionIDs.HM5 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission5",
        MissionIDs.HM6 : "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission6",
        MissionIDs.MM1 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission1",
        MissionIDs.MM2 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission2",
        MissionIDs.MM3 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission3",
        MissionIDs.MM4 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission4",
        MissionIDs.MM5 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission5",
        MissionIDs.MM6 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission6",
        MissionIDs.MM7 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission7",
        MissionIDs.MM8 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission8",
        MissionIDs.MM9 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission9",
        MissionIDs.MM10 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission10",
        MissionIDs.MM11 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission11",
        MissionIDs.MM12 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission12",
        MissionIDs.MM13 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission13",
        MissionIDs.MM14 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission14",
        MissionIDs.MM15 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission15",
        MissionIDs.MM16 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission16",
        MissionIDs.MM17 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission17",
        MissionIDs.MM18 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission18",
        MissionIDs.MM19 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission19",
        MissionIDs.MM20 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission20",
        MissionIDs.MM21 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission21",
        MissionIDs.MM22 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission22",
        MissionIDs.RM1 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.RandomMission1",
        MissionIDs.RM2 : "Custom.DS9FX.DS9FXMissions.MiniMissionMode.RandomMission2",
        MissionIDs.ORM1 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission1",
        MissionIDs.ORM2 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission2",
        MissionIDs.ORM3 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission3",
        MissionIDs.ORM4 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission4",
        MissionIDs.ORM5 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission5",
        MissionIDs.ORM6 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission6",
        MissionIDs.ORM7 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission7",
        MissionIDs.ORM8 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission8",
        MissionIDs.ORM9 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission9",
        MissionIDs.ORM10 : "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission10",
        MissionIDs.TW1 : "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission1",
        MissionIDs.TW2 : "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission2",
        MissionIDs.TW3 : "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission3",
        MissionIDs.TW4 : "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission4",
        MissionIDs.TW5 : "Custom.DS9FX.DS9FXMissions.CampaignMode.TrueWay.Mission5"}

def GetMissionModulePath(sID):   
    global dItems
    if (dItems.has_key(sID)):
        return dItems[sID]
    
    return None