CREATE TABLE games (
    id VARCHAR(10) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(30) NOT NULL,
    player_id VARCHAR(30),
    player_rating INT,
    winner VARCHAR(10),
    opening VARCHAR(100)
);


-- Need to add column to track player color instead of player id
-- Need to drop and readd table upon each fetch to have fresh data / no duplicates