import bcrypt
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()


class BcryptNameRequest(BaseModel):
    name: str


def bcrypt_name(name: str) -> str:
    name_bytes = name.encode("utf-8")
    hashed = bcrypt.hashpw(name_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


@router.post("/bcrypt-name")
async def bcrypt_name_endpoint(request: BcryptNameRequest):
    return {
        "original_name": request.name,
        "bcrypt_hash": bcrypt_name(request.name)
    }
