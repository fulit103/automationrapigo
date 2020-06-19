from typing import List, Any
from app.models import Service
from modules.services.domain import ServiceUpdaterInterface, ServiceUpdateRepositoryInterface

class ServiceSearcher(ServiceUpdaterInterface):

  def __init__(self, repository: ServiceUpdateRepositoryInterface ):
     self.repository = repository

  def update_column(self, services: List[Service], column: str, value:Any ):
    records = self.repository.update_column(services, column, value)    
