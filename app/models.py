from typing import Optional, List

from pydantic import BaseModel, ValidationError  # noqa: F401


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    id: str
    email: Optional[str] = None
    alias: Optional[str] = None
    disabled: Optional[bool] = None


class TokenData(BaseModel):
    sub: str
    user: User
    scopes: Optional[List[str]] = []
    exp: Optional[int]


class ApiStatus(BaseModel):
    status: str
