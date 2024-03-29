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
                "BuildLabel": {"type": "string"},
                "ConstructionProjects": {"type": "array"},
                "DTLS": {"type": "number", "enum": [0]},
                "DailyDeals": {"type": "array"},
                "Events": {"type": "array"},
                "ExperimentRecommended": {"type": "array"},
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
                "PrimeTokenAvailability": {"type": "boolean"},
                "PrimeVaultAvailabilities": {"type": "array"},
                "PrimeVaultTraders": {"type": "array"},
                "ProjectPct": {"type": "array"},
                "SeasonInfo": {"type": "object"},
                "Sorties": {"type": "array"},
                "SyndicateMissions": {"type": "array"},
                "Time": {"type": "integer"},
                "Tmp": {"type": "string"},
                "TwitchPromos": {"type": "array"},
                "Version": {"type": "integer"},
                "VoidTraders": {"type": "array"},
                "VoidStorms": {"type": "array"},
                "WorldSeed": {"type": "string"},
            },
            "required": ["ActiveMissions", "Alerts", "BuildLabel", "ConstructionProjects",
                         "DailyDeals", "Events", "FeaturedGuilds", "FlashSales", "ForceLogoutVersion",
                         "GlobalUpgrades", "Goals", "HubEvents", "Invasions", "LibraryInfo", "MobileVersion",
                         "NodeOverrides", "PVPActiveTournaments", "PVPAlternativeModes", "PVPChallengeInstances",
                         "PersistentEnemies", "PrimeAccessAvailability", "PrimeVaultAvailabilities", "ProjectPct",
                         "Sorties", "SyndicateMissions", "Time", "Tmp", "TwitchPromos", "Version", "VoidTraders",
                         "WorldSeed"]
        },
    },
}

prime_vault_traders = {
    "type": "object",
    "properties": {
        "PrimeVaultTraders": {
            "type": "array",
            "items": {"$ref": "#/definitions/primeVaultTraders"},
        }
    },
    "required": ["PrimeVaultTraders"],
    "definitions": {
        "primeVaultTraders": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Expiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                "InitialStartDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                    "additionalProperties": False,
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Completed": {"type": "boolean"},
                "Node": {"type": "string"},
                "Manifest": {"type": "array",
                             "items": {
                                 "type": "object",
                                 "additionalProperties": False,
                                 "properties": {
                                     "ItemType": {"type": "string"},
                                     "RegularPrice": {"type": "integer"},
                                     "PrimePrice": {"type": "integer"},
                                 }
                             }},
                "ScheduleInfo": {"type": "array",
                                 "items": {
                                     "type": "object",
                                     "additionalProperties": False,
                                     "properties": {
                                         "Expiry": {
                                             "type": "object",
                                             "additionalProperties": False,
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
                                         "FeaturedItem": {"type": "string"},
                                     }
                                 }},
            },
            "required": ["_id", "Activation", "Expiry", "InitialStartDate", "Completed", "Node",
                         "Manifest", "ScheduleInfo"],
        }
    }
}


pvp_tournament_schema = {
    "type": "object",
    "properties": {
        "PVPActiveTournaments": {
            "type": "array",
            "items": {"$ref": "#/definitions/pvpTournament"},
        }
    },
    "required": ["PVPActiveTournaments"],
    "definitions": {
        "pvpTournament": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
            },
            "required": [],
        }
    }
}

pvp_alternative_schema = {
    "type": "object",
    "properties": {
        "PVPAlternativeModes": {
            "type": "array",
            "items": {"$ref": "#/definitions/alternativePvP"},
        }
    },
    "required": ["PVPAlternativeModes"],
    "definitions": {
        "alternativePvP": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "TitleLoc": {"type": "string"},
                "DescriptionLoc": {"type": "string"},
                "DisableAmmoPickups": {"type": "boolean"},
                "DisableEnergyPickups": {"type": "boolean"},
                "DisableEnergySurge": {"type": "boolean"},
                "DisableWeaponHud": {"type": "boolean"},
                "DisableWeaponSwitching": {"type": "boolean"},
                "MatchTimeOverride": {"type": "number"},
                "MaxPlayersOverride": {"type": "number"},
                "MaxTeamCountDifferenceOverride": {"type": "number"},
                "MinPlayersPerTeamOverride": {"type": "number"},
                "TargetMode": {"type": "string"},
                "ForcedLoadouts": {"type": "array",
                                   "items": {
                                       "type": "object",
                                       "additionalProperties": False,
                                       "properties": {
                                       }
                                   }},
            },
            "required": ["TitleLoc", "DescriptionLoc", "DisableAmmoPickups", "DisableEnergyPickups",
                         "DisableEnergySurge", "DisableWeaponHud", "ForcedLoadouts",
                         "DisableWeaponSwitching", "MatchTimeOverride", "MaxPlayersOverride",
                         "MaxTeamCountDifferenceOverride", "MinPlayersPerTeamOverride"],
        }
    }
}

pvp_mission_schema = {
    "type": "object",
    "properties": {
        "PVPChallengeInstances": {
            "type": "array",
            "items": {"$ref": "#/definitions/pvpMissions"},
        }
    },
    "required": ["PVPChallengeInstances"],
    "definitions": {
        "pvpMissions": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "startDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Category": {"type": "string"},
                "PVPMode": {"type": "string"},
                "challengeTypeRefID": {"type": "string"},
                "subChallenges": {"type": "array"},
                "isGenerated": {"type": "boolean"},
                "params": {"type": "array",
                           "items": {
                               "type": "object",
                               "additionalProperties": False,
                               "properties": {
                                   "n": {"type": "string"},
                                   "v": {"type": "integer"}
                               }
                           }},
            },
            "required": ["startDate", "endDate", "_id", "Category", "PVPMode", "challengeTypeRefID", "isGenerated",
                         "subChallenges", "params"],
        }
    }
}

void_storm_schema = {
    "type": "object",
    "properties": {
        "VoidStorms": {
            "type": "array",
            "items": {"$ref": "#/definitions/voidStorm"},
        }
    },
    "required": ["VoidStorms"],
    "definitions": {
        "voidStorm": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Expiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                    "additionalProperties": False,
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "ActiveMissionTier": {"type": "string"},
                "Node": {"type": "string"},
            },
            "required": ["_id", "Activation", "Expiry", "ActiveMissionTier", "Node"],
        }
    }
}

experiment_recommended_schema = {
    "type": "object",
    "properties": {
        "ExperimentRecommended": {
            "type": "array",
            "items": {"$ref": "#/definitions/experimentRecommended"},
        }
    },
    "required": ["ExperimentRecommended"],
    "definitions": {
        "experimentRecommended": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
            },
            "required": [],
        }
    }
}

fissure_schema = {
    "type": "object",
    "properties": {
        "ActiveMissions": {
            "type": "array",
            "items": {"$ref": "#/definitions/fissure"},
        }
    },
    "required": ["ActiveMissions"],
    "definitions": {
        "fissure": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Expiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                    "additionalProperties": False,
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Seed": {"type": "integer"},
                "Region": {"type": "integer"},
                "Modifier": {"type": "string"},
                "Node": {"type": "string"},
                "MissionType": {"type": "string"},
            },
            "required": ["Activation", "Expiry", "_id", "Seed", "Region", "Modifier", "Node", "MissionType"],
        }
    }
}

flash_sales_schema = {
    "type": "object",
    "properties": {
        "FlashSales": {
            "type": "array",
            "items": {"$ref": "#/definitions/sales"},
        }
    },
    "required": ["FlashSales"],
    "definitions": {
        "sales": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "StartDate": {
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
                "EndDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                "ProductExpiryOverride": {
                    "type": "object",
                    "additionalProperties": False,
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
                "ExperimentFeatured": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "ExperimentGroup": {"type": "string"},
                            "FeaturedIndex": {"type": "integer"}
                        }
                    }

                },
                "BannerIndex": {"type": "integer"},
                "BogoBuy": {"type": "integer", "enum": [0]},
                "BogoGet": {"type": "integer", "enum": [0]},
                "Discount": {"type": "integer"},
                "PremiumOverride": {"type": "integer"},
                "RegularOverride": {"type": "integer"},
                "ShowInMarket": {"type": "boolean"},
                "ShowWithRecommended": {"type": "boolean"},
                "Featured": {"type": "boolean"},
                "Popular": {"type": "boolean"},
                "TypeName": {"type": "string"},
            },
            "required": ["StartDate", "EndDate", "BannerIndex", "BogoBuy", "BogoGet", "Discount", "PremiumOverride",
                         "RegularOverride", "ShowInMarket",
                         "Featured", "Popular", "TypeName"],
        }
    }
}

sortie_schema = {
    "type": "object",
    "properties": {
        "Sorties": {
            "type": "array",
            "items": {"$ref": "#/definitions/sortie"},
        }
    },
    "required": ["Sorties"],
    "definitions": {
        "sortie": {
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
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Seed": {"type": "integer"},
                "Boss": {"type": "string"},
                "Reward": {"type": "string"},
                "ExtraDrops": {"type": "array",
                               "items": {"type": "object",
                                         "additionalProperties": False,
                                         }},
                "Variants": {"type": "array",
                             "items": {"type": "object",
                                       "additionalProperties": False,
                                       "properties": {
                                           "missionType": {"type": "string"},
                                           "modifierType": {"type": "string"},
                                           "node": {"type": "string"},
                                           "tileset": {"type": "string"},
                                       },
                                       "required": ["missionType", "modifierType", "node", "tileset"]
                                       }},
                "Twitter": {"type": "boolean"}
            },
            "required": ["_id", "Activation", "Expiry", "Seed", "Boss", "Reward", "ExtraDrops", "Variants"],
        }
    }
}

void_traders_schema = {
    "type": "object",
    "properties": {
        "VoidTraders": {
            "type": "array",
            "items": {"$ref": "#/definitions/baroKiTeer"},
        }
    },
    "required": ["VoidTraders"],
    "definitions": {
        "baroKiTeer": {
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
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Node": {"type": "string"},
                "Character": {"type": "string"},
                "Manifest": {"type": "array",
                             "items": {
                                 "type": "object",
                                 "additionalProperties": False,
                                 "properties": {
                                     "ItemType": {"type": "string"},
                                     "PrimePrice": {"type": "integer"},
                                     "RegularPrice": {"type": "integer"},
                                 },
                                 "required": ["ItemType", "PrimePrice", "RegularPrice"],
                             }}
            },
            "required": ["Activation", "Expiry", "_id", "Node", "Character"],
        }
    }
}

syndicate_schema = {
    "type": "object",
    "properties": {
        "SyndicateMissions": {
            "type": "array",
            "items": {"$ref": "#/definitions/syndicate"},
        }
    },
    "required": ["SyndicateMissions"],
    "definitions": {
        "syndicate": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Tag": {
                    "type": "string",
                    "enum": ["ArbitersSyndicate", "CephalonSudaSyndicate", "NewLokaSyndicate",
                             "PerrinSyndicate", "RedVeilSyndicate", "SteelMeridianSyndicate", "AssassinsSyndicate",
                             "QuillsSyndicate", "CetusSyndicate", "VentKidsSyndicate", "VoxSyndicate",
                             "SolarisSyndicate", "RadioLegionSyndicate", "RadioLegionIntermissionSyndicate",
                             "RadioLegion2Syndicate", "RadioLegionIntermission2Syndicate", "EventSyndicate",
                             "RadioLegion3Syndicate", "RadioLegionIntermission3Syndicate", "EntratiSyndicate",
                             "NecraloidSyndicate", "RadioLegionIntermission4Syndicate", "ZarimanSyndicate",
                             "RadioLegionIntermission5Syndicate"]
                },
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Expiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                        "$oid": {"type": "string"}
                    }
                },
                "Seed": {"type": "integer"},
                "Nodes": {"type": "array",
                          "items": {"type": "string"}},
                'Jobs': {"type": "array",
                         "items": {
                             "type": "object",
                             "properties": {
                                 "jobType": {"type": "string"},
                                 "rewards": {"type": "string"},
                                 "masteryReq": {"type": "integer"},
                                 "minEnemyLevel": {"type": "integer"},
                                 "maxEnemyLevel": {"type": "integer"},
                                 "xpAmounts": {"type": "array", "items": {"type": "integer"}},
                             }
                         }},
            },
            "required": ["Tag", "Activation", "Expiry", "_id", "Seed", "Nodes"],
        }
    }
}

season_info_schema = {
    "type": "object",
    "properties": {
        "SeasonInfo": {
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
                "AffiliationTag": {"type": "string"},
                "Params": {"type": "string"},
                "Phase": {"type": "integer"},
                "Season": {"type": "integer"},
                "ActiveChallenges": {"type": "array",
                                     "items": {
                                         "type": "object",
                                         "additionalProperties": False,
                                         "properties": {
                                             "_id": {
                                                 "type": "object",
                                                 "properties": {
                                                     "$oid": {"type": "string"}
                                                 }
                                             },
                                             "Activation": {
                                                 "type": "object",
                                                 "additionalProperties": False,
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
                                             "Expiry": {
                                                 "type": "object",
                                                 "additionalProperties": False,
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
                                             "Challenge": {"type": "string"},
                                             "Daily": {"type": "boolean"},
                                         },
                                         "required": ["_id", "Activation", "Expiry", "Challenge"],
                                     }
                                     },

            },
            "required": ["Activation", "Expiry", "AffiliationTag", "Season", "Phase", "Params", "ActiveChallenges"],
        }
    },
    "required": ["SeasonInfo"],
}

construction_projects_schema = {
    "type": "object",
    "properties": {
        "ConstructionProjects": {
            "type": "array",
            "items": {"$ref": "#/definitions/constructionSchema"},
        }
    },
    "required": ["ConstructionProjects"],
    "definitions": {
        "constructionSchema": {
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
                "Tag": {"type": "string"},
                "Node": {"type": "string"},
                "HunterBoostTask": {"type": "string"},
                "Tasks": {"type": "array",
                          "items": {"type": "string"}},
                "ToolTips": {"type": "array",
                             "items": {"type": "string"}},
            },
            "required": ["Activation", "Tasks", "Node", "Tag", "HunterBoostTask"],
        }
    }
}

goals_schema = {
    "type": "object",
    "properties": {
        "Goals": {
            "type": "array",
            "items": {"$ref": "#/definitions/WfEvents"},
        }
    },
    "required": ["Goals"],
    "definitions": {
        "WfEvents": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
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
                "Tag": {"type": "string"},
                "Desc": {"type": "string"},
                # Extra data
                "Icon": {"type": "string"},
                "Count": {"type": "integer"},
                "Personal": {"type": "boolean"},
                "Community": {"type": "boolean"},
                "ClampNodeScores": {"type": "boolean"},
                "Bounty": {"type": "boolean"},
                "ToolTip": {"type": "string"},
                "ScoreLocTag": {"type": "string"},
                "ScoreMaxTag": {"type": "string"},
                "ScoreVar": {"type": "string"},
                "MissionKeyRotation": {"type": "array",
                                       "items": {"type": "string"}},
                "MissionKeyName": {"type": "string"},
                "MissionKeyRotationInterval": {"type": "integer"},
                "ConcurrentMissionKeyNames": {"type": "array",
                                              "items": {"type": "string"}},
                "Success": {"type": "integer"},
                "Faction": {"type": "string"},
                "InstructionalItem": {"type": "string"},
                "RoamingVIP": {"type": "string"},
                "PrereqGoalTags": {"type": "array",
                                   "items": {"type": "string"}},

                # Fomorian or ghoul data
                "HealthPct": {"type": "number"},
                "Fomorian": {"type": "boolean"},
                "Best": {"type": "boolean"},
                "ScoreTagBlocksGuildTierChanges": {"type": "boolean"},
                "RewardNode": {"type": "string"},
                "ClanGoal": {"type": "array",
                             "items": {"type": "string"}},
                "VictimNode": {"type": "string"},
                "Transmission": {"type": "string"},
                "OptionalInMission": {"type": "boolean"},
                "RelayReconstruction": {"type": "integer"},
                "Regions": {"type": "array",
                            "items": {"type": "integer"}},
                "RegionIdx": {"type": "integer"},
                "ArchwingDrops": {"type": "array",
                                  "items": {"type": "string"}},
                "RegionDrops": {"type": "array",
                                "items": {"type": "string"}},
                "UpgradeIds": {"type": "array",
                               "items": {
                                   "type": "object",
                                   "properties": {
                                       "$oid": {"type": "string"}
                                   }}
                               },
                "JobAffiliationTag": {"type": "string"},
                "JobCurrentVersion": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "JobPreviousVersion": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                'Jobs': {"type": "array",
                         "items": {
                             "type": "object",
                             "additionalProperties": False,
                             "properties": {
                                 "jobType": {"type": "string"},
                                 "rewards": {"type": "string"},
                                 "masteryReq": {"type": "integer"},
                                 "minEnemyLevel": {"type": "integer"},
                                 "maxEnemyLevel": {"type": "integer"},
                                 "xpAmounts": {"type": "array", "items": {"type": "integer"}},
                             }
                         }},
                'PreviousJobs': {"type": "array",
                                 "items": {
                                     "type": "object",
                                     "properties": {
                                         "jobType": {"type": "string"},
                                         "rewards": {"type": "string"},
                                         "masteryReq": {"type": "integer"},
                                         "minEnemyLevel": {"type": "integer"},
                                         "maxEnemyLevel": {"type": "integer"},
                                         "xpAmounts": {"type": "array", "items": {"type": "integer"}},
                                     }
                                 }},

                # Scarlet Spear Data
                "PauseAutoScheduling": {"type": "boolean"},
                "NextAltActivation": {
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
                "NextAltExpiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                "AltActivation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "AltExpiry": {
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
                "EpochNum": {"type": "integer"},
                "CompletionBonus": {"type": "array",
                                    "items": {"type": "integer"}},
                "Metadata": {"type": "string"},

                # Hub Event
                "ContinuousHubEvent": {"type": "object",
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
                                           "RepeatInterval": {
                                               "type": "integer"
                                           },
                                           "Transmission": {"type": "string"},
                                           "Transmissions": {"type": "array"}
                                       },
                                       "required": ["Expiry", "Activation", "RepeatInterval"]
                                       },

                "MissionInfo": {
                    "additionalProperties": False,
                    "properties": {
                        "location": {"type": "string"},
                        "levelOverride": {"type": "string"},
                        "missionType": {"type": "string"},
                        "faction": {"type": "string"},
                        "enemySpec": {"type": "string"},
                        "maxEnemyLevel": {"type": "integer"},
                        "minEnemyLevel": {"type": "integer"},
                        "archwingRequired": {"type": "boolean"},
                        "isSharkwingMission": {"type": "boolean"},
                        "maxWaveNum": {"type": "integer"},
                        "nightmare": {"type": "integer"},
                        "difficulty": {"type": "integer"},
                        "missionReward": {
                            "type": "object",
                            "properties": {
                                "additionalProperties": False,
                                "credits": {"type": "integer"},
                                "xp": {"type": "integer"},
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
                                },
                                "countedStoreItems": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "properties": {
                                            "ItemCount": {"type": "integer"},
                                            "StoreItem": {"type": "string"}
                                        }
                                    }
                                },
                                "randomizedItems": {"type": "string"},
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            },
                        },
                        "descText": {"type": "string"},
                        "extraEnemySpec": {"type": "string"},
                        # Extra Data
                        "goalTag": {"type": "string"},
                        "exclusiveWeapon": {"type": "string"},
                        "leadersAlwaysAllowed": {"type": "boolean"},
                        "advancedSpawners": {"type": "array",
                                             "items": {"type": "string"}},
                        "requiredItems": {"type": "array",
                                          "items": {"type": "string"}},
                        "requiredItemsCounts": {"type": "number"},
                        "consumeRequiredItems": {"type": "boolean"},
                        "levelAuras": {"type": "array",
                                       "items": {"type": "string"}},
                        "vipAgent": {"type": "string"},
                        "icon": {"type": "string"},
                    }
                },

                # Reward
                "Node": {"type": "string"},
                "ConcurrentNodes": {"type": "array",
                                    "items": {"type": "string"}},
                "ConcurrentNodeReqs": {"type": "array",
                                       "items": {"type": "integer"}},
                "Goal": {"type": "integer"},
                "BonusGoal": {"type": "integer"},
                "InterimGoals": {"type": "array",
                                 "items": {"type": "integer"}},

                "Reward": {"type": "object",
                           "additionalProperties": False,
                           "properties": {
                               "additionalProperties": False,
                               "credits": {"type": "integer"},
                               "xp": {"type": "integer"},
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
                               },
                               "countedStoreItems": {
                                   "type": "array",
                                   "items": {
                                       "type": "object",
                                       "additionalProperties": False,
                                       "properties": {
                                           "ItemCount": {"type": "integer"},
                                           "StoreItem": {"type": "string"}
                                       }
                                   }
                               },
                               "randomizedItems": {"type": "string"},
                               "items": {
                                   "type": "array",
                                   "items": {"type": "string"}
                               }
                           }
                           },
                "BonusReward": {"type": "object",
                                "properties": {
                                    "additionalProperties": False,
                                    "credits": {"type": "integer"},
                                    "xp": {"type": "integer"},
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
                                    },
                                    "countedStoreItems": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "additionalProperties": False,
                                            "properties": {
                                                "ItemCount": {"type": "integer"},
                                                "StoreItem": {"type": "string"}
                                            }
                                        }
                                    },
                                    "randomizedItems": {"type": "string"},
                                    "items": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    }
                                }
                                },
                "InterimRewards": {"type": "array",
                                   "items": {"type": "object",
                                             "additionalProperties": False,
                                             "properties": {
                                                 "additionalProperties": False,
                                                 "credits": {"type": "integer"},
                                                 "xp": {"type": "integer"},
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
                                                 },
                                                 "countedStoreItems": {
                                                     "type": "array",
                                                     "items": {
                                                         "type": "object",
                                                         "additionalProperties": False,
                                                         "properties": {
                                                             "ItemCount": {"type": "integer"},
                                                             "StoreItem": {"type": "string"}
                                                         }
                                                     }
                                                 },
                                                 "randomizedItems": {"type": "string"},
                                                 "items": {
                                                     "type": "array",
                                                     "items": {"type": "string"}
                                                 }
                                             }}},
            },
            "required": ["_id", "Activation", "Expiry", "Tag", "Desc"],
        }
    }
}

alerts_schema = {
    "type": "object",
    "properties": {
        "Alerts": {
            "type": "array",
            "items": {"$ref": "#/definitions/alert"},
        }
    },
    "required": ["Alerts"],
    "definitions": {
        "alert": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Expiry": {
                    "type": "object",
                    "additionalProperties": False,
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
                "Tag": {"type": "string"},
                "ForceUnlock": {"type": "boolean"},
                "MissionInfo": {
                    "additionalProperties": False,
                    "properties": {
                        "location": {"type": "string"},
                        "levelOverride": {"type": "string"},
                        "missionType": {"type": "string"},
                        "faction": {"type": "string"},
                        "enemySpec": {"type": "string"},
                        "maxEnemyLevel": {"type": "integer"},
                        "minEnemyLevel": {"type": "integer"},
                        "archwingRequired": {"type": "boolean"},
                        "isSharkwingMission": {"type": "boolean"},
                        "maxWaveNum": {"type": "integer"},
                        "nightmare": {"type": "integer"},
                        "difficulty": {"type": "integer"},
                        "missionReward": {
                            "type": "object",
                            "properties": {
                                "additionalProperties": False,
                                "credits": {"type": "integer"},
                                "xp": {"type": "integer"},
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
                                },
                                "countedStoreItems": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "properties": {
                                            "ItemCount": {"type": "integer"},
                                            "StoreItem": {"type": "string"}
                                        }
                                    }
                                },
                                "randomizedItems": {"type": "string"},
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            },
                        },
                        "descText": {"type": "string"},
                        "extraEnemySpec": {"type": "string"},
                        # Extra Data
                        "goalTag": {"type": "string"},
                        "exclusiveWeapon": {"type": "string"},
                        "leadersAlwaysAllowed": {"type": "boolean"},
                        "advancedSpawners": {"type": "array",
                                             "items": {"type": "string"}},
                        "requiredItems": {"type": "array",
                                          "items": {"type": "string"}},
                        "requiredItemsCounts": {"type": "number"},
                        "consumeRequiredItems": {"type": "boolean"},
                        "levelAuras": {"type": "array",
                                       "items": {"type": "string"}},
                        "vipAgent": {"type": "string"},
                        "fxLayer": {"type": "string"},
                        "icon": {"type": "string"},

                    },
                    "required": ["missionReward", "location", "missionType", "faction", "difficulty",
                                 "maxEnemyLevel", "minEnemyLevel", "levelOverride", "enemySpec"],
                },
            },
            "required": ["_id", "Activation", "Expiry", "MissionInfo"],
        }
    }
}

global_upgrades_schema = {
    "type": "object",
    "properties": {
        "GlobalUpgrades": {
            "type": "array",
            "items": {"$ref": "#/definitions/global_upgades"},
        }
    },
    "required": ["GlobalUpgrades"],
    "definitions": {
        "global_upgades": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Activation": {
                    "type": "object",
                    "additionalProperties": False,
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
                "ExpiryDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                "OperationType": {"type": "string"},
                "UpgradeType": {"type": "string"},
                "Value": {"type": "integer"},
                "LocalizeTag": {"type": "string"},
                "LocalizeDescTag": {"type": "string"},
                "ValidType": {"type": "string"},
                "Nodes": {
                    "type": "array",
                    "items": {"type": "string"}
                },
            },
            "required": ["_id", "Activation", "ExpiryDate", "OperationType", "UpgradeType", "Value"],
        }
    }
}

events_schema = {
    "type": "object",
    "properties": {
        "Events": {
            "type": "array",
            "items": {"$ref": "#/definitions/event"},
        }
    },
    "required": ["Events"],
    "definitions": {
        "event": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "_id": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    }
                },
                "Date": {
                    "type": "object",
                    "additionalProperties": False,
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
                "EventStartDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                "EventEndDate": {
                    "type": "object",
                    "additionalProperties": False,
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
                "EventLiveUrl": {"type": "string"},
                "Prop": {"type": "string"},
                "Priority": {"type": "boolean"},
                "Community": {"type": "boolean"},
                "MobileOnly": {"type": "boolean"},
                "ImageUrl": {"type": "string"},
                "Messages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "LanguageCode": {"type": "string"},
                            "Message": {"type": "string"}
                        }
                    }
                },
                "Links": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "LanguageCode": {"type": "string"},
                            "Link": {"type": "string"}
                        }
                    }
                }
            },
            "required": ["_id", "Date", "Prop", "Priority", "MobileOnly", "Messages"],
        }
    }
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
                    "properties": {
                        "faction": {"type": "string"},
                        "seed": {"type": "integer"}
                    }
                },
                "DefenderMissionInfo": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "faction": {"type": "string"},
                        "seed": {"type": "integer"},
                        "missionReward": {"type": "array",
                                          "items": {"type": "object",
                                                    "additionalProperties": False
                                                    }
                                          }
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
                    "additionalProperties": False,
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
            "items": {"$ref": "#/definitions/hubEvents"}
        }
    },
    "required": ["HubEvents"],
    "definitions": {
        "hubEvents": {
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
                    "additionalProperties": False,
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
                },
                "Transmission": {"type": "string"}
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "additionalProperties": False,
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
                    "type": "array",
                    "items": {"type": "string"}
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
                    "type": "string",
                    "enum": ["PRIME1", "PRIME2", "COMING_SOON"]
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
