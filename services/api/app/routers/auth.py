from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(tags=["auth"])


class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/signup", response_model=TokenResponse, status_code=201)
def signup(body: SignupRequest):
    # TODO: persist user, hash password, issue JWT
    return TokenResponse(access_token="stub-token")


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest):
    # TODO: verify credentials, issue JWT
    return TokenResponse(access_token="stub-token")
