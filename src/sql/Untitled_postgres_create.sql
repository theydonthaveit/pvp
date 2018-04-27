drop schema public cascade;
create schema public;

CREATE TABLE "user_account" (
	"username" VARCHAR(80) NOT NULL UNIQUE,
	"id" serial NOT NULL UNIQUE,
	"password" VARCHAR(1000) NOT NULL,
	"mobile" VARCHAR(15) NOT NULL UNIQUE,
	"email" VARCHAR(100) NOT NULL UNIQUE,
	"ip_address" VARCHAR(15) NOT NULL,
	"is_verified" BOOLEAN NOT NULL,
	"create_at" TIMESTAMP NOT NULL,
	"user_location" integer NOT NULL,
	CONSTRAINT user_account_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "user_location" (
	"id" serial NOT NULL,
	"country" VARCHAR(100) NOT NULL,
	"postal_code" VARCHAR(12) NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	CONSTRAINT user_location_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "gamer_profile" (
	"id" serial NOT NULL,
	"game_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"game_profile" integer NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	CONSTRAINT gamer_profile_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "game_list" (
	"id" serial NOT NULL,
	"game_title" VARCHAR(50) NOT NULL UNIQUE,
	"created_at" TIMESTAMP NOT NULL,
	CONSTRAINT game_list_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "league_of_legends_profile" (
	"id" serial NOT NULL,
	"summoner_name" VARCHAR(50) NOT NULL,
	"account_level" integer NOT NULL,
	"account_id" integer NOT NULL UNIQUE,
	"summoner_id" integer NOT NULL UNIQUE,
	"created_at" TIMESTAMP NOT NULL,
	"mmr" integer NOT NULL,
	CONSTRAINT league_of_legends_profile_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "league_of_legends_matches" (
	"id" serial NOT NULL,
	"match_id" integer NOT NULL UNIQUE,
	"league_of_legends_profile_id" integer NOT NULL,
	CONSTRAINT league_of_legends_matches_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "league_of_legends_champion_mastery" (
	"id" serial NOT NULL,
	"champion_name" VARCHAR(50) NOT NULL UNIQUE,
	"champion_id" integer NOT NULL UNIQUE,
	"league_of_legends_profile_id" integer NOT NULL,
	CONSTRAINT league_of_legends_champion_mastery_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "league_of_legends_stats" (
	"id" serial NOT NULL,
	"league_of_legends_profile_id" integer NOT NULL,
	"rank" VARCHAR(10) NOT NULL,
	CONSTRAINT league_of_legends_stats_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "user_account" ADD CONSTRAINT "user_account_fk0" FOREIGN KEY ("user_location") REFERENCES "user_location"("id");


ALTER TABLE "gamer_profile" ADD CONSTRAINT "gamer_profile_fk0" FOREIGN KEY ("game_id") REFERENCES "game_list"("id");
ALTER TABLE "gamer_profile" ADD CONSTRAINT "gamer_profile_fk1" FOREIGN KEY ("user_id") REFERENCES "user_account"("id");
ALTER TABLE "gamer_profile" ADD CONSTRAINT "gamer_profile_fk2" FOREIGN KEY ("game_profile") REFERENCES "league_of_legends_profile"("id");



ALTER TABLE "league_of_legends_matches" ADD CONSTRAINT "league_of_legends_matches_fk0" FOREIGN KEY ("league_of_legends_profile_id") REFERENCES "league_of_legends_profile"("id");

ALTER TABLE "league_of_legends_champion_mastery" ADD CONSTRAINT "league_of_legends_champion_mastery_fk0" FOREIGN KEY ("league_of_legends_profile_id") REFERENCES "league_of_legends_profile"("id");

ALTER TABLE "league_of_legends_stats" ADD CONSTRAINT "league_of_legends_stats_fk0" FOREIGN KEY ("league_of_legends_profile_id") REFERENCES "league_of_legends_profile"("id");

