from airtable import Airtable
from typing import List, Any
from app.modules.services.domain import Service, ServiceListRepositoryInterface, ReferenceValue

class ServiceListRepositoryAirtable(ServiceListRepositoryInterface):
  
  def __init__(self, api_key: str, filename:str, table: str ):
    self.context = Airtable(filename, table,  api_key=api_key)

  """
    return List of JSON

    JSON : {'id': 'recZgct2SLqfKlC0c1', 'fields': {'reference': '1'}, 'createdTime': '2020-01-23T23:50:29.000Z'},
  """
  def get_all(self) -> List[Service]:
    records = self.context.get_all()    
    services: List[Service] = [] 
    for r in records:
      fields = r["fields"]      
      print(fields)
      reference = ReferenceValue(fields["reference"])
      service = Service( reference )
      services.append(service)
    return services