import asyncpg
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from email_validator import validate_email, EmailNotValidError
import re

import random2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from redis_om import get_redis_connection

from app.jwtModel import UserSchema, UserLoginSchema
from app.auth.jwtBearer import JWTBearer
from app.auth.jwtHandler import decode_jwt_token

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from decouple import config
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


redis = get_redis_connection(
    host="redis-10788.c282.east-us-mz.azure.cloud.redislabs.com",
    port=10788,
    password="yKCjtyQum735j4UL1FeO914Ci9etLHwf",
    decode_responses=True
)


# @app.on_event("startup")
# async def startup():
#    try:
#        app.pool = await asyncpg.create_pool(user=config("DATABASE_USER"), password=config("DATABASE_PWD"),
#                                             database=config("DATABASE_NAME"), host=config("DATABASE_HOST"))
#        print("Database connection successful")
#    except Exception as e:
#        print(f"Database connection failed: {e}")


#@app.on_event("shutdown")
#async def shutdown():
#    await app.pool.close()


@app.get("/")
def default():
    return {"Welcome": "Our Page"}


@app.post("/sign_up", tags=["users"])
def create_new_user(user: UserSchema = Body(...)):
    sign_up_control(user.email, user.password)

    return {"Koçum": "Olacak Bu İş"}


def sign_up_control(email, password):
    key = random_key_generator()
    store_verification_code(email, key)
    email_control(email)
    password_control(password)
    email_sender(email, key)


def email_control(email):
    if email == None:
        raise HTTPException(status_code=400, detail="Email Area Empty")
    elif email == None:
        raise HTTPException(status_code=400, detail="Email is already exist")
    elif "@" not in email or "." not in email:
        raise HTTPException(status_code=400, detail="Invalid Email")
    elif not validate_email(email):
        raise HTTPException(status_code=400, detail="Invalid Email")
    else:
        print(email, "  : Valid")


def password_control(password):
    pattern = r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*\W).{8,20}$"
    if not re.match(pattern, password):
        raise HTTPException(status_code=400, detail="Invalid Password")


def email_sender(email, key):
    message = Mail(
        from_email='magictahsilat@gmail.com',
        to_emails=email,
        subject='MagicTahsilat Email Validation',
        html_content='Hello,\n Your Validation Key is'+key)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)
    return "Email Sent"


def random_key_generator():
    return str(random2.randint(100_000, 999_999))


def store_verification_code(email, code):
    """Store the verification code in Redis."""
    try:
        redis.setex(email + ":verification_code", 600, code)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to store verification code.")
