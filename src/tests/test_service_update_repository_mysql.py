from app.modules.services.infrastucture import ServiceUpdateRepositoryMysql
from app.modules.services.domain import Service, ReferenceValue
import mysql.connector
import docker
import pytest

import time

from .fixtures import mysqldocker

@pytest.fixture(scope='session')
def cnx(mysqldocker):  
  config = {
    'user': 'admin',
    'password': 'example',
    'host': '127.0.0.1',
    'database': 'automation',
    'raise_on_warnings': True
  }
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(
    """CREATE TABLE `automation`.`itinerarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `pagado_por_servientrega` INT NULL,
    `referencia` VARCHAR(45) NULL,
    PRIMARY KEY (`id`));"""
  )
  yield cnx
  print("close connection ")
  cnx.close()
  

def test_update_all_services(cnx):
  cursor = cnx.cursor()
  values = [
    ("1", 0),
    ("2", 0),
    ("3", 0),
    ("4", 0),
  ]
  cursor.executemany("INSERT INTO itinerarios ( referencia, pagado_por_servientrega) VALUES ( %s, %s )", values )
  

  s1 = Service(ReferenceValue("1"))
  s2 = Service(ReferenceValue("2"))
  s3 = Service(ReferenceValue("3"))

  list = [s1, s2, s3]

  repository = ServiceUpdateRepositoryMysql(cnx)
  repository.update_column(list, "pagado_por_servientrega", 1 )

  cursor.execute("SELECT referencia, pagado_por_servientrega FROM itinerarios WHERE pagado_por_servientrega=1")
  records = cursor.fetchall()

  print(records)

  assert records[0][1]==1
  assert records[1][1]==1
  assert records[2][1]==1
  assert len(records)==3  
  
