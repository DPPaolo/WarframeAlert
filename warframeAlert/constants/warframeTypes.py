# coding=utf-8

from typing import TypedDict, List

IdType = TypedDict('IdType', {'$oid': str})
DateUnixType = TypedDict('DateUnixType', {'$numberLong': int})
DateType = TypedDict('DateType', {'$date': DateUnixType})


class MissionRewardItem(TypedDict):
    ItemCount: int
    ItemType: str


class MissionRewardStoreItem(TypedDict):
    ItemCount: int
    StoreItem: str


class MissionReward(TypedDict):
    credits: int
    xp: int
    countedItems: List[MissionRewardItem]
    countedStoreItems: List[MissionRewardStoreItem]
    randomizedItems: str
    items: List[str]


class SyndicateJobs(TypedDict):
    jobType: str
    rewards: str
    masteryReq: int
    minEnemyLevel: int
    maxEnemyLevel: int
    xpAmounts: List[int]


class ActiveMission(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    MissionType: str
    Modifier: str
    Node: str
    Region: int
    Seed: int
    Hard: bool


ActiveMissions = List[ActiveMission]


class AlertMissionInfo(TypedDict):
    location: str
    levelOverride: str
    missionType: str
    faction: str
    enemySpec: str
    maxEnemyLevel: int
    minEnemyLevel: int
    archwingRequired: bool
    isSharkwingMission: bool
    maxWaveNum: int
    nightmare: bool
    difficulty: int
    missionReward: MissionReward
    descText: str
    extraEnemySpec: str
    goalTag: str
    exclusiveWeapon: str
    leadersAlwaysAllowed: bool
    advancedSpawners: List[str]
    requiredItems: List[str]
    requiredItemsCounts: int
    consumeRequiredItems: bool
    levelAuras: List[str]
    vipAgent: str
    fxLayer: str
    icon: str


class AlertData(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Tag: str
    ForceUnlock: bool
    MissionInfo: AlertMissionInfo


Alerts = List[AlertData]


class ConstructionProject(TypedDict, total=False):
    Activation: DateType
    Node: str
    Tag: str
    HunterBoostTask: str
    Tasks: List[str]
    ToolTips: List[str]


ConstructionProjects = List[ConstructionProject]


class DailyDeal(TypedDict, total=False):
    StoreItem: str
    Expiry: DateType
    Activation: DateType
    Discount: int
    OriginalPrice: int
    SalePrice: int
    AmountTotal: int
    AmountSold: int


DailyDealsData = List[DailyDeal]


class NewsMessage(TypedDict):
    LanguageCode: str
    Message: str


class NewsLinksMessage(TypedDict):
    LanguageCode: str
    Link: str


class Event(TypedDict, total=False):
    _id: IdType
    Date: DateType
    EventStartDate: DateType
    EventEndDate: DateType
    EventLiveUrl: str
    Prop: str
    HideEndDateModifier: bool
    Priority: bool
    Community: bool
    MobileOnly: bool
    ImageUrl: str
    Icon: str
    Messages: List[NewsMessage]
    Links: List[NewsLinksMessage]


Events = List[Event]


class Experiment(TypedDict, total=False):
    pass


ExperimentRecommended = List[Experiment]


class FeaturedGuild(TypedDict, total=False):
    Name: str
    Tier: int
    Emblem: bool
    _id: IdType
    AllianceId: IdType


FeaturedGuilds = List[FeaturedGuild]


class ExperimentFeatured(TypedDict):
    ExperimentGroup: str
    FeaturedIndex: int


class FlashSale(TypedDict, total=False):
    StartDate: DateType
    EndDate: DateType
    ProductExpiryOverride: DateType
    ExperimentFeatured: List[ExperimentFeatured]
    BannerIndex: int
    BogoBuy: int
    BogoGet: int
    Discount: int
    PremiumOverride: int
    RegularOverride: int
    ShowInMarket: bool
    HideFromMarket: bool
    ShowWithRecommended: bool
    VoidEclipse: bool
    SupporterPack: bool
    Featured: bool
    Popular: bool
    TypeName: str


FlashSales = List[FlashSale]


class GlobalUpgrade(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    ExpiryDate: DateType
    OperationType: str
    UpgradeType: str
    Value: int
    LocalizeTag: str
    LocalizeDescTag: str
    ValidType: str
    Nodes: List[str]


GlobalUpgrades = List[GlobalUpgrade]


class InGameMarketLandingPageCategory(TypedDict, total=False):
    CategoryName: str
    Icon: str
    Name: str
    Items: List[str]


class InGameMarketLandingPage(TypedDict, total=False):
    Categories: List[InGameMarketLandingPageCategory]


class InGameMarket(TypedDict, total=False):
    LandingPage: InGameMarketLandingPage


class HubEventData(TypedDict, total=False):
    Activation: DateType
    Expiry: DateType
    Tag: str
    Node: str
    CinematicTag: str
    CycleFrequency: int
    RepeatInterval: int
    Transmissions: List[str]
    Transmission: str


HubEvents = List[HubEventData]


class Goal(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Tag: str
    Desc: str
    Icon: str
    Count: int
    Personal: bool
    Community: bool
    ClampNodeScores: bool
    Bounty: bool
    ToolTip: str
    ScoreLocTag: str
    ScoreMaxTag: str
    ScoreVar: str
    MissionKeyRotation: List[str]
    MissionKeyName: str
    MissionKeyRotationInterval: int
    ConcurrentMissionKeyNames: List[str]
    NightLevel: str
    Success: int
    Faction: str
    InstructionalItem: str
    RoamingVIP: str
    PrereqGoalTags: List[str]
    HealthPct: float
    Fomorian: str
    Best: bool
    ScoreTagBlocksGuildTierChanges: bool
    RewardNode: str
    ClanGoal: List[str]
    RelayReconstruction: int
    VictimNode: str
    Transmission: str
    OptionalInMission: bool
    Regions: List[int]
    RegionIdx: int
    ArchwingDrops: List[str]
    RegionDrops: List[str]
    UpgradeIds: List[IdType]
    JobAffiliationTag: str
    JobCurrentVersion: IdType
    JobPreviousVersion: IdType
    Jobs: List[SyndicateJobs]
    PreviousJobs: List[SyndicateJobs]
    PauseAutoScheduling: bool
    NextAltActivation: DateType
    NextAltExpiry: DateType
    AltActivation: DateType
    AltExpiry: DateType
    EpochNum: int
    CompletionBonus: List[int]
    Metadata: str
    ContinuousHubEvent: HubEventData
    MissionInfo: AlertMissionInfo
    Node: str
    ConcurrentNodes: List[str]
    ConcurrentNodeReqs: List[int]
    Goal: int
    BonusGoal: int
    InterimGoals: List[int]
    Reward: MissionReward
    InterimRewards: List[MissionReward]


Goals = List[Goal]


class InvasionMissionInfo(TypedDict):
    faction: str
    seed: int
    missionReward: MissionReward


class Invasion(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    ChainID: IdType
    AttackerMissionInfo: InvasionMissionInfo
    DefenderMissionInfo: InvasionMissionInfo
    Completed: bool
    Count: int
    DefenderFaction: str
    Faction: str
    Goal: int
    LocTag: str
    Node: str
    AttackerReward: MissionReward
    DefenderReward: MissionReward


Invasions = List[Invasion]


class LiteSortieMission(TypedDict, total=False):
    missionType: str
    node: str


class LiteSortie(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Boss: str
    Missions: List[LiteSortieMission]
    Seed: int
    Reward: str


LiteSorties = List[LiteSortie]


class LibraryInfo(TypedDict, total=False):
    LastCompletedTargetType: str


class NodeOverride(TypedDict, total=False):
    _id: IdType
    Node: str
    Hide: bool
    Seed: str
    LevelOverride: str
    ExtraEnemySpec: str
    EnemySpec: str
    Faction: str
    Activation: DateType
    Expiry: DateType


NodeOverrides = List[NodeOverride]


class PVPActiveTournament(TypedDict, total=False):
    pass


PVPActiveTournaments = List[PVPActiveTournament]


class PvPAlternativeWeaponOverride(TypedDict):
    Override: bool
    Resource: str


class PvPAlternativeLoadouts(TypedDict):
    WeaponOverrides: List[PvPAlternativeWeaponOverride]


class PVPAlternativeMode(TypedDict, total=False):
    TitleLoc: str
    DescriptionLoc: str
    DisableAmmoPickups: bool
    DisableEnergyPickups: bool
    DisableEnergySurge: bool
    DisableWeaponHud: bool
    DisableWeaponSwitching: bool
    MatchTimeOverride: int
    MaxPlayersOverride: int
    MaxTeamCountDifferenceOverride: int
    MinPlayersPerTeamOverride: int
    TargetMode: str
    ForcedLoadouts: List[PvPAlternativeLoadouts]


PVPAlternativeModes = List[PVPAlternativeMode]


class PvPParam(TypedDict):
    n: str
    v: int


class PVPChallengeInstance(TypedDict, total=False):
    _id: IdType
    startDate: DateType
    endDate: DateType
    Category: str
    PVPMode: str
    challengeTypeRefID: str
    subChallenges: List[str]
    isGenerated: bool
    params: List[PvPParam]


PVPChallengeInstances = List[PVPChallengeInstance]


class PersistentEnemy(TypedDict, total=False):
    _id: IdType
    Discovered: bool
    AgentType: str
    Icon: str
    LastDiscoveredLocation: str
    LocTag: str
    FleeDamage: float
    HealthPercent: float
    Rank: float
    UseTicketing: bool
    Region: int
    LastDiscoveredTime: DateType


PersistentEnemies = List[PersistentEnemy]


class PrimeAccessAvailability(TypedDict, total=False):
    State: str


PrimeVaultAvailabilities = List[bool]

ProjectPoints = List[float]


class PrimeVaultManifestInfo(TypedDict, total=False):
    ItemType: str
    RegularPrice: int
    PrimePrice: int


class PrimeVaultScheduleInfo(TypedDict, total=False):
    Expiry: DateType
    FeaturedItem: str
    PreviewHiddenUntil: DateType


class PrimeVaultTradersData(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    InitialStartDate: DateType
    Completed: bool
    Node: str
    Manifest: List[PrimeVaultManifestInfo]
    EvergreenManifest: List[PrimeVaultManifestInfo]
    ScheduleInfo: List[PrimeVaultScheduleInfo]
    Params: str
    Phase: int


PrimeVaultTraders = List[PrimeVaultTradersData]


class NightwaweChallenge(TypedDict):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Challenge: str
    Daily: bool


class SeasonInfo(TypedDict, total=False):
    Activation: DateType
    Expiry: DateType
    AffiliationTag: str
    Params: str
    Phase: int
    Season: int
    ActiveChallenges: List[NightwaweChallenge]


class SortieMission(TypedDict):
    missionType: str
    modifierType: str
    node: str
    tileset: str


class Sortie(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Seed: int
    Boss: str
    Reward: str
    Twitter: bool
    ExtraDrops: List[str]
    Variants: List[SortieMission]


Sorties = List[Sortie]


class SyndicateMission(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Tag: str
    Seed: int
    Nodes: List[str]
    Jobs: List[SyndicateJobs]


SyndicateMissions = List[SyndicateMission]


class TwitchPromo(TypedDict, total=False):
    startDate: DateType
    endDate: DateType
    achievement: str
    type: str
    streamers: List[str]
    spawnChance: int
    cooldown: int
    agentTypes: List[str]


TwitchPromos = List[TwitchPromo]


class VoidStorm(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    ActiveMissionTier: str
    Node: str


VoidStorms = List[VoidStorm]


class VoidTraderItem(TypedDict):
    ItemType: str
    PrimePrice: int
    RegularPrice: int


class VoidTrader(TypedDict, total=False):
    _id: IdType
    Activation: DateType
    Expiry: DateType
    Node: str
    Character: str
    Manifest: List[VoidTraderItem]


VoidTraders = List[VoidTrader]


class JsonData(TypedDict, total=False):
    ActiveMissions: ActiveMissions
    Alerts: Alerts
    BuildLabel: str
    ConstructionProjects: ConstructionProjects
    DTLS: int
    DailyDeals: DailyDealsData
    Events: Events
    ExperimentRecommended: ExperimentRecommended
    FeaturedGuilds: FeaturedGuilds
    FlashSales: FlashSales
    ForceLogoutVersion: int
    GlobalUpgrades: GlobalUpgrades
    Goals: Goals
    HubEvents: HubEvents
    InGameMarket: InGameMarket
    Invasions: Invasions
    LibraryInfo: LibraryInfo
    LiteSorties: LiteSorties
    MobileVersion: str
    NodeOverrides: NodeOverrides
    PVPActiveTournaments: PVPActiveTournaments
    PVPAlternativeModes: PVPAlternativeModes
    PVPChallengeInstances: PVPChallengeInstances
    PersistentEnemies: PersistentEnemies
    PrimeAccessAvailability: PrimeAccessAvailability
    PrimeTokenAvailability: bool
    PrimeVaultAvailabilities: PrimeVaultAvailabilities
    PrimeVaultTraders: PrimeVaultTraders
    ProjectPct: ProjectPoints
    SeasonInfo: SeasonInfo
    Sorties: Sorties
    SyndicateMissions: SyndicateMissions
    Time: int
    Tmp: str
    TwitchPromos: TwitchPromos
    Version: int
    VoidStorms: VoidStorms
    VoidTraders: VoidTraders
    WorldSeed: str
