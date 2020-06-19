from app.modules.services.application import ServiceSearcher
from app.modules.services.domain import Service
from typing import List
from .moks import RepositoryFiveMock, RepositoryTenMock, RepositoryEmptyMock

def test_service_searcher():
  repositoryOne = RepositoryFiveMock()
  repositoryTen = RepositoryTenMock()
  repositoryEmpty = RepositoryEmptyMock()

  service_searcher = ServiceSearcher(repositoryOne)
  services = service_searcher.get_all()

  assert len(services)==5
  assert services[0].reference.get()=="1"
  assert services[1].reference.get()=="2"
  assert services[2].reference.get()=="3"
  assert services[3].reference.get()=="4"

  service_searcher = ServiceSearcher(repositoryTen)
  services = service_searcher.get_all()

  assert len(services)==10
  assert services[0].reference.get()=="1"
  assert services[1].reference.get()=="2"
  assert services[8].reference.get()=="9"
  assert services[9].reference.get()=="10"

  service_searcher = ServiceSearcher(repositoryEmpty)
  services = service_searcher.get_all()

  assert services==[]