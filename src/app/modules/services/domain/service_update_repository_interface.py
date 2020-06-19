import abc
from typing import List, Any
from .service import Service

class ServiceUpdateRepositoryInterface(metaclass=abc.ABCMeta):

  @classmethod
  def __subclasshook__(cls, subclass):
    return (
      hasattr(subclass, 'update_column') and 
      callable(subclass.update_column) or      
      NotImplemented
    )

  @abc.abstractmethod
  def update_column(self, services: List[Service], column: str, value:Any ):
    raise NotImplementedError