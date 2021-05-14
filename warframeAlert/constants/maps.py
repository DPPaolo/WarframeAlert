# -*- coding: utf-8 -*-


FACTION = {"FC_GRINEER": "Grineer",
           "FC_CORPUS": "Corpus",
           "FC_INFESTATION": "Infested",
           "FC_CORRUPTED": "Corrupted",
           "FC_OROKIN": "Orokin",
           "FC_SENTIENT": "Sentient",
           "FC_RED_VEIL": "Red Veil",
           }

REGION_MAP = {
    0: {"it": "Mercurio", "en": "Mercury"},
    1: {"it": "Venere", "en": "Venus"},
    2: {"it": "Terra", "en": "Earth"},
    3: {"it": "Marte", "en": "Mars"},
    4: {"it": "Giove", "en": "Jupiter"},
    5: {"it": "Saturno", "en": "Saturn"},
    6: {"it": "Urano", "en": "Uranus"},
    7: {"it": "Nettuno", "en": "Neptune"},
    8: {"it": "Plutone", "en": "Pluto"},
    9: {"it": "Cerere", "en": "Ceres"},
    10: {"it": "Eris", "en": "Eris"},
    11: {"it": "Sedna", "en": "Sedna"},
    12: {"it": "Europa", "en": "Europa"},
    13: {"it": "13", "en": "13"},
    14: {"it": "Void", "en": "Void"},
    15: {"it": "Phobos", "en": "Phobos"},
    16: {"it": "Deimos", "en": "Deimos"},
    17: {"it": "Lua", "en": "Lua"},
    18: {"it": "Fortezza Kuva", "en": "Kuva Fortress"},
    19: {"it": "Cetus", "en": "Cetus"},
    20: {"it": "Fortuna", "en": "Fortuna"},
    21: {"it": "Santuario", "en": "Sanctuary"},
    22: {"it": "Veil", "en": "Veil"},
}

MISSION_TYPE = {"MT_SURVIVAL": {"it": "Sopravvivenza", "en": "Survival"},
                "MT_DEFENSE": {"it": "Difesa", "en": "Defense"},
                "MT_MOBILE_DEFENSE": {"it": "Difesa Mobile", "en": "Mobile Defense"},
                "MT_RESCUE": {"it": "Salvataggio", "en": "Rescue"},
                "MT_CAPTURE": {"it": "Cattura", "en": "Capture"},
                "MT_EXTERMINATION": {"it": "Sterminio", "en": "Exterminate"},
                "MT_INTEL": {"it": "Spionaggio", "en": "Spy"},
                "MT_COUNTER_INTEL": {"it": "Inganno", "en": "Deception"},
                "MT_SABOTAGE": {"it": "Sabotaggio", "en": "Sabotage"},
                "MT_SABOTAGE_2": {"it": "Sabotaggio", "en": "Caches"},
                "MT_EXCAVATE": {"it": "Scavo", "en": "Excavation"},
                "MT_HIVE": {"it": "Alveare", "en": "Hive"},
                "MT_TERRITORY": {"it": "Intercettazione", "en": "Interception"},
                "MT_RETRIEVAL": {"it": "Dirottamento", "en": "Hijack"},
                "MT_EVACUATION": {"it": "Scorta", "en": "Defection"},
                "MT_ARENA": {"it": "Arena", "en": "Arena"},
                "MT_ASSASSINATION": {"it": "Assassinio", "en": "Assassination"},
                "MT_PURSUIT": {"it": "Inseguimento", "en": "Pursuit"},
                "MT_RACE": {"it": "Corsa", "en": "Rush"},
                "MT_ASSAULT": {"it": "Assalto", "en": "Assault"},
                "MT_PURIFY": {"it": "Recupero Infested", "en": "Infested Salvage"},
                "MT_RAID": {"it": "Raid", "en": "Raid"},
                "MT_SALVAGE": {"it": "Recupero", "en": "Recovery"},
                "MT_ARTIFACT": {"it": "Disturbo", "en": "Disruption"},
                "MT_SECTOR": {"it": "Dark Sector", "en": "Dark Sector"},
                "MT_JUNCTION": {"it": "Raccordo", "en": "Junction"},
                "MT_PVP": {"it": "Conclave", "en": "Conclave"},
                "MT_GENERIC": {"it": "Quest", "en": "Quest"},
                "MT_LANDSCAPE": {"it": "Esplorazione", "en": "Free Roam"},
                "MT_ENDLESS_EXTERMINATION": {"it": "Carneficina al Santuario", "en": "Sanctuary Onslaught"},
                "MT_RAILJACK": {"it": "Schermaglia (Railjack)", "en": "Skirmish  (Railjack)"},
                "MT_RAILJACK_ORPHIX": {"it": "Orphix (Railjack)", "en": "Orphix  (Railjack)"},
                "MT_RAILJACK_VOLATILE": {"it": "Volatile (Railjack)", "en": "Volatile  (Railjack)"},
                }

NODE_NAME_IT = {
    "SolNode1": ("Galatea", "Nettuno"),
    "SolNode2": ("Aphrodite", "Venere"),
    "SolNode3": ("Cordelia", "Urano"),
    "SolNode4": ("Acheron", "Plutone"),
    "SolNode5": ("Perdita", "Urano"),
    "SolNode6": ("Despina", "Nettuno"),
    "SolNode7": ("Epimetheus", "Saturno"),
    "SolNode8": ("Nix", "Plutone"),
    "SolNode9": ("Rosalind", "Urano"),
    "SolNode10": ("Thebe", "Giove"),
    "SolNode11": ("Tharsis", "Marte"),
    "SolNode12": ("Elion", "Mercurio"),
    "SolNode13": ("Bianca", "Urano"),
    "SolNode14": ("Ultor", "Marte"),
    "SolNode15": ("Pacific", "Terra"),
    "SolNode16": ("Augustus", "Marte"),
    "SolNode17": ("Proteus", "Nettuno"),
    "SolNode18": ("Rhea", "Saturno"),
    "SolNode19": ("Enceladus", "Saturno"),
    "SolNode20": ("Telesto", "Saturno"),
    "SolNode21": ("Narcissus", "Plutone"),
    "SolNode22": ("Tessera", "Venere"),
    "SolNode23": ("Cytherean", "Venere"),
    "SolNode24": ("Oro", "Terra"),
    "SolNode25": ("Callisto", "Giove"),
    "SolNode26": ("Lith", "Terra"),
    "SolNode27": ("E Prime", "Terra"),
    "SolNode28": ("Terminus", "Mercurio"),
    "SolNode29": ("Oberon", "Urano"),
    "SolNode30": ("Olympus", "Marte"),
    "SolNode31": ("Anthe", "Saturno"),
    "SolNode32": ("Tethys", "Saturno"),
    "SolNode33": ("Ariel", "Urano"),
    "SolNode34": ("Sycorax", "Urano"),
    "SolNode35": ("Arcadia", "Marte"),
    "SolNode36": ("Martialis", "Marte"),
    "SolNode37": ("Pallene", "Saturno"),
    "SolNode38": ("Minthe", "Plutone"),
    "SolNode39": ("Everest", "Terra"),
    "SolNode40": ("Prospero", "Urano"),
    "SolNode41": ("Arval", "Marte"),
    "SolNode42": ("Helene", "Saturno"),
    "SolNode43": ("Cerberus", "Plutone"),
    "SolNode44": ("Mimas", "Saturno"),
    "SolNode45": ("Ara", "Marte"),
    "SolNode46": ("Spear", "Marte"),
    "SolNode47": ("Janus", "Saturno"),
    "SolNode48": ("Regna", "Plutone"),
    "SolNode49": ("Larissa", "Nettuno"),
    "SolNode50": ("Numa", "Saturno"),
    "SolNode51": ("Hades", "Plutone"),
    "SolNode52": ("Portia", "Urano"),
    "SolNode53": ("Themisto", "Giove"),
    "SolNode54": ("Silvanus", "Marte"),
    "SolNode55": ("Methone", "Saturno"),
    "SolNode56": ("Cypress", "Plutone"),
    "SolNode57": ("Sao", "Nettuno"),
    "SolNode58": ("Hellas", "Marte"),
    "SolNode59": ("Eurasia", "Terra"),
    "SolNode60": ("Caliban", "Urano"),
    "SolNode61": ("Ishtar", "Venere"),
    "SolNode62": ("Neso", "Nettuno"),
    "SolNode63": ("Mantle", "Terra"),
    "SolNode64": ("Umbriel", "Urano"),
    "SolNode65": ("Gradivus", "Marte"),
    "SolNode66": ("Unda", "Venere"),
    "SolNode67": ("Dione", "Saturno"),
    "SolNode68": ("Vallis", "Marte"),
    "SolNode69": ("Ophelia", "Urano"),
    "SolNode70": ("Cassini", "Saturno"),
    "SolNode71": ("Vesper", "Venere"),
    "SolNode72": ("Outer Terminus", "Plutone"),
    "SolNode73": ("Ananke", "Giove"),
    "SolNode74": ("Carme", "Giove"),
    "SolNode75": ("Cervantes", "Terra"),
    "SolNode76": ("Hydra", "Plutone"),
    "SolNode77": ("Cupid", "Urano"),
    "SolNode78": ("Triton", "Nettuno"),
    "SolNode79": ("Cambria", "Terra"),
    "SolNode80": ("Phoebe", "Saturno"),
    "SolNode81": ("Palus", "Plutone"),
    "SolNode82": ("Calypso", "Saturno"),
    "SolNode83": ("Cressida", "Urano"),
    "SolNode84": ("Nereid", "Nettuno"),
    "SolNode85": ("Gaia", "Terra"),
    "SolNode86": ("Aegaeon", "Saturno"),
    "SolNode87": ("Ganymede", "Giove"),
    "SolNode88": ("Adrastea", "Giove"),
    "SolNode89": ("Mariana", "Terra"),
    "SolNode90": ("Miranda", "Urano"),
    "SolNode91": ("Iapetus", "Saturno"),
    "SolNode92": ("Charon", "Plutone"),
    "SolNode93": ("Keeler", "Saturno"),
    "SolNode94": ("Apollodorus", "Mercurio"),
    "SolNode95": ("Thalassa", "Nettuno"),
    "SolNode96": ("Titan", "Saturno"),
    "SolNode97": ("Amalthea", "Giove"),
    "SolNode98": ("Desdemona", "Urano"),
    "SolNode99": ("War", "Marte"),
    "SolNode100": ("Elara", "Giove"),
    "SolNode101": ("Kiliken", "Venere"),
    "SolNode102": ("Oceanum", "Plutone"),
    "SolNode103": ("M Prime", "Mercurio"),
    "SolNode104": ("Fossa", "Venere"),
    "SolNode105": ("Titania", "Urano"),
    "SolNode106": ("Alator", "Marte"),
    "SolNode107": ("Venera", "Venere"),
    "SolNode108": ("Tolstoj", "Mercurio"),
    "SolNode109": ("Linea", "Venere"),
    "SolNode110": ("Hyperion", "Saturno"),
    "SolNode111": ("Juliet", "Urano"),
    "SolNode112": ("Setebos", "Urano"),
    "SolNode113": ("Ares", "Marte"),
    "SolNode114": ("Puck", "Urano"),
    "SolNode115": ("Quirinus", "Marte"),
    "SolNode116": ("Mab", "Urano"),
    "SolNode117": ("Naiad", "Nettuno"),
    "SolNode118": ("Laomedeia", "Nettuno"),
    "SolNode119": ("Caloris", "Mercurio"),
    "SolNode120": ("Halimede", "Nettuno"),
    "SolNode121": ("Carpo", "Giove"),
    "SolNode122": ("Stephano", "Urano"),
    "SolNode123": ("V Prime", "Venere"),
    "SolNode124": ("Trinculo", "Urano"),
    "SolNode125": ("Io", "Giove"),
    "SolNode126": ("Metis", "Giove"),
    "SolNode127": ("Psamathe", "Nettuno"),
    "SolNode128": ("E Gate", "Venere"),
    "SolNode129": ("Orb Vallis", "Venere"),
    "SolNode130": ("Lares", "Mercurio"),
    "SolNode131": ("Pallas", "Cerere"),
    "SolNode132": ("Bode", "Cerere"),
    "SolNode133": ("Vedic", "Cerere"),
    "SolNode134": ("Varro", "Cerere"),
    "SolNode135": ("Thon", "Cerere"),
    "SolNode136": ("Olla", "Cerere"),
    "SolNode137": ("Nuovo", "Cerere"),
    "SolNode138": ("Ludi", "Cerere"),
    "SolNode139": ("Lex", "Cerere"),
    "SolNode140": ("Kiste", "Cerere"),
    "SolNode141": ("Ker", "Cerere"),
    "SolNode142": ("Hapke", "Cerere"),
    "SolNode143": ("Gefion", "Cerere"),
    "SolNode144": ("Exta", "Cerere"),
    "SolNode145": ("Egeria", "Cerere"),
    "SolNode146": ("Draco", "Cerere"),
    "SolNode147": ("Cinxia", "Cerere"),
    "SolNode148": ("Cerium", "Cerere"),
    "SolNode149": ("Casta", "Cerere"),
    "SolNode150": ("Albedo", "Cerere"),
    "SolNode151": ("Acanth", "Eris"),
    "SolNode152": ("Ascar", "Eris"),
    "SolNode153": ("Brugia", "Eris"),
    "SolNode154": ("Candiru", "Eris"),
    "SolNode155": ("Cosis", "Eris"),
    "SolNode156": ("Cyath", "Eris"),
    "SolNode157": ("Giardia", "Eris"),
    "SolNode158": ("Gnathos", "Eris"),
    "SolNode159": ("Lepis", "Eris"),
    "SolNode160": ("Histo", "Eris"),
    "SolNode161": ("Hymeno", "Eris"),
    "SolNode162": ("Isos", "Eris"),
    "SolNode163": ("Ixodes", "Eris"),
    "SolNode164": ("Kala-azar", "Eris"),
    "SolNode165": ("Sporid", "Eris"),
    "SolNode166": ("Nimus", "Eris"),
    "SolNode167": ("Oestrus", "Eris"),
    "SolNode168": ("Phalan", "Eris"),
    "SolNode169": ("Psoro", "Eris"),
    "SolNode170": ("Ranova", "Eris"),
    "SolNode171": ("Saxis", "Eris"),
    "SolNode172": ("Xini", "Eris"),
    "SolNode173": ("Solium", "Eris"),
    "SolNode174": ("Sparga", "Eris"),
    "SolNode175": ("Naeglar", "Eris"),
    "SolNode176": ("Viver", "Eris"),
    "SolNode177": ("Kappa", "Sedna"),
    "SolNode178": ("Hyosube", "Sedna"),
    "SolNode179": ("Jengu", "Sedna"),
    "SolNode180": ("Undine", "Sedna"),
    "SolNode181": ("Adaro", "Sedna"),
    "SolNode182": ("Camenae", "Sedna"),
    "SolNode183": ("Vodyanoi", "Sedna"),
    "SolNode184": ("Rusalka", "Sedna"),
    "SolNode185": ("Berehynia", "Sedna"),
    "SolNode186": ("Phithale", "Sedna"),
    "SolNode187": ("Selkie", "Sedna"),
    "SolNode188": ("Kelpie", "Sedna"),
    "SolNode189": ("Naga", "Sedna"),
    "SolNode190": ("Nakki", "Sedna"),
    "SolNode191": ("Marid", "Sedna"),
    "SolNode192": ("Tikoloshe", "Sedna"),
    "SolNode193": ("Merrow", "Sedna"),
    "SolNode194": ("Ponaturi", "Sedna"),
    "SolNode195": ("Hydron", "Sedna"),
    "SolNode196": ("Charybdis", "Sedna"),
    "SolNode197": ("Graeae", "Sedna"),
    "SolNode198": ("Scylla", "Sedna"),
    "SolNode199": ("Yam", "Sedna"),
    "SolNode200": ("Veles", "Sedna"),
    "SolNode201": ("Tiamat", "Sedna"),
    "SolNode202": ("Yamaja", "Sedna"),
    "SolNode203": ("Abaddon", "Europa"),
    "SolNode204": ("Armaros", "Europa"),
    "SolNode205": ("Baal", "Europa"),
    "SolNode206": ("Eligor", "Europa"),
    "SolNode207": ("Gamygyn", "Europa"),
    "SolNode208": ("Lillith", "Europa"),
    "SolNode209": ("Morax", "Europa"),
    "SolNode210": ("Naamah", "Europa"),
    "SolNode211": ("Ose", "Europa"),
    "SolNode212": ("Paimon", "Europa"),
    "SolNode213": ("Shax", "Europa"),
    "SolNode214": ("Sorath", "Europa"),
    "SolNode215": ("Valac", "Europa"),
    "SolNode216": ("Valefor", "Europa"),
    "SolNode217": ("Orias", "Europa"),
    "SolNode218": ("Zagan", "Europa"),
    "SolNode219": ("Abaddon", "Europa"),
    "SolNode220": ("Kokabiel", "Europa"),
    "SolNode221": ("Neruda", "Mercurio"),
    "SolNode222": ("Eminescu", "Mercurio"),
    "SolNode223": ("Boethius", "Mercurio"),
    "SolNode224": ("Odin", "Europa"),
    "SolNode225": ("Suisei", "Mercurio"),
    "SolNode226": ("Pantheon", "Mercurio"),
    "SolNode227": ("Verdi", "Mercurio"),
    "SolNode228": ("Pianure di Eidolon", "Terra"),
    "SolNode229": ("Cambion Drift", "Deimos"),

    "SolNode300": ("Plato", "Luna"),
    "SolNode301": ("Grimaldi", "Luna"),
    "SolNode302": ("Tycho", "Luna"),

    "SolNode304": ("Copernicus", "Luna"),
    "SolNode305": ("Stöfler", "Luna"),
    "SolNode306": ("Pavlov", "Luna"),
    "SolNode307": ("Zeipel", "Luna"),
    "SolNode308": ("Apollo", "Luna"),

    "SolNode400": ("Teshub", "Void"),
    "SolNode401": ("Hepit", "Void"),
    "SolNode402": ("Taranis", "Void"),
    "SolNode403": ("Tiwaz", "Void"),
    "SolNode404": ("Stribog", "Void"),
    "SolNode405": ("Ani", "Void"),
    "SolNode406": ("Ukko", "Void"),
    "SolNode407": ("Oxomoco", "Void"),
    "SolNode408": ("Belenus", "Void"),
    "SolNode409": ("Mot", "Void"),
    "SolNode410": ("Aten", "Void"),
    "SolNode411": ("Marduk", "Void"),
    "SolNode412": ("Mithra", "Void"),

    "SolNode701": ("Assassino Jordas Golem", "Eris"),
    "SolNode702": ("La Legge della Punizione", "Terra"),
    "SolNode703": ("La Legge della Punizione (Nightmare)", "Terra"),
    "SolNode704": ("Il Verdetto di Jordas", "Eris"),
    "SolNode705": ("Assassino Mutualist Alad V", "Eris"),
    "SolNode706": ("Horend", "Deimos"),
    "SolNode707": ("Hyf", "Deimos"),
    "SolNode708": ("Phlegyas", "Deimos"),
    "SolNode709": ("Dirus", "Deimos"),
    "SolNode710": ("Formido", "Deimos"),
    "SolNode711": ("Terrorem", "Deimos"),
    "SolNode712": ("Magnacidium", "Deimos"),
    "SolNode713": ("Exequias", "Deimos"),

    "SolNode740": ("Ropalolyst", "Giove"),
    "SolNode741": ("Koro", "Fortezza Kuva"),
    "SolNode742": ("Nabuk", "Fortezza Kuva"),
    "SolNode743": ("Rotuma", "Fortezza Kuva"),
    "SolNode744": ("Taveuni", "Fortezza Kuva"),
    "SolNode745": ("Tamu", "Fortezza Kuva"),
    "SolNode746": ("Dakata", "Fortezza Kuva"),
    "SolNode747": ("Pago", "Fortezza Kuva"),
    "SolNode748": ("Garus", "Fortezza Kuva"),

    "SolNode761": ("The Index", "Nettuno"),
    "SolNode762": ("The Index", "Nettuno"),
    "SolNode763": ("The Index", "Nettuno"),
    "SolNode764": ("The Index", "Nettuno"),

    "SolNode802": ("Carneficina al Santuario", "Sistema Solare"),

    "SolNode901": ("Caduceus", "Mercurio"),
    "SolNode902": ("Montes", "Venere"),
    "SolNode903": ("Erpo", "Terra"),
    "SolNode904": ("Syrtis", "Marte"),
    "SolNode905": ("Galilea", "Giove"),
    "SolNode906": ("Pandora", "Saturno"),
    "SolNode907": ("Caelus", "Urano"),
    "SolNode908": ("Salacia", "Nettuno"),

    "SettlementNode1": ("Roche", "Phobos"),
    "SettlementNode2": ("Skyresh", "Phobos"),
    "SettlementNode3": ("Stickney", "Phobos"),
    "SettlementNode4": ("Drunlo", "Phobos"),
    "SettlementNode5": ("Grildrig", "Phobos"),
    "SettlementNode6": ("Limtoc", "Phobos"),
    "SettlementNode7": ("Hall", "Phobos"),
    "SettlementNode8": ("Reldresal", "Phobos"),
    "SettlementNode9": ("Clustril", "Phobos"),
    "SettlementNode10": ("Kepler", "Phobos"),
    "SettlementNode11": ("Gulliver", "Phobos"),
    "SettlementNode12": ("Monolith", "Phobos"),
    "SettlementNode13": ("D'Arrest", "Phobos"),
    "SettlementNode14": ("Shklovsky", "Phobos"),
    "SettlementNode15": ("Sharpless", "Phobos"),
    "SettlementNode16": ("Wendell", "Phobos"),
    "SettlementNode17": ("Flimnap", "Phobos"),
    "SettlementNode18": ("Opik", "Phobos"),
    "SettlementNode19": ("Todd", "Phobos"),
    "SettlementNode20": ("Iliad", "Phobos"),

    "ClanNode0": ("Romula", "Venere"),
    "ClanNode1": ("Malva", "Venere"),
    "ClanNode2": ("Coba", "Terra"),
    "ClanNode3": ("Tikal", "Venere"),
    "ClanNode4": ("Sinai", "Giove"),
    "ClanNode5": ("Cameria", "Giove"),
    "ClanNode6": ("Larzac", "Europa"),
    "ClanNode7": ("Cholistan", "Europa"),
    "ClanNode8": ("Kadesh", "Marte"),
    "ClanNode9": ("Wahiba", "Marte"),
    "ClanNode10": ("Memphis", "Phobos"),
    "ClanNode11": ("Zeugma", "Phobos"),
    "ClanNode12": ("Caracol", "Saturno"),
    "ClanNode13": ("Piscinas", "Saturno"),
    "ClanNode14": ("Amarna", "Saturno"),
    "ClanNode15": ("Sangeru", "Saturno"),
    "ClanNode16": ("Ur", "Urano"),
    "ClanNode17": ("Assur", "Urano"),
    "ClanNode18": ("Akkad", "Eris"),
    "ClanNode19": ("Zabala", "Urano"),
    "ClanNode20": ("Yursa", "Nettuno"),
    "ClanNode21": ("Kelashin", "Nettuno"),
    "ClanNode22": ("Seimeni", "Cerere"),
    "ClanNode23": ("Gabii", "Cerere"),
    "ClanNode24": ("Sechura", "Plutone"),
    "ClanNode25": ("Hieracon", "Plutone"),

    "MercuryHUB": ("Stazione Larunda", "Mercurio"),
    "VenusHUB": ("Stazione Vesper", "Venere"),
    "EarthHUB": ("Stazione Strata", "Terra"),
    "EarthHUBRebuild": ("Sito Ricostruzione Stazione Strata", "Terra"),
    "SaturnHUB": ("Stazione Kronia", "Saturno"),
    "ErisHUB": ("Stazione Kuiper", "Eris"),
    "EuropaHUB": ("Stazione Leonov", "Europa"),
    "PlutoHUB": ("Stazione Orcus", "Plutone"),

    "VenusToMercuryJunction": ("Raccordo Mercurio", "Venere"),
    "EarthToVenusJunction": ("Raccordo Venere", "Terra"),
    "EarthToMarsJunction": ("Raccordo Marte", "Terra"),
    "MarsToCeresJunction": ("Raccordo Cerere", "Marte"),
    "MarsToPhobosJunction": ("Raccordo Phobos", "Marte"),
    "JupiterToEuropaJunction": ("Raccordo Europa", "Giove"),
    "JupiterToSaturnJunction": ("Raccordo Saturno", "Giove"),
    "SaturnToUranusJunction": ("Raccordo Urano", "Saturno"),
    "UranusToNeptuneJunction": ("Raccordo Nettuno", "Urano"),
    "NeptuneToPlutoJunction": ("Raccordo Plutone", "Nettuno"),
    "PlutoToSednaJunction": ("Raccordo Sedna", "Plutone"),
    "PlutoToErisJunction": ("Raccordo Eris", "Plutone"),
    "CeresToJupiterJunction": ("Raccordo Giove", "Cerere"),

    "MercuryToVenusShortcut": ("Verso Venere", "Mercurio"),
    "VenusToEarthShortcut": ("Verso la Terra", "Venere"),
    "VenusToMercuryShortcut": ("Verso Mercurio", "Venere"),
    "EarthToVenusShortcut": ("Verso Venere", "Terra"),
    "EarthToMarsShortcut": ("Verso Marte", "Terra"),
    "EarthToMoonShortcut": ("Verso la Luna", "Terra"),
    "MarsToCeresShortcut": ("Verso Cerere", "Marte"),
    "MarsToEarthShortcut": ("Verso la Terra", "Marte"),
    "MarsToPhobosShortcut": ("Verso Phobos", "Marte"),
    "JupiterToCeresShortcut": ("Verso Cerere", "Giove"),
    "JupiterToEuropaShortcut": ("Verso Europa", "Giove"),
    "JupiterToSaturnShortcut": ("Verso Saturno", "Giove"),
    "SaturnToJupiterShortcut": ("Verso Giove", "Saturno"),
    "SaturnToUranusShortcut": ("Verso Urano", "Saturno"),
    "UranusToNeptuneShortcut": ("Verso Nettuno", "Urano"),
    "UranusToSaturnShortcut": ("Verso Saturno", "Urano"),
    "NeptuneToUranusShortcut": ("Verso Urano", "Nettuno"),
    "NeptuneToPlutoShortcut": ("Verso Plutone", "Nettuno"),
    "NeptuneToVoidShortcut": ("Verso il Void", "Nettuno"),
    "PlutoToNeptuneShortcut": ("Verso Nettuno", "Plutone"),
    "PlutoToDerelictShortcut": ("Verso il Relitto", "Plutone"),
    "PlutoToErisShortcut": ("Verso Eris", "Plutone"),
    "PlutoToSednaShortcut": ("Verso Sedna", "Plutone"),
    "CeresToJupiterShortcut": ("Verso Giove", "Cerere"),
    "CeresToMarsShortcut": ("Verso Marte", "Cerere"),
    "ErisToPlutoShortcut": ("Verso Plutone", "Eris"),
    "SednaToVoidShortcut": ("Verso il Void", "Sedna"),
    "EuropaToJupiterShortcut": ("Verso Giove", "Europa"),
    "EuropaToVoidShortcut": ("Verso il Void", "Europa"),
    "SednaToPlutoShortcut": ("Verso Plutone", "Sedna"),
    "VoidToPhobosShortcut": ("Verso Phobos", "Void"),
    "VoidToEuropaShortcut": ("Verso Europa", "Void"),
    "VoidToSednaShortcut": ("Verso Sedna", "Void"),
    "VoidToNeptuneShortcut": ("Verso Nettuno", "Void"),
    "PhobosToVoidShortcut": ("Verso il Void", "Phobos"),
    "PhobosToMarsShortcut": ("Verso Marte", "Phobos"),
    "MoonToEarthShortcut": ("Verso la Terra", "Luna"),
    "DerelictToPlutoShortcut": ("Verso Plutone", "Relitto"),

    "EventNode0": ("Balor (Nodo Evento)", "Mercurio"),
    "EventNode1": ("Thetra e Defector (Nodo Evento)", "Mercurio"),
    "EventNode2": ("Gate Crash e Defector (Nodo Evento)", "Terra"),
    "EventNode3": ("Elatha (Nodo Evento)", "Marte"),
    "EventNode4": ("Bres (Nodo Evento)", "Giove"),
    "EventNode5": ("Birog (Nodo Evento)", "Saturno"),
    "EventNode6": ("Sealab (Nodo Evento)", "Urano"),
    "EventNode7": ("Buarainech (Nodo Evento)", "Nettuno"),
    "EventNode8": ("Corb (Nodo Evento)", "Plutone"),
    "EventNode9": ("Gate Crash (Nodo Evento)", "Cerere"),
    "EventNode10": ("Lugh (Nodo Evento)", "Eris"),
    "EventNode11": ("Nemed (Nodo Evento)", "Sedna"),
    "EventNode12": ("Cryotic Front (Nodo Evento)", "Europa"),
    "EventNode13": ("Shifting Sands (Nodo Evento)", "Phobos"),
    "EventNode14": ("Gate Crash (Nodo Evento)", "Phobos"),
    "EventNode15": ("Cryotic Front (Nodo Evento)", "Europa"),
    "EventNode16": ("Cryotic Front (Nodo Evento)", "Europa"),
    "EventNode17": ("Cryotic Front (Nodo Evento)", "Europa"),
    "EventNode18": ("(Nodo Evento)", "Marte"),
    "EventNode19": ("(Nodo Evento)", "Marte"),
    "EventNode20": ("Sealab (Nodo Evento)", "Urano"),
    "EventNode21": ("Sealab (Nodo Evento)", "Urano"),
    "EventNode22": ("Sealab (Nodo Evento)", "Urano"),
    "EventNode23": ("Sealab (Nodo Evento)", "Urano"),
    "EventNode24": ("Gate Crash (Nodo Evento)", "Terra"),
    "EventNode25": ("Gate Crash (Nodo Evento)", "Terra"),
    "EventNode26": ("Doni Rubati (Nodo Evento)", "Terra"),
    "EventNode27": ("Doni Rubati (Nodo Evento)", "Void"),
    "EventNode28": ("Caccia a Wolf", "Saturno"),
    "EventNode29": ("Caccia a Wolf", "Saturno"),
    "EventNode30": ("Hostile Mergers (Nodo Evento)", "Giove"),
    "EventNode31": ("Hostile Mergers (Nodo Evento)", "Giove"),
    "EventNode32": ("Hostile Mergers (Nodo Evento)", "Giove"),
    "EventNode33": ("Hostile Mergers (Nodo Evento)", "Giove"),
    "EventNode34": ("Dog Days (Nodo Evento)", "Terra"),
    "EventNode35": ("Dog Days (Nodo Evento)", "Terra"),
    "EventNode36": ("Doni Rubati (Nodo Evento)", "Terra"),
    "EventNode37": ("Doni Rubati (Nodo Evento)", "Marte"),

    "EventNode761": ("The Index (Nodo Evento)", "Nettuno"),
    "EventNode762": ("The Index (Nodo Evento)", "Nettuno"),
    "EventNode763": ("The Index (Nodo Evento)", "Nettuno"),

    "PvpNode0": ("Cattura Cephalon (PvP Versus 50-150)", "Saturno"),
    "PvpNode1": ("PvP Versus 8-120", "Venere"),
    "PvpNode2": ("PvP Versus 500-700", "Phobos"),
    "PvpNode3": ("Cattura Cephalon (PvP Versus 150-300)", "Nettuno"),
    "PvpNode4": ("Pvp Versus 350-500", "Eris"),
    "PvpNode5": ("PvP Versus 500-1200", "Europa"),
    "PvpNode6": ("PvP Versus 1000-1500", "Plutone"),
    "PvpNode7": ("PvP Versus 300-700", "Sedna"),
    "PvpNode8": ("PvP Versus 200-300", "Giove"),
    "PvpNode9": ("Annientamento a Squadre", "Saturno"),
    "PvpNode10": ("Annientamento", "Saturno"),
    "PvpNode11": ("Arena Lunaro", "Saturno"),
    "PvpNode12": ("Cattura Cephalon (Variante)", "Saturno"),
    "PvpNode13": ("Annientamento a Squadre (Variante)", "Conclave"),
    "PvpNode14": ("Annientamento (Variante)", "Conclave"),

    "CetusHUB4": ("Cetus", "Terra"),

    "SolarisUnitedHub1": ("Solaris", "Venere"),

    "DeimosHub": ("Necralisk", "Deimos"),

    "TradeHUB1": ("Bazaar di Maroo", "Marte"),

    "TennoConHUB1": ("Stazione TennoCon", "Terra"),
    "TennoConHUB2": ("Stazione TennoCon", "Terra"),
    "TennoConBHUB6": ("Stazione TennoLive 2020", "Terra"),
    "DevStreamHUB7": ("Stazione Dev Stream", "Terra"),

    "IronwakeHUB": ("Iron Wake", "Terra"),

    "ScenarioEventHub5": ("Scarlet Spear", "Terra"),

    "DojoHub_HUB": ("Dojo", "Sistema Solare"),

    "PlayerShip": ("Orbiter", "Sistema Solare"),

    "CrewBattleNodeDojo": ("Spazio Porto", "Sistema Solare"),

    "CrewBattleNode501": ("Ammasso Mordo", "Saturno Proxima"),
    "CrewBattleNode502": ("Stretto Sover", "Terra Proxima"),
    "CrewBattleNode503": ("Eco Bifrost", "Venere Proxima"),
    "CrewBattleNode504": ("Vettore Arva", "Nettuno Proxima"),
    "CrewBattleNode505": ("Campo di Battaglia Ruse", "Veil Proxima"),  # removed
    "CrewBattleNode506": ("Ammasso Posit", "Terra Proxima"),  # removed
    "CrewBattleNode507": ("Stazione Minhast", "Terra Proxima"),  # removed
    "CrewBattleNode508": ("Satelliti Phanghoul", "Terra Proxima"),  # removed
    "CrewBattleNode509": ("Tempio Iota", "Terra Proxima"),
    "CrewBattleNode510": ("Punto Gian", "Veil Proxima"),  # removed
    "CrewBattleNode511": ("Anello Protezione del Faro", "Venere Proxima"),
    "CrewBattleNode512": ("Orvin-Haarc", "Venere Proxima"),
    "CrewBattleNode513": ("Stretto Vesper", "Venere Proxima"),
    "CrewBattleNode514": ("Gloria Perduta", "Venere Proxima"),

    "CrewBattleNode516": ("Miniere Nu-Gua", "Nettuno Proxima"),
    "CrewBattleNode517": ("Sentieri Jex", "Terra Proxima"),  # removed
    "CrewBattleNode518": ("Ammasso Ogal", "Terra Proxima"),
    "CrewBattleNode519": ("Cintura Korms", "Terra Proxima"),
    "CrewBattleNode520": ("Cintura Rian", "Terra Proxima"),  # removed
    "CrewBattleNode521": ("Deriva dei Ghiaccio Enkidu", "Nettuno Proxima"),
    "CrewBattleNode522": ("Ammasso Bendar", "Terra Proxima"),
    "CrewBattleNode523": ("Prospetto di Mammon", "Nettuno Proxima"),
    "CrewBattleNode524": ("Percezione di Sovereign", "Nettuno Proxima"),

    "CrewBattleNode526": ("Emissario Khufu", "Plutone Proxima"),
    "CrewBattleNode527": ("Sette Sirene", "Plutone Proxima"),
    "CrewBattleNode528": ("Frontiera Obol", "Plutone Proxima"),
    "CrewBattleNode529": ("Margine di Profitto", "Plutone Proxima"),
    "CrewBattleNode530": ("Riposo di Kasio", "Saturno Proxima"),
    "CrewBattleNode531": ("Varco Vila", "Saturno Proxima"),  # removed
    "CrewBattleNode532": ("Varco Spiro", "Saturno Proxima"),  # removed
    "CrewBattleNode533": ("Varco Nodo", "Saturno Proxima"),
    "CrewBattleNode534": ("Passo Lupal", "Saturno Proxima"),
    "CrewBattleNode535": ("Ammasso Vand", "Saturno Proxima"),
    "CrewBattleNode536": ("Asse Peregrine", "Plutone Proxima"),

    "CrewBattleNode538": ("Calabash", "Veil Proxima"),
    "CrewBattleNode539": ("Numina", "Veil Proxima"),
    "CrewBattleNode540": ("Arco d'Argento", "Veil Proxima"),
    "CrewBattleNode541": ("Erato", "Veil Proxima"),
    "CrewBattleNode542": ("Lu-Yan", "Veil Proxima"),

    "CrewBattleNode550": ("Reticolo Nsu", "Veil Proxima"),
    "CrewBattleNode551": ("Tomba di Ganalen", "Veil Proxima"),  # removed
    "CrewBattleNode552": ("Rya", "Veil Proxima"),  # removed
    "CrewBattleNode553": ("Flexa", "Veil Proxima"),
    "CrewBattleNode554": ("Nebulosa H-2", "Veil Proxima"),
    "CrewBattleNode555": ("Nebulosa R-9", "Veil Proxima"),
    "CrewBattleNode556": ("Volo Libero", "Terra Proxima"),

    "/Lotus/Types/Keys/SortieBossKeyPhorid": ("???", "Mercurio"),
}
