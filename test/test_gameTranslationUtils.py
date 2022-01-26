# coding=utf-8
from unittest.mock import patch

from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.utils.gameTranslationUtils import get_node, get_enemy_name, get_simaris_target, get_item_name, \
    get_faction, get_invasion_loc_tag, get_acolyte_name, get_region, get_upgrade_type, get_mission_type, \
    get_alert_info, get_alert_weapon_restriction, get_mission_from_starchart, get_map_type, get_alert_aura, \
    get_alert_fx, get_vip_agent, get_task_type, get_syndicate, get_syndicate_rank, get_bounty_job, \
    get_bounty_job_desc, get_nightwave_challenge, get_sortie_boss, get_sortie_modifier, get_stage_name, get_rarity, \
    get_pvp_mission_type, get_pvp_mission_name, get_pvp_desc, get_pvp_alt_desc


class TestGameTranslationsUtils():
    NODE = "SolNode145"
    NODE_NOT_EXISTING = "SolNode789453"
    NODE_TRANSLATED_IT = ("Egeria", "(Cerere)")
    NODE_TRANSLATED_EN = ("Egeria", "(Ceres)")
    NODE_NOT_FOUND = (NODE_NOT_EXISTING), "(????)"
    ITEM_NAME_UNKNOWN = "/Lotus/Types/Items/MiscItems/FormaSpecial"
    ITEM_NAME_NOT_FOUND = "FormaSpecial"
    LOC_TAG_NAME_UNKNOWN = "/Lotus/Language/Menu/SentientsInvasion"
    LOC_TAG_NAME_NOT_FOUND = "SentientsInvasion"
    UPGRADE_TYPE = "GAMEPLAY_PICKUP_AMOUNT"
    UPGRADE_TYPE_IT = "Bonus Drop Risorse"
    UPGRADE_TYPE_EN = "Resource Drop Chance"
    MISSION_TYPE = "MT_SURVIVAL"
    MISSION_TYPE_IT = "Sopravvivenza"
    MISSION_TYPE_EN = "Survival"
    ALERT_TYPE = "/Lotus/Language/Alerts/LotusGiftDesc"
    ALERT_TYPE_IT = "Dono di Lotus"
    ALERT_TYPE_EN = "Lotus Gift"
    WEAPON_TYPE_RESTRICTION = "/Lotus/Weapons/Tenno/LotusLongGun"
    WEAPON_TYPE_RESTRICTION_IT = "Solo Arma Primaria"
    WEAPON_TYPE_RESTRICTION_EN = "Primary Weapon Only"
    MAP_TYPE = "OrokinTower"
    MAP_TYPE_IT = "Torre Orokin"
    MAP_TYPE_EN = "Orokin Tower"
    ALERT_AURA = "/Lotus/Upgrades/Mods/DirectorMods/BossDropReductionAura"
    ALERT_AURA_IT = "Nessun Drop dai Boss"
    ALERT_AURA_EN = "No drop from boss"
    ALERT_FX = "LightningStorm"
    ALERT_FX_IT = "Fulmini"
    ALERT_FX_EN = "Lightning Storm"
    VIP_BOSS = "/Lotus/Types/Enemies/Grineer/Vip/CaptainVorBossAgent"
    VIP_BOSS_IT = "Capitano Vor"
    VIP_BOSS_EN = "Captain Vor"
    VIP_AGENT = "/Lotus/Types/Enemies/TennoReplicants/SyndicateAllies/PalladinoDefenseAgent"
    VIP_AGENT_EN = "Palladino"
    TASK_TYPE = "/Lotus/Types/Challenges/StarChart/RelayReconstruction/RRFireKillDeathSquad"
    TASK_TYPE_IT = ("Sconfiggi il Trio Gustrag", 3)
    TASK_TYPE_EN = ("Defeat Gustrag Tree", 3)
    SYNDICATE_NAME = "RadioLegion2Syndicate"
    SYNDICATE_NAME_IT = "Nightwave - L'emissario"
    SYNDICATE_NAME_EN = "Nightwave - The Emissary"
    SYNDICATE_RANK_NAME = "NecraloidSyndicate"
    SYNDICATE_RANK_NAME_IT = "Autorizzazione: Agnesis"
    SYNDICATE_RANK_NAME_EN = "Clearance: Agnesis"
    BOUNTY_JOB_NAME = "/Lotus/Types/Gameplay/Eidolon/Jobs/AttritionBountySab"
    BOUNTY_JOB_NAME_IT = "Sabota le Linee di Rifornimento Grineer"
    BOUNTY_JOB_NAME_EN = "Sabotage the Enemy Supply Lines"
    BOUNTY_JOB_DESC = "/Lotus/Types/Gameplay/Eidolon/Jobs/AttritionBountySab"
    BOUNTY_JOB_DESC_IT = "Tronca la linea di rifornimento Grineer."
    BOUNTY_JOB_DESC_EN = "Cut off the Grineer supply line."
    NIGHTWAVE_TASK = "/Lotus/Types/Challenges/Seasons/Daily/SeasonDailyDeployGlyph"
    NIGHTWAVE_TASK_IT = ("Graffiti", "Piazza un Glifo", 1000)
    NIGHTWAVE_TASK_EN = ("Graffiti", "Deploy a Glyph while in a mission", 1000)
    SORTIE_BOSS = "SORTIE_BOSS_VOR"
    SORTIE_BOSS_IT = "Capitano Vor"
    SORTIE_BOSS_EN = "Captain Vor"
    SORTIE_MODIFIER = "SORTIE_MODIFIER_LOW_ENERGY"
    SORTIE_MODIFIER_IT = "Riduzione Energia"
    SORTIE_MODIFIER_EN = "Energy Reduction"
    BOUNTY_STAGE = "Stage 1"
    BOUNTY_STAGE_IT = "Fase 1"
    BOUNTY_STAGE_EN = "Stage 1"
    RARITY = "COMMON"
    RARITY_IT = "Comune"
    RARITY_EN = "Common"
    PVP_MISSION_TYPE = "PVPMODE_NONE"
    PVP_MISSION_TYPE_IT = "Nessuno"
    PVP_MISSION_TYPE_EN = "None"
    PVP_CHALLENGE_TYPE = "PVPTimedChallengeWeeklyStandardSet"
    PVP_CHALLENGE_TYPE_COMPLETE = "/Lotus/PVPChallengeTypes/PVPTimedChallengeWeeklyStandardSet"
    PVP_CHALLENGE_TYPE_IT = "Set Missioni Settimanali"
    PVP_CHALLENGE_TYPE_EN = "the standard set of weekly challenges"
    PVP_CHALLENGE_DESC = "PVPTimedChallengeWeeklyStandardSet"
    PVP_CHALLENGE_DESC_IT = "Completa tutte le 3 missioni Settimanali"
    PVP_CHALLENGE_DESC_EN = "Complete all weekly missions"
    PVP_ALT_DESC = "/Lotus/Language/Menu/PVPDMAlternativeModeDesc"
    PVP_ALT_DESC_IT = "Equipaggiato solo con un Opticor modificato, combatti i tuoi compagni Tenno in una battaglia " \
                      "in cui un solo colpo è letale!"
    PVP_ALT_DESC_EN = "Equipped only with a modified Opticor, fight your fellow Tenno in a battle where one shot is " \
                      "lethal!"

    def test_get_node_empty(self) -> None:
        res = get_node("")
        assert ("", "(????)") == res

    def test_get_node_it_found(self) -> None:
        res = get_node(self.NODE)
        assert self.NODE_TRANSLATED_IT == res

    def test_get_node_it_not_found(self) -> None:
        res = get_node(self.NODE_NOT_EXISTING)
        assert self.NODE_NOT_FOUND == res

    def test_get_node_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE)
        assert self.NODE_TRANSLATED_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_not_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node(self.NODE_NOT_EXISTING)
        assert self.NODE_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_no_space(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node("PvpNode1")
        assert ("Conclave", "(????)") == res
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_too_many_space(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_node("PvpNode10")
        assert ("Conclave Domination", "(????)") == res
        OptionsHandler.set_option("Language", "it")

    def test_get_node_en_key_error_exception(self) -> None:
        OptionsHandler.set_option("Language", "en")
        with patch('builtins.open',  side_effect=KeyError('mocked error')):
            res = get_node(self.NODE)
            assert (self.NODE, "(????)") == res
        OptionsHandler.set_option("Language", "it")

    def test_get_enemy_name_found(self) -> None:
        self.ENEMY_NAME = "/Lotus/Types/Enemies/Grineer/AIWeek/ShieldLancer"
        self.ENEMY_TRANSLATED = "Shield Launcher"
        res = get_enemy_name(self.ENEMY_NAME)
        assert self.ENEMY_TRANSLATED == res

    def test_get_enemy_name_not_found(self) -> None:
        self.ENEMY_NAME_UNKNOWN = "/Lotus/Types/Enemies/Grineer/AIWeek/RandomEnemy"
        self.ENEMY_NOT_FOUND = "RandomEnemy"
        res = get_enemy_name(self.ENEMY_NAME_UNKNOWN)
        assert self.ENEMY_NOT_FOUND == res

    def test_get_simaris_target_found(self) -> None:
        self.SYMARIS_TARGET = "/Lotus/Types/Game/Library/Targets/Research7Target"
        self.SYMARIS_TARGET_TRANSLATED = "Guardsman"
        res = get_simaris_target(self.SYMARIS_TARGET)
        assert self.SYMARIS_TARGET_TRANSLATED == res

    def test_get_simaris_target_not_found(self) -> None:
        self.SYMARIS_TARGET_UNKNOWN = "/Lotus/Types/Game/Library/Targets/Research0Target"
        self.SYMARIS_TARGET_NOT_FOUND = "Research0Target"
        res = get_simaris_target(self.SYMARIS_TARGET_UNKNOWN)
        assert self.SYMARIS_TARGET_NOT_FOUND == res

    def test_get_item_name_found_it(self) -> None:
        self.ITEM_NAME = "/Lotus/StoreItems/Types/Items/MiscItems/FormaAura"
        self.ITEM_NAME_TRANSLATED = "Forma Aura"
        res = get_item_name(self.ITEM_NAME)
        assert self.ITEM_NAME_TRANSLATED == res

    def test_get_get_item_name_not_found_it(self) -> None:
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        assert self.ITEM_NAME_NOT_FOUND == res

    def test_get_item_name_found_en(self) -> None:
        self.ITEM_NAME_EN = "/Lotus/StoreItems/Upgrades/Focus/PowerLensGreater"
        self.ITEM_NAME_TRANSLATED_EN = "Greater Zenurik Lens"
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_EN)
        assert self.ITEM_NAME_TRANSLATED_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_get_item_name_not_found_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_item_name(self.ITEM_NAME_UNKNOWN)
        assert self.ITEM_NAME_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_get_item_en_key_error_exception(self) -> None:
        OptionsHandler.set_option("Language", "en")
        with patch('builtins.open',  side_effect=KeyError('mocked error')):
            res = get_item_name(self.ITEM_NAME_UNKNOWN)
            assert self.ITEM_NAME_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_faction_found(self) -> None:
        self.FACTION_NAME = "FC_INFESTATION"
        self.FACTION_NAME_TRANSLATED = "Infested"
        res = get_faction(self.FACTION_NAME)
        assert self.FACTION_NAME_TRANSLATED == res

    def test_get_faction_not_found(self) -> None:
        self.FACTION_NAME_UNKNOWN = "FC_GRINIIER"
        self.FACTION_NAME_NOT_FOUND = "FC_GRINIIER"
        res = get_faction(self.FACTION_NAME_UNKNOWN)
        assert self.FACTION_NAME_NOT_FOUND == res

    def test_get_loc_tag_it_found(self) -> None:
        res = get_invasion_loc_tag("/Lotus/Language/Menu/GrineerInvasionGeneric")
        assert "Offensiva Grineer" == res

    def test_get_loc_tag_it_not_found(self) -> None:
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_UNKNOWN)
        assert self.LOC_TAG_NAME_NOT_FOUND == res

    def test_get_loc_tag_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loc_tag("/Lotus/Language/Menu/CorpusInvasionGeneric")
        assert "Corpus Siege" == res
        OptionsHandler.set_option("Language", "it")

    def test_get_loc_tag_en_not_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_invasion_loc_tag(self.LOC_TAG_NAME_UNKNOWN)
        assert self.LOC_TAG_NAME_NOT_FOUND == res
        OptionsHandler.set_option("Language", "it")

    def test_get_accolyte_name_found(self) -> None:
        self.ACCOLYTE_NAME = "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent"
        self.ACCOLYTE_NAME_TRANSLATED = "Angst"
        res = get_acolyte_name(self.ACCOLYTE_NAME)
        assert self.ACCOLYTE_NAME_TRANSLATED == res

    def test_get_accolyte_name_not_found(self) -> None:
        self.ACCOLYTE_NAME_UNKNOWN = "/Lotus/Types/Enemies/Acolytes/GuardianAcolyteAgent"
        self.ACCOLYTE_NAME_NOT_FOUND = "GuardianAcolyteAgent"
        res = get_acolyte_name(self.ACCOLYTE_NAME_UNKNOWN)
        assert self.ACCOLYTE_NAME_NOT_FOUND == res

    def test_get_region_it_found(self) -> None:
        res = get_region(5)
        assert "Giove" == res

    def test_get_region_it_not_found(self) -> None:
        res = get_region(-2)
        assert "-2" == res

    def test_get_region_en_found(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_region(5)
        assert "Jupiter" == res
        OptionsHandler.set_option("Language", "it")

    def test_get_upgrade_type_it(self) -> None:
        res = get_upgrade_type(self.UPGRADE_TYPE)
        assert self.UPGRADE_TYPE_IT == res

    def test_get_upgrade_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_upgrade_type(self.UPGRADE_TYPE)
        assert self.UPGRADE_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_upgrade_type_unknown(self) -> None:
        res = get_upgrade_type("unknownType")
        assert "unknownType" == res

    def test_get_mission_type_it(self) -> None:
        res = get_mission_type(self.MISSION_TYPE)
        assert self.MISSION_TYPE_IT == res

    def test_get_mission_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_mission_type(self.MISSION_TYPE)
        assert self.MISSION_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_mission_type_empty(self) -> None:
        res = get_mission_type("")
        assert "" == res

    def test_get_mission_type_unknown(self) -> None:
        res = get_mission_type("unknownType")
        assert "unknownType" == res

    def test_get_alert_info_it(self) -> None:
        res = get_alert_info(self.ALERT_TYPE)
        assert self.ALERT_TYPE_IT == res

    def test_get_alert_info_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_alert_info(self.ALERT_TYPE)
        assert self.ALERT_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_alert_info_unknown(self) -> None:
        res = get_alert_info("unknownType")
        assert "unknownType" == res

    def test_get_alert_weapon_restriction_it(self) -> None:
        res = get_alert_weapon_restriction(self.WEAPON_TYPE_RESTRICTION)
        assert self.WEAPON_TYPE_RESTRICTION_IT == res

    def test_get_alert_weapon_restriction_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_alert_weapon_restriction(self.WEAPON_TYPE_RESTRICTION)
        assert self.WEAPON_TYPE_RESTRICTION_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_alert_weapon_restriction_unknown(self) -> None:
        res = get_alert_weapon_restriction("unknownType")
        assert "unknownType" == res

    def test_get_mission_from_starchart(self) -> None:
        res = get_mission_from_starchart("Egeria")
        assert "Ancient Retribution" == res

    def test_get_mission_from_starchart_not_found(self) -> None:
        res = get_mission_from_starchart(self.NODE_NOT_EXISTING)
        assert "" == res

    def test_get_mission_from_starchart_exception(self) -> None:
        with patch('builtins.open',  side_effect=KeyError('mocked error')):
            res = get_mission_from_starchart(self.NODE)
            assert "" == res

    def test_get_map_type_it(self) -> None:
        res = get_map_type(self.MAP_TYPE)
        assert self.MAP_TYPE_IT == res

    def test_get_map_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_map_type(self.MAP_TYPE)
        assert self.MAP_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_map_type_unknown(self) -> None:
        res = get_map_type("unknownType")
        assert "unknownType" == res

    def test_get_alert_aura_it(self) -> None:
        res = get_alert_aura(self.ALERT_AURA)
        assert self.ALERT_AURA_IT == res

    def test_get_alert_aura_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_alert_aura(self.ALERT_AURA)
        assert self.ALERT_AURA_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_alert_aura_unknown(self) -> None:
        res = get_alert_aura("unknownType")
        assert "unknownType" == res

    def test_get_alert_fx_it(self) -> None:
        res = get_alert_fx(self.ALERT_FX)
        assert self.ALERT_FX_IT == res

    def test_get_alert_fx_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_alert_fx(self.ALERT_FX)
        assert self.ALERT_FX_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_alert_fx_unknown(self) -> None:
        res = get_alert_fx("unknownType")
        assert "unknownType" == res

    def test_get_vip_agent_it(self) -> None:
        res = get_vip_agent(self.VIP_BOSS)
        assert self.VIP_BOSS_IT == res

    def test_get_vip_agent_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_vip_agent(self.VIP_AGENT)
        assert self.VIP_AGENT_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_vip_agent_empty(self) -> None:
        res = get_vip_agent("")
        assert "" == res

    def test_get_vip_agent_unknown(self) -> None:
        res = get_vip_agent("unknownType")
        assert "unknownType" == res

    def test_get_task_type_it(self) -> None:
        res = get_task_type(self.TASK_TYPE)
        assert self.TASK_TYPE_IT == res

    def test_get_task_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_task_type(self.TASK_TYPE)
        assert self.TASK_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_task_type_unknown(self) -> None:
        res = get_task_type("unknownType")
        assert ("unknownType", 0) == res

    def test_get_syndicate_it(self) -> None:
        res = get_syndicate(self.SYNDICATE_NAME)
        assert self.SYNDICATE_NAME_IT == res

    def test_get_syndicate_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_syndicate(self.SYNDICATE_NAME)
        assert self.SYNDICATE_NAME_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_syndicate_unknown(self) -> None:
        res = get_syndicate("unknownType")
        assert "unknownType" == res

    def test_get_syndicate_rank_it(self) -> None:
        res = get_syndicate_rank(self.SYNDICATE_RANK_NAME, 0)
        assert self.SYNDICATE_RANK_NAME_IT == res

    def test_get_syndicate_rank_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_syndicate_rank(self.SYNDICATE_RANK_NAME, 0)
        assert self.SYNDICATE_RANK_NAME_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_syndicate_rank_unknown(self) -> None:
        res = get_syndicate_rank("unknownType", 0)
        assert "unknownType" == res

    def test_get_bounty_job_it(self) -> None:
        res = get_bounty_job(self.BOUNTY_JOB_NAME)
        assert self.BOUNTY_JOB_NAME_IT == res

    def test_get_bounty_job_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_bounty_job(self.BOUNTY_JOB_NAME)
        assert self.BOUNTY_JOB_NAME_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_bounty_job_unknown(self) -> None:
        res = get_bounty_job("unknownType")
        assert "unknownType" == res

    def test_get_bounty_job_desc_it(self) -> None:
        res = get_bounty_job_desc(self.BOUNTY_JOB_DESC)
        assert self.BOUNTY_JOB_DESC_IT == res

    def test_get_bounty_job_desc_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_bounty_job_desc(self.BOUNTY_JOB_DESC)
        assert self.BOUNTY_JOB_DESC_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_bounty_job_desc_unknown(self) -> None:
        res = get_bounty_job_desc("unknownType")
        assert "Descrizione non Disponibile" == res

    def test_get_nightwave_challenge_it(self) -> None:
        res = get_nightwave_challenge(self.NIGHTWAVE_TASK)
        assert self.NIGHTWAVE_TASK_IT == res

    def test_get_nightwave_challenge_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_nightwave_challenge(self.NIGHTWAVE_TASK)
        assert self.NIGHTWAVE_TASK_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_nightwave_challenge_unknown(self) -> None:
        res = get_nightwave_challenge("unknownType")
        assert ('???', "unknownType", 0) == res

    def test_get_nightwave_challenge_exception(self) -> None:
        OptionsHandler.set_option("Language", "en")
        with patch('builtins.open', side_effect=KeyError('mocked error')):
            res = get_nightwave_challenge(self.NIGHTWAVE_TASK)
            assert ("???", "SeasonDailyDeployGlyph", 0) == res
        OptionsHandler.set_option("Language", "it")

    def test_get_nightwave_challenge_unknown_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_nightwave_challenge("")
        assert ("???", "", 0) == res
        OptionsHandler.set_option("Language", "it")

    def test_get_sortie_boss_it(self) -> None:
        res = get_sortie_boss(self.SORTIE_BOSS)
        assert self.SORTIE_BOSS_IT == res

    def test_get_sortie_boss_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_sortie_boss(self.SORTIE_BOSS)
        assert self.SORTIE_BOSS_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_sortie_boss_unknown(self) -> None:
        res = get_sortie_boss("unknownType")
        assert "unknownType" == res

    def test_get_sortie_modifier_it(self) -> None:
        res = get_sortie_modifier(self.SORTIE_MODIFIER)
        assert self.SORTIE_MODIFIER_IT == res

    def test_get_sortie_modifier_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_sortie_modifier(self.SORTIE_MODIFIER)
        assert self.SORTIE_MODIFIER_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_sortie_modifier_unknown(self) -> None:
        res = get_sortie_modifier("unknownType")
        assert "unknownType" == res

    def test_get_stage_name_it(self) -> None:
        res = get_stage_name(self.BOUNTY_STAGE)
        assert self.BOUNTY_STAGE_IT == res

    def test_get_stage_name_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_stage_name(self.BOUNTY_STAGE)
        assert self.BOUNTY_STAGE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_stage_name_unknown(self) -> None:
        res = get_stage_name("unknownType")
        assert "unknownType" == res

    def test_get_rarity_it(self) -> None:
        res = get_rarity(self.RARITY)
        assert self.RARITY_IT == res

    def test_get_rarity_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_rarity(self.RARITY)
        assert self.RARITY_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_rarity_unknown(self) -> None:
        res = get_rarity("unknownType")
        assert "unknownType" == res

    def test_get_pvp_mission_type_it(self) -> None:
        res = get_pvp_mission_type(self.PVP_MISSION_TYPE)
        assert self.PVP_MISSION_TYPE_IT.upper() == res

    def test_get_pvp_mission_type_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_pvp_mission_type(self.PVP_MISSION_TYPE)
        assert self.PVP_MISSION_TYPE_EN.upper() == res
        OptionsHandler.set_option("Language", "it")

    def test_get_pvp_mission_type_unknown(self) -> None:
        res = get_pvp_mission_type("unknownType")
        assert "unknownType".upper() == res

    def test_get_pvp_mission_name_it(self) -> None:
        res = get_pvp_mission_name(self.PVP_CHALLENGE_TYPE, self.PVP_CHALLENGE_TYPE_COMPLETE)
        assert self.PVP_CHALLENGE_TYPE_IT == res

    def test_get_pvp_mission_name_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_pvp_mission_name(self.PVP_CHALLENGE_TYPE, self.PVP_CHALLENGE_TYPE_COMPLETE)
        assert self.PVP_CHALLENGE_TYPE_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_pvp_mission_name_unknown(self) -> None:
        res = get_pvp_mission_name("unknownType", "unknownType")
        assert "unknownType" == res

    def test_get_pvp_desc_it(self) -> None:
        res = get_pvp_desc(self.PVP_CHALLENGE_DESC, "0")
        assert self.PVP_CHALLENGE_DESC_IT == res

    def test_get_pvp_desc_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_pvp_desc(self.PVP_CHALLENGE_DESC, "0")
        assert self.PVP_CHALLENGE_DESC_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_pvp_desc_unknown(self) -> None:
        res = get_pvp_desc("unknownType", "0")
        assert "unknownType 0" == res

    def test_get_pvp_alt_desc_it(self) -> None:
        res = get_pvp_alt_desc(self.PVP_ALT_DESC)
        assert self.PVP_ALT_DESC_IT == res

    def test_get_pvp_alt_desc_en(self) -> None:
        OptionsHandler.set_option("Language", "en")
        res = get_pvp_alt_desc(self.PVP_ALT_DESC)
        assert self.PVP_ALT_DESC_EN == res
        OptionsHandler.set_option("Language", "it")

    def test_get_pvp_alt_desc_unknown(self) -> None:
        res = get_pvp_alt_desc("unknownType")
        assert "unknownType" == res
