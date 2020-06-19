from fastapi import FastAPI
from app.modules.services.application import ServiceSearcher
from app.modules.services.infrastucture import ServiceListRepositoryAirtable
from app.modules.services.infrastucture.pydantic import ServicePydantic
from app.config import Settings

settings = Settings()
app = FastAPI()


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
