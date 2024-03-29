# -*- coding: utf-8 -*-

PVP_MISSION_POINT = (500, 1500, 3000)

PVP_MISSION_TYPE = {
    "PVPMODE_NONE": {"it": "Nessuno", "en": "None"},
    "PVPMODE_ALL": {"it": "Tutti", "en": "All"},
    "PVPMODE_DEATHMATCH": {"it": "Annientamento", "en": "Death Match"},
    "PVPMODE_TEAMDEATHMATCH": {"it": "Annientamento a Squadre", "en": "Team Death Match"},
    "PVPMODE_CAPTURETHEFLAG": {"it": "Cattura Cephalon", "en": "Capture the Cephalon"},
    "PVPMODE_SPEEDBALL": {"it": "Lunaro", "en": "Lunaro"},
    "PVPChallengeTypeCategory_WEEKLY_ROOT": {"it": "Nessuna", "en": "None"},
    "PVPChallengeTypeCategory_WEEKLY": {"it": "Settimanale", "en": "Weekly"},
    "PVPChallengeTypeCategory_DAILY": {"it": "Giornaliera", "en": "Daily"},
    "PVPChallengeTypeCategory_MODEAFFECTOR": {"it": "Modificatore", "en": "Mode Affector"},
    "PVPChallengeTypeCategory_POWERUP": {"it": "Potenziamento", "en": "Power Up"}
}

PVP_CHALLENGE_TYPE = {
    "PVPTimedChallengeWeeklyStandardSet": "Set Missioni Settimanali",
    "PVPTimedChallengeOtherChallengeCompleteANY": "Condizionamento",
    "PVPTimedChallengeGameModeComplete": "Partita Completata",
    "PVPTimedChallengeGameModeWins": "Partita Vinta",
    # DEATHMATCH
    # TEAMDEATHMATCH
    "PVPTimedChallengeMatchComplete": "Portare a Termine",
    "PVPTimedChallengeKillsPrimary": "Bersaglio Primario",
    "PVPTimedChallengeKillsSecondary": "Bersaglio Secondario",
    "PVPTimedChallengeKillsMelee": "Gladiatore",
    "PVPTimedChallengeKillsHeadShots": "Pistolero",
    "PVPTimedChallengeKillsWhileInAir": "Attacco Aereo",
    "PVPTimedChallengeKillsTargetInAir": "Attacco Antiaereo",
    "PVPTimedChallengeKillsWhileSliding": "Attacco in Scivolata",
    "PVPTimedChallengeKillsCombo": "Destrezza",
    "PVPTimedChallengeKillsMulti": "Versatilità",
    "PVPTimedChallengeKillsPower": "Artista del Void",
    "PVPTimedChallengeKillsPayback": "Vendetta",
    "PVPTimedChallengeKillsPayback_": "Vendetta",
    "PVPTimedChallengeKillsStreakStopped": "Serie Interrotta",
    "PVPTimedChallengeKillsStreakStopped_": "Serie Interrotta",
    "PVPTimedChallengeKillsStreak": "Uccisioni Consecutive",
    "PVPTimedChallengeKillsStreak_": "Uccisioni Consecutive",
    "PVPTimedChallengeKillsStreakDomination": "Dominazione",
    "PVPTimedChallengeKillsStreakDomination_": "Dominazione",
    # CAPTURE THE CEPHALON
    "PVPTimedChallengeFlagCapture": "Liberatore",
    "PVPTimedChallengeFlagReturn": "Bandito",
    # LUNARO
    "PVPTimedChallengeSpeedballCatches": "Presa!",
    "PVPTimedChallengeSpeedballSteals": "Agguanta e Scappa",
    "PVPTimedChallengeSpeedballChecks": "Blocco",
    "PVPTimedChallengeSpeedballGoals": "Goal!",
    "PVPTimedChallengeSpeedballInterceptions": "Intercettato!",
    "PVPTimedChallengeSpeedballPasses": "Passaggio!",
    # MODIFIER
    "PVPTimedAffectorSuperPistolDamage": "Showdown",
    "PVPTimedAffectorSuperEnergy": "Energy Flux",
    "PVPTimedAffectorSuperPowerDamage": "Potency",
    "PVPTimedAffectorSuperMeleeDamage": "Martial Law",
    "PVPTimedAffectorSuperEverything": "Overpowered",
}

PVP_CHALLENGE_DESC = {
    "PVPTimedChallengeWeeklyStandardSet": {"it": "Completa tutte le 3 missioni Settimanali",
                                           "en": "Complete all weekly missions"},
    "PVPTimedAffectorSuperPistolDamage": {"it": "Aumento danno Pistola di {{X}} volte",
                                          "en": "Pistol Damage Boost by {{X}} times"},
    "PVPTimedAffectorSuperEnergy": {"it": "Aumento drop energia e munizioni di {{X}} volte",
                                    "en": "Energy and Munition Drop Boost by {{X}} times"},
    "PVPTimedAffectorSuperPowerDamage": {"it": "Aumento danno abilità di {{X}} volte",
                                         "en": "Ability Damage Boost by {{X}} times"},
    "PVPTimedAffectorSuperMeleeDamage": {"it": "Aumento danno Corpo a Corpo di {{X}} volte",
                                         "en": "Melee Damage Boost by {{X}} times"},
    "PVPTimedAffectorSuperEverything": {
        "it": "Aumento danno Pistola, Abilità, Corpo a Corpo  e drop energia di {{X}} volte",
        "en": "Pistol, Ability, Melee Damage Boost and Energy drop boost by {{X}} times"},
    "PVPTimedChallengeGameModeWins": {"it": "Completa {{X}} partite giornaliere in qualsiasi modalità di gioco",
                                      "en": "Complete {{X}} daily missions in any game mode"},
    "PVPTimedChallengeOtherChallengeCompleteANY": {"it": "Completa {{X}} sfide Giornaliere",
                                                   "en": "Complete {{X}} daily missions"},
    "PVPTimedChallengeGameModeComplete": {"it": "Completa {{X}} partite di qualsiasi modalità di gioco",
                                          "en": "Complete {{X}} any game in any game mode"},
    "PVPTimedChallengeMatchComplete": {"it": "Completa {{X}} partite", "en": "Complete {{X}} match"},
    "PVPTimedChallengeKillsPrimary": {"it": "Uccidi {{X}} nemici con la tua arma primaria in una partita",
                                      "en": "Kill {{X}} enemies with your primary weapon in a match"},
    "PVPTimedChallengeKillsSecondary": {"it": "Completa {{X}} nemici con la tua arma secondari in una partita",
                                        "en": "Complete {{X}} enemies with your secondary weapon in a match"},
    "PVPTimedChallengeKillsMelee": {"it": "Completa {{X}} nemici con la tua arma corpo a corpo in una partita",
                                    "en": "Complete {{X}} enemies with your melee weapon in a match"},
    "PVPTimedChallengeKillsStreak": {"it": "Ottieni una serie di {{X}} uccisioni in una partita",
                                     "en": "Obtain {{X}} kill streak in a match"},
    "PVPTimedChallengeKillsStreak_": {"it": "Ottieni una serie di {{X}} uccisioni", "en": "Obtain {{X}} kill streak"},
    "PVPTimedChallengeKillsWhileInAir": {"it": "Uccidi {{X}} nemici mentre sei in volo",
                                         "en": "Kill {{X}} enemies while airborne"},
    "PVPTimedChallengeKillsHeadShots": {"it": "Fai {{X}} uccisioni con colpo in test",
                                        "en": "Obtain {{X}} headshot kill"},
    "PVPTimedChallengeKillsStreakDomination": {"it": "Elimina {{X}} nemici senza essere ucciso in una partita",
                                               "en": "Kill {{X}} enemies in a kill streak in a match"},
    "PVPTimedChallengeKillsStreakDomination_": {"it": "Elimina {{X}} nemici senza essere ucciso",
                                                "en": "Kill {{X}} enemies in a kill streak"},
    "PVPTimedChallengeKillsTargetInAir": {"it": "Uccidi {{X}} nemici in volo", "en": "Kill {{X}} enemies in air"},
    "PVPTimedChallengeKillsWhileSliding": {"it": "Uccidi {{X}} nemici durante una scivolata in una partita",
                                           "en": "Kill {{X}} enemies while sliding in a match"},
    "PVPTimedChallengeKillsPower": {"it": "Fai {{X}} uccisioni con poteri Warframe",
                                    "en": "Kill {{X}} enemies with Warframe abilities"},
    "PVPTimedChallengeKillsCombo": {"it": "Uccidi {{X}} nemici usando corpo a corpo, armi e poteri",
                                    "en": "Kill {{X}} enemies with melee, weapon and abilities"},
    "PVPTimedChallengeKillsMulti": {"it": "Uccidi {{X}} nemici con due tra corpo a copro, armi e poteri",
                                    "en": "Kill {{X}} enemies with two of melee, weapon or abilities"},
    "PVPTimedChallengeKillsPayback": {"it": "Uccidi {{X}} nemici che ti hanno ucciso in una partita",
                                      "en": "Kill {{X}} enemies that killed you in a match"},
    "PVPTimedChallengeKillsPayback_": {"it": "Uccidi {{X}} nemici che ti hanno ucciso",
                                       "en": "Kill {{X}} enemies that killed you"},
    "PVPTimedChallengeKillsStreakStopped": {"it": "Uccidi {{X}} nemici in serie di uccisioni in una partita",
                                            "en": "Kill {{X}} enemies in a kill streak in a match"},
    "PVPTimedChallengeKillsStreakStopped_": {"it": "Uccidi {{X}} nemici in serie di uccisioni",
                                             "en": "Kill {{X}} enemies in a kill streak"},
    "PVPTimedChallengeFlagReturn": {"it": "Riporta il Cephalon della tua squadra {{X}} volte",
                                    "en": "Return the cephalon of your team {{X}} times"},
    "PVPTimedChallengeFlagCapture": {"it": "Cattura {{X}} Cephalon", "en": "Capture {{X}} Cephalon"},
    "PVPTimedChallengeSpeedballChecks": {"it": "Colpisci {{X}} volte gli avversari in possesso della palla",
                                         "en": "Hit {{X}} an enemy with the ball"},
    "PVPTimedChallengeSpeedballSteals": {"it": "Ruba la palla {{X}} volte", "en": "Steal the ball {{X}} times"},
    "PVPTimedChallengeSpeedballCatches": {"it": "Ricevi {{X}} passaggi dai compagni di squadra",
                                          "en": "Get {{X}} catches"},
    "PVPTimedChallengeSpeedballGoals": {"it": "Segna {{X}} Goal", "en": "Do {{X}} goals"},
    "PVPTimedChallengeSpeedballInterceptions": {"it": "Intercetta {{X}} passaggi dagli avversari",
                                                "en": "Intercept {{X}} times a ball"},
    "PVPTimedChallengeSpeedballPasses": {"it": "Completa con successo {{X}} passaggi tra i tuoi compagni",
                                         "en": "Pass the ball {{X}} times"},
}

PVP_ALT_DESC = {
    "/Lotus/Language/Menu/PVPDMAlternativeModeDesc": {
        "it": "Equipaggiato solo con un Opticor modificato, combatti i tuoi compagni Tenno in una battaglia in cui un "
              "solo colpo è letale!",
        "en": "Equipped only with a modified Opticor, fight your fellow Tenno in a battle where one shot is lethal!"},
    "/Lotus/Language/Game/DM_NinjaVariantDescription": {
        "it": "Affronta i tuoi avversari con l'affilata Nikana e il veloce Hikou in questa eccitante partita mortale.",
        "en": "Take on your opponents with the sharp Nikana and the swift Hikou in this exciting death match."},
    "/Lotus/Language/G1Quests/ValentinesVariantToolTip": {
        "it": "Uccidi con gentilezza in questa speciale variante che mischia passione con precisione.",
        "en": "Kill with kindness in this special variant that mixes passion with precision."},
    "/Lotus/Language/G1Quests/TacAlertSnowballFightToolTip": {
        "it": "Una schermaglia fresca di palle di neve e caos alla menta.",
        "en": "A fresh skirmish of snowballs and mint chaos."},
}
