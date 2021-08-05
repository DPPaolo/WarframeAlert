# coding=utf-8
from jsonschema import validate

from warframeAlert.assets.validator.json_data_validator import *
from warframeAlert.constants.warframeTypes import *


def check_json_data(json_data: JsonData) -> None:
    validate_all_json(json_data)
    validate_fissure(json_data['ActiveMissions'])
    validate_alerts(json_data['Alerts'])
    validate_construction_projects(json_data['ConstructionProjects'])
    validate_daily_deals(json_data['DailyDeals'])
    validate_events(json_data['Events'])
    validate_experiment_recommended(json_data['ExperimentRecommended'])
    validate_featured_guilds(json_data['FeaturedGuilds'])
    validate_flash_sales(json_data['FlashSales'])
    validate_global_upgrades(json_data['GlobalUpgrades'])
    validate_goals(json_data['Goals'])
    validate_hub_events(json_data['HubEvents'])
    validate_invasions(json_data['Invasions'])
    validate_library_info(json_data['LibraryInfo'])
    validate_node_overrides(json_data['NodeOverrides'])
    validate_pvp_tournament(json_data['PVPActiveTournaments'])
    validate_pvp_alternative_mission(json_data['PVPAlternativeModes'])
    validate_pvp_mission(json_data['PVPChallengeInstances'])
    validate_persistent_enemies(json_data['PersistentEnemies'])
    validate_prime_access_availabilities(json_data['PrimeAccessAvailability'])
    validate_prime_vault_availabilities(json_data['PrimeVaultAvailabilities'])
    validate_invasion_project(json_data['ProjectPct'])
    if ('SeasonInfo' in json_data):
        validate_nightwave(json_data['SeasonInfo'])
    validate_sortie(json_data['Sorties'])
    validate_syndicate(json_data['SyndicateMissions'])
    validate_twich_promos(json_data['TwitchPromos'])
    validate_void_traders(json_data['VoidTraders'])
    validate_void_storm(json_data['VoidStorms'])
    validate_version(json_data['Version'])
    validate_mobile_version(json_data['MobileVersion'])
    validate_world_seed(json_data['WorldSeed'])


def validate_all_json(json_data: JsonData) -> None:
    validate(instance={'json_data': json_data}, schema=all_json_schema)


def validate_fissure(json_data: ActiveMissions) -> None:
    validate(instance={'ActiveMissions': json_data}, schema=fissure_schema)


def validate_alerts(json_data: Alerts) -> None:
    validate(instance={'Alerts': json_data}, schema=alerts_schema)


def validate_construction_projects(json_data: ConstructionProjects) -> None:
    validate(instance={'ConstructionProjects': json_data}, schema=construction_projects_schema)


def validate_daily_deals(json_data: DailyDeals) -> None:
    validate(instance={'DailyDeals': json_data}, schema=daily_deals_schema)


def validate_events(json_data: Events) -> None:
    validate(instance={'Events': json_data}, schema=events_schema)


def validate_experiment_recommended(json_data: ExperimentRecommended) -> None:
    validate(instance={'ExperimentRecommended': json_data}, schema=experiment_recommended_schema)


def validate_featured_guilds(json_data: FeaturedGuilds) -> None:
    validate(instance={'FeaturedGuilds': json_data}, schema=featured_guilds_schema)


def validate_flash_sales(json_data: FlashSales) -> None:
    validate(instance={'FlashSales': json_data}, schema=flash_sales_schema)


def validate_global_upgrades(json_data: GlobalUpgrades) -> None:
    validate(instance={'GlobalUpgrades': json_data}, schema=global_upgrades_schema)


def validate_goals(json_data: Goals) -> None:
    validate(instance={'Goals': json_data}, schema=goals_schema)


def validate_hub_events(json_data: HubEvents) -> None:
    validate(instance={'HubEvents': json_data}, schema=hub_events_schema)


def validate_invasions(json_data: Invasions) -> None:
    validate(instance={'Invasions': json_data}, schema=invasion_schema)


def validate_library_info(json_data: LibraryInfo) -> None:
    validate(instance={'LibraryInfo': json_data}, schema=library_info_schema)


def validate_node_overrides(json_data: NodeOverrides) -> None:
    validate(instance={'NodeOverrides': json_data}, schema=node_overrides_schema)


def validate_pvp_tournament(json_data: PVPActiveTournaments) -> None:
    validate(instance={'PVPActiveTournaments': json_data}, schema=pvp_tournament_schema)


def validate_pvp_alternative_mission(json_data: PVPAlternativeModes) -> None:
    validate(instance={'PVPAlternativeModes': json_data}, schema=pvp_alternative_schema)


def validate_pvp_mission(json_data: PVPChallengeInstances) -> None:
    validate(instance={'PVPChallengeInstances': json_data}, schema=pvp_mission_schema)


def validate_persistent_enemies(json_data: PersistentEnemies) -> None:
    validate(instance={'PersistentEnemies': json_data}, schema=persistent_enemies_schema)


def validate_prime_access_availabilities(json_data: PrimeAccessAvailability) -> None:
    validate(instance={'PrimeAccessAvailability': json_data}, schema=prime_access_availabilities_schema)


def validate_prime_vault_availabilities(json_data: PrimeVaultAvailabilities) -> None:
    validate(instance={'PrimeVaultAvailabilities': json_data}, schema=prime_vault_availabilities_schema)


def validate_invasion_project(json_data: ProjectPcts) -> None:
    validate(instance={'ProjectPct': json_data}, schema=invasion_project_schema)


def validate_nightwave(json_data: SeasonInfo) -> None:
    validate(instance={'SeasonInfo': json_data}, schema=season_info_schema)


def validate_sortie(json_data: Sorties) -> None:
    validate(instance={'Sorties': json_data}, schema=sortie_schema)


def validate_syndicate(json_data: SyndicateMissions) -> None:
    validate(instance={'SyndicateMissions': json_data}, schema=syndicate_schema)


def validate_twich_promos(json_data: TwitchPromos) -> None:
    validate(instance={'TwitchPromos': json_data}, schema=twitch_promos_schema)


def validate_void_traders(json_data: VoidTraders) -> None:
    validate(instance={'VoidTraders': json_data}, schema=void_traders_schema)


def validate_void_storm(json_data: VoidStorms) -> None:
    validate(instance={'VoidStorms': json_data}, schema=void_storm_schema)


def validate_version(json_data: int) -> None:
    validate(instance={'Version': json_data}, schema=version_schema)


def validate_mobile_version(json_data: str) -> None:
    validate(instance={'MobileVersion': json_data}, schema=mobile_version_schema)


def validate_world_seed(json_data: str) -> None:
    validate(instance={'WorldSeed': json_data}, schema=world_seed_schema)
