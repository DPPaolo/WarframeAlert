# coding=utf-8
from jsonschema import validate
from warframeAlert.assets.validator.json_data_validator import *


def check_json_data(json_data):
    validate_all_json(json_data)
    validate_fissure(json_data['ActiveMissions'])
    validate_alerts(json_data['Alerts'])
    validate_construction_projects(json_data['ConstructionProjects'])
    validate_daily_deals(json_data['DailyDeals'])
    validate_global_upgrades(json_data['GlobalUpgrades'])
    validate_goals(json_data['Goals'])
    validate_events(json_data['Events'])
    validate_featured_guilds(json_data['FeaturedGuilds'])
    validate_flash_sales(json_data['FlashSales'])
    validate_hub_events(json_data['HubEvents'])
    validate_invasions(json_data['Invasions'])
    validate_library_info(json_data['LibraryInfo'])
    validate_node_overrides(json_data['NodeOverrides'])
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
    validate_version(json_data['Version'])
    validate_mobile_version(json_data['MobileVersion'])
    validate_world_seed(json_data['WorldSeed'])


def validate_all_json(json_data):
    validate(instance={'json_data': json_data}, schema=all_json_schema)


def validate_fissure(json_data):
    validate(instance={'ActiveMissions': json_data}, schema=fissure_schema)


def validate_alerts(json_data):
    validate(instance={'Alerts': json_data}, schema=alerts_schema)


def validate_construction_projects(json_data):
    validate(instance={'ConstructionProjects': json_data}, schema=construction_projects_schema)


def validate_daily_deals(json_data):
    validate(instance={'DailyDeals': json_data}, schema=daily_deals_schema)


def validate_global_upgrades(json_data):
    validate(instance={'GlobalUpgrades': json_data}, schema=global_upgrades_schema)


def validate_goals(json_data):
    validate(instance={'Goals': json_data}, schema=goals_schema)


def validate_events(json_data):
    validate(instance={'Events': json_data}, schema=events_schema)


def validate_featured_guilds(json_data):
    validate(instance={'FeaturedGuilds': json_data}, schema=featured_guilds_schema)


def validate_flash_sales(json_data):
    validate(instance={'FlashSales': json_data}, schema=flash_sales_schema)


def validate_hub_events(json_data):
    validate(instance={'HubEvents': json_data}, schema=hub_events_schema)


def validate_invasions(json_data):
    validate(instance={'Invasions': json_data}, schema=invasion_schema)


def validate_library_info(json_data):
    validate(instance={'LibraryInfo': json_data}, schema=library_info_schema)


def validate_node_overrides(json_data):
    validate(instance={'NodeOverrides': json_data}, schema=node_overrides_schema)


def validate_persistent_enemies(json_data):
    validate(instance={'PersistentEnemies': json_data}, schema=persistent_enemies_schema)


def validate_prime_access_availabilities(json_data):
    validate(instance={'PrimeAccessAvailability': json_data}, schema=prime_access_availabilities_schema)


def validate_prime_vault_availabilities(json_data):
    validate(instance={'PrimeVaultAvailabilities': json_data}, schema=prime_vault_availabilities_schema)


def validate_invasion_project(json_data):
    validate(instance={'ProjectPct': json_data}, schema=invasion_project_schema)


def validate_nightwave(json_data):
    validate(instance={'SeasonInfo': json_data}, schema=season_info_schema)


def validate_sortie(json_data):
    validate(instance={'Sorties': json_data}, schema=sortie_schema)


def validate_syndicate(json_data):
    validate(instance={'SyndicateMissions': json_data}, schema=syndicate_schema)


def validate_twich_promos(json_data):
    validate(instance={'TwitchPromos': json_data}, schema=twitch_promos_schema)


def validate_void_traders(json_data):
    validate(instance={'VoidTraders': json_data}, schema=void_traders_schema)


def validate_version(json_data):
    validate(instance={'Version': json_data}, schema=version_schema)


def validate_mobile_version(json_data):
    validate(instance={'MobileVersion': json_data}, schema=mobile_version_schema)


def validate_world_seed(json_data):
    validate(instance={'WorldSeed': json_data}, schema=world_seed_schema)
