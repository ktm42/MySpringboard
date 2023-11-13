--Design a schema for a simple sports league. Your schema shoul keep track of
    --All of the teams in the league
    --All of the goals scored by every player for each game
    --All of the players in the league and their corresponding teams
    --All of the referees who have been part of each game
    --All of the matches played between teams
    --All of the start and end dates for season that a league has
    --The standings/rankings of each team in the league (This doesn't have to be its own table if the data can be captured somehow).

CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
)

CREATE TABLE season(
    id SERIAL PRIMARY KEY,
    start_date INTEGER NOT NULL,
    end_date INTEGER NOT Null,
)

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    team_id INTEGER REFERENCES teams,
)

CREATE TABLE refs(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
)

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    home_id INTEGER REFERENCES teams,
    away_id INTEGER REFERENCES teams,
    location TEXT NOT NULL,
    date INTEGER NOT NULL,
    season_id INTEGER REFERENCES season,
    head_ref_id INTEGER REFERENCES refs,
    asst_ref_1 INTEGER REFERENCES refs,
    asst_ref_2 INTEGER REFERENCES refs,
)

CREATE TABLE results(
    id SERIAL PRIMARY KEY,
    match_id INTEGER REFERENCES matches,
    outcome TEXT needs to equal win, loss, tie
)

CREATE TABLE goals(
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players,
    match_id INTEGER REFERENCES matches,
)