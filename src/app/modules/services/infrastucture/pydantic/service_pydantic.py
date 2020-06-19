from pydantic import BaseModel
from app.modules.services.domain import Service
from app.modules.services.domain import ReferenceValue
from app.modules.shared.infrastructure import PydanticSerializer

class ServicePydantic(BaseModel, PydanticSerializer):  
  reference: str = ''  
  
  def serialize(self, domain_model: Service ) -> BaseModel:    
    data = {
      "reference": domain_model.reference.get()
    }
    service = ServicePydantic(**data)
    return service
  
  def deserialize(self) -> Service:
    service = Service( ReferenceValue(self.reference) )
    return service
    