# coding=utf-8

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

persistent_enemies_schema = {
    "type": "object",
    "properties": {
        "PersistentEnemies": {
            "type": "array",
            "items": {"$ref": "#/definitions/persistent_enemy"},
        }
    },
    "required": ["PersistentEnemies"],
    "definitions": {
        "persistent_enemy": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Discovered": {"type": "boolean"},
                "AgentType": {"type": "string"},
                "Icon": {"type": "string"},
                "LastDiscoveredLocation": {"type": "string"},
                "LocTag": {"type": "string"},
                "FleeDamage": {"type": "number"},
                "HealthPercent": {"type": "number"},
                "Rank": {"type": "number"},
                "UseTicketing": {"type": "boolean"},
                "Region": {"type": "number"},
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "LastDiscoveredTime": {
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
                }
            },
            "required": ["_id", "Discovered", "AgentType", "Icon", "LastDiscoveredLocation", "LocTag", "FleeDamage",
                         "HealthPercent", "Rank", "UseTicketing", "LastDiscoveredTime"]
        }
    }
}

invasion_schema = {
    "type": "object",
    "properties": {
        "Invasions": {
            "type": "array",
            "items": {"$ref": "#/definitions/invasion"},
        }
    },
    "required": ["Invasions"],
    "definitions": {
        "invasion": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Activation": {
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
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "ChainID": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "AttackerMissionInfo": {
                    "type": "object",
                    "properties": {
                        "faction": {"type": "string"},
                        "seed": {"type": "integer"}
                    }
                },
                "DefenderMissionInfo": {
                    "type": "object",
                    "properties": {
                        "faction": {"type": "string"},
                        "seed": {"type": "integer"}
                    }
                },
                "Completed": {
                    "type": "boolean"
                },
                "Count": {
                    "type": "integer"
                },
                "DefenderFaction": {
                    "type": "string"
                },
                "Faction": {
                    "type": "string"
                },
                "Goal": {
                    "type": "integer"
                },
                "LocTag": {
                    "type": "string"
                },
                "Node": {
                    "type": "string"
                },
                "AttackerReward": {
                    "type": ["object", "array"],
                    "properties": {
                        "additionalProperties": False,
                        "countedItems": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "properties": {
                                    "ItemCount": {"type": "integer"},
                                    "ItemType": {"type": "string"}
                                }
                            }
                        }
                    }
                },
                "DefenderReward": {
                    "type": "object",
                    "properties": {
                        "additionalProperties": False,
                        "countedItems": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "properties": {
                                    "ItemCount": {"type": "integer"},
                                    "ItemType": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            },
            "required": ["Activation", "_id", "ChainID", "AttackerMissionInfo", "Completed", "Count",
                         "DefenderFaction", "DefenderMissionInfo", "Goal", "LocTag", "Node",
                         "Faction", "AttackerReward", "DefenderReward"]
        }
    }
}

invasion_project_schema = {
    "type": "object",
    "properties": {
        "ProjectPct": {
            "type": "array",
            "items": {"type": "number"}
        }
    }
}

daily_deals_schema = {
    "type": "object",
    "properties": {
        "DailyDeals": {
            "type": "array",
            "items": {"$ref": "#/definitions/dailyDeals"}
        }
    },
    "required": ["DailyDeals"],
    "definitions": {
        "dailyDeals": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "StoreItem": {
                    "type": "string"
                },
                "Expiry": {
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
                "Activation": {
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
                "Discount": {
                    "type": "integer"
                },
                "OriginalPrice": {
                    "type": "integer"
                },
                "SalePrice": {
                    "type": "integer"
                },
                "AmountTotal": {
                    "type": "integer"
                },
                "AmountSold": {
                    "type": "integer"
                }
            },
            "required": ["Activation", "StoreItem", "Expiry", "Discount", "OriginalPrice",
                         "SalePrice", "AmountTotal", "AmountSold"]
        }
    }
}

featured_guilds_schema = {
    "type": "object",
    "properties": {
        "FeaturedGuilds": {
            "type": "array",
            "items": {"$ref": "#/definitions/featuredGuilds"}
        }
    },
    "required": ["FeaturedGuilds"],
    "definitions": {
        "featuredGuilds": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Name": {
                    "type": "string"
                },
                "Tier": {
                    "type": "integer"
                },
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "AllianceId": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                }
            },
            "required": ["_id", "Name", "Tier"]
        }
    }
}

hub_events_schema = {
    "type": "object",
    "properties": {
        "HubEvents": {
            "type": "array",
            "items": {"$ref": "#/definitions/HubEvents"}
        }
    },
    "required": ["HubEvents"],
    "definitions": {
        "dailyDeals": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Expiry": {
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
                "Activation": {
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
                "Tag": {
                    "type": "string"
                },
                "Node": {
                    "type": "string"
                },
                "CinematicTag": {
                    "type": "string"
                },
                "CycleFrequency": {
                    "type": "integer"
                },
                "RepeatInterval": {
                    "type": "integer"
                },
                "Transmissions": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["Expiry", "Activation", "RepeatInterval", "Transmissions"]
        }
    }
}

node_overrides_schema = {
    "type": "object",
    "properties": {
        "NodeOverrides": {
            "type": "array",
            "items": {
                "oneOf": [{"$ref": "#/definitions/HidedNode"}, {"$ref": "#/definitions/newRelay"},
                          {"$ref": "#/definitions/occupedNode"}, {"$ref": "#/definitions/customNodes"},
                          {"$ref": "#/definitions/otherNode"}]
            }
        }
    },
    "definitions": {
        "HidedNode": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "Node": {
                    "type": "string",
                },
                "Hide": {
                    "type": "boolean",
                },
            },
            "required": ["_id", "Node", "Hide"]
        },
        "otherNode": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "Node": {
                    "type": "string",
                },
                "Seed": {
                    "type": "integer",
                },
            },
            "required": ["_id", "Node", "Seed"]
        },
        "newRelay": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "Node": {
                    "type": "string",
                },
                "Hide": {
                    "type": "boolean",
                },
                "LevelOverride": {
                    "type": "string",
                },
                "Activation": {
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
                }
            },
            "required": ["_id", "Node", "Hide", "Activation"]
        },
        "occupedNode": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "Node": {
                    "type": "string",
                },
                "ExtraEnemySpec": {
                    "type": "string",
                },
                "EnemySpec": {
                    "type": "string",
                },
                "Faction": {
                    "type": "string",
                },
                "Expiry": {
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
            },
            "required": ["_id", "Node", "ExtraEnemySpec", "Faction", "Expiry", "EnemySpec"]
        },
        "customNodes": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"},
                    },
                },
                "Node": {
                    "type": "string",
                },
                "ExtraEnemySpec": {
                    "type": "string",
                },
                "CustomNpcEncounters": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "Faction": {
                    "type": "string",
                },
                "Expiry": {
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
                "Activation": {
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
                }
            },
            "required": ["_id", "Node", "Expiry", "Activation", "CustomNpcEncounters"]
        }
    }
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
