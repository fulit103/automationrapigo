from app.modules.services.infrastucture import ServiceUpdateRepositoryMysql
from app.modules.services.domain import Service, ReferenceValue
import docker
import pytest

import time

from databases import Database
from app.config import Settings

@pytest.fixture
async def database():  
  settings = Settings()
  DATABASE_URL = settings.database_url #"mysql://root:secret@dbmysql/automation"
  database = Database(DATABASE_URL)
  await database.connect()
  query = """CREATE TABLE IF NOT EXISTS itinerario (
    id INT NOT NULL AUTO_INCREMENT,
    pagado_por_servientrega INT NULL,
    referencia VARCHAR(45) NULL,
    PRIMARY KEY (id));
  """
  await database.execute(query=query)

  yield database
  
  await database.execute(query="DROP TABLE `automation`.`itinerario`")
  await database.disconnect()
  
@pytest.mark.asyncio
async def test_update_all_services(database):  
  values = [
    {"referencia": "1", "pagado_por_servientrega": 1},
    {"referencia": "2", "pagado_por_servientrega": 2},
    {"referencia": "3", "pagado_por_servientrega": 3},
    {"referencia": "4", "pagado_por_servientrega": 4}
  ]
  await database.execute_many("INSERT INTO itinerario ( referencia, pagado_por_servientrega) VALUES ( :referencia, :pagado_por_servientrega )", values )
  

  s1 = Service(ReferenceValue("1"))
  s2 = Service(ReferenceValue("2"))
  s3 = Service(ReferenceValue("3"))

  list = [s1, s2, s3]

  repository = ServiceUpdateRepositoryMysql(database)
  await repository.update_column(list, "pagado_por_servientrega", 1 )
  
  records = await database.fetch_all("SELECT referencia, pagado_por_servientrega FROM itinerario WHERE pagado_por_servientrega=1")  

  assert records[0][1]==1
  assert records[1][1]==1
  assert records[2][1]==1
  assert len(records)==3  
  
