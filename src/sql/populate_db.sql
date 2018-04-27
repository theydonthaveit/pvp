insert into user_account (username, password, mobile, email, ip_address, is_verified) values ('meow side', '123', '07901648812', 'alan@test.com', '127.0.0.1', true);
insert into game_list (game) values ('League of Legends');
insert into user_location (country, postal_code, user_account_id) values ('UK', 'SE16 4AE', 1);
insert into gamer_profile (user_account_id, game_list_id) values (1, 1);
insert into league_of_legends_profile_base (gamer_profile_id, summoner_name, account_level, account_id, summoner_id, mmr) values (1, 'meow side', 61, 234897405, 102738872, 1873);