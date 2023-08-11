from datetime import date
import asyncpg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.pool = await asyncpg.create_pool(user='postgres', password='1234',
                                        database='postgres', host='172.31.55.2', port=5432)
    async with app.pool.acquire() as connection:
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS COUNTRIES(
                id UUID PRIMARY KEY,
                country  VARCHAR(80)
            );
            CREATE TABLE IF NOT EXISTS CITIES(
                id UUID PRIMARY KEY,
                country_id UUID REFERENCES COUNTRIES(id),
                cities  VARCHAR(80)    
            );
            CREATE TABLE IF NOT EXISTS TOWNS(
                id UUID PRIMARY KEY,
                city_id UUID REFERENCES CITIES(id),
                cities  VARCHAR(80)    
            );
            CREATE TABLE IF NOT EXISTS DISTRICTS(
                id UUID PRIMARY KEY,
                town_id UUID REFERENCES TOWNS(id),
                districts  VARCHAR(80)    
            );

            CREATE TABLE IF NOT EXISTS COMPANY_INFORMATIONS(
                id UUID PRIMARY KEY,
                company_name VARCHAR(80),
                                 tax_office VARCHAR(80),
                                    tax_number VARCHAR(80),
                                 phone VARCHAR(80),
                                    fax VARCHAR(80),
                                 users_id UUID REFERENCES USERS(id),
                                 mobile_phone VARCHAR(80),
                                    email VARCHAR(80),
                                 country_id UUID REFERENCES COUNTRIES(id),
                                    city_id UUID REFERENCES CITIES(id),
                                    town_id UUID REFERENCES TOWNS(id),
                                    district_id UUID REFERENCES DISTRICTS(id),
                                    address VARCHAR(80),
                                 
                                 );

            CREATE TABLE IF NOT EXISTS CURRENCIES(
                id UUID PRIMARY KEY,
                                 currency_code VARCHAR(80),
                                    currency_name VARCHAR(80),
                                 default_currency VARCHAR(80),
                                 status VARCHAR(80),
                                 currency_rate VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS POS_INFORMATION(
                id UUID PRIMARY KEY,
                                 pos_name VARCHAR(80),
                                 pos_type VARCHAR(80),
                                 company_information_id UUID REFERENCES COMPANY_INFORMATIONS(id),
                                 model VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS POS_DEFINITIONS(
                id UUID PRIMARY KEY,
                                 pos_information_id UUID REFERENCES POS_INFORMATION(id),
                                 default BOOLEAN,
                                 test_status BOOLEAN,
                                 cvv_required BOOLEAN,
                                 expiry DATE,
                                 single_payment_commission FLOAT,
                                 threeD VARCHAR(80),
                                 threeD_model VARCHAR(80),
                                 threeD_limit VARCHAR(80),
                                 currency_id UUID REFERENCES CURRENCIES(id),
                                 merchant_number VARCHAR(80),
                                 username VARCHAR(80),
                                 threeD_key VARCHAR(80),
                                 notification_url VARCHAR(80),
                                 ipn_address VARCHAR(80),
                                 store_code_normal_transaction VARCHAR(80),
                                 encoding_key_normal_transaction VARCHAR(80),
                                 store_code_3d_transaction VARCHAR(80),
                                 encoding_key_3d_transaction VARCHAR(80),
                                 api_key VARCHAR(80),
                                 secret_key VARCHAR(80),
                                 merchant_id VARCHAR(80),
                                 merchant_key VARCHAR(80),
                                 app_id VARCHAR(80),
                                 app_secret VARCHAR(80),
                                 webhook_key VARCHAR(80),
                                 webhook_url VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS POS_DEFINITIONS_CAMPAIGNS(
                                 pos_definitions_id UUID REFERENCES POS_DEFINITIONS(id),
                                    campaign_id UUID REFERENCES CAMPAIGNS(id),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS CAMPAIGNS(
                id UUID PRIMARY KEY,
                                    campaign_name VARCHAR(80),
                                    installment VARCHAR(80),
                                 payment_set_id UUID REFERENCES PAYMENT_SETS(id),
                                 commission VARCHAR(80),
                                 commercial_card_commission VARCHAR(80),
                                 sequence_number VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS PAYMENT_SETS(
                id UUID PRIMARY KEY,
                                    payment_set_name VARCHAR(80),
                                 activity_status BOOLEAN,
                                 member_group_status BOOLEAN,
                                 warning_text VARCHAR(8000),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS INSTALLMENTS(
                id UUID PRIMARY KEY,
                                banks_id UUID REFERENCES BANKS(id),
                                 brand VARCHAR(80),
                                 installment VARCHAR(80),
                                 member_group_id UUID REFERENCES MEMBER_GROUPS(id),
                                 commission VARCHAR(80),
                                 commercial_card_commission FLOAT,
                                 upper_limit FLOAT,
                                 status VARCHAR(80),
                                 commercial_card_status VARCHAR(80),
                                 pos_id UUID REFERENCES POS_DEFINITIONS(id),
                                 additional_installment INTEGER,
                                 additional_installment_limit FLOAT,
                                 additional_installment_upper_limit FLOAT,
                                 payment_set_id UUID REFERENCES PAYMENT_SETS(id),
                                 expiry DATE,

                                    );
                                 
            CREATE TABLE IF NOT EXISTS MEMBER_GROUPS(
                id UUID PRIMARY KEY,
                                    member_group_name VARCHAR(80),
                                 
                                 );

            CREATE TABLE IF NOT EXISTS BANKS(
                id UUID PRIMARY KEY,
                                    bank_name VARCHAR(80),
                                 default_single_installment_pos_id UUID REFERENCES POS_DEFINITIONS(id),
                                 default_installment_pos_id UUID REFERENCES POS_DEFINITIONS(id),
                                 single_installment_due_date INTEGER,
                                 single_installment_commission FLOAT,
                                 logo VARCHAR(80),
                                 color VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS CREDIT_CARDS(
                id UUID PRIMARY KEY,
                                 bank_id UUID REFERENCES BANKS(id),
                                 brand VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS BIN_LIST(
                id UUID PRIMARY KEY,
                                    bin VARCHAR(80),
                                    bank_id UUID REFERENCES BANKS(id),
                                 brand VARCHAR(80),
                                    card_type VARCHAR(80),
                                 hit VARCHAR(80),
                                 last_request_date DATE,
                                 commercial_card_status VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS USERS(
                id UUID PRIMARY KEY,
                                   name VARCHAR(80),
                                    surname VARCHAR(80),
                                 identity_number VARCHAR(80),
                                 username VARCHAR(80),
                                    password VARCHAR(80),
                                 webservice_code VARCHAR(80),
                                 group_id UUID REFERENCES GROUPS(id),
                                 role VARCHAR(80),
                                 email VARCHAR(80),
                                 phone VARCHAR(80),
                                 iban VARCHAR(80),
                                 photo VARCHAR(80),
                                 country_id UUID REFERENCES COUNTRIES(id),
                                    city_id UUID REFERENCES CITIES(id),
                                    town_id UUID REFERENCES TOWNS(id),
                                    district_id UUID REFERENCES DISTRICTS(id),
                                    address VARCHAR(80),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS GROUPS(
                id UUID PRIMARY KEY,
                                    group_name VARCHAR(80),
                                 ip VARCHAR(80),
                                 is_api_user BOOLEAN,
                                 user_authorizations_id UUID REFERENCES USER_AUTHORIZATIONS(id),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS USER_AUTHORIZATIONS(
                id UUID PRIMARY KEY,
                                 transaction_group VARCHAR(80),
                                 transactions_id UUID REFERENCES TRANSACTIONS(id),
                                 status VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS TRANSACTIONS(
                id UUID PRIMARY KEY,
                                    transaction_name VARCHAR(80),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS PAYMENT_OPTIONS(
                id UUID PRIMARY KEY,
                                    payment_option_name VARCHAR(80),
                                 service_description VARCHAR(80),
                                 vat FLOAT,
                                 options_id UUID REFERENCES OPTIONS(id),
                                 amount_effect VARCHAR(80),
                                 lower_limit FLOAT,
                                    upper_limit FLOAT,
                                 member_groups_id UUID REFERENCES MEMBER_GROUPS(id),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS OPTIONS(
                id UUID PRIMARY KEY,
                                 activity_status BOOLEAN,
                                 default_value VARCHAR(80),
                                 name VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS TARIFFS(
                id UUID PRIMARY KEY,
                                    tariff_name VARCHAR(80),
                                 lower_limit FLOAT,
                                 out_of_country_status BOOLEAN,
                                 out_of_city_status BOOLEAN,
                                 in_city_status BOOLEAN,

                                    );
                                 
            CREATE TABLE IF NOT EXISTS SHIPPING_COMPANIES(
                id UUID PRIMARY KEY,
                                    shipping_company_name VARCHAR(80),
                                 calculation_type VARCHAR(80),
                                 integrated BOOLEAN,
                                 member_groups_id UUID REFERENCES MEMBER_GROUPS(id),
                                 free_limit FLOAT,
                                 member_group_status VARCHAR(80),
                                 payment_method VARCHAR(80),
                                 activity_status BOOLEAN,
                                 default_value VARCHAR(80),
                                 regional VARCHAR(80),
                                 tariff_id UUID REFERENCES TARIFFS(id),
                                 country_city_id UUID REFERENCES COUNTRY_CITIES(id),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS COUNTRY_CITIES(
                id UUID PRIMARY KEY,
                                 country_code VARCHAR(80),
                                 country VARCHAR(80),
                                 shipping_zone_id UUID REFERENCES SHIPPING_ZONES(id),
                                 state_status BOOLEAN,
                                 status VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS SHIPPING_ZONES(
                id UUID PRIMARY KEY,
                                    shipping_zone_name VARCHAR(80),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS VARIABLES(
                id UUID PRIMARY KEY,
                                 variable VARCHAR(80),
                                 variable_query VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS PAYMENT_NOTIFICATIONS_VARIABLES(
                id UUID PRIMARY KEY,
                                    payment_notifications_id UUID REFERENCES PAYMENT_NOTIFICATIONS(id),
                                    variables_id UUID REFERENCES VARIABLES(id),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS PAYMENT_NOTIFICATIONS(
                id UUID PRIMARY KEY,
                                 members_id UUID REFERENCES MEMBERS(id),
                                 amount FLOAT,
                                 payment_set_id UUID REFERENCES PAYMENT_SETS(id),
                                 validity_period DATE,
                                 threeD_security_type VARCHAR(80),
                                 activation_status BOOLEAN,
                                 single_use BOOLEAN,
                                 unregistered BOOLEAN,
                                 fixed_price BOOLEAN,
                                 fixed_description BOOLEAN,
                                 show_description BOOLEAN,
                                 explanation VARCHAR(8000),
                                 email_subject VARCHAR(250),
                                 templates VARCHAR(80),
                                 email_content VARCHAR(250),
                                 send_sms BOOLEAN,

                                    );
                                 
            CREATE TABLE IF NOT EXISTS MEMBERS(
                id UUID PRIMARY KEY,
                                 member_description VARCHAR(80),
                                 name VARCHAR(80),
                                    surname VARCHAR(80),
                                    identity_number VARCHAR(80),
                                 company_name VARCHAR(80),
                                 tax_office VARCHAR(80),
                                    tax_number VARCHAR(80),
                                 mobile_phone VARCHAR(80),
                                 phone VARCHAR(80),
                                 fax VARCHAR(80),
                                 postal_code VARCHAR(80),
                                 country_id UUID REFERENCES COUNTRIES(id),
                                    city_id UUID REFERENCES CITIES(id),
                                    town_id UUID REFERENCES TOWNS(id),
                                    district_id UUID REFERENCES DISTRICTS(id),
                                    address VARCHAR(80),
                                 ws_code VARCHAR(80),
                                 customer_code VARCHAR(80),
                                 submember_opening_permission BOOLEAN,
                                 submember_creation_permission BOOLEAN,
                                 submember_payment_notification_permission BOOLEAN,
                                 can_create_payment_notification BOOLEAN,
                                 submember_credit_authorization BOOLEAN,
                                 can_enter_creditability BOOLEAN,
                                 member_group_id UUID REFERENCES MEMBER_GROUPS(id),
                                 representative_id UUID REFERENCES USERS(id),
                                 max_receivable_limit FLOAT,
                                 max_debt_limit FLOAT,
                                 email VARCHAR(80),
                                 password VARCHAR(80),
                                 balance FLOAT,
                                 banned_status BOOLEAN,
                                 risk_status BOOLEAN,
                                 approval_status BOOLEAN,

                                    );
                                 
            CREATE TABLE IF NOT EXISTS ENAIL_TEMPLATES_VARIABLES(
                                 email_templates_id UUID REFERENCES EMAIL_TEMPLATES(id),
                                 variables_id UUID REFERENCES VARIABLES(id),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS EMAIL_TEMPLATES(
                id UUID PRIMARY KEY,
                                 activity_status BOOLEAN,
                                    template_name VARCHAR(80),
                                 sender_email VARCHAR(80),
                                 recipient_email VARCHAR(80),
                                 cc_email VARCHAR(80),
                                 bcc_email VARCHAR(80),
                                 topic VARCHAR(250),
                                    content VARCHAR(8000),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS SMS_TEMPLATES_VARIABLES(
                                 variables_id UUID REFERENCES VARIABLES(id),
                                    sms_templates_id UUID REFERENCES SMS_TEMPLATES(id),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS SMS_TEMPLATES(
                id UUID PRIMARY KEY,
                                    activity_status BOOLEAN,
                                    template_name VARCHAR(80),
                                 sending_activity_status BOOLEAN,
                                 service_provider_id UUID REFERENCES SERVICE_PROVIDERS(id),
                                 user_id UUID REFERENCES USERS(id),
                                 password VARCHAR(80),
                                 content VARCHAR(8000),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS SERVICE_PROVIDERS(
                id UUID PRIMARY KEY,
                                    service_provider_name VARCHAR(80),
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS ACCOUNT_TRANSACTIONS(
                id UUID PRIMARY KEY,
                                    members_id UUID REFERENCES MEMBERS(id),
                                 date DATE,
                                 submember_id UUID REFERENCES MEMBERS(id),
                                 transaction_number VARCHAR(80),
                                 document_number VARCHAR(80),
                                 explanation VARCHAR(8000),
                                 debt FLOAT,
                                 receivable FLOAT,
                                 balance FLOAT,
                                 usd_debt FLOAT,
                                 usd_receivable FLOAT,
                                    usd_balance FLOAT,
                                 
                                    );
                                 
            CREATE TABLE IF NOT EXISTS PERIODIC_COLLECTION(
                id UUID PRIMARY KEY,
                                    members_id UUID REFERENCES MEMBERS(id),
                                 name VARCHAR(80),
                                 credit_card_id UUID REFERENCES CREDIT_CARDS(id),
                                 registration_date DATE,
                                 start_date DATE,
                                 collection_templates_id UUID REFERENCES COLLECTION_TEMPLATES(id),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS COLLECTION_TEMPLATES(
                id UUID PRIMARY KEY,
                                    template_name VARCHAR(80),
                                 amount FLOAT,
                                 payment_frequency VARCHAR(80),
                                 payment_period VARCHAR(80),
                                    payment_count INTEGER,
                                 explanation VARCHAR(8000),
                                 make_first_payment BOOLEAN,
                                 fixed_description BOOLEAN,

                                    );
                                 
            CREATE TABLE IF NOT EXISTS LANGUAGE_MANAGEMENT(
                id UUID PRIMARY KEY,
                                 language_code VARCHAR(80),
                                 alignment VARCHAR(80),
                                 language_name VARCHAR(80),
                                 shortest_code VARCHAR(80),
                                 icon_path VARCHAR(80),
                                 decimal_symbol VARCHAR(80),
                                 decimal_places INTEGER,
                                 thousands_separator VARCHAR(80),
                                 first_day_of_week VARCHAR(80),
                                 date VARCHAR(80),
                                 long_date VARCHAR(80),
                                    short_date VARCHAR(80),
                                 long_time VARCHAR(80),

                                    );
                                 
            CREATE TABLE IF NOT EXISTS PAYMENT_PAGE_FORM(
                id UUID PRIMARY KEY,
                                 field_name VARCHAR(80),
                                 name VARCHAR(80),
                                 type VARCHAR(80),
                                 record_visibility_status BOOLEAN,
                                 record_requirement_status BOOLEAN,
                                 update_visibility_status BOOLEAN,
                                 update_requirement_status BOOLEAN,
                                 max_character INTEGER,
                                 min_character INTEGER,
                                 unwanted_character VARCHAR(80),
                                 options VARCHAR(80),

                                    );
        ''')
        

@app.on_event("shutdown")
async def shutdown():
    await app.pool.close()


@app.get("/")
async def create_tables():
    return {"Success":"Voila"}

@app.post("/add_user")
async def add_user():

    return {"Success":"Voila"}