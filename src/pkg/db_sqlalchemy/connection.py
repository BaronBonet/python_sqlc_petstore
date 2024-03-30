from dataclasses import dataclass

import sqlalchemy
from sqlalchemy import Engine

@dataclass
class DB_Params:
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str

def create_sqlalchemy_engine(db_params: DB_Params) -> Engine:
    db_url = f"postgresql://{db_params.DB_USERNAME}:{db_params.DB_PASSWORD}@{db_params.DB_HOST}:{db_params.DB_PORT}/{db_params.DB_NAME}"
    return sqlalchemy.create_engine(db_url)
