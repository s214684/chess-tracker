# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PlayerCreate(BaseModel):
    name: str

class Player(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

class GameCreate(BaseModel):
    player_white_id: str
    player_black_id: str
    result: str
    date_played: datetime

class Game(BaseModel):
    id: int
    player_white_id: str
    player_black_id: str
    result: str
    date_played: datetime
    player_white: Player
    player_black: Player

    class Config:
        orm_mode = True
