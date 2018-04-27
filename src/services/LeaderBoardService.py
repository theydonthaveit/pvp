from database_setup import Engine, UserLocation, GameList, GamerProfile, LeagueOfLegendsProfileBase
from sqlalchemy.orm import sessionmaker
from Utils import retrieve_user_mmr

Session = sessionmaker(bind=Engine)
session = Session()


class LeaderBoardService(object):

    def leader_board_for_user(self, user_id, summoner_id):
        user_stats = retrieve_user_mmr(summoner_id)
        user_location = self.user_location(user_id)
        leader_board_region = self.leader_board_for_region(user_location.postal_code)
        leader_board_for_user_list = self.leader_board_check_for_user(user_id, leader_board_region, user_stats)
        return leader_board_for_user_list

    def leader_board_check_for_user(self, user_id, leader_board_region, user_stats):
        for lbr in leader_board_region:
            if lbr.user_account_id == user_id:
                return leader_board_region
            else:
                return self.add_user_to_leader_board(leader_board_region, user_stats)

    @staticmethod
    def user_location(user_id):
        return session.query(UserLocation).filter_by(user_account_id=user_id).first()

    @staticmethod
    def leader_board_for_region(user_postal_code):
        return session.query(UserLocation).filter_by(postal_code=user_postal_code).limit(10).all()

    @staticmethod
    def add_user_to_leader_board(leader_board_region, user_stats):
        leader_board_region.append(user_stats)
        return leader_board_region
