all_json_schema = {
    "type": "object",
    "required": ['json_data'],
    "properties": {
        "json_data": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "ActiveMissions": {"type": "array"},
                "Alerts": {"type": "array"},
                "BadlandNodes": {"type": "array"},
                "BuildLabel": {"type": "string"},
                "ConstructionProjects": {"type": "array"},
                "DailyDeals": {"type": "array"},
                "Date": {"type": "integer"},
                "Events": {"type": "array"},
                "FeaturedGuilds": {"type": "array"},
                "FlashSales": {"type": "array"},
                "ForceLogoutVersion": {"type": "integer"},
                "GlobalUpgrades": {"type": "array"},
                "Goals": {"type": "array"},
                "HubEvents": {"type": "array"},
                "Invasions": {"type": "array"},
                "LibraryInfo": {"type": "object"},
                "MobileVersion": {"type": "string"},
                "NodeOverrides": {"type": "array"},
                "PVPActiveTournaments": {"type": "array"},
                "PVPAlternativeModes": {"type": "array"},
                "PVPChallengeInstances": {"type": "array"},
                "PersistentEnemies": {"type": "array"},
                "PrimeAccessAvailability": {"type": "object"},
                "PrimeVaultAvailabilities": {"type": "array"},
                "ProjectPct": {"type": "array"},
                "SeasonInfo": {"type": "object"},
                "Sorties": {"type": "array"},
                "SyndicateMissions": {"type": "array"},
                "Time": {"type": "integer"},
                "Tmp": {"maxItems": 0},
                "TwitchPromos": {"type": "array"},
                "Version": {"type": "integer"},
                "VoidTraders": {"type": "array"},
                "WorldSeed": {"type": "string"}
            },
            "required": ["ActiveMissions", "Alerts", "BadlandNodes", "BuildLabel", "ConstructionProjects",
                         "DailyDeals",
                         "Date", "Events", "FeaturedGuilds", "FlashSales", "ForceLogoutVersion",
                         "GlobalUpgrades",
                         "Goals", "HubEvents", "Invasions", "LibraryInfo", "MobileVersion", "NodeOverrides",
                         "PVPActiveTournaments", "PVPAlternativeModes", "PVPChallengeInstances",
                         "PersistentEnemies",
                         "PrimeAccessAvailability", "PrimeVaultAvailabilities", "ProjectPct", "SeasonInfo",
                         "Sorties", "SyndicateMissions", "Time", "Tmp", "TwitchPromos", "Version", "VoidTraders",
                         "WorldSeed"]
        },
    },
}

twitch_promos_schema = {
    "type": "object",
    "properties": {
        "TwitchPromos": {
            "type": "array",
            "items": {"$ref": "#/definitions/twitchPromo"}
        }
    },
    "definitions": {
        "twitchPromo": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "achievement": {
                    "type": "string"
                },
                "type": {
                    "type": "string",
                    "enum": ["Cumulative", "MarkedEnemy", "SpecificAchievement"],
                },
                "streamers": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "spawnChance": {
                    "type": "integer"
                },
                "cooldown": {
                    "type": "integer"
                },
                "startDate": {
                    "type": "object",
                    "properties": {
                        "$date": {"type": "object"},
                        "items": {
                            "type": "object",
                            "properties": {
                                "$numberLong": {"type": "integer"}
                            }
                        }
                    }
                },
                "endDate": {
                    "type": "object",
                    "properties": {
                        "$date": {"type": "object"},
                        "items": {
                            "type": "object",
                            "properties": {
                                "$numberLong": {"type": "integer"}
                            }
                        }
                    }
                },
                "agentTypes": {
                    "type": "array"
                },
            },
            "required": ["type", "streamers", "achievement", "spawnChance", "cooldown", "agentTypes", "startDate",
                         "endDate"]
        }
    }
}

library_info_schema = {
    "type": "object",
    "properties": {
        "LibraryInfo": {
            "type": "object",
            "required": ["LastCompletedTargetType"],
            "additionalProperties": False,
            "properties": {
                "LastCompletedTargetType": {
                    "type": "string",
                }
            }
        }
    },
}

prime_access_availabilities_schema = {
    "type": "object",
    "properties": {
        "PrimeAccessAvailability": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "State": {
                    "type": "string"
                }
            },
            "required": ["State"]
        },
    },
}

prime_vault_availabilities_schema = {
    "type": "object",
    "properties": {
        "additionalProperties": False,
        "PrimeVaultAvailabilities": {
            "type": "array",
            "minimum": 5,
            "maximum": 5,
            "items": {
                "type": "boolean"
            }
        }
    },
    "required": ["PrimeVaultAvailabilities"]
}

version_schema = {
    "type": "object",
    "properties": {
        "Version": {
            "type": "integer"
        }
    },
    "required": ["Version"]
}

mobile_version_schema = {
    "type": "object",
    "properties": {
        "MobileVersion": {
            "type": "string"
        }
    },
    "required": ["MobileVersion"]
}

world_seed_schema = {
    "type": "object",
    "properties": {
        "WorldSeed": {
            "type": "string"
        }
    },
    "required": ["WorldSeed"]
}
