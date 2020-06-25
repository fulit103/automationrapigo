from typing import List, Any
from app.modules.services.domain import Service
from app.modules.services.domain import ServiceUpdateRepositoryInterface

class ServiceUpdater():

  def __init__(self, repository: ServiceUpdateRepositoryInterface ):
     self.repository = repository

  async def update_column(self, services: List[Service], column: str, value:Any ):
    return await self.repository.update_column(services, column, value)    
