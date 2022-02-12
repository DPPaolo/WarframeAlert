# -*- coding: utf-8 -*-

DEFAULT_DOWNLOAD_SITE = "http://content.warframe.com/PublicExport"

DEFAULT_MANIFEST_SITE = DEFAULT_DOWNLOAD_SITE + "/Manifest/"
MOBILE_MANIFEST_ID_SITE = DEFAULT_DOWNLOAD_SITE + "/index_en.txt.lzma"

DEFAULT_ALERT_IMAGE = "CorpusCreditCardHigh.png"
UPDATE_SITE = "http://deathmt2.altervista.org/warframe/"


DATA_SITE = {
    "PC": "http://content.warframe.com/dynamic/worldState.php",
    "PS4": "http://content.ps4.warframe.com/dynamic/worldState.php",
    "XBOX": "http://content.xb1.warframe.com/dynamic/worldState.php",
    "SWITCH": "http://content.swi.warframe.com/dynamic/worldState.php"
}

OTHER_FILE_SITE = (
    "https://raw.githubusercontent.com/WFCD/warframe-worldstate-data/master/data/languages.json",
    "https://raw.githubusercontent.com/WFCD/warframe-worldstate-data/master/data/solNodes.json",
    # Drop Files
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/relics.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/sortieRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/missionRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/keyRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/transientRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/cetusBountyRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/solarisBountyRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/deimosRewards.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/enemyModTables.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/modLocations.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/enemyBlueprintTables.json",
    "https://raw.githubusercontent.com/WFCD/warframe-drop-data/main/data/blueprintLocations.json",
)

OTHER_FILE_NAME = (
    "Language.json",
    "SolNodes.json",
    # drop file name
    "relic_en.json",
    "sortie_en.json",
    "mission_en.json",
    "key_en.json",
    "transient_en.json",
    "cetus_en.json",
    "fortuna_en.json",
    "deimos_en.json",
    "mod_by_source_en.json",
    "mod_by_item_en.json",
    "bp_by_source_en.json",
    "bp_by_item_en.json",
)

IMAGE_NAME = {
    # weapon for invasion
    "Karak Wraith": "/Lotus/Interface/Icons/Store/KarakWraith.png",
    "Latron Wraith": "/Lotus/Interface/Icons/Store/WraithLatron.png",
    "Strun Wraith": "/Lotus/Interface/Icons/Store/VandalStrun.png",
    "Twin Vipers Wraith": "/Lotus/Interface/Icons/Store/WraithTwinVipers.png",
    "Dera Vandal": "/Lotus/Interface/Icons/Store/DeraVandal.png",
    "Snipetron Vandal": "/Lotus/Interface/Icons/Store/SnipetronVandal.png",
    "Sheev": "/Lotus/Interface/Icons/Store/GrineerCombatKnife.png",

    # Weapon Parts for Invasion
    "Stock": "/Lotus/Interface/Icons/Store/GenericGunStock.png",
    "Barrel": "/Lotus/Interface/Icons/Store/GenericGunBarrel.png",
    "Receiver": "/Lotus/Interface/Icons/Store/GenericGunReceiver.png",
    "Blade": "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png",
    "Handle": "/Lotus/Interface/Icons/Store/GenericWeaponHilt.png",
    "Link": "/Lotus/Interface/Icons/Store/GenericComponentPlug.png",
    "Heatsink": "/Lotus/Interface/Icons/Store/GenericComponentPlug.png",
    "Limb": "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png",
    "Grip": "/Lotus/Interface/Icons/Store/GenericComponentLatch.png",
    "String": "/Lotus/Interface/Icons/Store/GenericGunStock.png",
    "Head": "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png",
    "Hilt": "/Lotus/Interface/Icons/Store/GenericWeaponHilt.png",
    "Pouch": "/Lotus/Interface/Icons/Store/GenericComponentLatch.png",
    "Stars": "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png",
    "Gauntlet": "/Lotus/Interface/Icons/Store/GenericWeaponHilt.png",
    "Disc": "/Lotus/Interface/Icons/Store/GenericWeaponBlade.png",

    # Other
    "Reattore Orokin (Schema)": "/Lotus/Interface/Icons/Store/ComponentReactor.png",
    "Reattore Orokin": "/Lotus/Interface/Icons/Store/ComponentReactor.png",
    "Catalizzatore Orokin (Schema)": "/Lotus/Interface/Icons/Store/ComponentCatalyst.png",
    "Catalizzatore Orokin": "/Lotus/Interface/Icons/Store/ComponentCatalyst.png",
    "Forma (Schema)": "/Lotus/Interface/Icons/Store/GenericComponent.png",
    "Forma": "/Lotus/Interface/Icons/Store/GenericComponent.png",
    "Adattatore Exilus (Schema)": "/Lotus/Interface/Icons/Store/UtilityModule.png",
    "Adattatore Exilus": "/Lotus/Interface/Icons/Store/UtilityModule.png",
    "Lith": "VoidProjectionsIron.png",
    "Meso": "VoidProjectionsBronze.png",
    "Neo": "VoidProjectionsSilver.png",
    "Axi": "VoidProjectionsGold.png",
    "Requiem": "VoidProjectionsRequiem",
}
