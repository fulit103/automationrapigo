from airtable import Airtable
from app.modules.services.infrastucture import ServiceListRepositoryAirtable
from app.config import Settings

def test_airtable_repository_impl():
  settings = Settings()
  repository = ServiceListRepositoryAirtable(settings.airtable_api_key, settings.airtable_base, "servicios_pagos_servientrega_test")

  services = repository.get_all()

  assert len(services)==3
