import asyncpg
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from email_validator import validate_email, EmailNotValidError
import re
from fastapi import Depends
import json
import random2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker,Session
from redis_om import get_redis_connection

from app.jwtModel import UserSchema, UserLoginSchema
from app.auth.jwtBearer import JWTBearer
from app.auth.jwtHandler import decode_jwt_token

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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


app = FastAPI()

redis = get_redis_connection(
    host = "redis-10788.c282.east-us-mz.azure.cloud.redislabs.com",
    port = 10788,
    password = "yKCjtyQum735j4UL1FeO914Ci9etLHwf",
    decode_responses = True
)

@app.get("/")
def default():
    return {"Welcome":"Our Page"}

@app.post("/login",tags=["users"])
def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"message": "Login successful"}

@app.post("/verify",tags=["users"])
def verify(email: str, key: str, db: Session = Depends(get_db)):
    stored_code = redis.get(email + ":verification_code")
    # If stored_code is bytes, then decode it. Otherwise, use it as-is.
    if isinstance(stored_code, bytes):
        stored_code = stored_code.decode("utf-8")
    temp_user_data_json = redis.get(email + ":temp_data")
    # Similar logic for temp_user_data_json
    if isinstance(temp_user_data_json, bytes):
        temp_user_data_json = temp_user_data_json.decode("utf-8")
    if stored_code and stored_code == key and temp_user_data_json:
        try:
            # Deserialize stored user data
            temp_user_data = json.loads(temp_user_data_json)
            # Insert user into the main database
            new_user = models.Users(**temp_user_data)
            db.add(new_user)
            db.commit()
            # Clean up - remove temporary data and code from Redis
            redis.delete(email + ":verification_code", email + ":temp_data")

            return {"message": "User verified and added successfully!"}
        except Exception as e:
            # Handle potential errors (like database insertion issues)
            db.rollback()
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred during verification.")
    else:
        raise HTTPException(status_code=400, detail="Invalid verification code or user data not found.")

@app.post("/sign_up",tags=["users"])
def create_new_user(user: models.UsersBase, 
        db: Session = Depends(get_db) ): 

    if db.query(models.Users).filter(models.Users.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email is already exist")
    if sign_up_control(user.email,user.password):
        key = random_key_generator()
        store_verification_code(user.email, key)
        email_sender(user.email,key)
        user_data_as_str = json.dumps(user.dict())
        redis.setex(user.email + ":temp_data", 3600, user_data_as_str)
        
        return {"message": "User created successfully!"}
    else:
        raise HTTPException(status_code=400, detail="There are some problems")
    
    return {"Koçum":"Olacak Bu İş"}

def sign_up_control(email,password):

    email_control(email)
    password_control(password)
    return True

def email_control(email):
    if email == None:
        raise HTTPException(status_code=400, detail="Email Area Empty")
    elif "@" not in email or "." not in email:
        raise HTTPException(status_code=400, detail="Invalid Email")
    elif not validate_email(email) :
        raise HTTPException(status_code=400, detail="Invalid Email")
    else:
        print(email,"  : Valid")
   
def password_control(password):
    pattern = r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*\W).{8,20}$"    
    if not re.match(pattern, password):
        raise HTTPException(status_code=400, detail="Invalid Password")

     
def email_sender(email,key):
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
        raise HTTPException(status_code=500, detail="Failed to store verification code.")
