import reflex as rx
from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship

import sqlalchemy


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ChatSession(rx.Model, table=True):
    """Table for chat sessions"""
    __tablename__ = "chatsession"  # ✅ Explicit table name

    id: int = Field(default=None, primary_key=True)
    messages: List["ChatSessionMessageModel"] = Relationship(back_populates="session")

    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )

    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "onupdate": sqlalchemy.func.now(),
            "server_default": sqlalchemy.func.now(),
        },
        nullable=False,
    )


class ChatSessionMessageModel(rx.Model, table=True):  # ✅ Change to `rx.Model`
    """Table for chat session messages"""
    __tablename__ = "chatsessionmessagemodel"  # ✅ Explicit table name

    id: int = Field(default=None, primary_key=True)
    session_id: int = Field( foreign_key="chatsession.id",nullable=False)  # ✅ Set nullable=True
    session: "ChatSession" = Relationship(back_populates="messages")  # ✅ Fix typing issue

    content: str
    role: str


    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )


    