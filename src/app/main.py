from fastapi import FastAPI
from app.modules.services.application import ServiceSearcher, ServiceUpdater
from app.modules.services.infrastucture import ServiceListRepositoryAirtable
from app.modules.services.infrastucture import ServiceUpdateRepositoryMysql
from app.modules.services.infrastucture.pydantic import ServicePydantic
from app.config import Settings
import databases

settings = Settings()
app = FastAPI()


DATABASE_URL = "mysql://root:secret@192.168.0.14/automation"

database = databases.Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def get_itinerarios(): 
    # json = {"reference":"a"}
    # a = Service(**json)
    # print(a.reference)    
    return {"reference":"a"}

@app.get("/call_task")
def call_task():    
    repository = ServiceListRepositoryAirtable(settings.airtable_api_key, settings.airtable_base, "servicios_pagos_servientrega")
    service_sercher = ServiceSearcher(repository)
    services = service_sercher.get_all()
    services_serialized = [ ServicePydantic().serialize(service) for service in services ]
    return services_serialized

@app.get("/pay_services")
async def pay_services():
    repository_airtable = ServiceListRepositoryAirtable(settings.airtable_api_key, settings.airtable_base, "servicios_pagos_servientrega")
    service_sercher = ServiceSearcher(repository_airtable)
    services = service_sercher.get_all()

    repository_mysql = ServiceUpdateRepositoryMysql(database)
    service_updater = ServiceUpdater(repository_mysql)
    await service_updater.update_column(services, "pagos", 1 )

    return { "message":"ok" }