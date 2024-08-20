# app/crud.py
from sqlalchemy.orm import Session
from api import models, schemas

def get_player(db: Session, player_id: str):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def get_player_by_name(db: Session, name: str):
    return db.query(models.Player).filter(models.Player.name == name).first()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(
        player_white_id=game.player_white_id,
        player_black_id=game.player_black_id,
        result=game.result,
        date_played=game.date_played
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_games(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Game).offset(skip).limit(limit).all()
