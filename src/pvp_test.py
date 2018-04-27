import requests
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, lazyload

from database_setup import Base, Engine, UserAccount

DBsession = sessionmaker(bind=Engine)
session = DBsession()

user = session.query(UserAccount).filter_by(id=8).first()
for ugp in user.gamer_profile:
    print(ugp.game_list_id)
# from services.LeaderBoardService import LeaderBoardService

# new_user = {
#     'mobile': "07901648815",
#     'email': "alan@test4.com",
#     'ip_address': "127.0.0.1"
# }

# r = requests.post("http://127.0.0.1:5000/signup", json=new_user)

# build_profile_data = {
#     'country': "United Kingdom",
#     'postal_code': "SE16 4AE",
#     'game': "League of Legends",
#     'summoner_name': "meow side",
#     'server': "EUW1"
# }

# r = requests.post("http://127.0.0.1:5000/build_gamer_profile/8", json=build_profile_data)

# LBS = LeaderBoardService()
# LBS.leader_board_for_user(8, 102738872)

# API_KEY='RGAPI-8deb9004-e152-47a5-8a93-bf555a8def65'
# HEADERS={
#     "Origin": 'null',
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#     "X-Riot-Token": API_KEY,
#     "Accept-Language": "en-GB,en;q=0.5"
# }

# def build_user_basic_profile(participants_json):

#     for participant in participants_json:
#         base = participant['players']
#         print(base['summonerName'])
#         # base['summonerId'] - used to build out profile
#         # base['accountId'] - used to build out profile


# def async_requests(urls):
#     data = []

#     for url in urls:
#         res = requests.get(url, headers=HEADERS)
#         useable_data_json = res.json()
#         build_user_basic_profile(useable_data_json['participantIdentities'])
#         data.append(res.json())
#         time.sleep(1)

#     return data

# def generate_urls(match_list_url=None, match_list=None):
#     urls = []

#     if match_list is None:
#         match_list = get_requests(match_list_url)

#     for match in match_list.json()['matches']:
#         urls.append(
#             'https://euw1.api.riotgames.com/lol/match/v3/matches/%s' % (match['gameId'])
#         )

#     return urls

# def get_requests(url):
#     res = requests.get(url, headers=HEADERS)
#     return res.json()

# async_requests(
#     generate_urls('https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/234897405?champion=19&queue=420&season=11')
# )