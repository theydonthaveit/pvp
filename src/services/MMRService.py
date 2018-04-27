# generate a mmr score with a better algorithm than that used in chess as we deserve better recognition

# find a way to get a medium score for your champ:
# example:
# warwick
# https://euw1.api.riotgames.com/lol/match/v1/stats/player_history/EUW1/234897405

# api -= RGAPI-9eb2a0b5-2a5a-4b3f-b546-5fc8da721090
# https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/234897405?champion=19&queue=420&season=11
# https://euw1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=false
# https://euw1.api.riotgames.com/lol/static-data/v3/items?locale=en_US
# https://euw1.api.riotgames.com/lol/static-data/v3/summoner-spells?locale=en_US&dataById=false

# {
#     "Origin": null,
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#     "X-Riot-Token": "RGAPI-8deb9004-e152-47a5-8a93-bf555a8def65",
#     "Accept-Language": "en-GB,en;q=0.5",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:59.0) Gecko/20100101 Firefox/59.0"
# }

import activites of a jungler (depending patch - ranked 1 to 5) and champion type:
warwick is the example used:
vision: 3
kills:
turrets:
dragons:
herald:
scuttler:
baron:
camps i.e. cs:
deaths:
assists:
global damage:
damage to champs:
healing:
damage taken:
itemization:
ganking (jungle proc):


json_data_for_games_by_champ = '{
    "matches": [
        {
            "lane": "JUNGLE",
            "gameId": 3602726395,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1523900060050,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3602474747,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1523879162099,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3602391104,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1523866556851,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3591097049,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522943384507,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3590473946,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522920596641,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3590448171,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522917959720,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "NONE",
            "gameId": 3588435900,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522779620165,
            "queue": 420,
            "role": "DUO_SUPPORT",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3588103304,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522765201634,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "NONE",
            "gameId": 3588076192,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522763809065,
            "queue": 420,
            "role": "DUO_SUPPORT",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3587101294,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522681112379,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3587043392,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522678625748,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3586761558,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522660508531,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3586723580,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522653104624,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3584668888,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522523551416,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3583919647,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522483130227,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3579721427,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1522175270532,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3555418993,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1520373787861,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3552795188,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1520175066215,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3551059615,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1520068662854,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3541102525,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1519333535189,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3539621950,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1519237618051,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3539526843,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1519232685610,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3532304948,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1518710814113,
            "queue": 420,
            "role": "NONE",
            "season": 11
        },
        {
            "lane": "JUNGLE",
            "gameId": 3529026911,
            "champion": 19,
            "platformId": "EUW1",
            "timestamp": 1518467829226,
            "queue": 420,
            "role": "NONE",
            "season": 11
        }
    ],
    "endIndex": 28,
    "startIndex": 0,
    "totalGames": 28
}'

json_data_by_game = '{
    "seasonId": 11,
    "queueId": 420,
    "gameId": 3588435900,
    "participantIdentities": [
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "Only Bronze ",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/202761568",
                "platformId": "EUW1",
                "currentAccountId": 202761568,
                "profileIcon": 1661,
                "summonerId": 44069835,
                "accountId": 202761568
            },
            "participantId": 1
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "Rapiddd",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/229064934",
                "platformId": "EUW1",
                "currentAccountId": 229064934,
                "profileIcon": 1297,
                "summonerId": 106089317,
                "accountId": 229064934
            },
            "participantId": 2
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "modesLTU",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/207134885",
                "platformId": "EUW1",
                "currentAccountId": 207134885,
                "profileIcon": 25,
                "summonerId": 51755641,
                "accountId": 207134885
            },
            "participantId": 3
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "o Zia o",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/225706044",
                "platformId": "EUW1",
                "currentAccountId": 225706044,
                "profileIcon": 1644,
                "summonerId": 82269497,
                "accountId": 225706044
            },
            "participantId": 4
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "meow side",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/234897405",
                "platformId": "EUW1",
                "currentAccountId": 234897405,
                "profileIcon": 3233,
                "summonerId": 102738872,
                "accountId": 234897405
            },
            "participantId": 5
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "Prince940",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/221832583",
                "platformId": "EUW1",
                "currentAccountId": 221832583,
                "profileIcon": 1588,
                "summonerId": 74037159,
                "accountId": 221832583
            },
            "participantId": 6
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "HideInLantern",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/23116758",
                "platformId": "EUW1",
                "currentAccountId": 23116758,
                "profileIcon": 3379,
                "summonerId": 20118635,
                "accountId": 23116758
            },
            "participantId": 7
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "c990gamer",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/28517420",
                "platformId": "EUW1",
                "currentAccountId": 28517420,
                "profileIcon": 3371,
                "summonerId": 24122893,
                "accountId": 28517420
            },
            "participantId": 8
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "Sisamoon",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/33778924",
                "platformId": "EUW1",
                "currentAccountId": 33778924,
                "profileIcon": 3369,
                "summonerId": 29974783,
                "accountId": 33778924
            },
            "participantId": 9
        },
        {
            "player": {
                "currentPlatformId": "EUW1",
                "summonerName": "One more Monky",
                "matchHistoryUri": "/v1/stats/player_history/EUW1/224063409",
                "platformId": "EUW1",
                "currentAccountId": 224063409,
                "profileIcon": 3159,
                "summonerId": 78538132,
                "accountId": 224063409
            },
            "participantId": 10
        }
    ],
    "gameVersion": "8.6.222.2149",
    "platformId": "EUW1",
    "gameMode": "CLASSIC",
    "mapId": 11,
    "gameType": "MATCHED_GAME",
    "teams": [
        {
            "firstDragon": true,
            "bans": [
                {
                    "pickTurn": 1,
                    "championId": 28
                },
                {
                    "pickTurn": 2,
                    "championId": 141
                },
                {
                    "pickTurn": 3,
                    "championId": 157
                },
                {
                    "pickTurn": 4,
                    "championId": 122
                },
                {
                    "pickTurn": 5,
                    "championId": 18
                }
            ],
            "firstInhibitor": false,
            "win": "Win",
            "firstRiftHerald": false,
            "firstBaron": false,
            "baronKills": 0,
            "riftHeraldKills": 0,
            "firstBlood": true,
            "teamId": 100,
            "firstTower": true,
            "vilemawKills": 0,
            "inhibitorKills": 0,
            "towerKills": 4,
            "dominionVictoryScore": 0,
            "dragonKills": 1
        },
        {
            "firstDragon": false,
            "bans": [
                {
                    "pickTurn": 6,
                    "championId": 51
                },
                {
                    "pickTurn": 7,
                    "championId": 110
                },
                {
                    "pickTurn": 8,
                    "championId": 141
                },
                {
                    "pickTurn": 9,
                    "championId": 107
                },
                {
                    "pickTurn": 10,
                    "championId": 105
                }
            ],
            "firstInhibitor": false,
            "win": "Fail",
            "firstRiftHerald": false,
            "firstBaron": false,
            "baronKills": 0,
            "riftHeraldKills": 0,
            "firstBlood": false,
            "teamId": 200,
            "firstTower": false,
            "vilemawKills": 0,
            "inhibitorKills": 0,
            "towerKills": 0,
            "dominionVictoryScore": 0,
            "dragonKills": 0
        }
    ],
    "participants": [
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 9,
                "magicDamageDealtToChampions": 172,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 127,
                "longestTimeSpentLiving": 474,
                "perk1Var1": 257,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8237,
                "perk4": 8243,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 4,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 172,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 0,
                "damageDealtToTurrets": 2195,
                "physicalDamageDealtToChampions": 9935,
                "damageDealtToObjectives": 2195,
                "perk2Var2": 0,
                "perk2Var3": 0,
                "totalUnitsHealed": 1,
                "perk2Var1": 7,
                "perk4Var1": 13,
                "totalDamageTaken": 7993,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 2,
                "quadraKills": 0,
                "magicDamageDealt": 172,
                "firstBloodAssist": false,
                "item2": 3047,
                "item3": 1031,
                "item0": 1055,
                "item1": 3071,
                "item6": 3363,
                "item4": 0,
                "item5": 0,
                "perk1": 8126,
                "perk0": 8112,
                "perk3": 8135,
                "perk2": 8138,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 4,
                "damageSelfMitigated": 8667,
                "magicalDamageTaken": 1120,
                "perk0Var2": 0,
                "trueDamageTaken": 925,
                "assists": 4,
                "perk4Var2": 0,
                "goldSpent": 5475,
                "trueDamageDealt": 632,
                "participantId": 1,
                "physicalDamageDealt": 44708,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 10740,
                "physicalDamageTaken": 5948,
                "totalPlayerScore": 0,
                "win": true,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 45514,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 3,
                "wardsPlaced": 6,
                "perkPrimaryStyle": 8100,
                "perkSubStyle": 8200,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 632,
                "goldEarned": 5975,
                "killingSprees": 2,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 10,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 503,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 1,
                "pentaKills": 0,
                "totalHeal": 688,
                "totalMinionsKilled": 76,
                "timeCCingOthers": 12
            },
            "spell1Id": 4,
            "participantId": 1,
            "highestAchievedSeasonTier": "SILVER",
            "spell2Id": 12,
            "teamId": 100,
            "timeline": {
                "lane": "NONE",
                "participantId": 1,
                "csDiffPerMinDeltas": {
                    "0-10": 1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 297.1
                },
                "xpDiffPerMinDeltas": {
                    "0-10": 70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 5.5
                },
                "xpPerMinDeltas": {
                    "0-10": 495.79999999999995
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": -82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 295
                }
            },
            "championId": 6
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 6,
                "magicDamageDealtToChampions": 5994,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 200,
                "longestTimeSpentLiving": 502,
                "perk1Var1": 986,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8304,
                "perk4": 8347,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 2,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 9,
                "perk5Var3": 0,
                "perk5Var2": 3,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 0,
                "damageDealtToTurrets": 3135,
                "physicalDamageDealtToChampions": 222,
                "damageDealtToObjectives": 3210,
                "perk2Var2": 0,
                "perk2Var3": 0,
                "totalUnitsHealed": 0,
                "perk2Var1": 0,
                "perk4Var1": 0,
                "totalDamageTaken": 4416,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 2,
                "quadraKills": 0,
                "magicDamageDealt": 29403,
                "firstBloodAssist": false,
                "item2": 3285,
                "item3": 3158,
                "item0": 1056,
                "item1": 3191,
                "item6": 3340,
                "item4": 0,
                "item5": 0,
                "perk1": 8226,
                "perk0": 8214,
                "perk3": 8237,
                "perk2": 8210,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 299,
                "damageSelfMitigated": 1964,
                "magicalDamageTaken": 2255,
                "perk0Var2": 570,
                "trueDamageTaken": 765,
                "assists": 10,
                "perk4Var2": 0,
                "goldSpent": 5600,
                "trueDamageDealt": 4780,
                "participantId": 2,
                "physicalDamageDealt": 9985,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 6216,
                "physicalDamageTaken": 1395,
                "totalPlayerScore": 0,
                "win": true,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 44168,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 2,
                "wardsPlaced": 5,
                "perkPrimaryStyle": 8200,
                "perkSubStyle": 8300,
                "turretKills": 1,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 0,
                "goldEarned": 6301,
                "killingSprees": 1,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 11,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 350,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 0,
                "totalMinionsKilled": 88,
                "timeCCingOthers": 7
            },
            "spell1Id": 4,
            "participantId": 2,
            "highestAchievedSeasonTier": "UNRANKED",
            "spell2Id": 12,
            "teamId": 100,
            "timeline": {
                "lane": "NONE",
                "participantId": 2,
                "csDiffPerMinDeltas": {
                    "0-10": 1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 277.6
                },
                "xpDiffPerMinDeltas": {
                    "0-10": 70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 7.1000000000000005
                },
                "xpPerMinDeltas": {
                    "0-10": 485.3
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": -82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 189.6
                }
            },
            "championId": 43
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 12,
                "magicDamageDealtToChampions": 3251,
                "largestMultiKill": 3,
                "totalTimeCrowdControlDealt": 133,
                "longestTimeSpentLiving": 582,
                "perk1Var1": 9,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 1,
                "perk5": 8210,
                "perk4": 8226,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 13,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 0,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 2,
                "damageDealtToTurrets": 5796,
                "physicalDamageDealtToChampions": 11528,
                "damageDealtToObjectives": 5796,
                "perk2Var2": 0,
                "perk2Var3": 0,
                "totalUnitsHealed": 2,
                "perk2Var1": 4,
                "perk4Var1": 775,
                "totalDamageTaken": 7462,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 9,
                "quadraKills": 0,
                "magicDamageDealt": 8043,
                "firstBloodAssist": false,
                "item2": 3144,
                "item3": 3004,
                "item0": 3025,
                "item1": 1055,
                "item6": 3363,
                "item4": 3158,
                "item5": 2055,
                "perk1": 8304,
                "perk0": 8359,
                "perk3": 8347,
                "perk2": 8345,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 0,
                "damageSelfMitigated": 3743,
                "magicalDamageTaken": 2436,
                "perk0Var2": 14,
                "trueDamageTaken": 532,
                "assists": 1,
                "perk4Var2": 0,
                "goldSpent": 7850,
                "trueDamageDealt": 850,
                "participantId": 3,
                "physicalDamageDealt": 63894,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 15233,
                "physicalDamageTaken": 4493,
                "totalPlayerScore": 0,
                "win": true,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 72788,
                "neutralMinionsKilledEnemyJungle": 2,
                "deaths": 1,
                "wardsPlaced": 7,
                "perkPrimaryStyle": 8300,
                "perkSubStyle": 8200,
                "turretKills": 1,
                "firstBloodKill": true,
                "trueDamageDealtToChampions": 454,
                "goldEarned": 10340,
                "killingSprees": 2,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": true,
                "champLevel": 10,
                "doubleKills": 4,
                "inhibitorKills": 0,
                "perk0Var1": 435,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 3,
                "pentaKills": 0,
                "totalHeal": 651,
                "totalMinionsKilled": 127,
                "timeCCingOthers": 4
            },
            "spell1Id": 7,
            "participantId": 3,
            "highestAchievedSeasonTier": "UNRANKED",
            "spell2Id": 4,
            "teamId": 100,
            "timeline": {
                "lane": "NONE",
                "participantId": 3,
                "csDiffPerMinDeltas": {
                    "0-10": 1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 446.2
                },
                "xpDiffPerMinDeltas": {
                    "0-10": 70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 7.800000000000001
                },
                "xpPerMinDeltas": {
                    "0-10": 327.4
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": -82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 370.9
                }
            },
            "championId": 81
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 14,
                "magicDamageDealtToChampions": 2151,
                "largestMultiKill": 0,
                "totalTimeCrowdControlDealt": 476,
                "longestTimeSpentLiving": 587,
                "perk1Var1": 362,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8345,
                "perk4": 8304,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 0,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 4,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 0,
                "damageDealtToTurrets": 1035,
                "physicalDamageDealtToChampions": 934,
                "damageDealtToObjectives": 1035,
                "perk2Var2": 14,
                "perk2Var3": 13,
                "totalUnitsHealed": 4,
                "perk2Var1": 40,
                "perk4Var1": 8,
                "totalDamageTaken": 10122,
                "perk4Var3": 0,
                "wardsKilled": 1,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 0,
                "quadraKills": 0,
                "magicDamageDealt": 4293,
                "firstBloodAssist": false,
                "item2": 3105,
                "item3": 0,
                "item0": 3401,
                "item1": 3117,
                "item6": 3340,
                "item4": 1033,
                "item5": 0,
                "perk1": 8473,
                "perk0": 8465,
                "perk3": 8453,
                "perk2": 8429,
                "perk3Var3": 0,
                "perk3Var2": 206,
                "perk3Var1": 129,
                "damageSelfMitigated": 8054,
                "magicalDamageTaken": 2029,
                "perk0Var2": 0,
                "trueDamageTaken": 1214,
                "assists": 10,
                "perk4Var2": 3,
                "goldSpent": 4100,
                "trueDamageDealt": 3463,
                "participantId": 4,
                "physicalDamageDealt": 4817,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 3086,
                "physicalDamageTaken": 6878,
                "totalPlayerScore": 0,
                "win": true,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 12574,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 3,
                "wardsPlaced": 8,
                "perkPrimaryStyle": 8400,
                "perkSubStyle": 8300,
                "turretKills": 2,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 0,
                "goldEarned": 5047,
                "killingSprees": 0,
                "unrealKills": 0,
                "firstTowerAssist": true,
                "firstTowerKill": false,
                "champLevel": 9,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 1091,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 1319,
                "totalMinionsKilled": 19,
                "timeCCingOthers": 20
            },
            "spell1Id": 4,
            "participantId": 4,
            "highestAchievedSeasonTier": "BRONZE",
            "spell2Id": 3,
            "teamId": 100,
            "timeline": {
                "lane": "NONE",
                "participantId": 4,
                "csDiffPerMinDeltas": {
                    "0-10": 1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 245.9
                },
                "xpDiffPerMinDeltas": {
                    "0-10": 70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 1.3
                },
                "xpPerMinDeltas": {
                    "0-10": 304.20000000000005
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": -82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 390.8
                }
            },
            "championId": 201
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 49,
                "visionScore": 9,
                "magicDamageDealtToChampions": 4300,
                "largestMultiKill": 2,
                "totalTimeCrowdControlDealt": 531,
                "longestTimeSpentLiving": 906,
                "perk1Var1": 529,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8105,
                "perk4": 8143,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 7,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 5,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 68,
                "damageDealtToTurrets": 605,
                "physicalDamageDealtToChampions": 3018,
                "damageDealtToObjectives": 6579,
                "perk2Var2": 40,
                "perk2Var3": 0,
                "totalUnitsHealed": 1,
                "perk2Var1": 12,
                "perk4Var1": 138,
                "totalDamageTaken": 15585,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 4,
                "quadraKills": 0,
                "magicDamageDealt": 20881,
                "firstBloodAssist": false,
                "item2": 3111,
                "item3": 3082,
                "item0": 1413,
                "item1": 3077,
                "item6": 3340,
                "item4": 0,
                "item5": 0,
                "perk1": 9111,
                "perk0": 8005,
                "perk3": 8014,
                "perk2": 9103,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 286,
                "damageSelfMitigated": 8428,
                "magicalDamageTaken": 1426,
                "perk0Var2": 820,
                "trueDamageTaken": 460,
                "assists": 6,
                "perk4Var2": 0,
                "goldSpent": 5800,
                "trueDamageDealt": 6404,
                "participantId": 5,
                "physicalDamageDealt": 36742,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 7664,
                "physicalDamageTaken": 13699,
                "totalPlayerScore": 0,
                "win": true,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 64027,
                "neutralMinionsKilledEnemyJungle": 4,
                "deaths": 1,
                "wardsPlaced": 6,
                "perkPrimaryStyle": 8000,
                "perkSubStyle": 8100,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 346,
                "goldEarned": 7452,
                "killingSprees": 2,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 10,
                "doubleKills": 1,
                "inhibitorKills": 0,
                "perk0Var1": 995,
                "combatPlayerScore": 0,
                "perk0Var3": 175,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 8578,
                "totalMinionsKilled": 8,
                "timeCCingOthers": 20
            },
            "spell1Id": 11,
            "participantId": 5,
            "highestAchievedSeasonTier": "UNRANKED",
            "spell2Id": 4,
            "teamId": 100,
            "timeline": {
                "lane": "NONE",
                "participantId": 5,
                "csDiffPerMinDeltas": {
                    "0-10": 1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 334.1
                },
                "xpDiffPerMinDeltas": {
                    "0-10": 70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 0.2
                },
                "xpPerMinDeltas": {
                    "0-10": 328.9
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": -82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 615.4000000000001
                }
            },
            "championId": 19
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 2,
                "visionScore": 4,
                "magicDamageDealtToChampions": 5221,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 167,
                "longestTimeSpentLiving": 788,
                "perk1Var1": 11,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8138,
                "perk4": 8126,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 4,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 12,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 2,
                "damageDealtToTurrets": 314,
                "physicalDamageDealtToChampions": 241,
                "damageDealtToObjectives": 711,
                "perk2Var2": 0,
                "perk2Var3": 0,
                "totalUnitsHealed": 0,
                "perk2Var1": 0,
                "perk4Var1": 218,
                "totalDamageTaken": 7371,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 2,
                "quadraKills": 0,
                "magicDamageDealt": 23223,
                "firstBloodAssist": false,
                "item2": 1052,
                "item3": 3020,
                "item0": 1056,
                "item1": 1026,
                "item6": 3340,
                "item4": 3802,
                "item5": 0,
                "perk1": 8243,
                "perk0": 8214,
                "perk3": 8236,
                "perk2": 8210,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 8,
                "damageSelfMitigated": 3118,
                "magicalDamageTaken": 3296,
                "perk0Var2": 0,
                "trueDamageTaken": 216,
                "assists": 4,
                "perk4Var2": 0,
                "goldSpent": 4035,
                "trueDamageDealt": 4817,
                "participantId": 6,
                "physicalDamageDealt": 4918,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 7791,
                "physicalDamageTaken": 3859,
                "totalPlayerScore": 0,
                "win": false,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 32959,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 2,
                "wardsPlaced": 3,
                "perkPrimaryStyle": 8200,
                "perkSubStyle": 8100,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 2328,
                "goldEarned": 5838,
                "killingSprees": 2,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 10,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 625,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 0,
                "totalMinionsKilled": 80,
                "timeCCingOthers": 13
            },
            "spell1Id": 21,
            "participantId": 6,
            "highestAchievedSeasonTier": "BRONZE",
            "spell2Id": 4,
            "teamId": 200,
            "timeline": {
                "lane": "NONE",
                "participantId": 6,
                "csDiffPerMinDeltas": {
                    "0-10": -1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 298.4
                },
                "xpDiffPerMinDeltas": {
                    "0-10": -70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 5.9
                },
                "xpPerMinDeltas": {
                    "0-10": 449.1
                },
                "role": "DUO",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": 82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 226.39999999999998
                }
            },
            "championId": 161
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 8,
                "magicDamageDealtToChampions": 530,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 47,
                "longestTimeSpentLiving": 223,
                "perk1Var1": 396,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8014,
                "perk4": 9105,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 1,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 49,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 4,
                "damageDealtToTurrets": 0,
                "physicalDamageDealtToChampions": 1584,
                "damageDealtToObjectives": 0,
                "perk2Var2": 13,
                "perk2Var3": 11,
                "totalUnitsHealed": 1,
                "perk2Var1": 40,
                "perk4Var1": 0,
                "totalDamageTaken": 11706,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 0,
                "quadraKills": 0,
                "magicDamageDealt": 576,
                "firstBloodAssist": false,
                "item2": 1001,
                "item3": 1029,
                "item0": 1054,
                "item1": 3071,
                "item6": 3340,
                "item4": 0,
                "item5": 0,
                "perk1": 8473,
                "perk0": 8437,
                "perk3": 8451,
                "perk2": 8429,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 63,
                "damageSelfMitigated": 9032,
                "magicalDamageTaken": 2317,
                "perk0Var2": 156,
                "trueDamageTaken": 448,
                "assists": 0,
                "perk4Var2": 0,
                "goldSpent": 4250,
                "trueDamageDealt": 2545,
                "participantId": 7,
                "physicalDamageDealt": 27430,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 2115,
                "physicalDamageTaken": 8940,
                "totalPlayerScore": 0,
                "win": false,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 30551,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 6,
                "wardsPlaced": 5,
                "perkPrimaryStyle": 8400,
                "perkSubStyle": 8000,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 0,
                "goldEarned": 4639,
                "killingSprees": 0,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 9,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 128,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 102,
                "totalMinionsKilled": 82,
                "timeCCingOthers": 15
            },
            "spell1Id": 4,
            "participantId": 7,
            "highestAchievedSeasonTier": "UNRANKED",
            "spell2Id": 12,
            "teamId": 200,
            "timeline": {
                "lane": "NONE",
                "participantId": 7,
                "csDiffPerMinDeltas": {
                    "0-10": -1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 220.1
                },
                "xpDiffPerMinDeltas": {
                    "0-10": -70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 5
                },
                "xpPerMinDeltas": {
                    "0-10": 337.5
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": 82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 486.4
                }
            },
            "championId": 86
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 4,
                "magicDamageDealtToChampions": 995,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 161,
                "longestTimeSpentLiving": 388,
                "perk1Var1": 510,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8014,
                "perk4": 9111,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 2,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 124,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 0,
                "damageDealtToTurrets": 377,
                "physicalDamageDealtToChampions": 4799,
                "damageDealtToObjectives": 377,
                "perk2Var2": 20,
                "perk2Var3": 0,
                "totalUnitsHealed": 1,
                "perk2Var1": 11,
                "perk4Var1": 136,
                "totalDamageTaken": 8662,
                "perk4Var3": 0,
                "wardsKilled": 1,
                "largestCriticalStrike": 351,
                "largestKillingSpree": 0,
                "quadraKills": 0,
                "magicDamageDealt": 8441,
                "firstBloodAssist": false,
                "item2": 0,
                "item3": 0,
                "item0": 1001,
                "item1": 3508,
                "item6": 3340,
                "item4": 0,
                "item5": 1055,
                "perk1": 8226,
                "perk0": 8229,
                "perk3": 8237,
                "perk2": 8233,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 210,
                "damageSelfMitigated": 3449,
                "magicalDamageTaken": 2903,
                "perk0Var2": 0,
                "trueDamageTaken": 82,
                "assists": 2,
                "perk4Var2": 0,
                "goldSpent": 4250,
                "trueDamageDealt": 1594,
                "participantId": 8,
                "physicalDamageDealt": 27642,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 5848,
                "physicalDamageTaken": 5676,
                "totalPlayerScore": 0,
                "win": false,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 37677,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 6,
                "wardsPlaced": 3,
                "perkPrimaryStyle": 8200,
                "perkSubStyle": 8000,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 54,
                "goldEarned": 4808,
                "killingSprees": 0,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 8,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 508,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 337,
                "totalMinionsKilled": 71,
                "timeCCingOthers": 5
            },
            "spell1Id": 4,
            "participantId": 8,
            "highestAchievedSeasonTier": "BRONZE",
            "spell2Id": 7,
            "teamId": 200,
            "timeline": {
                "lane": "NONE",
                "participantId": 8,
                "csDiffPerMinDeltas": {
                    "0-10": -1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 212.20000000000002
                },
                "xpDiffPerMinDeltas": {
                    "0-10": -70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 3.2
                },
                "xpPerMinDeltas": {
                    "0-10": 201.1
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": 82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 342.8
                }
            },
            "championId": 21
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 0,
                "visionScore": 11,
                "magicDamageDealtToChampions": 2521,
                "largestMultiKill": 0,
                "totalTimeCrowdControlDealt": 48,
                "longestTimeSpentLiving": 426,
                "perk1Var1": 765,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8347,
                "perk4": 8321,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 0,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 0,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 0,
                "damageDealtToTurrets": 0,
                "physicalDamageDealtToChampions": 854,
                "damageDealtToObjectives": 0,
                "perk2Var2": 0,
                "perk2Var3": 0,
                "totalUnitsHealed": 4,
                "perk2Var1": 6,
                "perk4Var1": 5,
                "totalDamageTaken": 8868,
                "perk4Var3": 0,
                "wardsKilled": 0,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 0,
                "quadraKills": 0,
                "magicDamageDealt": 3825,
                "firstBloodAssist": false,
                "item2": 1001,
                "item3": 0,
                "item0": 3096,
                "item1": 3107,
                "item6": 3340,
                "item4": 0,
                "item5": 0,
                "perk1": 8226,
                "perk0": 8214,
                "perk3": 8236,
                "perk2": 8234,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 8,
                "damageSelfMitigated": 3234,
                "magicalDamageTaken": 2695,
                "perk0Var2": 412,
                "trueDamageTaken": 319,
                "assists": 3,
                "perk4Var2": 0,
                "goldSpent": 3450,
                "trueDamageDealt": 118,
                "participantId": 9,
                "physicalDamageDealt": 3210,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 3494,
                "physicalDamageTaken": 5853,
                "totalPlayerScore": 0,
                "win": false,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 7154,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 5,
                "wardsPlaced": 8,
                "perkPrimaryStyle": 8200,
                "perkSubStyle": 8300,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 118,
                "goldEarned": 3756,
                "killingSprees": 0,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 8,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 287,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 4585,
                "totalMinionsKilled": 5,
                "timeCCingOthers": 11
            },
            "spell1Id": 4,
            "participantId": 9,
            "highestAchievedSeasonTier": "SILVER",
            "spell2Id": 3,
            "teamId": 200,
            "timeline": {
                "lane": "NONE",
                "participantId": 9,
                "csDiffPerMinDeltas": {
                    "0-10": -1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 171.89999999999998
                },
                "xpDiffPerMinDeltas": {
                    "0-10": -70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 0.4
                },
                "xpPerMinDeltas": {
                    "0-10": 241.8
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": 82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 400.4
                }
            },
            "championId": 267
        },
        {
            "stats": {
                "neutralMinionsKilledTeamJungle": 60,
                "visionScore": 7,
                "magicDamageDealtToChampions": 0,
                "largestMultiKill": 1,
                "totalTimeCrowdControlDealt": 15,
                "longestTimeSpentLiving": 297,
                "perk1Var1": 173,
                "perk1Var3": 0,
                "perk1Var2": 0,
                "tripleKills": 0,
                "perk5": 8135,
                "perk4": 8126,
                "playerScore9": 0,
                "playerScore8": 0,
                "kills": 3,
                "playerScore1": 0,
                "playerScore0": 0,
                "playerScore3": 0,
                "playerScore2": 0,
                "playerScore5": 0,
                "playerScore4": 0,
                "playerScore7": 0,
                "playerScore6": 0,
                "perk5Var1": 4,
                "perk5Var3": 0,
                "perk5Var2": 0,
                "totalScoreRank": 0,
                "neutralMinionsKilled": 64,
                "damageDealtToTurrets": 0,
                "physicalDamageDealtToChampions": 4473,
                "damageDealtToObjectives": 0,
                "perk2Var2": 40,
                "perk2Var3": 0,
                "totalUnitsHealed": 1,
                "perk2Var1": 14,
                "perk4Var1": 52,
                "totalDamageTaken": 16603,
                "perk4Var3": 0,
                "wardsKilled": 1,
                "largestCriticalStrike": 0,
                "largestKillingSpree": 0,
                "quadraKills": 0,
                "magicDamageDealt": 1950,
                "firstBloodAssist": false,
                "item2": 1001,
                "item3": 1037,
                "item0": 1419,
                "item1": 1043,
                "item6": 3340,
                "item4": 0,
                "item5": 0,
                "perk1": 9111,
                "perk0": 8008,
                "perk3": 8017,
                "perk2": 9104,
                "perk3Var3": 0,
                "perk3Var2": 0,
                "perk3Var1": 141,
                "damageSelfMitigated": 7291,
                "magicalDamageTaken": 5637,
                "perk0Var2": 30,
                "trueDamageTaken": 366,
                "assists": 4,
                "perk4Var2": 0,
                "goldSpent": 5250,
                "trueDamageDealt": 6196,
                "participantId": 10,
                "physicalDamageDealt": 41526,
                "sightWardsBoughtInGame": 0,
                "totalDamageDealtToChampions": 5869,
                "physicalDamageTaken": 10599,
                "totalPlayerScore": 0,
                "win": false,
                "objectivePlayerScore": 0,
                "totalDamageDealt": 49673,
                "neutralMinionsKilledEnemyJungle": 0,
                "deaths": 7,
                "wardsPlaced": 4,
                "perkPrimaryStyle": 8000,
                "perkSubStyle": 8100,
                "turretKills": 0,
                "firstBloodKill": false,
                "trueDamageDealtToChampions": 1395,
                "goldEarned": 5497,
                "killingSprees": 0,
                "unrealKills": 0,
                "firstTowerAssist": false,
                "firstTowerKill": false,
                "champLevel": 9,
                "doubleKills": 0,
                "inhibitorKills": 0,
                "perk0Var1": 0,
                "combatPlayerScore": 0,
                "perk0Var3": 0,
                "visionWardsBoughtInGame": 0,
                "pentaKills": 0,
                "totalHeal": 5181,
                "totalMinionsKilled": 3,
                "timeCCingOthers": 1
            },
            "spell1Id": 4,
            "participantId": 10,
            "highestAchievedSeasonTier": "SILVER",
            "spell2Id": 11,
            "teamId": 200,
            "timeline": {
                "lane": "NONE",
                "participantId": 10,
                "csDiffPerMinDeltas": {
                    "0-10": -1.4800000000000002
                },
                "goldPerMinDeltas": {
                    "0-10": 251.89999999999998
                },
                "xpDiffPerMinDeltas": {
                    "0-10": -70.70000000000003
                },
                "creepsPerMinDeltas": {
                    "0-10": 0
                },
                "xpPerMinDeltas": {
                    "0-10": 358.6
                },
                "role": "DUO_SUPPORT",
                "damageTakenDiffPerMinDeltas": {
                    "0-10": 82.71999999999997
                },
                "damageTakenPerMinDeltas": {
                    "0-10": 819.3
                }
            },
            "championId": 11
        }
    ],
    "gameDuration": 1010,
    "gameCreation": 1522779620165
}'

json_data_champ_info = '{
    "type": "champion",
    "version": "8.8.1",
    "data": {
        "MonkeyKing": {
            "title": "the Monkey King",
            "id": 62,
            "key": "MonkeyKing",
            "name": "Wukong"
        },
        "Jax": {
            "title": "Grandmaster at Arms",
            "id": 24,
            "key": "Jax",
            "name": "Jax"
        },
        "Fiddlesticks": {
            "title": "the Harbinger of Doom",
            "id": 9,
            "key": "Fiddlesticks",
            "name": "Fiddlesticks"
        },
        "Shaco": {
            "title": "the Demon Jester",
            "id": 35,
            "key": "Shaco",
            "name": "Shaco"
        },
        "Warwick": {
            "title": "the Uncaged Wrath of Zaun",
            "id": 19,
            "key": "Warwick",
            "name": "Warwick"
        },
        "Xayah": {
            "title": "the Rebel",
            "id": 498,
            "key": "Xayah",
            "name": "Xayah"
        },
        "Nidalee": {
            "title": "the Bestial Huntress",
            "id": 76,
            "key": "Nidalee",
            "name": "Nidalee"
        },
        "Zyra": {
            "title": "Rise of the Thorns",
            "id": 143,
            "key": "Zyra",
            "name": "Zyra"
        },
        "Kled": {
            "title": "the Cantankerous Cavalier",
            "id": 240,
            "key": "Kled",
            "name": "Kled"
        },
        "Brand": {
            "title": "the Burning Vengeance",
            "id": 63,
            "key": "Brand",
            "name": "Brand"
        },
        "Rammus": {
            "title": "the Armordillo",
            "id": 33,
            "key": "Rammus",
            "name": "Rammus"
        },
        "Illaoi": {
            "title": "the Kraken Priestess",
            "id": 420,
            "key": "Illaoi",
            "name": "Illaoi"
        },
        "Corki": {
            "title": "the Daring Bombardier",
            "id": 42,
            "key": "Corki",
            "name": "Corki"
        },
        "Braum": {
            "title": "the Heart of the Freljord",
            "id": 201,
            "key": "Braum",
            "name": "Braum"
        },
        "Darius": {
            "title": "the Hand of Noxus",
            "id": 122,
            "key": "Darius",
            "name": "Darius"
        },
        "Tryndamere": {
            "title": "the Barbarian King",
            "id": 23,
            "key": "Tryndamere",
            "name": "Tryndamere"
        },
        "MissFortune": {
            "title": "the Bounty Hunter",
            "id": 21,
            "key": "MissFortune",
            "name": "Miss Fortune"
        },
        "Yorick": {
            "title": "Shepherd of Souls",
            "id": 83,
            "key": "Yorick",
            "name": "Yorick"
        },
        "Xerath": {
            "title": "the Magus Ascendant",
            "id": 101,
            "key": "Xerath",
            "name": "Xerath"
        },
        "Sivir": {
            "title": "the Battle Mistress",
            "id": 15,
            "key": "Sivir",
            "name": "Sivir"
        },
        "Riven": {
            "title": "the Exile",
            "id": 92,
            "key": "Riven",
            "name": "Riven"
        },
        "Orianna": {
            "title": "the Lady of Clockwork",
            "id": 61,
            "key": "Orianna",
            "name": "Orianna"
        },
        "Gangplank": {
            "title": "the Saltwater Scourge",
            "id": 41,
            "key": "Gangplank",
            "name": "Gangplank"
        },
        "Malphite": {
            "title": "Shard of the Monolith",
            "id": 54,
            "key": "Malphite",
            "name": "Malphite"
        },
        "Poppy": {
            "title": "Keeper of the Hammer",
            "id": 78,
            "key": "Poppy",
            "name": "Poppy"
        },
        "Lissandra": {
            "title": "the Ice Witch",
            "id": 127,
            "key": "Lissandra",
            "name": "Lissandra"
        },
        "Jayce": {
            "title": "the Defender of Tomorrow",
            "id": 126,
            "key": "Jayce",
            "name": "Jayce"
        },
        "Nunu": {
            "title": "the Yeti Rider",
            "id": 20,
            "key": "Nunu",
            "name": "Nunu"
        },
        "Trundle": {
            "title": "the Troll King",
            "id": 48,
            "key": "Trundle",
            "name": "Trundle"
        },
        "Karthus": {
            "title": "the Deathsinger",
            "id": 30,
            "key": "Karthus",
            "name": "Karthus"
        },
        "Graves": {
            "title": "the Outlaw",
            "id": 104,
            "key": "Graves",
            "name": "Graves"
        },
        "Zoe": {
            "title": "the Aspect of Twilight",
            "id": 142,
            "key": "Zoe",
            "name": "Zoe"
        },
        "Gnar": {
            "title": "the Missing Link",
            "id": 150,
            "key": "Gnar",
            "name": "Gnar"
        },
        "Lux": {
            "title": "the Lady of Luminosity",
            "id": 99,
            "key": "Lux",
            "name": "Lux"
        },
        "Shyvana": {
            "title": "the Half-Dragon",
            "id": 102,
            "key": "Shyvana",
            "name": "Shyvana"
        },
        "Renekton": {
            "title": "the Butcher of the Sands",
            "id": 58,
            "key": "Renekton",
            "name": "Renekton"
        },
        "Fiora": {
            "title": "the Grand Duelist",
            "id": 114,
            "key": "Fiora",
            "name": "Fiora"
        },
        "Jinx": {
            "title": "the Loose Cannon",
            "id": 222,
            "key": "Jinx",
            "name": "Jinx"
        },
        "Kalista": {
            "title": "the Spear of Vengeance",
            "id": 429,
            "key": "Kalista",
            "name": "Kalista"
        },
        "Fizz": {
            "title": "the Tidal Trickster",
            "id": 105,
            "key": "Fizz",
            "name": "Fizz"
        },
        "Kassadin": {
            "title": "the Void Walker",
            "id": 38,
            "key": "Kassadin",
            "name": "Kassadin"
        },
        "Sona": {
            "title": "Maven of the Strings",
            "id": 37,
            "key": "Sona",
            "name": "Sona"
        },
        "Irelia": {
            "title": "the Blade Dancer",
            "id": 39,
            "key": "Irelia",
            "name": "Irelia"
        },
        "Viktor": {
            "title": "the Machine Herald",
            "id": 112,
            "key": "Viktor",
            "name": "Viktor"
        },
        "Rakan": {
            "title": "The Charmer",
            "id": 497,
            "key": "Rakan",
            "name": "Rakan"
        },
        "Kindred": {
            "title": "The Eternal Hunters",
            "id": 203,
            "key": "Kindred",
            "name": "Kindred"
        },
        "Cassiopeia": {
            "title": "the Serpent's Embrace",
            "id": 69,
            "key": "Cassiopeia",
            "name": "Cassiopeia"
        },
        "Maokai": {
            "title": "the Twisted Treant",
            "id": 57,
            "key": "Maokai",
            "name": "Maokai"
        },
        "Ornn": {
            "title": "The Fire below the Mountain",
            "id": 516,
            "key": "Ornn",
            "name": "Ornn"
        },
        "Thresh": {
            "title": "the Chain Warden",
            "id": 412,
            "key": "Thresh",
            "name": "Thresh"
        },
        "Kayle": {
            "title": "The Judicator",
            "id": 10,
            "key": "Kayle",
            "name": "Kayle"
        },
        "Hecarim": {
            "title": "the Shadow of War",
            "id": 120,
            "key": "Hecarim",
            "name": "Hecarim"
        },
        "Khazix": {
            "title": "the Voidreaver",
            "id": 121,
            "key": "Khazix",
            "name": "Kha'Zix"
        },
        "Olaf": {
            "title": "the Berserker",
            "id": 2,
            "key": "Olaf",
            "name": "Olaf"
        },
        "Ziggs": {
            "title": "the Hexplosives Expert",
            "id": 115,
            "key": "Ziggs",
            "name": "Ziggs"
        },
        "Syndra": {
            "title": "the Dark Sovereign",
            "id": 134,
            "key": "Syndra",
            "name": "Syndra"
        },
        "DrMundo": {
            "title": "the Madman of Zaun",
            "id": 36,
            "key": "DrMundo",
            "name": "Dr. Mundo"
        },
        "Karma": {
            "title": "the Enlightened One",
            "id": 43,
            "key": "Karma",
            "name": "Karma"
        },
        "Annie": {
            "title": "the Dark Child",
            "id": 1,
            "key": "Annie",
            "name": "Annie"
        },
        "Akali": {
            "title": "the Fist of Shadow",
            "id": 84,
            "key": "Akali",
            "name": "Akali"
        },
        "Volibear": {
            "title": "the Thunder's Roar",
            "id": 106,
            "key": "Volibear",
            "name": "Volibear"
        },
        "Yasuo": {
            "title": "the Unforgiven",
            "id": 157,
            "key": "Yasuo",
            "name": "Yasuo"
        },
        "Kennen": {
            "title": "the Heart of the Tempest",
            "id": 85,
            "key": "Kennen",
            "name": "Kennen"
        },
        "Rengar": {
            "title": "the Pridestalker",
            "id": 107,
            "key": "Rengar",
            "name": "Rengar"
        },
        "Ryze": {
            "title": "the Rune Mage",
            "id": 13,
            "key": "Ryze",
            "name": "Ryze"
        },
        "Shen": {
            "title": "the Eye of Twilight",
            "id": 98,
            "key": "Shen",
            "name": "Shen"
        },
        "Zac": {
            "title": "the Secret Weapon",
            "id": 154,
            "key": "Zac",
            "name": "Zac"
        },
        "Talon": {
            "title": "the Blade's Shadow",
            "id": 91,
            "key": "Talon",
            "name": "Talon"
        },
        "Swain": {
            "title": "the Noxian Grand General",
            "id": 50,
            "key": "Swain",
            "name": "Swain"
        },
        "Bard": {
            "title": "the Wandering Caretaker",
            "id": 432,
            "key": "Bard",
            "name": "Bard"
        },
        "Sion": {
            "title": "The Undead Juggernaut",
            "id": 14,
            "key": "Sion",
            "name": "Sion"
        },
        "Vayne": {
            "title": "the Night Hunter",
            "id": 67,
            "key": "Vayne",
            "name": "Vayne"
        },
        "Nasus": {
            "title": "the Curator of the Sands",
            "id": 75,
            "key": "Nasus",
            "name": "Nasus"
        },
        "Kayn": {
            "title": "the Shadow Reaper",
            "id": 141,
            "key": "Kayn",
            "name": "Kayn"
        },
        "TwistedFate": {
            "title": "the Card Master",
            "id": 4,
            "key": "TwistedFate",
            "name": "Twisted Fate"
        },
        "Chogath": {
            "title": "the Terror of the Void",
            "id": 31,
            "key": "Chogath",
            "name": "Cho'Gath"
        },
        "Udyr": {
            "title": "the Spirit Walker",
            "id": 77,
            "key": "Udyr",
            "name": "Udyr"
        },
        "Lucian": {
            "title": "the Purifier",
            "id": 236,
            "key": "Lucian",
            "name": "Lucian"
        },
        "Ivern": {
            "title": "the Green Father",
            "id": 427,
            "key": "Ivern",
            "name": "Ivern"
        },
        "Leona": {
            "title": "the Radiant Dawn",
            "id": 89,
            "key": "Leona",
            "name": "Leona"
        },
        "Caitlyn": {
            "title": "the Sheriff of Piltover",
            "id": 51,
            "key": "Caitlyn",
            "name": "Caitlyn"
        },
        "Sejuani": {
            "title": "Fury of the North",
            "id": 113,
            "key": "Sejuani",
            "name": "Sejuani"
        },
        "Nocturne": {
            "title": "the Eternal Nightmare",
            "id": 56,
            "key": "Nocturne",
            "name": "Nocturne"
        },
        "Zilean": {
            "title": "the Chronokeeper",
            "id": 26,
            "key": "Zilean",
            "name": "Zilean"
        },
        "Azir": {
            "title": "the Emperor of the Sands",
            "id": 268,
            "key": "Azir",
            "name": "Azir"
        },
        "Rumble": {
            "title": "the Mechanized Menace",
            "id": 68,
            "key": "Rumble",
            "name": "Rumble"
        },
        "Morgana": {
            "title": "Fallen Angel",
            "id": 25,
            "key": "Morgana",
            "name": "Morgana"
        },
        "Taliyah": {
            "title": "the Stoneweaver",
            "id": 163,
            "key": "Taliyah",
            "name": "Taliyah"
        },
        "Teemo": {
            "title": "the Swift Scout",
            "id": 17,
            "key": "Teemo",
            "name": "Teemo"
        },
        "Urgot": {
            "title": "the Dreadnought",
            "id": 6,
            "key": "Urgot",
            "name": "Urgot"
        },
        "Amumu": {
            "title": "the Sad Mummy",
            "id": 32,
            "key": "Amumu",
            "name": "Amumu"
        },
        "Galio": {
            "title": "the Colossus",
            "id": 3,
            "key": "Galio",
            "name": "Galio"
        },
        "Heimerdinger": {
            "title": "the Revered Inventor",
            "id": 74,
            "key": "Heimerdinger",
            "name": "Heimerdinger"
        },
        "Anivia": {
            "title": "the Cryophoenix",
            "id": 34,
            "key": "Anivia",
            "name": "Anivia"
        },
        "Ashe": {
            "title": "the Frost Archer",
            "id": 22,
            "key": "Ashe",
            "name": "Ashe"
        },
        "Velkoz": {
            "title": "the Eye of the Void",
            "id": 161,
            "key": "Velkoz",
            "name": "Vel'Koz"
        },
        "Singed": {
            "title": "the Mad Chemist",
            "id": 27,
            "key": "Singed",
            "name": "Singed"
        },
        "Skarner": {
            "title": "the Crystal Vanguard",
            "id": 72,
            "key": "Skarner",
            "name": "Skarner"
        },
        "Varus": {
            "title": "the Arrow of Retribution",
            "id": 110,
            "key": "Varus",
            "name": "Varus"
        },
        "Twitch": {
            "title": "the Plague Rat",
            "id": 29,
            "key": "Twitch",
            "name": "Twitch"
        },
        "Garen": {
            "title": "The Might of Demacia",
            "id": 86,
            "key": "Garen",
            "name": "Garen"
        },
        "Blitzcrank": {
            "title": "the Great Steam Golem",
            "id": 53,
            "key": "Blitzcrank",
            "name": "Blitzcrank"
        },
        "MasterYi": {
            "title": "the Wuju Bladesman",
            "id": 11,
            "key": "MasterYi",
            "name": "Master Yi"
        },
        "Elise": {
            "title": "the Spider Queen",
            "id": 60,
            "key": "Elise",
            "name": "Elise"
        },
        "Alistar": {
            "title": "the Minotaur",
            "id": 12,
            "key": "Alistar",
            "name": "Alistar"
        },
        "Katarina": {
            "title": "the Sinister Blade",
            "id": 55,
            "key": "Katarina",
            "name": "Katarina"
        },
        "Ekko": {
            "title": "the Boy Who Shattered Time",
            "id": 245,
            "key": "Ekko",
            "name": "Ekko"
        },
        "Mordekaiser": {
            "title": "the Iron Revenant",
            "id": 82,
            "key": "Mordekaiser",
            "name": "Mordekaiser"
        },
        "Lulu": {
            "title": "the Fae Sorceress",
            "id": 117,
            "key": "Lulu",
            "name": "Lulu"
        },
        "Camille": {
            "title": "the Steel Shadow",
            "id": 164,
            "key": "Camille",
            "name": "Camille"
        },
        "Aatrox": {
            "title": "the Darkin Blade",
            "id": 266,
            "key": "Aatrox",
            "name": "Aatrox"
        },
        "Draven": {
            "title": "the Glorious Executioner",
            "id": 119,
            "key": "Draven",
            "name": "Draven"
        },
        "TahmKench": {
            "title": "the River King",
            "id": 223,
            "key": "TahmKench",
            "name": "Tahm Kench"
        },
        "Pantheon": {
            "title": "the Artisan of War",
            "id": 80,
            "key": "Pantheon",
            "name": "Pantheon"
        },
        "XinZhao": {
            "title": "the Seneschal of Demacia",
            "id": 5,
            "key": "XinZhao",
            "name": "Xin Zhao"
        },
        "AurelionSol": {
            "title": "The Star Forger",
            "id": 136,
            "key": "AurelionSol",
            "name": "Aurelion Sol"
        },
        "LeeSin": {
            "title": "the Blind Monk",
            "id": 64,
            "key": "LeeSin",
            "name": "Lee Sin"
        },
        "Taric": {
            "title": "the Shield of Valoran",
            "id": 44,
            "key": "Taric",
            "name": "Taric"
        },
        "Malzahar": {
            "title": "the Prophet of the Void",
            "id": 90,
            "key": "Malzahar",
            "name": "Malzahar"
        },
        "Kaisa": {
            "title": "Daughter of the Void",
            "id": 145,
            "key": "Kaisa",
            "name": "Kai'Sa"
        },
        "Diana": {
            "title": "Scorn of the Moon",
            "id": 131,
            "key": "Diana",
            "name": "Diana"
        },
        "Tristana": {
            "title": "the Yordle Gunner",
            "id": 18,
            "key": "Tristana",
            "name": "Tristana"
        },
        "RekSai": {
            "title": "the Void Burrower",
            "id": 421,
            "key": "RekSai",
            "name": "Rek'Sai"
        },
        "Vladimir": {
            "title": "the Crimson Reaper",
            "id": 8,
            "key": "Vladimir",
            "name": "Vladimir"
        },
        "JarvanIV": {
            "title": "the Exemplar of Demacia",
            "id": 59,
            "key": "JarvanIV",
            "name": "Jarvan IV"
        },
        "Nami": {
            "title": "the Tidecaller",
            "id": 267,
            "key": "Nami",
            "name": "Nami"
        },
        "Jhin": {
            "title": "the Virtuoso",
            "id": 202,
            "key": "Jhin",
            "name": "Jhin"
        },
        "Soraka": {
            "title": "the Starchild",
            "id": 16,
            "key": "Soraka",
            "name": "Soraka"
        },
        "Veigar": {
            "title": "the Tiny Master of Evil",
            "id": 45,
            "key": "Veigar",
            "name": "Veigar"
        },
        "Janna": {
            "title": "the Storm's Fury",
            "id": 40,
            "key": "Janna",
            "name": "Janna"
        },
        "Nautilus": {
            "title": "the Titan of the Depths",
            "id": 111,
            "key": "Nautilus",
            "name": "Nautilus"
        },
        "Evelynn": {
            "title": "Agony's Embrace",
            "id": 28,
            "key": "Evelynn",
            "name": "Evelynn"
        },
        "Gragas": {
            "title": "the Rabble Rouser",
            "id": 79,
            "key": "Gragas",
            "name": "Gragas"
        },
        "Zed": {
            "title": "the Master of Shadows",
            "id": 238,
            "key": "Zed",
            "name": "Zed"
        },
        "Vi": {
            "title": "the Piltover Enforcer",
            "id": 254,
            "key": "Vi",
            "name": "Vi"
        },
        "KogMaw": {
            "title": "the Mouth of the Abyss",
            "id": 96,
            "key": "KogMaw",
            "name": "Kog'Maw"
        },
        "Ahri": {
            "title": "the Nine-Tailed Fox",
            "id": 103,
            "key": "Ahri",
            "name": "Ahri"
        },
        "Quinn": {
            "title": "Demacia's Wings",
            "id": 133,
            "key": "Quinn",
            "name": "Quinn"
        },
        "Leblanc": {
            "title": "the Deceiver",
            "id": 7,
            "key": "Leblanc",
            "name": "LeBlanc"
        },
        "Ezreal": {
            "title": "the Prodigal Explorer",
            "id": 81,
            "key": "Ezreal",
            "name": "Ezreal"
        }
    }
}'

json_data_item_info = '{
    "type": "item",
    "version": "8.8.1",
    "data": {
        "1001": {
            "plaintext": "Slightly increases Movement Speed",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +25 Movement Speed",
            "id": 1001,
            "name": "Boots of Speed"
        },
        "1004": {
            "plaintext": "Slightly increases Mana Regen",
            "description": "<stats><mana>+25% Base Mana Regen </mana></stats>",
            "id": 1004,
            "name": "Faerie Charm"
        },
        "1006": {
            "plaintext": "Slightly increases Health Regen",
            "description": "<stats>+50% Base Health Regen </stats>",
            "id": 1006,
            "name": "Rejuvenation Bead"
        },
        "1011": {
            "plaintext": "Greatly increases Health",
            "description": "<stats>+380 Health</stats>",
            "id": 1011,
            "name": "Giant's Belt"
        },
        "1018": {
            "plaintext": "Increases critical strike chance",
            "description": "<stats>+20% Critical Strike Chance</stats>",
            "id": 1018,
            "name": "Cloak of Agility"
        },
        "1026": {
            "plaintext": "Moderately increases Ability Power",
            "description": "<stats>+40 Ability Power</stats>",
            "id": 1026,
            "name": "Blasting Wand"
        },
        "1027": {
            "plaintext": "Increases Mana",
            "description": "<stats><mana>+250 Mana</mana></stats>",
            "id": 1027,
            "name": "Sapphire Crystal"
        },
        "1028": {
            "plaintext": "Increases Health",
            "description": "<stats>+150 Health</stats>",
            "id": 1028,
            "name": "Ruby Crystal"
        },
        "1029": {
            "plaintext": "Slightly increases Armor",
            "description": "<stats>+15 Armor</stats>",
            "id": 1029,
            "name": "Cloth Armor"
        },
        "1031": {
            "plaintext": "Greatly increases Armor",
            "description": "<stats>+40 Armor</stats>",
            "id": 1031,
            "name": "Chain Vest"
        },
        "1033": {
            "plaintext": "Slightly increases Magic Resist",
            "description": "<stats>+25 Magic Resist</stats>",
            "id": 1033,
            "name": "Null-Magic Mantle"
        },
        "1036": {
            "plaintext": "Slightly increases Attack Damage",
            "description": "<stats>+10 Attack Damage</stats>",
            "id": 1036,
            "name": "Long Sword"
        },
        "1037": {
            "plaintext": "Moderately increases Attack Damage",
            "description": "<stats>+25 Attack Damage</stats>",
            "id": 1037,
            "name": "Pickaxe"
        },
        "1038": {
            "plaintext": "Greatly increases Attack Damage",
            "description": "<stats>+40 Attack Damage</stats>",
            "id": 1038,
            "name": "B. F. Sword"
        },
        "1039": {
            "plaintext": "Provides damage against Monsters and Mana Regen in the Jungle",
            "description": "<stats><mana>+150% Base Mana Regen while in Jungle  </mana></stats><br><br><unique>UNIQUE Passive - Tooth:</unique> Damaging a monster with a spell or attack  steals 25 Health over 5 seconds and burns them for 20 magic damage. Killing monsters grants <font color='#99BBBB'><a href='SpecialJungleExperience'>special bonus experience</a></font>.<br><br><font color='#8C8C8C' size='16'><scaleLevel>Kindle - </scaleLevel>Burn damage increases to 50 if you have bonus health from an item or effect.",
            "id": 1039,
            "name": "Hunter's Talisman"
        },
        "1041": {
            "plaintext": "Provides damage and life steal versus Monsters",
            "description": "<stats>+10% Life Steal vs. Monsters</stats><br><br><unique>UNIQUE Passive - Nail:</unique> Basic attacks vs. Monsters deal 25 bonus damage on hit and grant you 15% bonus Attack Speed for 2 seconds. Killing monsters grants <font color='#99BBBB'><a href='SpecialJungleExperience'>special bonus experience</a></font>.",
            "id": 1041,
            "name": "Hunter's Machete"
        },
        "1042": {
            "plaintext": "Slightly increases Attack Speed",
            "description": "<stats>+12% Attack Speed</stats>",
            "id": 1042,
            "name": "Dagger"
        },
        "1043": {
            "plaintext": "Greatly increases Attack Speed",
            "description": "<stats>+25% Attack Speed</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal an additional 15 physical damage on hit.",
            "id": 1043,
            "name": "Recurve Bow"
        },
        "1051": {
            "plaintext": "Slightly increases Critical Strike Chance",
            "description": "<stats>+10% Critical Strike Chance</stats>",
            "id": 1051,
            "name": "Brawler's Gloves"
        },
        "1052": {
            "plaintext": "Slightly increases Ability Power",
            "description": "<stats>+20 Ability Power</stats>",
            "id": 1052,
            "name": "Amplifying Tome"
        },
        "1053": {
            "plaintext": "Basic attacks restore Health",
            "description": "<stats>+15 Attack Damage<br>+10% Life Steal</stats>",
            "id": 1053,
            "name": "Vampiric Scepter"
        },
        "1054": {
            "plaintext": "Good defensive starting item",
            "description": "<stats>+80 Health</stats><br><br><passive>Passive: </passive>Restores 6 Health every 5 seconds.<br><passive>Passive: </passive>Basic attacks deal an additional 5 physical damage to minions on hit.<br><unique>UNIQUE Passive:</unique> Regain an additional 20 health over 10 seconds after taking damage from an enemy champion.",
            "id": 1054,
            "name": "Doran's Shield"
        },
        "1055": {
            "plaintext": "Good starting item for attackers",
            "description": "<stats>+8 Attack Damage<br>+80 Health<br>+3% Life Steal</stats>",
            "id": 1055,
            "name": "Doran's Blade"
        },
        "1056": {
            "plaintext": "Good starting item for casters",
            "description": "<stats>+60 Health<br>+15 Ability Power<br><mana>+50% Base Mana Regen </mana></stats><br><br><mana><passive>UNIQUE Passive:</passive> Restores 4 Mana upon killing a unit.</mana>",
            "id": 1056,
            "name": "Doran's Ring"
        },
        "1057": {
            "plaintext": "Moderately increases Magic Resist",
            "description": "<stats>+40 Magic Resist</stats>",
            "id": 1057,
            "name": "Negatron Cloak"
        },
        "1058": {
            "plaintext": "Greatly increases Ability Power",
            "description": "<stats>+60 Ability Power</stats>",
            "id": 1058,
            "name": "Needlessly Large Rod"
        },
        "1082": {
            "plaintext": "Provides Ability Power and Mana.  Increases in power as you kill enemies.",
            "description": "<stats>+15 Ability Power<br>+25% Increased Healing from Potions<br><mana>+100 Mana</mana></stats><br><br><unique>UNIQUE Passive - Dread:</unique> Grants +3 Ability Power per Glory.  <br><unique>UNIQUE Passive - Do or Die:</unique> Grants 2 Glory for a champion kill or 1 Glory for an assist, up to 10 Glory total. Lose 4 Glory on death.",
            "id": 1082,
            "name": "The Dark Seal"
        },
        "1083": {
            "plaintext": "Provides damage and Life Steal on hit - Killing minions grant bonus Gold",
            "description": "<stats>+7 Attack Damage<br>+3 Life on Hit</stats><br><br><unique>UNIQUE Passive:</unique> Killing a lane minion grants 1 additional Gold. Killing 100 lane minions grants an additional 350 bonus gold immediately and disables this passive.",
            "id": 1083,
            "name": "Cull"
        },
        "1400": {
            "plaintext": "Grants Attack Damage and Cooldown Reduction",
            "description": "<stats>+60 Attack Damage<br>+10% Cooldown Reduction</stats>",
            "id": 1400,
            "name": "Enchantment: Warrior"
        },
        "1401": {
            "plaintext": "Grants Health and Immolate Aura",
            "description": "<stats>+300 Health<br>+15% Bonus Health</stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 11 (+1 per champion level) magic damage a second to nearby enemies while in combat. Deals 200% bonus damage to minions and monsters. ",
            "id": 1401,
            "name": "Enchantment: Cinderhulk"
        },
        "1402": {
            "plaintext": "Grants Ability Power and periodically empowers your Spells",
            "description": "<stats>+60 Ability Power<br>+7% Movement Speed</stats><br><br><unique>UNIQUE Passive - Echo:</unique> Gain charges upon moving or casting. At 100 charges, the next damaging spell hit expends all charges to deal 60 (+10% of Ability Power) bonus magic damage to up to 4 targets on hit.<br><br>This effect deals 250% damage to Large Monsters. Hitting a Large Monster with this effect will restore 25% of your missing Mana.",
            "id": 1402,
            "name": "Enchantment: Runic Echoes"
        },
        "1412": {
            "plaintext": "Grants Attack Damage and Cooldown Reduction",
            "description": "<stats>+60 Attack Damage<br>+10% Cooldown Reduction</stats>",
            "id": 1412,
            "name": "Enchantment: Warrior"
        },
        "1413": {
            "plaintext": "Grants Health and Immolate Aura",
            "description": "<stats>+300 Health<br>+15% Bonus Health</stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 11 (+1 per champion level) magic damage a second to nearby enemies while in combat. Deals 200% bonus damage to minions and monsters. ",
            "id": 1413,
            "name": "Enchantment: Cinderhulk"
        },
        "1414": {
            "plaintext": "Grants Ability Power and periodically empowers your Spells",
            "description": "<stats>+60 Ability Power<br>+7% Movement Speed</stats><br><br><unique>UNIQUE Passive - Echo:</unique> Gain charges upon moving or casting. At 100 charges, the next damaging spell hit expends all charges to deal 60 (+10% of Ability Power) bonus magic damage to up to 4 targets on hit.<br><br>This effect deals 250% damage to Large Monsters. Hitting a Large Monster with this effect will restore 25% of your missing Mana.",
            "id": 1414,
            "name": "Enchantment: Runic Echoes"
        },
        "1416": {
            "plaintext": "Increases Attack Speed and deals damage based on the target's Health",
            "description": "<stats>+50% Attack Speed</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal 4% of the target's maximum Health in bonus physical damage (max 75 vs. monsters and minions) on hit.",
            "id": 1416,
            "name": "Enchantment: Bloodrazor"
        },
        "1419": {
            "plaintext": "Increases Attack Speed and deals damage based on the target's Health",
            "description": "<stats>+50% Attack Speed</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal 4% of the target's maximum Health in bonus physical damage (max 75 vs. monsters and minions) on hit.",
            "id": 1419,
            "name": "Enchantment: Bloodrazor"
        },
        "2003": {
            "plaintext": "Consume to restore Health over time",
            "description": "<groupLimit>Limited to 5 at one time. Limited to 1 type of Healing Potion.</groupLimit><br><br><consumable>Click to Consume:</consumable> Restores 150 Health over 15 seconds.",
            "id": 2003,
            "name": "Health Potion"
        },
        "2004": {
            "plaintext": "Consume to restore Mana over time",
            "description": "<groupLimit>Limited to 5 at one time.</groupLimit><br><br><consumable>Click to Consume:</consumable> <mana>Restores 100 Mana over 15 seconds.</mana>",
            "id": 2004,
            "name": "Mana Potion"
        },
        "2009": {
            "description": "<consumable>Click to Consume:</consumable> Restores 80 Health and 50 Mana over 10 seconds.",
            "id": 2009,
            "name": "Total Biscuit of Rejuvenation"
        },
        "2010": {
            "description": "<consumable>Click to Consume:</consumable> Restores 15% of missing Health and Mana over 15 seconds.",
            "id": 2010,
            "name": "Total Biscuit of Everlasting Will"
        },
        "2011": {
            "description": "<consumable>Click to Consume:</consumable> Grants <font color='#29E3D6'>+1 Skill Point</font>.",
            "id": 2011,
            "name": "Elixir Of Skill"
        },
        "2012": {
            "description": "<consumable>Click to Consume:</consumable> Restores 15% of missing Health and Mana over 15 seconds.",
            "id": 2012,
            "name": "Looted Biscuit of Rejuvenation"
        },
        "2013": {
            "plaintext": "Allows champion to see invisible or unseen enemy units",
            "description": "<consumable>Click to Consume:</consumable> Grants detection of nearby invisible or unseen enemy units for 15 to 40 seconds, based on level.",
            "id": 2013,
            "name": "Looted Oracle's Extract"
        },
        "2015": {
            "plaintext": "Attack speed and a chargable magic hit",
            "description": "<stats>+15% Attack Speed</stats><br><br><passive>Passive:</passive> Moving and attacking will make an attack <a href='Energized'>Energized</a>.<br><br><unique>UNIQUE Passive - Energized Strike:</unique> Your Energized attacks deal 50 bonus magic damage on hit.",
            "id": 2015,
            "name": "Kircheis Shard"
        },
        "2031": {
            "plaintext": "Restores Health over time. Refills at shop.",
            "description": "<groupLimit>Limited to 1 type of Healing Potion.</groupLimit><br><br><active>UNIQUE Active:</active> Consumes a charge to restore 125 Health over 12 seconds. Holds up to 2 charges and refills upon visiting the shop.",
            "id": 2031,
            "name": "Refillable Potion"
        },
        "2032": {
            "plaintext": "Restores Health and Mana over time - Refills at shop and has increased capacity",
            "description": "<groupLimit>Limited to 1 type of Healing Potion.</groupLimit><br><br><active>UNIQUE Active:</active> Consumes a charge to restore 60 Health and 35 Mana over 8 seconds. Holds up to 5 charges and refills upon visiting the shop.<br><br>Killing a Large Monster grants 1 charge.<br><br><rules>(Killing a Large Monster at full charges will automatically consume the newest charge.)</rules>",
            "id": 2032,
            "name": "Hunter's Potion"
        },
        "2033": {
            "plaintext": "Restores Health and Mana over time and boosts combat power - Refills at Shop",
            "description": "<groupLimit>Limited to 1 type of Healing Potion.</groupLimit><br><br><active>UNIQUE Active:</active> Consumes a charge to restore 125 Health and 75 Mana over 12 seconds and grants <font color='#FF8811'><u>Touch of Corruption</u></font> during that time. Holds up to 3 charges that refills upon visiting the shop.<br><br><font color='#FF8811'><u>Touch of Corruption:</u></font> Damaging spells and attacks burn enemy champions for <scaleLevel>15 - 30</scaleLevel> magic damage over 3 seconds. (Half Damage for Area of Effect or Damage over Time spells. Damage increases with champion level.)<br><br><rules>(Corrupting Potion can be used even at full Health and Mana.)</rules>",
            "id": 2033,
            "name": "Corrupting Potion"
        },
        "2047": {
            "plaintext": "Allows champion to see invisible or unseen enemy units",
            "description": "<consumable>Click to Consume:</consumable> Grants detection of nearby invisible or unseen enemy units for 5 minutes.",
            "id": 2047,
            "name": "Oracle's Extract"
        },
        "2050": {
            "description": "<consumable>Click to Consume:</consumable> Places an invisible ward that reveals the surrounding area for 60 seconds.",
            "id": 2050,
            "name": "Explorer's Ward"
        },
        "2051": {
            "plaintext": "Good starting item for tanks",
            "description": "<stats>+150 Health</stats><br><br><passive>Passive: </passive>Restores 20 Health every 5 seconds.<br><unique>UNIQUE Passive:</unique> Blocks 12 damage from attacks and spells from champions (25% effectiveness vs. damage over time abilities).<br><br><groupLimit>Limited to 1 Guardian's Item.</groupLimit>",
            "id": 2051,
            "name": "Guardian's Horn"
        },
        "2052": {
            "description": "This savory blend of free-range, grass-fed Avarosan game hens and organic, non-ZMO Freljordian herbs contains the essential nutrients necessary to keep your Poro purring with pleasure.<br><br><i>All proceeds will be donated towards fighting Noxian animal cruelty.</i>",
            "id": 2052,
            "name": "Poro-Snax"
        },
        "2053": {
            "plaintext": "Enhances Movement Speed near turrets",
            "description": "<stats>+30 Armor<br>+125% Base Health Regen </stats><br><br><unique>UNIQUE Passive - Point Runner:</unique> Builds up to +20% Movement Speed over 2 seconds while near turrets, fallen turrets and Void Gates.",
            "id": 2053,
            "name": "Raptor Cloak"
        },
        "2054": {
            "description": "All the flavor of regular Poro-Snax, without the calories! Keeps your Poro happy AND healthy.<br><br><consumable>Click to Consume:</consumable> Gives your Poros a delicious healthy treat.",
            "id": 2054,
            "name": "Diet Poro-Snax"
        },
        "2055": {
            "plaintext": "Used to disable wards and invisible traps in an area.",
            "description": "<groupLimit>Can only carry 3 Control Wards in inventory.</groupLimit><br><br><consumable>Click to Consume:</consumable> Places a ward that grants vision of the surrounding area. This device will also reveal invisible traps and reveal / disable wards. Control Wards do not disable other Control Wards. Camouflaged units will also be revealed. <br><br>Limit 1 <font color='#BBFFFF'>Control Ward</font> on the map per player.",
            "id": 2055,
            "name": "Control Ward"
        },
        "2056": {
            "plaintext": "Use to temporarily provide vision in an area",
            "description": "<groupLimit>Can only carry 3 Stealth Wards in inventory.</groupLimit><br><br><consumable>Click to Consume:</consumable> Place an invisible <font color='#BBFFFF'>Stealth Ward</font> which reveals the surrounding area for <scaleLevel>60 - 120</scaleLevel> seconds.",
            "id": 2056,
            "name": "Pilfered Stealth Ward"
        },
        "2057": {
            "plaintext": "Grants increased range and reveals the targetted area",
            "description": "<consumable>Click to Consume:</consumable> Reveals an area and places a visible fragile ward up to 2000 units away. This ward is untargetable by allies.",
            "id": 2057,
            "name": "Peering Farsight Ward"
        },
        "2058": {
            "plaintext": "Temporarily increases defenses. Leaves a trail for allies to follow.",
            "description": "<consumable>Click to Consume:</consumable> Grants +150 Health, 25% Tenacity, increased champion size, and <font color='#FF8811'><u>Path of Iron</u></font> for 45 to 90 seconds, based on level.<br><br><font color='#FF8811'><u>Path of Iron:</u></font> Moving leaves a path behind that boosts allied champion's Movement Speed by 15%.<br><br><rules>(Travel Size Elixirs may stack with one another.)</rules>",
            "id": 2058,
            "name": "Travel Size Elixir of Iron"
        },
        "2059": {
            "plaintext": "Temporarily grants Ability Power and Bonus Damage to champions and turrets.",
            "description": "<consumable>Click to Consume:</consumable> Grants +25 Ability Power, 7.5 bonus Mana Regen per 5 seconds and <font color='#FF8811'><u>Sorcery</u></font> for 45 to 90 seconds, based on level. <br><br><font color='#FF8811'><u>Sorcery:</u></font> Damaging a champion or turret deals 15 bonus True Damage. This effect has a 5 second cooldown versus champions but no cooldown versus turrets.<br><br><rules>(Travel Size Elixirs may stack with one another.)</rules><br>",
            "id": 2059,
            "name": "Travel Size Elixir of Sorcery"
        },
        "2060": {
            "plaintext": "Temporarily grants Attack Damage and heals you when dealing physical damage to champions.",
            "description": "<consumable>Click to Consume:</consumable> Grants +15 Attack Damage and <font color='#FF8811'><u>Bloodlust</u></font> for 45 to 90 seconds, based on level.<br><br><font color='#FF8811'><u>Bloodlust:</u></font> Dealing physical damage to champions heals for 10% of the damage dealt.<br><br><rules>(Travel Size Elixirs may stack with one another.)</rules>",
            "id": 2060,
            "name": "Travel Size Elixir of Wrath"
        },
        "2061": {
            "plaintext": "Consume to restore Health over time",
            "description": "<consumable>Click to Consume:</consumable> Restores 50 Health over 5 seconds.",
            "id": 2061,
            "name": "Pilfered Health Potion"
        },
        "2062": {
            "plaintext": "Consume to gain a short window of power.",
            "description": "<consumable>Click to Consume:</consumable> Grants 10 (+1/Level) Adaptive Force for 45 seconds. ",
            "id": 2062,
            "name": "Pilfered Potion of Rouge"
        },
        "2065": {
            "plaintext": "Grants Health, Ability Power, Cooldown Reduction, and Movement Speed. Activate to speed up nearby allies.",
            "description": "<stats>+40 Ability Power<br>+200 Health</stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> +8% Movement Speed<br><active>UNIQUE Active:</active> Grants yourself and nearby allies +40% Movement Speed for 3 seconds. (60 second cooldown).",
            "id": 2065,
            "name": "Shurelya's Reverie"
        },
        "2138": {
            "plaintext": "Temporarily increases defenses. Leaves a trail for allies to follow.",
            "description": "<stats><levelLimit>Level 9 required to purchase.</levelLimit></stats><br><br><consumable>Click to Consume:</consumable> Grants +300 Health, 25% Tenacity, increased champion size, and <font color='#FF8811'><u>Path of Iron</u></font> for 3 minutes.<br><br><font color='#FF8811'><u>Path of Iron:</u></font> Moving leaves a path behind that boosts allied champion's Movement Speed by 15%.<br><br><rules>(Only one Elixir effect may be active at a time.)</rules>",
            "id": 2138,
            "name": "Elixir of Iron"
        },
        "2139": {
            "plaintext": "Temporarily grants Ability Power and Bonus Damage to champions and turrets.",
            "description": "<stats><levelLimit>Level 9 required to purchase.</levelLimit></stats><br><br><consumable>Click to Consume:</consumable> Grants +50 Ability Power, 15 bonus Mana Regen per 5 seconds and <font color='#FF8811'><u>Sorcery</u></font> for 3 minutes. <br><br><font color='#FF8811'><u>Sorcery:</u></font> Damaging a champion or turret deals 25 bonus True Damage. This effect has a 5 second cooldown versus champions but no cooldown versus turrets.<br><br><rules>(Only one Elixir effect may be active at a time.)</rules><br>",
            "id": 2139,
            "name": "Elixir of Sorcery"
        },
        "2140": {
            "plaintext": "Temporarily grants Attack Damage and heals you when dealing physical damage to champions.",
            "description": "<stats><levelLimit>Level 9 required to purchase.</levelLimit></stats><br><br><consumable>Click to Consume:</consumable> Grants +30 Attack Damage and <font color='#FF8811'><u>Bloodlust</u></font> for 3 minutes.<br><br><font color='#FF8811'><u>Bloodlust:</u></font> Dealing physical damage to champions heals for 15% of the damage dealt.<br><br><rules>(Only one Elixir effect may be active at a time.)</rules>",
            "id": 2140,
            "name": "Elixir of Wrath"
        },
        "2319": {
            "plaintext": "Filled with gold",
            "description": "<mainText><font color='#FF9900'>Click to Consume:</font> Contains 40-110 gold.<br><br>Can be sold for @Value@ gold.</mainText>",
            "id": 2319,
            "name": "Sly Sack of Gold"
        },
        "2403": {
            "description": "<consumable>Click to Consume:</consumable> Kill target Lane Minion (550 Range, 10 Second Cooldown).",
            "id": 2403,
            "name": "Minion Dematerializer"
        },
        "2419": {
            "description": "Transforms into a Stopwatch after 10 minutes. That Stopwatch contributes 250 gold for the items it builds into.<br><br><rules>(Stopwatch normally contributes 600 gold)</rules>",
            "id": 2419,
            "name": "Commencing Stopwatch"
        },
        "2420": {
            "plaintext": "Activate to become invincible but unable to take actions",
            "description": "<active>UNIQUE Active - Stasis:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (One time use).",
            "id": 2420,
            "name": "Stopwatch"
        },
        "2421": {
            "plaintext": "Upgrades to stopwatch",
            "description": "<unique>UNIQUE Passive:</unique> Is broken, but can still be upgraded.<br><br><rules>After breaking one Stopwatch, the shopkeeper will only sell you Broken Stopwatches.</rules>",
            "id": 2421,
            "name": "Broken Stopwatch"
        },
        "2422": {
            "plaintext": "Slightly increases Movement Speed",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +25 Movement Speed<br><br><unique>UNIQUE Passive:</unique> +10 Movement Speed<br><br>Boots that build from Slightly Magical Boots retains the +10 Movement Speed.",
            "id": 2422,
            "name": "Slightly Magical Boots"
        },
        "2423": {
            "description": "<active>UNIQUE Active - Stasis:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (One time use).",
            "id": 2423,
            "name": "Stopwatch"
        },
        "2424": {
            "description": "<unique>UNIQUE Passive:</unique> Is broken, but can still be upgraded.<br><br><rules>After breaking one Stopwatch, the shopkeeper will only sell you Broken Stopwatches.</rules>",
            "id": 2424,
            "name": "Broken Stopwatch"
        },
        "3001": {
            "plaintext": "Nearby enemies take more magic damage",
            "description": "<stats>+350 Health<br><mana>+300 Mana</mana><br>+55 Magic Resist<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Eternity:</unique> 15% of damage taken from champions is gained as Mana. Spending Mana restores 20% of the cost as Health, up to 25 per spell cast.<br><aura>UNIQUE Aura:</aura> Nearby enemy champions take 15% more magic damage.",
            "id": 3001,
            "name": "Abyssal Mask"
        },
        "3003": {
            "plaintext": "Increases Ability Power based on maximum Mana",
            "description": "<stats>+50 Ability Power<br><mana>+650 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><mana><unique>UNIQUE Passive - Awe:</unique> Grants Ability Power equal to 1% of maximum Mana. Refunds 25% of Mana spent.<br><unique>UNIQUE Passive - Mana Charge:</unique> Grants +8 maximum Mana (max +750 Mana) for each Mana expenditure (occurs up to 3 times every 12 seconds).<br><br>Transforms into Seraph's Embrace at +750 Mana.</mana>",
            "id": 3003,
            "name": "Archangel's Staff"
        },
        "3004": {
            "plaintext": "Increases Attack Damage based on maximum Mana",
            "description": "<stats>+25 Attack Damage<br><mana>+250 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Grants bonus Attack Damage equal to 2% of maximum Mana. Refunds 15% of Mana spent.<br><unique>UNIQUE Passive - Mana Charge:</unique> Grants +5 maximum Mana (max +750 Mana) for each basic attack or Mana expenditure (occurs up to 3 times every 12 seconds).<br><br>Transforms into Muramana at +750 Mana.</mana>",
            "id": 3004,
            "name": "Manamune"
        },
        "3006": {
            "plaintext": "Enhances Movement Speed and Attack Speed",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><stats> +35% Attack Speed</stats><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +45 Movement Speed",
            "id": 3006,
            "name": "Berserker's Greaves"
        },
        "3007": {
            "plaintext": "Increases Ability Power based on maximum Mana",
            "description": "<stats>+50 Ability Power<br><mana>+650 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><mana><unique>UNIQUE Passive - Awe:</unique> Grants Ability Power equal to 1% of maximum Mana. Refunds 25% of Mana spent. <br><unique>UNIQUE Passive - Mana Charge:</unique> Grants +12 maximum Mana (max +750 Mana) for each Mana expenditure (occurs up to 3 times every 12 seconds).<br><br>Transforms into Seraph's Embrace at +750 Mana.</mana>",
            "id": 3007,
            "name": "Archangel's Staff (Quick Charge)"
        },
        "3008": {
            "plaintext": "Increases Attack Damage based on maximum Mana",
            "description": "<stats>+25 Attack Damage<br><mana>+250 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Grants bonus Attack Damage equal to 2% of maximum Mana. Refunds 15% of Mana spent.<br><unique>UNIQUE Passive - Mana Charge:</unique> Grants +6 maximum Mana (max +750 Mana) for each basic attack or Mana expenditure (occurs up to 3 times every 12 seconds).<br><br>Transforms into Muramana at +750 Mana.</mana>",
            "id": 3008,
            "name": "Manamune (Quick Charge)"
        },
        "3009": {
            "plaintext": "Enhances Movement Speed and reduces the effect of slows",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +55 Movement Speed<br><unique>UNIQUE Passive - Slow Resist:</unique> Movement slowing effects are reduced by 25%.",
            "id": 3009,
            "name": "Boots of Swiftness"
        },
        "3010": {
            "plaintext": "Spend Mana to recover Health",
            "description": "<stats>+225 Health<br><mana>+300 Mana</mana></stats><br><br><unique>UNIQUE Passive - Eternity:</unique> 15% of damage taken from champions is gained as Mana. <br><br>Spending Mana restores 20% of the cost as Health, up to 15 per spell cast.  <br><br><rules>(Toggled Spells heal for a maximum of 15 per second.)</rules>",
            "id": 3010,
            "name": "Catalyst of Aeons"
        },
        "3020": {
            "plaintext": "Enhances Movement Speed and magic damage",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><stats>+18 <a href='FlatMagicPen'>Magic Penetration</a></stats><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +45 Movement Speed",
            "id": 3020,
            "name": "Sorcerer's Shoes"
        },
        "3022": {
            "plaintext": "Basic attacks slow enemies",
            "description": "<stats>+700 Health<br>+30 Attack Damage</stats><br><br><unique>UNIQUE Passive - Icy:</unique> Basic attacks slow the target's Movement Speed for 1.5 seconds on hit (40% slow for melee attacks, 20% slow for ranged attacks).",
            "id": 3022,
            "name": "Frozen Mallet"
        },
        "3024": {
            "plaintext": "Increases Armor and Cooldown Reduction",
            "description": "<stats>+20 Armor<br><mana>+250 Mana</mana></stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction",
            "id": 3024,
            "name": "Glacial Shroud"
        },
        "3025": {
            "plaintext": "Basic attacks create a slow field after spell cast",
            "description": "<stats>+65 Armor<br>+20% Cooldown Reduction<br><mana>+500 Mana</mana></stats><br><br><unique>UNIQUE Passive - Spellblade:</unique> After using an ability, the next basic attack deals bonus physical damage equal to 100% of base Attack Damage in an area and creates an icy zone for 2 seconds that slows Movement Speed by 30% (1.5 second cooldown).<br><br>Size of zone increases with bonus armor.",
            "id": 3025,
            "name": "Iceborn Gauntlet"
        },
        "3026": {
            "plaintext": "Periodically revives champion upon death",
            "description": "<stats>+40 Attack Damage<br>+30 Armor</stats><br><br><unique>UNIQUE Passive:</unique> Upon taking lethal damage, restores 50% of base Health and 30% of maximum Mana after 4 seconds of stasis (300 second cooldown).",
            "id": 3026,
            "name": "Guardian Angel"
        },
        "3027": {
            "plaintext": "Greatly increases Health, Mana, and Ability Power",
            "description": "<stats>+300 Health<br><mana>+300 Mana</mana><br>+60 Ability Power</stats><br><br><passive>Passive:</passive> Grants +20 Health, +10 Mana, and +4 Ability Power per stack (max +200 Health, +100 Mana, and +40 Ability Power). Grants 1 stack per minute (max 10 stacks).<br><unique>UNIQUE Passive - Eternity:</unique> 15% of damage taken from champions is gained as Mana. Spending Mana restores 20% of the cost as Health, up to 25 per spell cast.",
            "id": 3027,
            "name": "Rod of Ages"
        },
        "3028": {
            "plaintext": "Increases Mana and Health Regeneration",
            "description": "<stats>+30 Magic Resist<br><mana>+50% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive - Harmony:</unique> Grants bonus % Base Health Regen equal to your bonus % Base Mana Regen.</unique>",
            "id": 3028,
            "name": "Chalice of Harmony"
        },
        "3029": {
            "plaintext": "Greatly increases Health, Mana, and Ability Power",
            "description": "<stats>+300 Health<br><mana>+300 Mana</mana><br>+60 Ability Power</stats><br><br><passive>Passive:</passive> Grants +20 Health, +10 Mana, and +4 Ability Power per stack (max +200 Health, +100 Mana, and +40 Ability Power). Grants 1 stack per 40 seconds (max 10 stacks).<br><unique>UNIQUE Passive - Eternity:</unique> 15% of damage taken from champions is gained as Mana. Spending Mana restores 20% of the cost as Health, up to 25 per spell cast.",
            "id": 3029,
            "name": "Rod of Ages (Quick Charge)"
        },
        "3030": {
            "plaintext": "Activate to fire icy bolts to slow enemies",
            "description": "<stats>+80 Ability Power<br><mana>+500 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><unique>UNIQUE Active - Frost Bolt:</unique> Fires a spray of icy bolts that explode on first unit hit, dealing <scaleLevel>100 - 200</scaleLevel> (+20% of your Ability Power) magic damage to all enemies hit. (40 second cooldown, shared with other <font color='#9999FF'><a href='itembolt'>Hextech</a></font> items).<br><br> Enemies hit are slowed by 65% decaying over 1 second.",
            "id": 3030,
            "name": "Hextech GLP-800"
        },
        "3031": {
            "plaintext": "Massively enhances critical strikes",
            "description": "<stats>+70 Attack Damage<br>+20% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> Critical strike bonus damage is increased by 50%.",
            "id": 3031,
            "name": "Infinity Edge"
        },
        "3033": {
            "plaintext": "Overcomes enemies with high Health recovery and Armor",
            "description": "<stats>+50 Attack Damage</stats><br><br><unique>UNIQUE Passive - Executioner:</unique> Physical damage inflicts <a href='GrievousWounds'>Grievous Wounds</a> on enemy champions for 5 seconds.<br><unique>UNIQUE Passive - Last Whisper:</unique> +35% <a href='BonusArmorPen'>Bonus Armor Penetration</a>.",
            "id": 3033,
            "name": "Mortal Reminder"
        },
        "3034": {
            "plaintext": "Overcomes enemies with high Health",
            "description": "<stats>+10 Attack Damage</stats><br><br><unique>UNIQUE Passive - Giant Slayer:</unique> Grants up to +10% physical damage against enemy champions with greater maximum Health than you (+1% damage per 200 Health difference, maxing at 2000 Health difference).<br><br><rules>(Unique Passives with the same name don't stack.)</rules>",
            "id": 3034,
            "name": "Giant Slayer"
        },
        "3035": {
            "plaintext": "Overcomes enemies with high Armor",
            "description": "<stats>+10 Attack Damage</stats><br><br><unique>UNIQUE Passive - Last Whisper:</unique> +35% <a href='BonusArmorPen'>Bonus Armor Penetration</a>",
            "id": 3035,
            "name": "Last Whisper"
        },
        "3036": {
            "plaintext": "Overcomes enemies with high health and armor",
            "description": "<stats>+50 Attack Damage</stats><br><br><unique>UNIQUE Passive - Giant Slayer:</unique> Grants up to +20% physical damage against enemy champions with greater maximum Health than you (+2% damage per 200 Health difference, maxing at 2000 Health difference).<br><unique>UNIQUE Passive - Last Whisper:</unique> +35% <a href='BonusArmorPen'>Bonus Armor Penetration</a>",
            "id": 3036,
            "name": "Lord Dominik's Regards"
        },
        "3040": {
            "description": "<stats>+50 Ability Power<br><mana>+1400 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><mana><unique>UNIQUE Passive - Awe:</unique> Grants Ability Power equal to 3% of maximum Mana. Refunds 25% of Mana spent.</mana><br><active>UNIQUE Active - Mana Shield:</active> Consumes 15% of current Mana to grant a shield for 2 seconds that absorbs damage equal to 150 plus the amount of Mana consumed (120 second cooldown).",
            "id": 3040,
            "name": "Seraph's Embrace"
        },
        "3041": {
            "plaintext": "Grants Ability Power for kills and assists",
            "description": "<stats>+20 Ability Power<br><mana>+200 Mana</mana></stats><br><br><unique>UNIQUE Passive - Dread:</unique> Grants +5 Ability Power per Glory. Grants 10% Movement Speed if you have at least 15 Glory.<br><unique>UNIQUE Passive - Do or Die:</unique> Grants 4 Glory for a champion kill or 2 Glory for an assist, up to 25 Glory total. Lose 10 stacks of Glory upon dying.",
            "id": 3041,
            "name": "Mejai's Soulstealer"
        },
        "3042": {
            "description": "<stats>+25 Attack Damage<br><mana>+1000 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Grants bonus Attack Damage equal to 2% of maximum Mana. Refunds 15% of Mana spent.</mana><br><mana><unique>UNIQUE Passive - Shock:</unique> Single target spells and attacks (on hit) on <font color='#FFFFFF'>Champions</font> consume 3% of current Mana to deal bonus physical damage equal to twice the amount of Mana consumed.<br><br>This effect only activates while you have greater than 20% maximum Mana.</mana>",
            "id": 3042,
            "name": "Muramana"
        },
        "3043": {
            "description": "<stats>+25 Attack Damage<br><mana>+1000 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Grants bonus Attack Damage equal to 2% of maximum Mana. Refunds 15% of Mana spent.</mana><br><mana><unique>UNIQUE Passive - Shock:</unique> Single target spells and attacks (on hit) on <font color='#FFFFFF'>Champions</font> consume 3% of current Mana to deal bonus physical damage equal to twice the amount of Mana consumed.<br><br>This effect only activates while you have greater than 20% maximum Mana.</mana>",
            "id": 3043,
            "name": "Muramana"
        },
        "3044": {
            "plaintext": "Attacks and kills give a small burst of speed",
            "description": "<stats>+200 Health<br>+15 Attack Damage</stats><br><br><unique>UNIQUE Passive - Rage:</unique> Basic attacks grant 20 Movement Speed for 2 seconds. Kills grant 60 Movement Speed instead. This Movement Speed bonus is halved for ranged champions.",
            "id": 3044,
            "name": "Phage"
        },
        "3046": {
            "plaintext": "Move faster near enemies and reduce incoming damage",
            "description": "<stats>+45% Attack Speed<br>+30% Critical Strike Chance<br>+5% Movement Speed</stats><br><br><unique>UNIQUE Passive - Spectral Waltz:</unique> While within 550 units of an enemy champion you can see, +7% Movement Speed and you can move through units.<br><unique>UNIQUE Passive - Lament:</unique> The last champion hit deals 12% less damage to you (ends after 10 seconds of not hitting).",
            "id": 3046,
            "name": "Phantom Dancer"
        },
        "3047": {
            "plaintext": "Enhances Movement Speed and reduces incoming basic attack damage",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><stats>+20 Armor</stats><br><br><unique>UNIQUE Passive:</unique> Blocks 12% of the damage from basic attacks.<br><unique>UNIQUE Passive - Enhanced Movement:</unique> +45 Movement Speed",
            "id": 3047,
            "name": "Ninja Tabi"
        },
        "3048": {
            "description": "<stats>+50 Ability Power<br><mana>+1400 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><mana><unique>UNIQUE Passive - Awe:</unique> Grants Ability Power equal to 3% of maximum Mana. Refunds 25% of Mana spent.</mana><br><active>UNIQUE Active - Mana Shield:</active> Consumes 15% of current Mana to grant a shield for 2 seconds that absorbs damage equal to 150 plus the amount of Mana consumed (120 second cooldown).",
            "id": 3048,
            "name": "Seraph's Embrace"
        },
        "3050": {
            "plaintext": "Grants you and your ally bonuses when you cast your ultimate.",
            "description": "<stats>+60 Armor<br>+30 Magic Resist<br><mana>+250 Mana</mana><br>+10% Cooldown Reduction</stats><br><mainText><active>UNIQUE Active - Conduit:</active> Bind to an ally without an existing Conduit.<br><unique>UNIQUE Passive:</unique> Casting your ultimate near your ally surrounds you with a frost storm and ignites your ally's basic attacks for 10 seconds. Enemies inside your frost storm are slowed by 20% and your ally's attacks burn their target for 50% bonus magic damage over 2 seconds (45 second cooldown).<br><br><unlockedPassive>Frostfire Covenant:</unlockedPassive> Your frost storm ignites when it slows a burning enemy, dealing 40 magic damage per second and slowing by 40% instead for 3 seconds.</maintext><br><br><rules>(Champions can only be linked by one Zeke's Convergence at a time.)</rules>",
            "id": 3050,
            "name": "Zeke's Convergence"
        },
        "3052": {
            "plaintext": "Attack Damage and stacking Health on Unit Kill",
            "description": "<stats>+15 Attack Damage<br>+200 Health</stats><br><br><unique>UNIQUE Passive:</unique> Killing a unit grants 5 maximum Health. This bonus stacks up to 20 times.",
            "id": 3052,
            "name": "Jaurim's Fist"
        },
        "3053": {
            "plaintext": "Shields against large bursts of damage",
            "description": "<stats>+450 Health</stats><br><br><unique>UNIQUE Passive:</unique> +50% Base Attack Damage <br><unique>UNIQUE Passive - Lifeline:</unique> Upon taking at least 400 to 1800 damage (based on level) within 5 seconds, gain a shield for 75% of your bonus Health. After 0.75 seconds, the shield decays over 3 seconds (60 second cooldown).<br><br><unlockedPassive>Sterak's Fury:</unlockedPassive> When <i>Lifeline</i> triggers, grow in size and strength, gaining +30% Tenacity for 8 seconds.",
            "id": 3053,
            "name": "Sterak's Gage"
        },
        "3056": {
            "plaintext": "Temporarily disables enemy turrets",
            "description": "<stats>+300 Health<br>+50 Armor<br>+150% Base Health Regen <br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active:</active> Prevents nearby enemy turrets from attacking for 3 seconds (120 second cooldown). This effect cannot be used against the same turret more than once every 8 seconds.<br><br><unique>UNIQUE Passive - Point Runner:</unique> Builds up to +20% Movement Speed over 2 seconds while near turrets (including fallen turrets) and Void Gates.",
            "id": 3056,
            "name": "Ohmwrecker"
        },
        "3057": {
            "plaintext": "Grants a bonus to next attack after spell cast",
            "description": "<stats><mana>+250 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Spellblade:</unique> After using an ability, the next basic attack deals bonus physical damage equal to 100% base Attack Damage on hit (1.5 second cooldown).",
            "id": 3057,
            "name": "Sheen"
        },
        "3060": {
            "plaintext": "Promotes a siege minion to a more powerful unit",
            "description": "<stats>+60 Armor<br>+30 Magic Resist<br>+125% Base Health Regen <br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active - Promote:</active> Greatly increases the power of a lane minion and grants it immunity to magic damage (120 second cooldown).<br><unique>UNIQUE Passive - Point Runner:</unique> Builds up to +20% Movement Speed over 2 seconds while near turrets, fallen turrets and Void Gates.",
            "id": 3060,
            "name": "Banner of Command"
        },
        "3065": {
            "plaintext": "Increases Health and healing effects",
            "description": "<stats>+450 Health<br>+55 Magic Resist<br>+100% Base Health Regen <br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Increases all healing received by 30%.",
            "id": 3065,
            "name": "Spirit Visage"
        },
        "3067": {
            "plaintext": "Increases Health and Cooldown Reduction",
            "description": "<stats>+200 Health  </stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction",
            "id": 3067,
            "name": "Kindlegem"
        },
        "3068": {
            "plaintext": "Constantly deals damage to nearby enemies",
            "description": "<stats>+425 Health<br>+60 Armor  </stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 25 (+1 per champion level) magic damage per second to nearby enemies. Deals 50% bonus damage to minions and monsters.",
            "id": 3068,
            "name": "Sunfire Cape"
        },
        "3069": {
            "plaintext": "Provides Gold, Mana, and Stealth Wards over time",
            "description": "<stats>+200 Health<br>+10 Movement Speed<br>+125% Base Health Regen <br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Favor: </unique>Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>45</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 4 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><rules><font color='#447777'>''Praise the sun.'' - Historian Shurelya, 22 September, 25 CLE</font></rules>",
            "id": 3069,
            "name": "Remnant of the Ascended"
        },
        "3070": {
            "plaintext": "Increases maximum Mana as Mana is spent",
            "description": "<stats><mana>+250 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Refunds 15% of Mana spent.<br><unique>UNIQUE Passive - Mana Charge:</unique> Grants 4 maximum Mana on Mana expenditure (up to 3 times per 12 seconds).<br><br>Caps at +750 Mana.</mana>",
            "id": 3070,
            "name": "Tear of the Goddess"
        },
        "3071": {
            "plaintext": "Dealing physical damage to enemy champions reduces their Armor",
            "description": "<stats>+400 Health<br>+40 Attack Damage<br>+20% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Dealing physical damage to an enemy champion Cleaves them, reducing their Armor by 4% for 6 seconds (stacks up to 6 times, up to 24%).<br><unique>UNIQUE Passive - Rage:</unique> Dealing physical damage grants 20 movement speed for 2 seconds. Assists on Cleaved enemy champions or kills on any unit grant 60 movement speed for 2 seconds instead. This Movement Speed is halved for ranged champions.",
            "id": 3071,
            "name": "The Black Cleaver"
        },
        "3072": {
            "plaintext": "Grants Attack Damage, Life Steal and Life Steal now overheals",
            "description": "<stats>+80 Attack Damage</stats><br><br><unique>UNIQUE Passive:</unique> +20% Life Steal<br><unique>UNIQUE Passive:</unique> Your basic attacks can now overheal you. Excess life is stored as a shield that can block 50-350 damage, based on champion level.<br><br>This shield decays slowly if you haven't dealt or taken damage in the last 25 seconds.",
            "id": 3072,
            "name": "The Bloodthirster"
        },
        "3073": {
            "plaintext": "Increases maximum Mana as Mana is spent",
            "description": "<stats><mana>+250 Mana</mana></stats><br><br><mana><unique>UNIQUE Passive - Awe:</unique> Refunds 15% of Mana spent.<br><unique>UNIQUE Passive - Mana Charge:</unique> Grants 6 maximum Mana on Mana expenditure (up to 3 times per 12 seconds).<br><br>Caps at +750 Mana.</mana>",
            "id": 3073,
            "name": "Tear of the Goddess (Quick Charge)"
        },
        "3074": {
            "plaintext": "Melee attacks hit nearby enemies, dealing damage and restoring Health",
            "description": "<stats>+80 Attack Damage<br>+100% Base Health Regen <br>+12% Life Steal</stats><br><br><passive>Passive:</passive> 50% of total Life Steal applies to damage dealt by this item.<br><unique>UNIQUE Passive - Cleave:</unique> Basic attacks deal 20% to 60% of total Attack Damage as bonus physical damage to enemies near the target on hit (enemies closest to the target take the most damage).<br><active>UNIQUE Active - Crescent:</active> Deals 60% to 100% of total Attack Damage as physical damage to nearby enemy units (closest enemies take the most damage) (10 second cooldown).",
            "id": 3074,
            "name": "Ravenous Hydra"
        },
        "3075": {
            "plaintext": "Returns damage taken from basic attacks as magic damage",
            "description": "<stats>+250 Health<br>+80 Armor</stats><br><br><unique>UNIQUE Passive - Thorns:</unique> Upon being hit by a basic attack, reflects magic damage equal to 10% of your bonus Armor plus 25, inflicting <a href='GrievousWounds'>Grievous Wounds</a> on the attacker for 1 second.<br><unique>UNIQUE Passive - Cold Steel:</unique> When hit by basic attacks, reduces the attacker's Attack Speed by 15% for 1 second.",
            "id": 3075,
            "name": "Thornmail"
        },
        "3076": {
            "plaintext": "Prevents enemies from using Life Steal against you.",
            "description": "<stats>+35 Armor</stats><br><br><unique>UNIQUE Passive - Thorns:</unique> Upon being hit by a basic attack, reflects magic damage equal to 3 plus 10% of your bonus Armor, inflicting <a href='GrievousWounds'>Grievous Wounds</a> on the attacker for 1 second.",
            "id": 3076,
            "name": "Bramble Vest"
        },
        "3077": {
            "plaintext": "Melee attacks hit nearby enemies",
            "description": "<stats>+25 Attack Damage<br>+50% Base Health Regen </stats><br><br><unique>UNIQUE Passive - Cleave:</unique> Basic attacks deal 20% to 60% of total Attack Damage as bonus physical damage to enemies near the target on hit (enemies closest to the target take the most damage).<br><active>UNIQUE Active - Crescent:</active> Deals 60% to 100% of total Attack Damage as physical damage to nearby enemy units (enemies closest to the target take the most damage) (10 second cooldown).",
            "id": 3077,
            "name": "Tiamat"
        },
        "3078": {
            "plaintext": "Tons of Damage",
            "description": "<stats>+250 Health<br><mana>+250 Mana</mana><br>+25 Attack Damage<br>+40% Attack Speed<br>+20% Cooldown Reduction<br>+5% Movement Speed</stats><br><br><unique>UNIQUE Passive - Rage:</unique> Basic attacks grant 20 Movement Speed for 2 seconds. Kills grant 60 Movement Speed instead. This Movement Speed bonus is halved for ranged champions.<br><unique>UNIQUE Passive - Spellblade:</unique> After using an ability, the next basic attack deals bonus physical damage equal to 200% of base Attack Damage on hit (1.5 second cooldown).",
            "id": 3078,
            "name": "Trinity Force"
        },
        "3082": {
            "plaintext": "Slows Attack Speed of enemy champions when receiving basic attacks",
            "description": "<stats>+40 Armor</stats><br><br><unique>UNIQUE Passive - Cold Steel:</unique> When hit by basic attacks, reduces the attacker's Attack Speed by 15% for 1 seconds.",
            "id": 3082,
            "name": "Warden's Mail"
        },
        "3083": {
            "plaintext": "Grants massive Health and Health Regen",
            "description": "<stats>+800 Health<br>+200% Base Health Regen </stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> Grants <unlockedPassive>Warmog's Heart</unlockedPassive> if you have at least 3000 maximum Health.<br><br><unlockedPassive>Warmog's Heart:</unlockedPassive> Restores 25% of maximum Health every 5 seconds if damage hasn't been taken within 6 seconds (3 seconds for damage from minions and monsters).",
            "id": 3083,
            "name": "Warmog's Armor"
        },
        "3084": {
            "plaintext": "Restores Health on kill or assist",
            "description": "<stats>+800 Health<br>+100% Base Health Regen </stats><br><br><unique>UNIQUE Passive:</unique> Upon champion kill or assist, restores 300 Health over 5 seconds.",
            "id": 3084,
            "name": "Overlord's Bloodmail"
        },
        "3085": {
            "plaintext": "Ranged attacks fire two bolts at nearby enemies",
            "description": "<stats>+40% Attack Speed<br>+30% Critical Strike Chance<br>+7% Movement Speed</stats><br><br><unique>UNIQUE Passive - Wind's Fury:</unique> When basic attacking, bolts are fired at up to 2 enemies near the target, each dealing (40% of Attack Damage) physical damage. Bolts can critically strike and apply on hit effects.",
            "id": 3085,
            "name": "Runaan's Hurricane"
        },
        "3086": {
            "plaintext": "Slight bonuses to Critical Strike Chance, Movement Speed and Attack Speed",
            "description": "<stats>+15% Attack Speed<br>+20% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> +5% Movement Speed",
            "id": 3086,
            "name": "Zeal"
        },
        "3087": {
            "plaintext": "Movement builds charges that release chain lightning on basic attack",
            "description": "<stats>+35% Attack Speed<br>+30% Critical Strike Chance<br>+5% Movement Speed</stats><br><br><passive>Passive:</passive> Moving and attacking will make an attack <a href='Energized'>Energized</a>.<br><br><unique>UNIQUE Passive - Shiv Lightning:</unique> Your Energized attacks deal 60~140 bonus magic damage (based on level) to up to 5 targets on hit. This effect can critically strike.",
            "id": 3087,
            "name": "Statikk Shiv"
        },
        "3089": {
            "plaintext": "Massively increases Ability Power",
            "description": "<stats>+120 Ability Power  </stats><br><br><unique>UNIQUE Passive:</unique> Increases Ability Power by 40%.",
            "id": 3089,
            "name": "Rabadon's Deathcap"
        },
        "3090": {
            "plaintext": "Massively increases Ability Power and can be activated to enter stasis",
            "description": "<stats>+100 Ability Power<br>+45 Armor  </stats><br><br><unique>UNIQUE Passive:</unique> Increases Ability Power by 25%<br><active>UNIQUE Active:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (120 second cooldown).",
            "id": 3090,
            "name": "Wooglet's Witchcap"
        },
        "3091": {
            "plaintext": "Deals bonus magic damage on basic attacks",
            "description": "<stats>+40% Attack Speed<br>+40 Magic Resist</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal 42 bonus magic damage on hit.<br><unique>UNIQUE Passive:</unique> Basic attacks steal 3 Magic Resist from the target on hit (6 if the attacker is melee), up to a maximum of 30 Magic Resist.",
            "id": 3091,
            "name": "Wit's End"
        },
        "3092": {
            "plaintext": "Provides Ability Power and Stealth Wards over time",
            "description": "<stats>+200 Health<br>+35 Ability Power<br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds<br><mana>+50% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 18 additional magic damage and grant 20 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 4 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3092,
            "name": "Remnant of the Watchers"
        },
        "3094": {
            "plaintext": "Movement builds charges that release a sieging fire attack on release",
            "description": "<stats>+30% Attack Speed<br>+30% Critical Strike Chance<br>+5% Movement Speed</stats><br><br><passive>Passive:</passive> Moving and attacking will make an attack <a href='Energized'>Energized</a>.<br><br><unique>UNIQUE Passive - Firecannon:</unique> Your Energized attacks gain 35% bonus Range (+150 range maximum) and deal 60~140 bonus magic damage (based on level) on hit.<br><br>Attacks become Energized 25% faster. Energized attacks function on structures.",
            "id": 3094,
            "name": "Rapid Firecannon"
        },
        "3096": {
            "plaintext": "Grants gold and mana when nearby minions die that you didn't kill",
            "description": "<stats>+10 Movement Speed<br>+50% Base Health Regen <br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Favor:</unique> Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>45</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><rules><font color='#447777'>''The medallion shines with the glory of a thousand voices when exposed to the sun.'' - Historian Shurelya, 22 June, 24 CLE</font></rules>",
            "id": 3096,
            "name": "Nomad's Medallion"
        },
        "3097": {
            "plaintext": "Periodically kill enemy minions to heal and grant gold to a nearby ally",
            "description": "<stats>+125 Health<br>+50% Base Health Regen <br>+1 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 200 (+10 per level) Health. Killing a minion heals the owner and the nearest allied champion for 40 Health (+2% missing health) and grants them kill Gold. 50% healing if the owner is ranged. These effects require a nearby ally. Recharges every 30 seconds. Max 3 charges.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3097,
            "name": "Targon's Brace"
        },
        "3098": {
            "plaintext": "Grants gold when you damage an enemy",
            "description": "<stats>+20 Ability Power<br>+2 Gold per 10 seconds<br><mana>+50% Base Mana Regen </mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 18 additional magic damage and grant 20 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3098,
            "name": "Frostfang"
        },
        "3100": {
            "plaintext": "Grants a bonus to next attack after spell cast",
            "description": "<stats>+80 Ability Power<br>+7% Movement Speed<br>+10% Cooldown Reduction<br><mana>+250 Mana</mana></stats><br><br><unique>UNIQUE Passive - Spellblade:</unique> After using an ability, the next basic attack deals 75% Base Attack Damage (+50% of Ability Power) bonus magic damage on hit (1.5 second cooldown).",
            "id": 3100,
            "name": "Lich Bane"
        },
        "3101": {
            "plaintext": "Increased Attack Speed and Cooldown Reduction",
            "description": "<stats>+35% Attack Speed</stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction",
            "id": 3101,
            "name": "Stinger"
        },
        "3102": {
            "plaintext": "Periodically blocks enemy abilities",
            "description": "<stats>+70 Ability Power<br>+60 Magic Resist<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Grants a spell shield that blocks the next enemy ability. This shield refreshes after no damage is taken from enemy champions for 40 seconds.",
            "id": 3102,
            "name": "Banshee's Veil"
        },
        "3104": {
            "plaintext": "Reduces Armor of nearby enemies",
            "description": "<stats>+300 Health<br>+50 Attack Damage<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Ashes to Ashes:</unique> Controlling the nearest Altar sets you aflame, dealing 25 (+1 per champion level) magic damage per second to nearby enemies (Deals 50% bonus damage to minions and monsters). Controlling the furthest Altar causes your basic attacks to burn targets for up to 114 true damage (based on champion level) over 3 seconds.",
            "id": 3104,
            "name": "Lord Van Damm's Pillager"
        },
        "3105": {
            "plaintext": "Grants Armor and Magic Resistance",
            "description": "<stats>+30 Armor<br>+30 Magic Resist</stats>",
            "id": 3105,
            "name": "Aegis of the Legion"
        },
        "3107": {
            "plaintext": "Activate to heal allies and damage enemies in an area",
            "description": "<stats>+200 Health<br>+50% Base Health Regen <br><mana>+150% Base Mana Regen </mana><br>+10% Cooldown Reduction</stats><br><br><passive>UNIQUE Passive:</passive> +10% Heal and Shield Power<br><active>UNIQUE Active:</active> Target an area within 5500 range. After 2.5 seconds, call down a beam of light to heal allies for 10 (+20 per level of target) Health, burn enemy champions for 10% of their maximum Health as <font color='#FFFFFF'>true</font> damage and deal 250 <font color='#FFFFFF'>true</font> damage to enemy minions (120 second cooldown). Heal and Shield Power is 3 times as effective on Redemption's heal.<br><br>Can be used while dead.<br><br><rules>Half effect if the target has been affected by another Redemption recently.</rules>",
            "id": 3107,
            "name": "Redemption"
        },
        "3108": {
            "plaintext": "Increases Ability Power and Cooldown Reduction",
            "description": "<stats>+30 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction",
            "id": 3108,
            "name": "Fiendish Codex"
        },
        "3109": {
            "plaintext": "Partner with an ally to protect each other",
            "description": "<stats>+250 Health<br>+40 Armor<br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active:</active> Designate an allied champion as your <a href='KnightsVowPartner'>Partner</a> (90 second cooldown).<br><passive>UNIQUE Passive:</passive> If your <a href='KnightsVowPartner'>Partner</a> is nearby, gain +20 additional Armor and +15% Movement Speed towards them.<br><passive>UNIQUE Passive:</passive> If your <a href='KnightsVowPartner'>Partner</a> is nearby, heal for 12% of the damage your <a href='KnightsVowPartner'>Partner</a> deals to champions and redirect 12% of the damage your <a href='KnightsVowPartner'>Partner</a> takes from champions to you as <font color='#FFFFFF'>true</font> damage (healing and damage redirection are reduced by 50% if you are ranged).<br><br><rules>(Champions can only be linked by one Knight's Vow at a time.)</rules>",
            "id": 3109,
            "name": "Knight's Vow"
        },
        "3110": {
            "plaintext": "Massively increases Armor and slows enemy basic attacks",
            "description": "<stats>+100 Armor<br>+20% Cooldown Reduction<br><mana>+400 Mana</mana></stats><br><br><aura>UNIQUE Aura:</aura> Reduces the Attack Speed of nearby enemies by 15%.",
            "id": 3110,
            "name": "Frozen Heart"
        },
        "3111": {
            "plaintext": "Increases Movement Speed and reduces duration of disabling effects",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><stats>+25 Magic Resist</stats><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +45 Movement Speed<br><unique>UNIQUE Passive - Tenacity:</unique> Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 30%.",
            "id": 3111,
            "name": "Mercury's Treads"
        },
        "3112": {
            "plaintext": "Good starting item for mages",
            "description": "<stats>+150 Health<br>+35 Ability Power<br><mana>+10 Mana regen per 5 seconds</mana></stats><br><br><groupLimit>Limited to 1 Guardian's Item.</groupLimit>",
            "id": 3112,
            "name": "Guardian's Orb"
        },
        "3113": {
            "plaintext": "Increases Ability Power and Movement Speed",
            "description": "<stats>+30 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> +5% Movement Speed",
            "id": 3113,
            "name": "Aether Wisp"
        },
        "3114": {
            "plaintext": "Increases Mana Regeneration and Cooldown Reduction",
            "description": "<stats><mana>+50% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> +8% Heal and Shield Power",
            "id": 3114,
            "name": "Forbidden Idol"
        },
        "3115": {
            "plaintext": "Increases Attack Speed, Ability Power, and Cooldown Reduction",
            "description": "<stats>+50% Attack Speed<br>+80 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> +20% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> Basic attacks deal 15 (+15% of Ability Power) bonus magic damage on hit.<br>",
            "id": 3115,
            "name": "Nashor's Tooth"
        },
        "3116": {
            "plaintext": "Abilities slow enemies",
            "description": "<stats>+300 Health<br>+85 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> Damaging spells and abilities reduce enemy movement speed by 20% for 1 second.",
            "id": 3116,
            "name": "Rylai's Crystal Scepter"
        },
        "3117": {
            "plaintext": "Greatly enhances Movement Speed when out of combat",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><unique>UNIQUE Passive - Enhanced Movement:</unique> +25 Movement Speed. Increases to +115 Movement Speed when out of combat for 5 seconds.",
            "id": 3117,
            "name": "Boots of Mobility"
        },
        "3122": {
            "plaintext": "Critical Strikes cause your target to bleed",
            "description": "<stats>+20 Attack Damage<br>+10% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> Critical Strikes cause your target to bleed for an additional 60% of your bonus Attack Damage as magic damage over 3 seconds.",
            "id": 3122,
            "name": "Wicked Hatchet"
        },
        "3123": {
            "plaintext": "Overcomes enemies with high health gain",
            "description": "<stats>+15 Attack Damage</stats><br><br><unique>UNIQUE Passive - Executioner:</unique> Physical damage inflicts <a href='GrievousWounds'>Grievous Wounds</a> on enemy champions for 3 seconds.",
            "id": 3123,
            "name": "Executioner's Calling"
        },
        "3124": {
            "plaintext": "Increases Attack Speed, Attack Damage, and Ability Power",
            "description": "<stats>+25 Attack Damage<br>+25 Ability Power<br>+25% Attack Speed</stats><br><br><passive>Passive: </passive>Basic attacks deal 5 (+10% Bonus Attack Damage) physical and 5 (+10% Ability Power) magic damage on hit.<br><unique>UNIQUE Passive:</unique> Basic attacks grant +8% Attack Speed, +4% Bonus Attack Damage, and +4% Ability Power for 5 seconds (up to 6 stacks). At max stacks, gain <unlockedPassive>Guinsoo's Rage</unlockedPassive>.<br><br><unlockedPassive>Guinsoo's Rage:</unlockedPassive> Every other basic attack triggers on hit effects twice.<br><br><rules><font color='#8c8c8c'>While at half stacks, melee champions' next attack will fully stack Rageblade.</font></rules>",
            "id": 3124,
            "name": "Guinsoo's Rageblade"
        },
        "3133": {
            "plaintext": "Attack Damage and Cooldown Reduction",
            "description": "<stats>+25 Attack Damage</stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction",
            "id": 3133,
            "name": "Caulfield's Warhammer"
        },
        "3134": {
            "plaintext": "Increases Attack Damage and Lethality",
            "description": "<stats>+25 Attack Damage</stats><br><br><unique>UNIQUE Passive:</unique> +10 <a href='Lethality'>Lethality</a><br><unique>UNIQUE Passive - Headhunter:</unique> After killing any enemy, your next damaging spell will deal 40 bonus physical damage (30 second cooldown).",
            "id": 3134,
            "name": "Serrated Dirk"
        },
        "3135": {
            "plaintext": "Increases magic damage",
            "description": "<stats>+70 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> +40% <a href='TotalMagicPen'>Magic Penetration</a>.",
            "id": 3135,
            "name": "Void Staff"
        },
        "3136": {
            "plaintext": "Increases magic damage",
            "description": "<stats>+35 Ability Power<br>+200 Health</stats><br><br><unique>UNIQUE Passive - Madness:</unique> Deal 2% more damage for each second in combat with champions (10% maximum).",
            "id": 3136,
            "name": "Haunting Guise"
        },
        "3137": {
            "plaintext": "Activate to remove all debuffs and grant massive Movement Speed",
            "description": "<stats>+50% Attack Speed<br>+45 Magic Resist<br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active - Quicksilver:</active> Removes all debuffs, and if the champion is melee, also grants +50% bonus Movement Speed for 1 second (90 second cooldown).",
            "id": 3137,
            "name": "Dervish Blade"
        },
        "3139": {
            "plaintext": "Activate to remove all crowd control debuffs and grant massive Movement Speed",
            "description": "<stats>+65 Attack Damage<br>+35 Magic Resist<br>+10% Life Steal</stats><br><br><active>UNIQUE Active - Quicksilver:</active> Removes all crowd control debuffs and also grants +50% bonus Movement Speed for 1 second (90 second cooldown).",
            "id": 3139,
            "name": "Mercurial Scimitar"
        },
        "3140": {
            "plaintext": "Activate to remove all crowd control debuffs",
            "description": "<stats>+30 Magic Resist</stats><br><br><active>UNIQUE Active - Quicksilver:</active> Removes all crowd control debuffs (90 second cooldown).",
            "id": 3140,
            "name": "Quicksilver Sash"
        },
        "3142": {
            "plaintext": "Activate to greatly increase Movement Speed",
            "description": "<stats>+55 Attack Damage<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> +18 <a href='Lethality'>Lethality</a><br><unique>UNIQUE Passive:</unique> +40 Movement Speed out of Combat<br><active>UNIQUE Active:</active> Grants +20% Movement Speed for 6 seconds (45 second cooldown).",
            "id": 3142,
            "name": "Youmuu's Ghostblade"
        },
        "3143": {
            "plaintext": "Greatly increases defenses, activate to slow nearby enemies",
            "description": "<stats>+400 Health<br>+60 Armor</stats><br><br><unique>UNIQUE Passive:</unique> -20% damage taken from basic attack critical strikes.<br><unique>UNIQUE Passive - Cold Steel:</unique> When hit by basic attacks, reduces the attacker's Attack Speed by 15% for 1 second.<br><active>UNIQUE Active:</active> Slows the Movement Speed of nearby enemy units by 55% for 2 seconds (60 second cooldown).",
            "id": 3143,
            "name": "Randuin's Omen"
        },
        "3144": {
            "plaintext": "Activate to deal magic damage and slow target champion",
            "description": "<stats>+25 Attack Damage<br>+10% Life Steal</stats><br><br><active>UNIQUE Active:</active> Deals 100 magic damage and slows the target champion's Movement Speed by 25% for 2 seconds (90 second cooldown).",
            "id": 3144,
            "name": "Bilgewater Cutlass"
        },
        "3145": {
            "plaintext": "Increases Ability Power. Deal bonus magic damage on attack periodically.",
            "description": "<stats>+40 Ability Power</stats><br><br><unique>UNIQUE Passive - Magic Bolt:</unique> Damaging an enemy champion with a basic attack shocks them for <scaleLevel>50 - 125</scaleLevel> bonus magic damage (40 second cooldown, shared with other <font color='#9999FF'><a href='itembolt'>Hextech</a></font> items).<br><br>Magic Bolt's cooldown is reduced by Active Item cooldown reduction.<br><br><rules>(Damage scales based on level. Hextech effects can trigger other item spell effects.)</rules>",
            "id": 3145,
            "name": "Hextech Revolver"
        },
        "3146": {
            "plaintext": "Increases Attack Damage and Ability Power, activate to slow a target",
            "description": "<stats>+40 Attack Damage<br>+80 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> Heal for 15% of damage dealt. This is 33% as effective for Area of Effect damage.<br><active>UNIQUE Active - Lightning Bolt:</active> Deals <scaleLevel>175 - 253</scaleLevel> (+30% of Ability Power) magic damage and slows the target champion's Movement Speed by 40% for 2 seconds (40 second cooldown, shared with other <font color='#9999FF'><a href='itembolt'>Hextech</a></font> items).",
            "id": 3146,
            "name": "Hextech Gunblade"
        },
        "3147": {
            "plaintext": "Deals additional physical damage when ambushing enemies and provides trap and ward detection periodically",
            "description": "<stats>+55 Attack Damage<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> +18 <a href='Lethality'>Lethality</a><br><unique>UNIQUE Passive - Blackout:</unique> When spotted by an enemy ward, reveal traps and disable wards around you for 8 seconds. Melee attacks instantly kill these devices. (90 second cooldown).<br><unique>UNIQUE Passive - Nightstalker:</unique> After being unseen for at least 1 second, your next basic attack against an enemy champion deals <scaleLevel>30 - 200</scaleLevel> bonus physical damage and slows them by 99% for 0.25 seconds. Ranged basic attacks do not apply the slow. (Lasts for 5 seconds after being seen by an enemy champion).",
            "id": 3147,
            "name": "Duskblade of Draktharr"
        },
        "3151": {
            "plaintext": "Spell damage burns enemies for a portion of their Health",
            "description": "<stats>+80 Ability Power<br>+300 Health</stats><br><br><unique>UNIQUE Passive - Madness:</unique> Deal 2% more damage for each second in combat with champions (10% maximum).<br><unique>UNIQUE Passive - Torment:</unique> Spells burn enemies for 3 seconds, dealing bonus magic damage equal to 1% of their maximum Health per second. Burn damage is doubled against <a href='MovementImpaired'>movement-impaired</a> units.",
            "id": 3151,
            "name": "Liandry's Torment"
        },
        "3152": {
            "plaintext": "Activate to dash forward and unleash a fiery explosion",
            "description": "<stats>+300 Health<br>+60 Ability Power<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Active - Fire Bolt:</unique> Dash forward and unleash a nova of fire bolts that deal <scaleLevel>75 - 150</scaleLevel> (+25% of your Ability Power) as magic damage (40 second cooldown, shared with other <font color='#9999FF'><a href='itembolt'>Hextech</a></font> items).<br><br>Champions and Monsters hit by multiple fire bolts take 10% damage per additional bolt.<br><br><rules>(This dash cannot pass through terrain.)</rules>",
            "id": 3152,
            "name": "Hextech Protobelt-01"
        },
        "3153": {
            "plaintext": "Deals damage based on target's Health, can steal Movement Speed",
            "description": "<stats>+40 Attack Damage<br>+25% Attack Speed<br>+12% Life Steal</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal 8% of the target's current Health as bonus physical damage on hit.<br><active>UNIQUE Active:</active> Deals 100 magic damage to target champion and steals 25% of their Movement Speed for 3 seconds (90 second cooldown).<br><br><rules>Minimum bonus physical damage dealt is 15.<br>Maximum bonus physical damage dealt to monsters and minions is 60.<br>User's Life Steal is applied to bonus physical damage dealt.</rules>",
            "id": 3153,
            "name": "Blade of the Ruined King"
        },
        "3155": {
            "plaintext": "Increases Attack Damage and Magic Resist",
            "description": "<stats>+20 Attack Damage<br>+35 Magic Resist</stats><br><br><unique>UNIQUE Passive - Lifeline:</unique> Upon taking magic damage that would reduce Health below 30%, grants a shield that absorbs 110 to 280 (based on level) magic damage for 5 seconds (90 second cooldown).",
            "id": 3155,
            "name": "Hexdrinker"
        },
        "3156": {
            "plaintext": "Grants bonus Attack Damage when Health is low",
            "description": "<stats>+50 Attack Damage<br>+45 Magic Resist<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Lifeline:</unique> Upon taking magic damage that would reduce Health below 30%, grants a shield that absorbs magic damage equal to 300 + 1 per bonus Magic Resistance for 5 seconds (90 second cooldown).<br><unlockedPassive>Lifegrip:</unlockedPassive> When <i>Lifeline</i> triggers, gain +20 Attack Damage, +10% Spell Vamp and +10% Life Steal until out of combat.",
            "id": 3156,
            "name": "Maw of Malmortius"
        },
        "3157": {
            "plaintext": "Activate to become invincible but unable to take actions",
            "description": "<stats>+70 Ability Power<br>+45 Armor<br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active - Stasis:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (120 second cooldown).",
            "id": 3157,
            "name": "Zhonya's Hourglass"
        },
        "3158": {
            "plaintext": "Increases Movement Speed and Cooldown Reduction",
            "description": "<groupLimit>Limited to 1 pair of boots.</groupLimit><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive - Enhanced Movement:</unique> +45 Movement Speed<br><unique>UNIQUE Passive:</unique> Reduces Summoner Spell cooldowns by 10%<br><br><br><rules><font color='#FDD017'>''This item is dedicated in honor of Ionia's victory over Noxus in the Rematch for the Southern Provinces on 10 December, 20 CLE.''</font></rules>",
            "id": 3158,
            "name": "Ionian Boots of Lucidity"
        },
        "3165": {
            "plaintext": "Increases magic damage",
            "description": "<stats>+80 Ability Power<br>+300 Health</stats><br><br><unique>UNIQUE Passive - Touch of Death:</unique> +15 <a href='FlatMagicPen'>Magic Penetration</a><br><unique>UNIQUE Passive - Cursed Strike:</unique> Magic damage dealt to champions inflicts them with <a href='GrievousWounds'>Grievous Wounds</a> for 3 seconds.",
            "id": 3165,
            "name": "Morellonomicon"
        },
        "3170": {
            "plaintext": "Improves defense and reduces duration of disabling effects",
            "description": "<stats>+50 Ability Power<br>+50 Armor<br>+50 Magic Resist</stats><br><br><unique>UNIQUE Passive - Tenacity:</unique> Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.",
            "id": 3170,
            "name": "Moonflair Spellblade"
        },
        "3174": {
            "plaintext": "Deal damage to empower your heals and shields",
            "description": "<stats>+30 Ability Power<br>+30 Magic Resist<br>+10% Cooldown Reduction<br><mana>+100% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive:</unique> Gain 25% of the <a href='premitigation'><font color='#6666FF'><u>premitigation</u></font></a> damage dealt to champions as Blood Charges, up to <scaleLevel>100 - 250</scaleLevel> max. Healing or shielding another ally consumes charges equal to 100% of the heal or shield value, healing the ally for that amount.<br><unique>UNIQUE Passive - Dissonance:</unique> Grants 5 ability power per 25% Base Mana Regen you have. Disables <unique>Harmony</unique> on your other items.<br><br><rules>(Maximum amount of Blood Charges stored is based on level. Healing amplification is applied to the total heal value.)</rules>",
            "id": 3174,
            "name": "Athene's Unholy Grail"
        },
        "3175": {
            "description": "<unique>UNIQUE Active - Bonetooth Totem:</unique> Places a Stealth Ward that lasts 180 seconds (90 Second cooldown). Limit 3 Stealth Wards on the map per player.<br><br><unique>UNIQUE Passive - Mementos of the Hunt:</unique> Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.<br><br><passive>3 Trophies:</passive> Rengar gains 25 Movement Speed whilst out of combat or in brush. <br><passive>6 Trophies:</passive> Increases the range of Rengar's Leap by 125.<br><passive>12 Trophies:</passive> Thrill of the Hunt's duration is increased by 5 seconds.<br><passive>20 Trophies:</passive> Rengar gains the movement speed bonus of Thrill of the Hunt while he is stealthed.",
            "id": 3175,
            "name": "Head of Kha'Zix"
        },
        "3181": {
            "plaintext": "Greatly increases Attack Damage and Life Steal",
            "description": "<stats>+45 Attack Damage<br>+10% Life Steal</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks grant +6 Attack Damage and +1% Life Steal for 8 seconds on hit (effect stacks up to 5 times).",
            "id": 3181,
            "name": "Sanguine Blade"
        },
        "3184": {
            "plaintext": "Good starting item for attackers",
            "description": "<stats>+150 Health<br>+20 Attack Damage<br>+10% Life Steal</stats><br><br><groupLimit>Limited to 1 Guardian's Item.</groupLimit>",
            "id": 3184,
            "name": "Guardian's Hammer"
        },
        "3185": {
            "plaintext": "Critical Strikes cause your target to bleed and be revealed",
            "description": "<stats>+30 Attack Damage<br>+30% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> Critical Strikes cause enemies to bleed for an additional 90% of bonus Attack Damage as magic damage over 3 seconds and reveal them for the duration.<br><unique>UNIQUE Passive - Trap Detection:</unique> Nearby stealthed enemy traps are revealed.<br><active>UNIQUE Active - Hunter's Sight:</active> A stealth-detecting mist grants vision in the target area for 5 seconds, revealing enemy champions that enter for 3 seconds (60 second cooldown).",
            "id": 3185,
            "name": "The Lightbringer"
        },
        "3187": {
            "plaintext": "Activate to reveal a nearby area of the map",
            "description": "<stats>+225 Health<br>+250 Mana<br>+25 Armor<br>+20% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Trap Detection:</unique> Grants <font color='#ee91d7'>True Sight</font>  of nearby enemy traps.<br><active>UNIQUE Active - Hunter's Sight:</active> An arcane mist grants vision in the target area for 5 seconds, revealing enemy champions in the area for 3 seconds (60 second cooldown).",
            "id": 3187,
            "name": "Arcane Sweeper"
        },
        "3190": {
            "plaintext": "Activate to shield nearby allies from damage",
            "description": "<stats>+30 Armor<br>+60 Magic Resist</stats><br><br><active>UNIQUE Active:</active> Grants a decaying shield to nearby allied champions for 2.5 seconds that absorbs up to 30 (+15 per level) <scaleHealth>(+20% of your bonus health)</scaleHealth> damage (120 second cooldown).<br><br><rules>Shield per level uses the higher of your level or the target's level.<br>Shield ratio scales with your level.<br>Shield amount is reduced to 25% if the target has been affected by another Locket of the Iron Solari in the last 20 seconds.</rules>",
            "id": 3190,
            "name": "Locket of the Iron Solari"
        },
        "3191": {
            "plaintext": "Increases Armor and Ability Power",
            "description": "<stats>+30 Armor<br>+20 Ability Power</stats><br><br><unique>UNIQUE Passive:</unique> Killing a unit grants 0.5 bonus Armor and Ability Power. This bonus stacks up to 30 times.",
            "id": 3191,
            "name": "Seeker's Armguard"
        },
        "3193": {
            "plaintext": "Greatly increases defense near multiple enemies.",
            "description": "<stats>+40 Armor<br>+40 Magic Resist</stats></stats><br><br><unique>UNIQUE Passive - Stone Skin:</unique> If 3+ enemy champions are nearby, grants 40 bonus Armor and Magic Resist.<br><active>UNIQUE Active - Metallicize:</active> Increases Health by 40% and increases champion size, but reduces damage dealt by 60% for 4 seconds (92 second cooldown). If Stone Skin is active, the Health increase becomes 100% instead.",
            "id": 3193,
            "name": "Gargoyle Stoneplate"
        },
        "3194": {
            "plaintext": "Reduces damage from repeated spells and effects.",
            "description": "<stats>+350 Health<br>+55 Magic Resist<br>+100% Base Health Regeneration <br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Taking magic damage from a spell or effect reduces all subsequent magic damage from that same spell or effect by 20% for 4 seconds.",
            "id": 3194,
            "name": "Adaptive Helm"
        },
        "3196": {
            "plaintext": "Allows Viktor to improve an ability of his choice",
            "description": "<stats>+3 Ability Power per level<br>+15 Mana per level</stats><br><br><unique>UNIQUE Passive - Progress:</unique> Viktor can upgrade one of his basic spells.",
            "id": 3196,
            "name": "The Hex Core mk-1"
        },
        "3197": {
            "plaintext": "Allows Viktor to improve an ability of his choice",
            "description": "<stats>+6 Ability Power per level<br>+20 Mana per level</stats><br><br><unique>UNIQUE Passive - Progress:</unique> Viktor can upgrade one of his basic spells.",
            "id": 3197,
            "name": "The Hex Core mk-2"
        },
        "3198": {
            "plaintext": "Allows Viktor to improve an ability of his choice",
            "description": "<stats>+10 Ability Power per level<br>+25 Mana per level</stats><br><br><unique>UNIQUE Passive - Glorious Evolution:</unique> Viktor has reached the pinnacle of his power, upgrading Chaos Storm in addition to his basic spells.",
            "id": 3198,
            "name": "Perfect Hex Core"
        },
        "3200": {
            "plaintext": "Increases Ability Power and can be upgraded to improve Viktor's abilities",
            "description": "<stats>+1 Ability Power per level<br>+10 Mana per level</stats><br><br><unique>UNIQUE Passive - Progress:</unique> This item can be upgraded three times to enhance Viktor's basic abilities.",
            "id": 3200,
            "name": "Prototype Hex Core"
        },
        "3211": {
            "plaintext": "Improves defense and grants regeneration upon being damaged",
            "description": "<stats>+250 Health<br>+25 Magic Resist</stats><br><br><unique>UNIQUE Passive:</unique> Grants 150% Base Health Regen for up to 10 seconds after taking damage from an enemy champion.",
            "id": 3211,
            "name": "Spectre's Cowl"
        },
        "3222": {
            "plaintext": "Activate to remove all disabling effects from an allied champion",
            "description": "<stats>+40 Magic Resist<br>+10% Cooldown Reduction<br><mana>+100% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive:</unique> +20% Heal and Shield Power<br><unique>UNIQUE Passive - Harmony:</unique> Grants bonus % Base Health Regen equal to your bonus % Base Mana Regen.<br><active>UNIQUE Active:</active> Cleanses all stuns, roots, taunts, fears, silences, and slows on an allied champion and grants them slow immunity for 2 seconds (120 second cooldown). <br><br>Cleansing an effect grants the ally 40% movement speed for 2 seconds.",
            "id": 3222,
            "name": "Mikael's Crucible"
        },
        "3252": {
            "plaintext": "Transforms into a Serrated Dirk after poaching in the enemy jungle.",
            "description": "<stats>+10 Attack Damage</stats><br><br><unique>UNIQUE Passive - Headhunter:</unique> After killing any enemy, your next damaging spell will deal 40 bonus physical damage (30 second cooldown).<br><unique>UNIQUE Passive:</unique> After poaching 4 large monsters from the enemy jungle, transforms into a Serrated Dirk.",
            "id": 3252,
            "name": "Poacher's Dirk"
        },
        "3285": {
            "plaintext": "Increases Ability Power, Mana, and Cooldown Reduction",
            "description": "<stats>+90 Ability Power<br><mana>+500 Mana</mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Haste:</unique> This item gains an additional 10% Cooldown Reduction.<br><unique>UNIQUE Passive - Echo:</unique> Gain charges upon moving or casting. At 100 charges, the next damaging spell hit expends all charges to deal 100 (+10% of Ability Power) bonus magic damage to up to 4 targets on hit.",
            "id": 3285,
            "name": "Luden's Echo"
        },
        "3301": {
            "plaintext": "Grants gold and mana when nearby minions die that you didn't kill",
            "description": "<stats>+5 Movement Speed<br>+5% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Favor:</unique> Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>25</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<hr><passive>QUEST:</passive> Earn 500 gold using this item and upgrade to <font color='#CFBF84'>Nomad's Medallion</font>.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><i><font color='#447777'>''Gold dust rises from the desert and clings to the coin.'' - Historian Shurelya, 11 November, 23 CLE</font></i>",
            "id": 3301,
            "name": "Ancient Coin"
        },
        "3302": {
            "plaintext": "Kill minions periodically to heal and grant gold to a nearby ally",
            "description": "<stats>+50 Health<br>+1 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 195 (+5 per level) Health. Killing a minion heals the owner and the nearest allied champion for 15 Health (+2% missing health) and grants them kill Gold. 50% healing if the owner is ranged. These effects require a nearby ally. Recharges every 40 seconds. Max 2 charges.<hr><passive>QUEST:</passive> Earn 500 gold using this item and upgrade to <font color='#CFBF84'>Targon's Brace</font>.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3302,
            "name": "Relic Shield"
        },
        "3303": {
            "plaintext": "Grants gold when you damage enemies",
            "description": "<stats>+10 Ability Power<br>+2 Gold per 10 seconds<br><mana>+25% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 13 additional magic damage and grant 10 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<hr><passive>QUEST:</passive> Earn 500 gold using this item and upgrade to <font color='#CFBF84'>Frostfang</font>.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 3 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3303,
            "name": "Spellthief's Edge"
        },
        "3304": {
            "plaintext": "Grants gold and mana when nearby minions die that you didn't kill",
            "description": "<stats>+5 Movement Speed<br>+5% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Favor:</unique> Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>25</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<hr><passive>QUEST:</passive> Earn 750 gold using this item and upgrade to <font color='#CFBF84'>Nomad's Medallion</font>.<br><passive>REWARD:</passive> <font color='#CFBF84'>Favor</font> is upgraded to <font color='#CFBF84'><a href='coinlinequestreward'>Emperor's Favor</a></font> and allied champions moving toward you gain 8% movement speed.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><i><font color='#447777'>''Gold dust rises from the desert and clings to the coin.'' - Historian Shurelya, 11 November, 23 CLE</font></i>",
            "id": 3304,
            "name": "Timeworn Ancient Coin"
        },
        "3305": {
            "plaintext": "Grants gold and mana when nearby minions die that you didn't kill",
            "description": "<stats>+10 Movement Speed<br>+50% Base Health Regen <br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Favor:</unique> Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>45</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Favor</font> is upgraded to <font color='#CFBF84'><a href='coinlinequestreward'>Emperor's Favor</a></font> and allied champions moving toward you gain 8% movement speed.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><rules><font color='#447777'>''The medallion shines with the glory of a thousand voices when exposed to the sun.'' - Historian Shurelya, 22 June, 24 CLE</font></rules>",
            "id": 3305,
            "name": "Timeworn Nomad's Medallion"
        },
        "3306": {
            "plaintext": "Increases Health / Mana Regeneration and Cooldown Reduction. Activate to speed up nearby allies.",
            "description": "<stats>+10 Movement Speed<br>+45 Armor<br>+175% Base Health Regen <br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds</stats><br><br><unique>UNIQUE Passive - Point Runner:</unique> Builds up to +20% Movement Speed over 2 seconds while near turrets, fallen turrets and Void Gates.<br><unique>UNIQUE Passive - Favor: </unique>Enemy minions killed by your allies sometimes drop coins that give either <font color='#D4AF37'>45</font> gold or <font color='#44DDFF'>6%</font> missing mana (minimum 10). Cannon minions always drop coins.<br><active>UNIQUE Active:</active> Grants nearby allies +@Effect5Amount*100@% Movement Speed for @Effect6Amount@ seconds (60 second cooldown).<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Favor</font> is upgraded to <font color='#CFBF84'><a href='coinlinequestreward'>Emperor's Favor</a></font> and allied champions moving toward you gain 8% movement speed.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit><br><br><rules><font color='#447777'>''Praise the sun.'' - Historian Shurelya, 22 September, 25 CLE</font></rules>",
            "id": 3306,
            "name": "Timeworn Talisman of Ascension"
        },
        "3307": {
            "plaintext": "Kill minions periodically to heal and grant gold to a nearby ally",
            "description": "<stats>+50 Health<br>+2 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 195 (+5 per level) Health. Killing a minion heals the owner and the nearest allied champion for 15 Health (+2% missing health) and grants them kill Gold. Healing is halved if the owner is ranged. These effects require a nearby ally. Recharges every 40 seconds. Max 2 charges.<hr><passive>QUEST:</passive> Earn 750 gold using this item and upgrade to <font color='#CFBF84'>Targon's Brace</font>.<br><passive>REWARD:</passive> <font color='#CFBF84'>Shield Battery</font>, a permanent shield that regenerates slowly outside of combat.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3307,
            "name": "Timeworn Relic Shield"
        },
        "3308": {
            "plaintext": "Periodically kill enemy minions to heal and grant gold to a nearby ally",
            "description": "<stats>+125 Health<br>+50% Base Health Regen <br>+4 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 200 (+10 per level) Health. Killing a minion heals the owner and the nearest allied champion for 40 Health (+2% missing health) and grants them kill Gold. Healing is halved if the owner is ranged. These effects require a nearby ally. Recharges every 30 seconds. Max 3 charges.<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Shield Battery</font>, a permanent shield that regenerates slowly outside of combat.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3308,
            "name": "Timeworn Targon's Brace"
        },
        "3309": {
            "plaintext": "Shield an ally from damage based on your Health",
            "description": "<stats>+350 Health<br>+100% Base Health Regen <br>+10% Cooldown Reduction<br>+4 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 320 (+20 per level) Health. Killing a minion heals the owner and the nearest allied champion for 50 Health (+2% missing health) and grants them kill Gold. Healing is halved if the owner is ranged. These effects require a nearby ally. Recharges every 20 seconds. Max 4 charges.<br><unique>UNIQUE Active:</unique> Grant a shield to you and an ally equal to 10% of your maximum Health for 4 seconds. After 4 seconds, the shields explode to slow nearby enemies by 40% for 2 seconds (60 second cooldown).  Automatically targets the most wounded ally if cast upon self.<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Shield Battery</font>, a permanent shield that regenerates slowly outside of combat.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3309,
            "name": "Timeworn Face of the Mountain"
        },
        "3310": {
            "plaintext": "Grants gold when you damage enemies",
            "description": "<stats>+10 Ability Power<br>+2 Gold per 10 seconds<br><mana>+25% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 13 additional magic damage and grant 10 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<hr><passive>QUEST:</passive> Earn 750 gold using this item and upgrade to <font color='#CFBF84'>Frostfang</font>.<br><passive>REWARD:</passive> <font color='#CFBF84'>Tribute</font> is upgraded into <font color='#CFBF84'><a href='frostqueenslinequestreward'>Queen's Tribute</a></font>.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3310,
            "name": "Timeworn Spellthief's Edge"
        },
        "3311": {
            "plaintext": "Grants gold when you damage an enemy",
            "description": "<stats>+20 Ability Power<br>+2 Gold per 10 seconds<br><mana>+50% Base Mana Regen </mana><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 18 additional magic damage and grant 20 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Tribute</font> is upgraded into <font color='#CFBF84'><a href='frostqueenslinequestreward'>Queen's Tribute</a></font>.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3311,
            "name": "Timeworn Frostfang"
        },
        "3312": {
            "plaintext": "Sends out seeking wraiths that track hidden enemies and slow them",
            "description": "<stats>+60 Ability Power<br>+10% Cooldown Reduction<br>+2 Gold per 10 seconds<br><mana>+50% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive - Tribute:</unique> Damaging spells and attacks against champions or buildings deal 18 additional magic damage and grant 20 Gold per unique spell cast. This can occur up to 3 times every 30 seconds. Before quest completion, killing minions and non-epic monsters slows Tribute and gold generation.<br><active>UNIQUE Active:</active> Summon 2 icy ghosts for 6 seconds that seek out nearby enemy champions. Ghosts reveal enemies on contact and slow them by 40% for between 2 and 5 seconds based on how far the ghosts have traveled (90 second cooldown).<hr><passive>QUEST:</passive> Earn 750 gold using this item.<br><passive>REWARD:</passive> <font color='#CFBF84'>Tribute</font> is upgraded into <font color='#CFBF84'><a href='frostqueenslinequestreward'>Queen's Tribute</a></font>.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3312,
            "name": "Timeworn Frost Queen's Claim"
        },
        "3340": {
            "plaintext": "Periodically place a Stealth Ward",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Consume a charge to place an invisible <font color='#BBFFFF'>Stealth Ward</font> which reveals the surrounding area for <scaleLevel>60 - 120</scaleLevel> seconds. <br><br>Stores one charge every <scaleLevel>180 - 90</scaleLevel> seconds, up to 2 maximum charges.<br><br>Ward duration and recharge time gradually improve with level.<br><br><rules>(Limit 3 <font color='#BBFFFF'>Stealth Wards</font> on the map per player.</rules>",
            "id": 3340,
            "name": "Warding Totem (Trinket)"
        },
        "3345": {
            "plaintext": "Consumes charge to revive champion.",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Consumes a charge to instantly revive at your Summoner Platform and grants 125% Movement Speed that decays over 12 seconds.<br><br><rules>Additional charges are gained at levels 9 and 14.</rules><br><br><font color='#BBFFFF'>(Max: 2 charges)</font></rules><br><br>",
            "id": 3345,
            "name": "Soul Anchor (Trinket)"
        },
        "3348": {
            "plaintext": "Activate to reveal a nearby area of the map",
            "description": "<active>UNIQUE Active - Hunter's Sight:</active> An arcane mist grants vision in the target area for 5 seconds, revealing enemy champions and granting <font color='#ee91d7'>True Sight</font> of traps in the area for 3 seconds (90 second cooldown).",
            "id": 3348,
            "name": "Arcane Sweeper"
        },
        "3361": {
            "plaintext": "Periodically place a Stealth Ward",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><levelLimit> *Level 9+ required to upgrade.</levelLimit><stats></stats><br><br><unique>UNIQUE Active:</unique> Consume a charge to place an invisible ward that reveals the surrounding area for 180 seconds.  Stores a charge every 60 seconds, up to 2 total. Limit 3 <font color='#BBFFFF'>Stealth Wards</font> on the map per player.<br><br><rules>(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds).</rules>",
            "id": 3361,
            "name": "Greater Stealth Totem (Trinket)"
        },
        "3362": {
            "plaintext": "Periodically place a Vision Ward",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><levelLimit> *Level 9+ required to upgrade.</levelLimit><stats></stats><br><br><unique>UNIQUE Active:</unique> Places a visible ward that reveals the surrounding area and invisible units in the area until killed (120 second cooldown). Limit 1 <font color='#BBFFFF'>Vision Ward</font> on the map per player.<br><br><rules>(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds).</rules>",
            "id": 3362,
            "name": "Greater Vision Totem (Trinket)"
        },
        "3363": {
            "plaintext": "Grants increased range and reveals the targetted area",
            "description": "<levelLimit>Level 9+ required to upgrade.</levelLimit><br><groupLimit>Limited to 1 Trinket.</groupLimit><br><br>Alters the <font color='#FFFFFF'>Warding Totem</font> Trinket:<br><br><stats><font color='#00FF00'>+</font> Massively increased cast range (+650%)<br><font color='#00FF00'>+</font> Infinite duration and does not count towards ward limit<br><font color='#FF0000'>-</font> <font color='#FF6600'>10% increased cooldown</font><br><font color='#FF0000'>-</font> <font color='#FF6600'>Ward is visible, fragile, untargetable by allies</font><br><font color='#FF0000'>-</font> <font color='#FF6600'>45% reduced ward vision radius</font><br><font color='#FF0000'>-</font> <font color='#FF6600'>Cannot store charges</font></stats>",
            "id": 3363,
            "name": "Farsight Alteration"
        },
        "3364": {
            "plaintext": "Disables nearby invisible wards and traps for a duration",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Scans around you, warning against hidden hostile units, and revealing invisible traps and revealing / disabling nearby wards for 10 seconds (90 to 60 second cooldown).</maintext>",
            "id": 3364,
            "name": "Oracle Lens"
        },
        "3371": {
            "plaintext": "Massively enhances critical strikes",
            "description": "<stats><font color='#FFFFFF'>+100 Attack Damage</font><br>+20% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> Critical strike bonus damage is increased by 50%.",
            "id": 3371,
            "name": "Molten Edge"
        },
        "3373": {
            "plaintext": "Constantly deals damage to nearby enemies",
            "description": "<stats><font color='#FFFFFF'>+625 Health</font><br><font color='#FFFFFF'>+90 Armor</font></stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 25 (+1 per champion level) magic damage per second to nearby enemies. Deals 50% bonus damage to minions and monsters.",
            "id": 3373,
            "name": "Forgefire Cape"
        },
        "3374": {
            "plaintext": "Massively increases Ability Power",
            "description": "<stats><font color='#FFFFFF'>+175 Ability Power</font>  </stats><br><br><unique>UNIQUE Passive:</unique> Increases Ability Power by 40%.",
            "id": 3374,
            "name": "Rabadon's Deathcrown"
        },
        "3379": {
            "plaintext": "Nearby enemies take more magic damage",
            "description": "<stats><font color='#FFFFFF'>+550 Health</font><br><mana>+300 Mana</mana><br><font color='#FFFFFF'>+90 Magic Resist</font><br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive - Eternity:</unique> 15% of damage taken from champions is gained as Mana. Spending Mana restores 20% of the cost as Health, up to 25 per spell cast.<br><aura>UNIQUE Aura:</aura> Nearby enemy champions take 15% more magic damage.",
            "id": 3379,
            "name": "Infernal Mask"
        },
        "3380": {
            "plaintext": "Dealing physical damage to enemy champions reduces their Armor",
            "description": "<stats><font color='#FFFFFF'>+550 Health</font><br><font color='#FFFFFF'>+60 Attack Damage</font><br>+20% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Dealing physical damage to an enemy champion Cleaves them, reducing their Armor by 4% for 6 seconds (stacks up to 6 times, up to 24%).<br><unique>UNIQUE Passive - Rage:</unique> Dealing physical damage grants 20 movement speed for 2 seconds. Assists on Cleaved enemy champions or kills on any unit grant 60 movement speed for 2 seconds instead. This Movement Speed is halved for ranged champions.",
            "id": 3380,
            "name": "The Obsidian Cleaver"
        },
        "3382": {
            "plaintext": "Activate to heal allies and damage enemies in an area",
            "description": "<stats><font color='#FFFFFF'>+300 Health</font><br><font color='#FFFFFF'>+150% Base Health Regen </font><br><font color='#FFFFFF'>+200% Base Mana Regen </font><br>+10% Cooldown Reduction</stats><br><br><passive>UNIQUE Passive:</passive> +10% Heal and Shield Power<br><active>UNIQUE Active:</active> Target an area within 5500 range. After 2.5 seconds, call down a beam of light to heal allies for 10 (+20 per level of target) Health, burn enemy champions for 10% of their maximum Health as <font color='#FFFFFF'>true</font> damage and deal 250 <font color='#FFFFFF'>true</font> damage to enemy minions (120 second cooldown). Heal and Shield Power is 3 times as effective on Salvation's heal.<br><br>Can be used while dead.<br><br><rules>Half effect if the target has been affected by Redemption recently.</rules>",
            "id": 3382,
            "name": "Salvation"
        },
        "3383": {
            "plaintext": "Activate to shield nearby allies from damage",
            "description": "<stats><font color='#FFFFFF'>+45 Armor</font><br><font color='#FFFFFF'>+75 Magic Resist</font></stats><br><br><active>UNIQUE Active:</active> Grants a decaying shield to nearby allied champions for 2.5 seconds that absorbs up to 30 (+15 per level) <scaleHealth>(+20% of your bonus health)</scaleHealth> damage (120 second cooldown).<br><br><rules>Shield per level uses the higher of your level or the target's level.<br>Shield ratio scales with your level.<br>Shield amount is reduced to 25% if the target has been affected by another Locket of the Iron Solari in the last 20 seconds.</rules>",
            "id": 3383,
            "name": "Circlet of the Iron Solari"
        },
        "3384": {
            "plaintext": "Tons of Damage",
            "description": "<stats><font color='#FFFFFF'>+350 Health</font><br><font color='#FFFFFF'><mana>+350 Mana</mana></font><br><font color='#FFFFFF'>+35 Attack Damage</font><br><font color='#FFFFFF'>+50% Attack Speed</font><br>+20% Cooldown Reduction<br><font color='#FFFFFF'>+8% Movement Speed</font></stats><br><br><unique>UNIQUE Passive - Rage:</unique> Basic attacks grant 20 Movement Speed for 2 seconds. Kills grant 60 Movement Speed instead. This Movement Speed bonus is halved for ranged champions.<br><unique>UNIQUE Passive - Spellblade:</unique> After using an ability, the next basic attack deals bonus physical damage equal to 200% of base Attack Damage on hit (1.5 second cooldown).",
            "id": 3384,
            "name": "Trinity Fusion"
        },
        "3385": {
            "plaintext": "Massively increases Ability Power and can be activated to enter stasis",
            "description": "<stats><font color='#FFFFFF'>+155 Ability Power</font><br>+45 Armor  </stats><br><br><unique>UNIQUE Passive:</unique> Increases Ability Power by 25%<br><active>UNIQUE Active:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (120 second cooldown).",
            "id": 3385,
            "name": "Wooglet's Witchcrown"
        },
        "3386": {
            "plaintext": "Activate to become invincible but unable to take actions",
            "description": "<stats><font color='#FFFFFF'>+100 Ability Power</font><br><font color='#FFFFFF'>+60 Armor</font><br>+10% Cooldown Reduction</stats><br><br><active>UNIQUE Active - Stasis:</active> Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (120 second cooldown).",
            "id": 3386,
            "name": "Zhonya's Paradox"
        },
        "3401": {
            "plaintext": "Provides Health and Stealth Wards over time",
            "description": "<stats>+350 Health<br>+200% Base Health Regen <br>+10% Cooldown Reduction<br>+1 Gold per 10 seconds </stats><br><br><unique>UNIQUE Passive - Spoils of War:</unique> Melee basic attacks execute minions below 320 (+20 per level) Health. Killing a minion heals the owner and the nearest allied champion for 50 Health (+2% missing health) and grants them kill Gold. 50% healing if the owner is ranged. These effects require a nearby ally. Recharges every 20 seconds. Max 4 charges.<hr><passive>QUEST:</passive> Earn 500 gold using this item.<br><passive>REWARD:</passive> Gain <active>UNIQUE Active - Warding:</active> Consumes a charge to place a <font color='#BBFFFF'>Stealth Ward</font> that reveals the surrounding area for 150 seconds.  Holds up to 4 charges which refill upon visiting the shop.<br><br><groupLimit>Limited to 1 Gold Income item.</groupLimit>",
            "id": 3401,
            "name": "Remnant of the Aspect"
        },
        "3410": {
            "description": "<unique>UNIQUE Active - Sweeping Lens:</unique> Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius and grants detection of invisible units for 10 seconds (60 second cooldown).<br><br><unique>UNIQUE Passive - Mementos of the Hunt:</unique> Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.<br><br><passive>3 Trophies:</passive> Rengar gains 25 Movement Speed whilst out of combat or in brush. <br><passive>6 Trophies:</passive> Increases the range of Rengar's Leap by 125.<br><passive>12 Trophies:</passive> Thrill of the Hunt's duration is increased by 5 seconds.<br><passive>20 Trophies:</passive> Thrill of the Hunt's Movement Speed while stealthed is doubled.",
            "id": 3410,
            "name": "Head of Kha'Zix"
        },
        "3416": {
            "description": "<unique>UNIQUE Active - Scrying:</unique> Reveals a small location within 4000 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (90 second cooldown).<br><br><unique>UNIQUE Passive - Mementos of the Hunt:</unique> Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.<br><br><passive>3 Trophies:</passive> Rengar gains 25 Movement Speed whilst out of combat or in brush. <br><passive>6 Trophies:</passive> Increases the range of Rengar's Leap by 125.<br><passive>12 Trophies:</passive> Thrill of the Hunt's duration is increased by 5 seconds.<br><passive>20 Trophies:</passive> Thrill of the Hunt's Movement Speed while stealthed is doubled.",
            "id": 3416,
            "name": "Head of Kha'Zix"
        },
        "3422": {
            "description": "<unique>UNIQUE Passive - Mementos of the Hunt:</unique> Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.<br><br><passive>3 Trophies:</passive> Rengar gains 25 Movement Speed whilst out of combat or in brush. <br><passive>6 Trophies:</passive> Increases the range of Rengar's Leap by 125.<br><passive>12 Trophies:</passive> Thrill of the Hunt's duration is increased by 5 seconds.<br><passive>20 Trophies:</passive> Thrill of the Hunt's Movement Speed while stealthed is doubled.",
            "id": 3422,
            "name": "Head of Kha'Zix"
        },
        "3455": {
            "description": "<unique>UNIQUE Passive - Mementos of the Hunt:</unique> Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.<br><br><passive>3 Trophies:</passive> Rengar gains 25 Movement Speed whilst out of combat or in brush. <br><passive>6 Trophies:</passive> Increases the range of Rengar's Leap by 125.<br><passive>12 Trophies:</passive> Thrill of the Hunt's duration is increased by 5 seconds.<br><passive>20 Trophies:</passive> Thrill of the Hunt's Movement Speed while stealthed is doubled.",
            "id": 3455,
            "name": "Head of Kha'Zix"
        },
        "3460": {
            "description": "<unique>Active:</unique> Use this trinket to teleport to one of the battle platforms. Can only be used from the summoning platform.<br><br><i><font color='#FDD017'>''It is at this magical precipice where a champion is dismantled, reforged, and empowered.''</font></i>",
            "id": 3460,
            "name": "Golden Transcendence"
        },
        "3461": {
            "description": "<unique>Active:</unique> Use this trinket to teleport to one of the battle platforms. Can only be used from the summoning platform.<br><br><i><font color='#FDD017'>''It is at this magical precipice where a champion is dismantled, reforged, and empowered.''</font></i>",
            "id": 3461,
            "name": "Golden Transcendence (Disabled)"
        },
        "3462": {
            "plaintext": "Briefly reveals a nearby targeted area",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Reveals a small area within <font color='#FFFFF'>2500</font> range for 3 seconds. Enemy champions will be revealed for 5 seconds (60 second cooldown)",
            "id": 3462,
            "name": "Seer Stone (Trinket)"
        },
        "3504": {
            "plaintext": "Shield and heal effects on other units grant both of you Attack Speed and their attacks deal additional on-hit magic damage.",
            "description": "<stats>+60 Ability Power<br>+10% Cooldown Reduction<br><mana>+50% Base Mana Regen </mana></stats><br><br><unique>UNIQUE Passive:</unique> +10% Heal and Shield Power<br><unique>UNIQUE Passive:</unique> +8% Movement Speed<br><unique>UNIQUE Passive:</unique> Whenever you heal or shield an ally, you and your ally gain 10% - 30% Attack Speed and your attacks deal an additional 5 - 20 on-hit magic damage for 6 seconds. <br><br><rules>This does not include regeneration effects. Bonus effects are based on target's level.</rules>",
            "id": 3504,
            "name": "Ardent Censer"
        },
        "3508": {
            "plaintext": "Critical Strike provides Cooldown Reduction and Mana",
            "description": "<stats>+70 Attack Damage<br>+20% Critical Strike Chance</stats><br><br><unique>UNIQUE Passive:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> Gain increasingly more Cooldown Reduction from Critical Strike Chance provided by other sources (maximum +20% additional Cooldown Reduction at 30% Critical Strike Chance).<br><unique>UNIQUE Passive:</unique> Critical strikes restore 3% of your maximum Mana pool.",
            "id": 3508,
            "name": "Essence Reaver"
        },
        "3512": {
            "plaintext": "Makes a Voidspawn generating Void Gate to push a lane with.",
            "description": "<stats>+55 Armor<br>+55 Magic Resist<br>+125% Base Health Regen <br></stats><br><unique>UNIQUE Passive - Point Runner:</unique> Builds up to +20% Movement Speed over 2 seconds while near turrets, fallen turrets and Void Gates.<br><active>UNIQUE Active:</active> Spawns a <a href='VoidGate'>Void Gate</a> for 120 seconds (120 second cooldown).<br><br>Every 4 seconds the gate makes a <a href='Voidspawn'>Voidspawn</a>. The first and every fourth Voidspawn gains 15% of maximum Health as damage.",
            "id": 3512,
            "name": "Zz'Rot Portal"
        },
        "3513": {
            "plaintext": "Eye of the Herald - a Gift of the Void.",
            "description": "<br><unique>UNIQUE Passive - Glimpse of the Void:</unique> The holder of the Eye of the Herald has Empowered Recall.<br><br><active>UNIQUE Active:</active> Channel for 3.5 seconds to crush the Eye of the Herald, summoning the Rift Herald to siege enemy turrets.<br><br>The Eye of the Herald will be lost to the Void if not used within 240 seconds.</font>",
            "id": 3513,
            "name": "Eye of the Herald"
        },
        "3599": {
            "plaintext": "Kalista's spear that binds an Oathsworn Ally.",
            "description": "<stats></stats><br><active>Active:</active> Offer to bind with an ally for the remainder of the game, becoming Oathsworn Allies. Oathsworn empowers you both while near one another.",
            "id": 3599,
            "name": "The Black Spear"
        },
        "3630": {
            "description": "<unique>Active:</unique> Use this trinket to teleport to one of your team's port pads. Can only be used from the summoning platform.",
            "id": 3630,
            "name": "Siege Teleport"
        },
        "3631": {
            "plaintext": "Place a long range anti-turret ballista",
            "description": "<br><font color='#FF9900'>Deploys a ballista that shoots the closest turret.</font><br><br>Places a long range ballista if within 2200 range of an enemy turret. After a 5 second delay, it will begin firing at the nearest enemy turret, dealing heavy damage. If the targeted turret expires, the ballista will as well.",
            "id": 3631,
            "name": "Siege Ballista"
        },
        "3633": {
            "description": "<unique>Active:</unique> Use this trinket to teleport to one of your team's port pads. Can only be used from the summoning platform.",
            "id": 3633,
            "name": "Siege Teleport"
        },
        "3634": {
            "plaintext": "Attaches a three shot beam to a turret which can then be aimed and fired",
            "description": "<br><font color='#FF9900'>Attach, then recast to fire a damaging beam from a turret to your cursor.</font><br><br><font color='#FF9900'>First Cast:</font> Attach a Slayer Beam to the target turret that can be fired 3 times.<br></br><font color='#FF9900'>Next Three Casts:</font> Fires the attached beam towards your cursor, dealing 30/level + 30% of the hit target's maximum health (20% damage to minions) in magic damage to all targets in a line.<br></br><br></br>Beam will last 15 seconds, or until it has been fired 3 times.",
            "id": 3634,
            "name": "Tower: Beam of Ruination"
        },
        "3635": {
            "plaintext": "Creates another point for your team to Teleport to",
            "description": "<br><font color='#FF9900'>Deploy an additional teleport target.</font><br><br>Places a Port Pad at target location. After a 4 second delay, it activates, allowing you or your allies to teleport to it from base.",
            "id": 3635,
            "name": "Port Pad"
        },
        "3636": {
            "plaintext": "Make a turret go invulnerable while charging a powerful barrage",
            "description": "<br><font color='#FF9900'>Makes a turret go invulnerable, then rain fire.</font><br><br>Makes the target turret invulnerable for 6 seconds. Two seconds before expiry, it unleashes a missile volley, dealing 2600 true damage over the remaining time to all nearby enemies.<br><br>Cannot be used on the same turret more than once in 15 seconds.",
            "id": 3636,
            "name": "Tower: Storm Bulwark"
        },
        "3637": {
            "description": "In Nexus Siege, Summoner Spells are replaced with Siege Weapon Slots. Spend Crystal Shards to buy single-use Siege Weapons from the item shop, then use your Summoner Spell keys to activate them!",
            "id": 3637,
            "name": "Nexus Siege: Siege Weapon Slot"
        },
        "3640": {
            "plaintext": "Allows you and allies to repeatedly flash while in a zone",
            "description": "<br><font color='#FF9900'>Allows team to cast Flash repeatedly in a limited zone.</font><br><br>Creates a magic zone for your team for 5 seconds. While in this zone, you and your allies have your summoner spells replaced by an instant cast blink that moves you to any location in the zone (1 second cooldown).",
            "id": 3640,
            "name": "Flash Zone"
        },
        "3641": {
            "plaintext": "Strengthens nearby minions",
            "description": "<br><font color='#FF9900'>Place a banner that buffs minions.</font><br><br>Place a Vanguard Banner at target location. After a 2 second delay, any nearby minions will be granted a buff, increasing their damage by 50%, and granting them 50 Armor and 100 Magic Resistance while within range.",
            "id": 3641,
            "name": "Vanguard Banner"
        },
        "3642": {
            "plaintext": "Refunds all current Siege Weapons",
            "description": "Refunds all purchased Siege Weapons for their full price.",
            "id": 3642,
            "name": "Siege Refund"
        },
        "3643": {
            "plaintext": "Places a field that stuns enemy minions and slows champions",
            "description": "<br><font color='#FF9900'>Stun minions and slow champions in an area.</font><br><br>Places an Entropy Field at target location for 5 seconds.  Enemy minions and Siege Ballistas trapped in the field are unable to move or attack while in the field.  Enemy champions in the field have their Movement Speed reduced by 25%.",
            "id": 3643,
            "name": "Entropy Field"
        },
        "3645": {
            "plaintext": "Briefly reveals a nearby targeted area",
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Reveals a small area within <font color='#FFFFF'>1400</font> range for 3 seconds. Enemy champions will be revealed for 5 seconds (60 second cooldown)",
            "id": 3645,
            "name": "Seer Stone (Trinket)"
        },
        "3647": {
            "plaintext": "Grants bonus health to nearby Siege Weapons",
            "description": "<br><font color='#FF9900'>Place a totem that shields nearby deployables.</font><br><br>Places a Shield Totem at target location. After a 2 second delay, the totem will activate, granting a 2 (+1 per additional Shield Totem) strength shield to all nearby deployables.",
            "id": 3647,
            "name": "Shield Totem"
        },
        "3648": {
            "id": 3648,
            "name": "Siege Teleport (Inactive)"
        },
        "3649": {
            "description": "<groupLimit>Limited to 1 Trinket.</groupLimit><br><br><active>Active:</active> Places a <font color='#FFFFFF'>Stealth Ward</font> that lasts <font color='#FFFFFF'>30</font> seconds (30 second cooldown).",
            "id": 3649,
            "name": "Siege Sight Warder"
        },
        "3671": {
            "description": "<stats>+60 Attack Damage<br>+10% Cooldown Reduction</stats>",
            "id": 3671,
            "name": "Enchantment: Warrior"
        },
        "3672": {
            "description": "<stats>+325 Health<br>+15% Bonus Health</stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 7 (+2 per champion level) magic damage a second to nearby enemies while in combat. Deals 100% bonus damage to monsters. ",
            "id": 3672,
            "name": "Enchantment: Cinderhulk"
        },
        "3673": {
            "description": "<stats>+60 Ability Power<br>+7% Movement Speed</stats><br><br><unique>UNIQUE Passive - Echo:</unique> Gain charges upon moving or casting. At 100 charges, the next damaging spell hit expends all charges to deal 60 (+10% of Ability Power) bonus magic damage to up to 4 targets on hit.<br><br>This effect deals 250% damage to Large Monsters. Hitting a Large Monster with this effect will restore 18% of your missing Mana.",
            "id": 3673,
            "name": "Enchantment: Runic Echoes"
        },
        "3675": {
            "description": "<stats>+50% Attack Speed</stats><br><br><unique>UNIQUE Passive:</unique> Basic attacks deal 4% of the target's maximum Health in bonus physical damage (max 75 vs. monsters and minions) on hit.",
            "id": 3675,
            "name": "Enchantment: Bloodrazor"
        },
        "3680": {
            "plaintext": "King: Fires a barrage of icy artillery",
            "description": "<active>Active - <a href='FeedTheKing'>Feed The King</a>:</active> The King lobs many projectiles at far-away enemies, each dealing <scaleLevel>213-775</scaleLevel> magic damage to targets in the center of the impact, scaling down to <scaleLevel>85-310</scaleLevel> on the edge. (120s cooldown)",
            "id": 3680,
            "name": "Frosted Snax"
        },
        "3681": {
            "plaintext": "King: Shoots flames that burn units and Turrets",
            "description": "<active>Active - <a href='FeedTheKing'>Feed The King</a>:</active> The King breathes fire for 4 seconds, dealing <scaleLevel>705-1479</scaleLevel> true damage over the duration to enemies caught in the cone. Deals up to 560 true damage to Turrets. (120s cooldown)",
            "id": 3681,
            "name": "Super Spicy Snax"
        },
        "3682": {
            "plaintext": "King: Knocks back and grants a large shield",
            "description": "<active>Active - <a href='FeedTheKing'>Feed The King</a>:</active> The King leaps into the air and crashes down twice, knocking enemies away and dealing <scaleLevel>40-190</scaleLevel> physical damage. He also gains a decaying shield for <font color='#FF3300'>20% of his maximum health</font>, lasting 4 seconds. (30s cooldown)",
            "id": 3682,
            "name": "Espresso Snax"
        },
        "3683": {
            "plaintext": "King: Poros knock enemies towards him",
            "description": "<active>Active - <a href='FeedTheKing'>Feed The King</a>:</active> The King tosses many Snax behind the enemy, attracting Poros which dash back towards him. Enemy champions hit will be knocked forwards and dealt <scaleLevel>230-680</scaleLevel> physical damage. (120s cooldown)",
            "id": 3683,
            "name": "Rainbow Snax Party Pack!"
        },
        "3690": {
            "description": "<passive>Passive - Cosmic Shackle: </passive>Death Sentence pulls much farther (based on the target's Missing Health), and can be ignited by the Dark Star to do more damage.<br><br><flavorText>''A still more glorious dawn awaits.''</flavorText>",
            "id": 3690,
            "name": "Cosmic Shackle"
        },
        "3691": {
            "description": "<passive>Passive - Singularity Lantern: </passive>Dark Passage automatically saves disabled allies. However, it no longer provides a shield.<br><br><flavorText>''The stars call to us.''</flavorText>",
            "id": 3691,
            "name": "Singularity Lantern"
        },
        "3692": {
            "description": "<passive>Passive - Dark Matter Scythe: </passive>Flay's on-hit passive charges damage very quickly. Flay will throw enemies much farther (based on their Missing Health).<br><br><flavorText>''If you want to make a Singularity from scratch, you must first destroy the universe.''</flavorText>",
            "id": 3692,
            "name": "Dark Matter Scythe"
        },
        "3693": {
            "description": "<passive>Passive - Mass Conversion: </passive>Thresh's Health represents how far enemy pulls and pushes will send him. At lower Health, he will be thrown farther.<br><br><passive>Passive - Terminus Dwellers: </passive>Abyss Scuttlers emerge periodically, and will scurry towards the Dark Star when attacked. Gravitational disturbances will temporarily attract many of them.",
            "id": 3693,
            "name": "Gravity Boots"
        },
        "3694": {
            "description": "<passive>Passive - Stellar Spirit: </passive>Upon spawning, Thresh is invulnerable, untargetable, cannot cast, and is able to travel in open space. This is lost when stepping foot on stable ground.<br><br>Being saved by Dark Passage or using Death Sentence on one of the three <font color='#3091ec'>Gravity Anchors</font> will briefly put you into this invulnerable state and break enemy chains on you.",
            "id": 3694,
            "name": "Cloak of Stars"
        },
        "3695": {
            "description": "<passive>Passive - Stellar Fealty: </passive>Thresh cannot kill units directly - their souls, experience, and gold belong to the Dark Star.<br><br>Pulling or pushing an enemy into the Dark Star will destroy them instantly, scoring points for your team (+5, or +1 for Abyss Scuttlers).<br><br>Winning a round requires 100 points, and the final points must be from a champion kill.",
            "id": 3695,
            "name": "Dark Star Sigil"
        },
        "3706": {
            "plaintext": "Lets your Smite slow Champions",
            "description": "<groupLimit>Limited to 1 Jungle item</groupLimit><br><br><stats>+10% Life Steal vs. Monsters<br><mana>+225% Base Mana Regen while in Jungle</mana></stats><br><br><unique>UNIQUE Passive - Chilling Smite:</unique> Smite can be cast on enemy champions, dealing reduced true damage and stealing 20% Movement Speed for 2 seconds.<br><unique>UNIQUE Passive - Tooth / Nail:</unique> Basic attacks vs. monsters deal @Effect2Amount@ bonus damage and grant you @Effect12Amount@% bonus Attack Speed for @Effect11Amount@ seconds. Damaging a monster with a spell or attack steals @Effect1Amount@ Health over @Effect4Amount@ seconds and burns them for @Effect13Amount@ magic damage. Killing monsters grants <font color='#99BBBB'><a href='SpecialJungleExperience'>special bonus experience</a></font>.",
            "id": 3706,
            "name": "Stalker's Blade"
        },
        "3715": {
            "plaintext": "Lets your Smite mark Champions, giving you combat power against them.",
            "description": "<groupLimit>Limited to 1 Jungle item</groupLimit><br><br><stats>+10% Life Steal vs. Monsters<br><mana>+225% Base Mana Regen while in Jungle</mana></stats><br><br><passive>Passive - Challenging Smite:</passive> Smite can be cast on enemy champions, marking them for 4 seconds. While marked, the target is revealed, your basic attacks deal bonus true damage over 3 seconds, and their damage to you is reduced by 20%.<br><unique>UNIQUE Passive - Tooth / Nail:</unique> Basic attacks vs. monsters deal @Effect2Amount@ bonus damage and grant you @Effect12Amount@% bonus Attack Speed for @Effect11Amount@ seconds. Damaging a monster with a spell or attack steals @Effect1Amount@ Health over @Effect4Amount@ seconds and burns them for @Effect13Amount@ magic damage. Killing monsters grants <font color='#99BBBB'><a href='SpecialJungleExperience'>special bonus experience</a></font>.",
            "id": 3715,
            "name": "Skirmisher's Sabre"
        },
        "3742": {
            "plaintext": "Build momentum as you move around then smash into enemies.",
            "description": "<stats>+425 Health<br>+60 Armor</stats><br><br><unique>UNIQUE Passive - Dreadnought:</unique> While moving, build stacks of Momentum, increasing movement speed by up to 60 at 100 stacks. Momentum decays while under the effect of a stun, taunt, fear, polymorph, or immobilize effect.<br><unique>UNIQUE Passive - Crushing Blow:</unique> Basic attacks deal 1 magic damage per stack of Momentum, discharging all stacks. At max stacks, if the attacker is melee, they also slow the target by 50% for 1 second.<br><br><flavorText>''There's only one way you'll get this armor from me...'' - forgotten namesake</flavorText>",
            "id": 3742,
            "name": "Dead Man's Plate"
        },
        "3748": {
            "plaintext": "Deals area of effect damage based on owner's health",
            "description": "<stats>+450 Health<br>+40 Attack Damage<br>+100% Base Health Regen </stats><br><br><unique>UNIQUE Passive - Cleave:</unique> Basic attacks deal 5 + 1% of your maximum health as bonus physical damage  to your target and 40 + 2.5% of your maximum health as physical damage  to other enemies in a cone on hit.<br><active>UNIQUE Active - Crescent:</active> Cleave damage to all targets is increased to 40 + 10% of your maximum health as bonus physical damage  in a larger cone for your next basic attack (20 second cooldown).<br><br><rules>(Unique Passives with the same name don't stack.)</rules>",
            "id": 3748,
            "name": "Titanic Hydra"
        },
        "3751": {
            "plaintext": "Grants Health and Immolate Aura",
            "description": "<stats>+200 Health  </stats><br><br><unique>UNIQUE Passive - Immolate:</unique> Deals 5 (+1 per champion level) magic damage per second to nearby enemies. Deals 100% bonus damage to minions and monsters.",
            "id": 3751,
            "name": "Bami's Cinder"
        },
        "3800": {
            "plaintext": "Grants Health, Mana, and Armor. Activate to speed towards enemies and slow them.",
            "description": "<stats>+400 Health<br><mana>+300 Mana</mana><br>+30 Armor<br>+100% Base Health Regen <br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Active:</unique> Grants 75% Movement Speed when moving towards enemies or enemy turrets for 4 seconds. Once near an enemy (or after 4 seconds) a shockwave is emitted, slowing nearby enemy champion Movement Speed by 75% for 2 second(s) (90 second cooldown).",
            "id": 3800,
            "name": "Righteous Glory"
        },
        "3801": {
            "plaintext": "Grants Health and Health Regen",
            "description": "<stats>+200 Health<br>+50% Base Health Regen </stats>",
            "id": 3801,
            "name": "Crystalline Bracer"
        },
        "3802": {
            "plaintext": "Restores Mana upon levelling up.",
            "description": "<stats>+25 Ability Power<br><mana>+300 Mana</mana></stats><br><br><unique>UNIQUE Passive - Haste:</unique> +10% Cooldown Reduction<br><unique>UNIQUE Passive:</unique> Upon levelling up, restores 20% of your maximum Mana over 3 seconds.",
            "id": 3802,
            "name": "Lost Chapter"
        },
        "3812": {
            "plaintext": "Trades incoming damage now for incoming damage later",
            "description": "<stats>+80 Attack Damage<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Passive:</unique> Dealing physical damage heals for 15% of the damage dealt. This is 33% as effective for Area of Effect damage.<br><unique>UNIQUE Passive:</unique> 30% of damage taken is dealt as a Bleed effect over 3 seconds instead.",
            "id": 3812,
            "name": "Death's Dance"
        },
        "3814": {
            "plaintext": "Blocks an incoming enemy spell.",
            "description": "<stats>+250 Health<br>+55 Attack Damage</stats><br><br><unique>UNIQUE Passive:</unique> +18 <a href='Lethality'>Lethality</a><br><unique>UNIQUE Active - Night's Veil:</unique> Channel for 1.5 second to grant a spell shield that blocks the next enemy ability. Lasts for 7 seconds (40 second cooldown).<br><br><rules>(Can move while channeling, but taking damage breaks the channel.)</rules>",
            "id": 3814,
            "name": "Edge of Night"
        },
        "3901": {
            "plaintext": "Cannon Barrage gains extra waves",
            "description": "Requires 500 Silver Serpents.<br><br><unique>UNIQUE Passive:</unique> Cannon Barrage fires at an increasing rate over time (additional 6 waves over the duration).",
            "id": 3901,
            "name": "Fire at Will"
        },
        "3902": {
            "plaintext": "Cannon Barrage fires a mega-cannonball",
            "description": "Requires 500 Silver Serpents.<br><br><unique>UNIQUE Passive:</unique> Cannon Barrage additionally fires a mega-cannonball at center of the Barrage, dealing 300% true damage and slowing them by 60% for 1.5 seconds. ",
            "id": 3902,
            "name": "Death's Daughter"
        },
        "3903": {
            "plaintext": "Cannon Barrage hastes allies",
            "description": "Requires 500 Silver Serpents.<br><br><unique>UNIQUE Passive:</unique> Allies in the Cannon Barrage gain 30% Movement Speed for 2 seconds.",
            "id": 3903,
            "name": "Raise Morale"
        },
        "3905": {
            "plaintext": "Increases Ability Power and Movement Speed",
            "description": "<stats>+60 Ability Power<br>+7% Movement Speed<br>+10% Cooldown Reduction</stats><br><br><unique>UNIQUE Active - Spectral Pursuit:</unique> Summons 2 spooky ghosts that hunt down nearby champions, revealing and Haunting them on contact. <br><br>Haunted enemies are slowed by 40% for up to 5 seconds based on the distance the ghosts travel. (90 second cooldown).",
            "id": 3905,
            "name": "Twin Shadows"
        },
        "3907": {
            "plaintext": "Stores nearby spellcasts and can consume them to grant Movement Speed and Ability Power.",
            "description": "<stats>+100 Ability Power<br>+10% Movement Speed<br></stats><br><unique>UNIQUE Passive:</unique> Nearby allied and enemy spellcasts charge Spellbinder up to a cap (100 maximum). <br><unique>UNIQUE Active:</unique> Gain a maximum of 100 Ability Power and 30% decaying Movement Speed for 4 seconds. <br><br>Each spellcast stored contributes +1 Ability Power and +0.3% Movement Speed to the effect. (60 second cooldown).",
            "id": 3907,
            "name": "Spellbinder"
        },
        "3916": {
            "plaintext": "Increases magic damage",
            "description": "<stats>+25 Ability Power<br>+200 Health</stats><br><br><unique>UNIQUE Passive - Touch of Death:</unique> +15 <a href='FlatMagicPen'>Magic Penetration</a>",
            "id": 3916,
            "name": "Oblivion Orb"
        }
    }
}'

json_data_summoner_spells = '{
    "type": "summoner",
    "version": "8.8.1",
    "data": {
        "SummonerSiegeChampSelect2": {
            "id": 34,
            "summonerLevel": 1,
            "name": "Nexus Siege: Siege Weapon Slot",
            "key": "SummonerSiegeChampSelect2",
            "description": "In Nexus Siege, Summoner Spells are replaced with Siege Weapon Slots. Spend Crystal Shards to buy single-use Siege Weapons from the item shop, then use your Summoner Spell keys to activate them!"
        },
        "SummonerTeleport": {
            "id": 12,
            "summonerLevel": 7,
            "name": "Teleport",
            "key": "SummonerTeleport",
            "description": "After channeling for 4.5 seconds, teleports your champion to target allied structure, minion, or ward."
        },
        "SummonerSiegeChampSelect1": {
            "id": 33,
            "summonerLevel": 1,
            "name": "Nexus Siege: Siege Weapon Slot",
            "key": "SummonerSiegeChampSelect1",
            "description": "In Nexus Siege, Summoner Spells are replaced with Siege Weapon Slots. Spend Crystal Shards to buy single-use Siege Weapons from the item shop, then use your Summoner Spell keys to activate them!"
        },
        "SummonerExhaust": {
            "id": 3,
            "summonerLevel": 4,
            "name": "Exhaust",
            "key": "SummonerExhaust",
            "description": "Exhausts target enemy champion, reducing their Movement Speed by 30%, and their damage dealt by 40% for 2.5 seconds."
        },
        "SummonerBarrier": {
            "id": 21,
            "summonerLevel": 4,
            "name": "Barrier",
            "key": "SummonerBarrier",
            "description": "Shields your champion from 115-455 damage (depending on champion level) for 2 seconds."
        },
        "SummonerMana": {
            "id": 13,
            "summonerLevel": 6,
            "name": "Clarity",
            "key": "SummonerMana",
            "description": "Restores 50% of your champion's maximum Mana. Also restores allies for 25% of their maximum Mana."
        },
        "SummonerSnowURFSnowball_Mark": {
            "id": 39,
            "summonerLevel": 6,
            "name": "Ultra (Rapidly Flung) Mark",
            "key": "SummonerSnowURFSnowball_Mark",
            "description": "It's a snowball! It's a Poro! It's...uh...one of those."
        },
        "SummonerFlash": {
            "id": 4,
            "summonerLevel": 7,
            "name": "Flash",
            "key": "SummonerFlash",
            "description": "Teleports your champion a short distance toward your cursor's location."
        },
        "SummonerSnowball": {
            "id": 32,
            "summonerLevel": 6,
            "name": "Mark",
            "key": "SummonerSnowball",
            "description": "Throw a snowball in a straight line at your enemies. If it hits an enemy, they become marked, granting True Sight, and your champion can quickly travel to the marked target as a follow up."
        },
        "SummonerDot": {
            "id": 14,
            "summonerLevel": 9,
            "name": "Ignite",
            "key": "SummonerDot",
            "description": "Ignites target enemy champion, dealing 80-505 true damage (depending on champion level) over 5 seconds, grants you vision of the target, and reduces healing effects on them for the duration."
        },
        "SummonerDarkStarChampSelect2": {
            "id": 36,
            "summonerLevel": 1,
            "name": "Disabled Summoner Spells",
            "key": "SummonerDarkStarChampSelect2",
            "description": "Summoner spells are disabled in this mode."
        },
        "SummonerDarkStarChampSelect1": {
            "id": 35,
            "summonerLevel": 1,
            "name": "Disabled Summoner Spells",
            "key": "SummonerDarkStarChampSelect1",
            "description": "Summoner spells are disabled in this mode."
        },
        "SummonerPoroRecall": {
            "id": 30,
            "summonerLevel": 1,
            "name": "To the King!",
            "key": "SummonerPoroRecall",
            "description": "Quickly travel to the Poro King's side."
        },
        "SummonerHaste": {
            "id": 6,
            "summonerLevel": 1,
            "name": "Ghost",
            "key": "SummonerHaste",
            "description": "Your champion gains increased Movement Speed and can move through units for 10 seconds. Grants a maximum of 28-45% (depending on champion level) Movement Speed after accelerating for 2 seconds."
        },
        "SummonerHeal": {
            "id": 7,
            "summonerLevel": 1,
            "name": "Heal",
            "key": "SummonerHeal",
            "description": "Restores 90-345 Health (depending on champion level) and grants 30% Movement Speed for 1 second to you and target allied champion. This healing is halved for units recently affected by Summoner Heal."
        },
        "SummonerPoroThrow": {
            "id": 31,
            "summonerLevel": 1,
            "name": "Poro Toss",
            "key": "SummonerPoroThrow",
            "description": "Toss a Poro at your enemies. If it hits, you can quickly travel to your target as a follow up."
        },
        "SummonerBoost": {
            "id": 1,
            "summonerLevel": 9,
            "name": "Cleanse",
            "key": "SummonerBoost",
            "description": "Removes all disables (excluding suppression and airborne) and summoner spell debuffs affecting your champion and lowers the duration of incoming disables by 65% for 3 seconds."
        },
        "SummonerSmite": {
            "id": 11,
            "summonerLevel": 9,
            "name": "Smite",
            "key": "SummonerSmite",
            "description": "Deals 390-1000 true damage (depending on champion level) to target epic, large, or medium monster or enemy minion. Restores Health based on your maximum life when used against monsters."
        }
    }
}'