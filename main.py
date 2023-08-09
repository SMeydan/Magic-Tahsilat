import asyncpg
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from email_validator import validate_email, EmailNotValidError
import re

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

from Models.AccountTransactions import AccountTransactions
from Models.AccountTransactions import AccountTransactionsBase

from Models.Banks import Banks
from Models.Banks import BanksBase

from Models.BinList import BinList
from Models.BinList import BinListBase

from Models.Campaigns import Campaigns
from Models.Campaigns import CampaignsBase

from Models.Cities import Cities
from Models.Cities import CitiesBase

from Models.CollectionTemplates import CollectionTemplates
from Models.CollectionTemplates import CollectionTemplatesBase

from Models.CompanyInformations import CompanyInformations
from Models.CompanyInformations import CompanyInformationsBase

from Models.Countries import Countries
from Models.Countries import CountriesBase

from Models.CountryCities import CountryCities
from Models.CountryCities import CountryCitiesBase

from Models.CreditCards import CreditCards
from Models.CreditCards import CreditCardsBase

from Models.Currencies import Currencies
from Models.Currencies import CurrenciesBase

from Models.Districts import Districts
from Models.Districts import DistrictsBase

from Models.EmailTemplates import EmailTemplates
from Models.EmailTemplates import EmailTemplatesBase

from Models.EmailTemplatesVariables import EmailTemplatesVariables
from Models.EmailTemplatesVariables import EmailTemplatesVariablesBase

from Models.Groups import Groups
from Models.Groups import GroupsBase

from Models.Installments import Installments
from Models.Installments import InstallmentsBase

from Models.LanguageManagement import LanguageManagement
from Models.LanguageManagement import LanguageManagementBase

from Models.MemberGroups import MemberGroups
from Models.MemberGroups import MemberGroupsBase

from Models.Members import Members
from Models.Members import MembersBase

from Models.Options import Options
from Models.Options import OptionsBase

from Models.PaymentNotifications import PaymentNotifications
from Models.PaymentNotifications import PaymentNotificationsBase

from Models.PaymentNotificationsVariables import PaymentNotificationsVariables
from Models.PaymentNotificationsVariables import PaymentNotificationsVariablesBase

from Models.PaymentOptions import PaymentOptions
from Models.PaymentOptions import PaymentOptionsBase

from Models.PaymentPageForm import PaymentPageForm
from Models.PaymentPageForm import PaymentPageFormBase

from Models.PaymentSets import PaymentSets
from Models.PaymentSets import PaymentSetsBase

from Models.PeriodicCollection import PeriodicCollection
from Models.PeriodicCollection import PeriodicCollectionBase

from Models.PosDefinitions import PosDefinitions
from Models.PosDefinitions import PosDefinitionsBase

from Models.PosDefinitionsCampaigns import PosDefinitionsCampaigns
from Models.PosDefinitionsCampaigns import PosDefinitionsCampaignsBase

from Models.PosInformation import PosInformation
from Models.PosInformation import PosInformationBase

from Models.ServiceProviders import ServiceProviders
from Models.ServiceProviders import ServiceProvidersBase

from Models.ShippingCompanies import ShippingCompanies
from Models.ShippingCompanies import ShippingCompaniesBase

from Models.ShippingZones import ShippingZones
from Models.ShippingZones import ShippingZonesBase

from Models.SmsTemplates import SmsTemplates
from Models.SmsTemplates import SmsTemplatesBase

from Models.SmsTemplatesVariables import SmsTemplatesVariables
from Models.SmsTemplatesVariables import SmsTemplatesVariablesBase

from Models.Tariffs import Tariffs
from Models.Tariffs import TariffsBase

from Models.Towns import Towns
from Models.Towns import TownsBase

from Models.Transactions import Transactions
from Models.Transactions import TransactionsBase

from Models.UserAuthorizations import UserAuthorizations
from Models.UserAuthorizations import UserAuthorizationsBase

from Models.Users import Users
from Models.Users import UsersBase

from Models.Variables import Variables
from Models.Variables import VariablesBase

app = FastAPI()




redis = get_redis_connection(
    host = "redis-10788.c282.east-us-mz.azure.cloud.redislabs.com",
    port = 10788,
    password = "yKCjtyQum735j4UL1FeO914Ci9etLHwf",
    decode_responses = True
)

#@app.on_event("startup")
#async def startup():
#    app.pool = await asyncpg.create_pool(user='postgres', password='1234',
#                                         database='postgres', host='127.0.0.1')
    
#@app.on_event("shutdown")
#async def shutdown():
#    await app.pool.close()

@app.get("/")
def default():
    message = Mail(
    from_email='magictahsilat@gmail.com',
    to_emails='tachsinachmet@gmail.com',
    subject='voila! It works!',
    html_content='<strong>I LOVE U, BABE <3</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)


@app.post("/sign_up",tags=["users"])
def create_new_user(user: UserSchema = Body(...) ): 
    #get user from form
    sign_up_control(redis.get(user.email),redis.get(user.password))
    return {"Koçum":"Olacak Bu İş"}

def sign_up_control(email,password):
    key = random_key_generator()
    email_control(email)
    password_control(password)
    email_sender(email,key)

def email_control(mail):
    if mail == None:
        raise HTTPException(status_code=400, detail="Email Area Empty")
    elif redis.get(user.email) == None:
        raise HTTPException(status_code=400, detail="Email is already exist")
    elif redis.get(user.email).find("@") == -1 or redis.get(user.email).find(".") == -1:
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
    html_content='<strong>I LOVE U, BABE <3</strong>'+key)
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
    return ''.join(random.choice(string.ascii_letters) for i in range(10))