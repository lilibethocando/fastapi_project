from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, conint, ValidationError

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

try:
    PostBase(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_type'


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserOut

    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True


# Exclude validate method
PostOut.__annotations__ = {'Post': Post, 'votes': int}


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)