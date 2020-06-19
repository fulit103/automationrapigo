from app.modules.services.domain import ServiceListRepositoryInterface, Service, ReferenceValue
from typing import List

class RepositoryFiveMock(ServiceListRepositoryInterface):
  def get_all(self) -> List[Service]:
    return [
      Service(ReferenceValue("1")),
      Service(ReferenceValue("2")),
      Service(ReferenceValue("3")),
      Service(ReferenceValue("4")),
      Service(ReferenceValue("5"))      
    ]

class RepositoryTenMock(ServiceListRepositoryInterface):
  def get_all(self) -> List[Service]:
    return [
      Service(ReferenceValue("1")),
      Service(ReferenceValue("2")),
      Service(ReferenceValue("3")),
      Service(ReferenceValue("4")),
      Service(ReferenceValue("5")),
      Service(ReferenceValue("6")),
      Service(ReferenceValue("7")),
      Service(ReferenceValue("8")),
      Service(ReferenceValue("9")),
      Service(ReferenceValue("10"))
    ]

class RepositoryEmptyMock(ServiceListRepositoryInterface):
  def get_all(self) -> List[Service]:
    return []