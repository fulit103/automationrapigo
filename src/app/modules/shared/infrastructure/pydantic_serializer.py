from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any

class PydanticSerializer(ABC):

  @abstractmethod
  def serialize(self, domain_model: Any ) -> BaseModel:
    pass

  @abstractmethod
  def deserialize(self) -> Any:
    pass