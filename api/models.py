# api/models.py
import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, index=True, nullable=False)

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    player_white_id = Column(String(36), ForeignKey('players.id'), nullable=False)
    player_black_id = Column(String(36), ForeignKey('players.id'), nullable=False)
    result = Column(String(10), nullable=False)
    date_played = Column(DateTime, nullable=False)

    player_white = relationship("Player", foreign_keys=[player_white_id])
    player_black = relationship("Player", foreign_keys=[player_black_id])
