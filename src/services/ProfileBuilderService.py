import requests
import json
import time
from champion_db import champion_dict

from database_setup import Engine, UserLocation, GameList, GamerProfile, LeagueOfLegendsProfileBase
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=Engine)
session = Session()

# TODO
"""
Regions can be passed in from the URL
SummonerID can be a unique identifier and passed in from URL
AccountID can be a unique identifier and passed in from URL
need to refactor
"""

class ProfileBuilderService(object):

    API_KEY='RGAPI-8909cbe6-df46-49f0-8f73-49d1cd63f3c2'
    HEADERS={
        "Origin": 'null',
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": API_KEY,
        "Accept-Language": "en-GB,en;q=0.5"
    }


    def build_summoner_url(self, region, playerName):
        BASE_URL = 'https://%s.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s' % (region, playerName)
        return BASE_URL

    def build_champion_mastery_url(self, region, summonerId):
        BASE_URL = 'https://%s.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/%s' % (region, summonerId)
        return BASE_URL

    def build_champion_info_url(self, region, championId):
        BASE_URL = 'https://%s.api.riotgames.com/lol/static-data/v3/champions/%s' % (region, championId)
        return BASE_URL

    def build_recent_match_list_url(self, region, accountId):
        BASE_URL = 'https://%s.api.riotgames.com/lol/match/v3/matchlists/by-account/%s/recent' % (region, accountId)
        return BASE_URL

    def build_mmr_url(self, region, summonerId):
        BASE_URL = 'https://%s.api.riotgames.com/lol/league/v3/mmr-af/by-summoner/%s' % (region, summonerId)
        return BASE_URL

    def build_league_url(self, region, summonerId):
        BASE_URL = 'https://%s.api.riotgames.com/lol/league/v3/positions/by-summoner/%s' % (region, summonerId)
        return BASE_URL

    def build_static_champion_data_url(self, region):
        BASE_URL = 'https://%s.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&champListData=all&tags=all&dataById=false' % (region)
        return BASE_URL


    def build_profile(self, data, user_id):
        profile_data = []

        game = session.query(GameList).filter_by(game=data['game']).first()

        user_location = UserLocation(
            country = data['country'],
            postal_code = data['postal_code'],
            user_account_id = user_id
        )
        session.add(user_location)
        gamer_profile = GamerProfile(
            user_account_id = user_id,
            game_list_id = game.id
        )
        session.add(gamer_profile)
        session.commit()

        init_res = self.initial_call(data['server'], data['summoner_name'])

        lolpb = LeagueOfLegendsProfileBase(
            gamer_profile_id = gamer_profile.id,
            summoner_name = data['summoner_name'],
            account_level = init_res['summonerLevel'],
            account_id = init_res['accountId'],
            summoner_id = init_res['id'],
            mmr = 1998
        )
        session.add(lolpb)
        session.commit()
        # champion_mastery_res = self.retrieve_champion_mastery(region, init_res['id'])
        # recent_match_list_res = self.retrieve_recent_games(region, init_res['accountId'])
        # league_res = self.retrieve_legaue(region, init_res['id'])

        # profile_data.extend([
        #     init_res,
        #     mmr_res,
        #     league_res,
        #     recent_match_list_res
        # ])

        # for cmr in champion_mastery_res:
        #     cmr_champ_id_string = str(cmr['championId'])
        #     if cmr_champ_id_string in champion_dict:
        #         cmr['championName'] = champion_dict[cmr_champ_id_string]

        # profile_data.extend(champion_mastery_res)

        return 'profile_data'


    def initial_call(self, region, playerName):
        url = self.build_summoner_url(region, playerName)
        res = requests.get(url, headers=self.HEADERS)
        return res.json()

    def retrieve_champion_mastery(self, region, summonerId):
        url = self.build_champion_mastery_url(region, summonerId)
        res = requests.get(url, headers=self.HEADERS)
        return res.json()

    def retrieve_recent_games(self, region, accountId):
        url = self.build_recent_match_list_url(region, accountId)
        res = requests.get(url, headers=self.HEADERS)
        return res.json()

    def retrieve_mmr(self, region, summonerId):
        url = self.build_mmr_url(region, summonerId)
        res = requests.get(url, headers=self.HEADERS)
        return res.json()

    def retrieve_legaue(self, region, summonerId):
        url = self.build_league_url(region, summonerId)
        res = requests.get(url, headers=self.HEADERS)
        return res.json()


    # Utilities
    def async_requests(self, urls):
        data = []

        for url in urls:
            res = requests.get(url, headers=self.HEADERS)
            data.append(res.json())
            time.sleep(1)

        return data

    def retrieve_summoner_id(self, region, playerName):
        res = self.initial_call(region, playerName)
        return res['id']

    def retrieve_account_id(self, region, playerName):
        res = self.initial_call(region, playerName)
        return res['accountId']

    def retrieve_summoner_level(self, region, playerName):
        res = self.initial_call(region, playerName)
        return res['summonerLevel']