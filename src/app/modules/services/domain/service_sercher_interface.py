import abc
from typing import List
from .service import Service

class ServiceSearcherInterface(metaclass=abc.ABCMeta):

  @classmethod
  def __subclasshook__(cls, subclass):
    return (
      hasattr(subclass, 'get_all') and 
      callable(subclass.get_all) or      
      NotImplemented
    )

  @abc.abstractmethod
  def get_all(self) -> List[Service]:
    raise NotImplementedError