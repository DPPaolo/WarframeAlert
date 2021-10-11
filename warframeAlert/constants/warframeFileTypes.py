# coding=utf-8
from typing import TypedDict, List, Union


class SortieFileRewards(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float


class SortieFileData(TypedDict):
    sortieRewards: List[SortieFileRewards]


class BountyFileRotationRewardsData(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float
    stage: str


class BountyFileData(TypedDict):
    _id: str
    bountyLevel: str
    rewards: dict[str, List[BountyFileRotationRewardsData]]


class BountyFile(TypedDict, total=False):
    cetusBountyRewards: List[BountyFileData]
    solarisBountyRewards: List[BountyFileData]
    deimosRewards: List[BountyFileData]


class RelicFileRewardsData(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float


class RelicFileData(TypedDict):
    _id: str
    tier: str
    relicName: str
    state: str
    rewards: List[RelicFileRewardsData]


class RelicFile(TypedDict):
    relics: List[RelicFileData]


class MissionFileRewardData(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float


class MissionFileData(TypedDict):
    gameMode: str
    isEvent: bool
    rewards: Union[List[MissionFileRewardData], dict[str, List[MissionFileRewardData]]]


class MissionFile(TypedDict):
    missionRewards: dict[str, dict[str, MissionFileData]]


class KeyFileRewardData(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float


class KeyFileData(TypedDict):
    _id: str
    keyName: str
    rewards: dict[str, List[KeyFileRewardData]]


class KeyFile(TypedDict):
    keyRewards: List[KeyFileData]


class TransientFileRewardData(TypedDict):
    _id: str
    rotation: str
    itemName: str
    rarity: str
    chance: float


class TransientFileData(TypedDict):
    _id: str
    objectiveName: str
    rewards: List[TransientFileRewardData]


class TransientFile(TypedDict):
    transientRewards: List[TransientFileData]


class BpByItemFileEnemyData(TypedDict):
    _id: str
    enemyName: str
    enemyItemDropChance: float
    enemyBlueprintDropChance: float
    rarity: str
    chance: float


class BpByItemFileData(TypedDict):
    _id: str
    itemName: str
    blueprintName: str
    enemies: List[BpByItemFileEnemyData]


class BpByItemFile(TypedDict):
    blueprintLocations: List[BpByItemFileData]


class BpBySourceFileItemsData(TypedDict):
    _id: str
    itemName: str
    rarity: str
    chance: float


class BpBySourceFileData(TypedDict):
    _id: str
    enemyName: str
    enemyItemDropChance: str
    blueprintDropChance: str
    items: List[BpBySourceFileItemsData]


class BpBySourceFile(TypedDict):
    enemyBlueprintTables: List[BpBySourceFileData]


class ModByItemFileEnemyData(TypedDict):
    _id: str
    enemyName: str
    enemyModDropChance: float
    rarity: str
    chance: float


class ModByItemFileData(TypedDict):
    _id: str
    modName: str
    enemies: List[ModByItemFileEnemyData]


class ModByItemFile(TypedDict):
    modLocations: List[ModByItemFileData]


class ModBySourceFileModsData(TypedDict):
    _id: str
    modName: str
    rarity: str
    chance: float


class ModBySourceFileData(TypedDict):
    _id: str
    enemyName: str
    ememyModDropChance: str
    enemyModDropChance: str
    mods: List[ModBySourceFileModsData]


class ModBySourceFile(TypedDict):
    enemyModTables: List[ModBySourceFileData]
