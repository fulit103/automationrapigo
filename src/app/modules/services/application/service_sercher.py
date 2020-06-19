from typing import List, Any
from app.modules.services.domain import Service
from app.modules.services.domain import ServiceSearcherInterface, ServiceListRepositoryInterface

class ServiceSearcher(ServiceSearcherInterface):

  def __init__(self, repository: ServiceListRepositoryInterface ):
     self.repository = repository

  def get_all(self) -> List[Service]:
    services = self.repository.get_all()    
    return services
