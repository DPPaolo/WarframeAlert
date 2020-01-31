from jsonschema import validate
from warframeAlert.assets.validator.json_data_validator import *

# jsonschema.exceptions.ValidationError – is invalid
# jsonschema.exceptions.SchemaError – is invalid


def check_json_data(json_data):
    validate_all_json(json_data)
    validate_daily_deals(json_data['DailyDeals'])
    validate_featured_guilds(json_data['FeaturedGuilds'])
    validate_hub_events(json_data['HubEvents'])
    validate_invasions(json_data['Invasions'])
    validate_library_info(json_data['LibraryInfo'])
    validate_node_overrides(json_data['NodeOverrides'])
    validate_prime_access_availabilities(json_data['PrimeAccessAvailability'])
    validate_prime_vault_availabilities(json_data['PrimeVaultAvailabilities'])
    validate_invasion_project(json_data['ProjectPct'])
    validate_twich_promos(json_data['TwitchPromos'])
    validate_version(json_data['Version'])
    validate_mobile_version(json_data['MobileVersion'])
    validate_world_seed(json_data['WorldSeed'])


def validate_all_json(json_data):
    validate(instance={'json_data': json_data}, schema=all_json_schema)


def validate_daily_deals(json_data):
    validate(instance={'DailyDeals': json_data}, schema=daily_deals_schema)


def validate_featured_guilds(json_data):
    validate(instance={'FeaturedGuilds': json_data}, schema=featured_guilds_schema)


def validate_hub_events(json_data):
    validate(instance={'HubEvents': json_data}, schema=hub_events_schema)


def validate_invasions(json_data):
    validate(instance={'Invasions': json_data}, schema=invasion_schema)


def validate_library_info(json_data):
    validate(instance={'LibraryInfo': json_data}, schema=library_info_schema)


def validate_node_overrides(json_data):
    validate(instance={'NodeOverrides': json_data}, schema=node_overrides_schema)


def validate_prime_access_availabilities(json_data):
    validate(instance={'PrimeAccessAvailability': json_data}, schema=prime_access_availabilities_schema)


def validate_prime_vault_availabilities(json_data):
    validate(instance={'PrimeVaultAvailabilities': json_data}, schema=prime_vault_availabilities_schema)


def validate_invasion_project(json_data):
    validate(instance={'ProjectPct': json_data}, schema=invasion_project_schema)


def validate_twich_promos(json_data):
    validate(instance={'TwitchPromos': json_data}, schema=twitch_promos_schema)


def validate_version(json_data):
    validate(instance={'Version': json_data}, schema=version_schema)


def validate_mobile_version(json_data):
    validate(instance={'MobileVersion': json_data}, schema=mobile_version_schema)


def validate_world_seed(json_data):
    validate(instance={'WorldSeed': json_data}, schema=world_seed_schema)
