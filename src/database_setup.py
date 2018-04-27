import sys
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.hash import pbkdf2_sha512

Base = declarative_base()


class BaseMixin(object):

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, unique=True)

    @declared_attr
    def created_at(self):
        return Column(DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, default=datetime.datetime.utcnow)


class UserAccount(Base, BaseMixin):
    __tablename__ = 'user_account'

    def __init__(self, username, passcode, mobile, email, ip_address):
        self.username = username
        self.password = pbkdf2_sha512.hash(passcode)
        self.mobile = mobile
        self.email = email
        self.ip_address = ip_address

    username = Column(String(80), nullable=False)
    password = Column(String(1000), nullable=False)
    mobile = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    ip_address = Column(String(15), nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    user_location = relationship("UserLocation", uselist=False, back_populates="user_account")
    gamer_profile = relationship("GamerProfile")

    # Not implemented: part of email / mobile account verification
    def is_verified_check(self):
        return self.is_verified

    def decode_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)


class UserLocation(Base, BaseMixin):
    __tablename__ = 'user_location'

    country = Column(String(100), nullable=False)
    postal_code = Column(String(12), nullable=False)
    user_account_id = Column(Integer, ForeignKey('user_account.id'))
    user_account = relationship("UserAccount", back_populates="user_location", foreign_keys=[user_account_id])


class GamerProfile(Base, BaseMixin):
    __tablename__ = 'gamer_profile'

    user_account_id = Column(Integer, ForeignKey('user_account.id'))
    game_list_id = Column(Integer, nullable=False)
    league_of_legends_profile_base = relationship("LeagueOfLegendsProfileBase", uselist=False, back_populates="gamer_profile")


class GameList(Base, BaseMixin):
    __tablename__ = 'game_list'

    game = Column(String(100), nullable=False)


class LeagueOfLegendsProfileBase(Base, BaseMixin):
    __tablename__ = 'league_of_legends_profile_base'

    gamer_profile_id = Column(Integer, ForeignKey('gamer_profile.id'))
    gamer_profile = relationship("GamerProfile", back_populates="league_of_legends_profile_base", foreign_keys=[gamer_profile_id])
    summoner_name= Column(String(25), nullable=False)
    account_level = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False, unique=True)
    summoner_id = Column(Integer, nullable=False, unique=True)
    mmr = Column(Integer, nullable=False)


# class LeagueOfLegendsChampionMastery(Base, BaseMixin):
#     __tablename__ = 'league_of_legends_champion_mastery'

#     league_of_legends_profile_base_id = Column(Integer, ForeignKey('league_of_legends_profile_base.id'))
#     champion_name = Column(Integer, nullable=False)
#     champion_level = Column(Integer, nullable=False)
#     champion_points = Column(Integer, nullable=False)
#     last_play_time = Column(Integer, nullable=False)


# class LeagueOfLegendsLeaguePositionSolo(Base, BaseMixin):
#     __tablename__ = 'league_of_legends_league_position_solo'

#     league_of_legends_profile_base_id = Column(Integer, ForeignKey('league_of_legends_profile_base.id'))
#     league_id = Column(String(50), nullable=False)
#     tier = Column(String(20), nullable=False)
#     league_Points = Column(Integer, nullable=False)
#     wins = Column(Integer, nullable=False)
#     losses = Column(Integer, nullable=False)
#     veteran = Column(Boolean, nullable=False)
#     inactive = Column(Boolean, nullable=False)


# class LeagueOfLegendsMatchList(Base, BaseMixin):
#     __tablename__ = 'league_of_legends_match_list'

#     league_of_legends_profile_base_id = Column(Integer, ForeignKey('league_of_legends_profile_base.id'))
#     game_id = Column(Integer, nullable=False)
#     champion_name = Column(String(50), nullable=False)
#     queue_type = Column(String(20), nullable=False)
#     season = Column(Integer, nullable=False)
#     timestamp = Column(Integer, nullable=False)
#     role = Column(String(20), nullable=False)
#     lane = Column(String(20), nullable=False)


# class LeagueOfLegendsChampionInfo(Base, BaseMixin):
#     __tablename__ = 'league_of_legends_champion_info'

#     champion_id = Column(Integer, nullable=False)
#     name = Column(String(100), nullable=False)

Engine = create_engine('postgres://localhost:5434/pvp')
Base.metadata.create_all(Engine)
