import docker
import time
import pytest
import sys

@pytest.fixture(scope='session')
def mysqldocker():
  client = docker.from_env()
  container = client.containers.run("mysql", environment=
    {
      "MYSQL_ROOT_PASSWORD": "secret",
      "MYSQL_DATABASE": "automation",
      "MYSQL_USER": "admin",
      "MYSQL_PASSWORD": "example"
    }, 
    ports = {
      '3306/tcp':'3306/tcp'
    },    
    detach=True
  )
  i = 0
  for line in container.logs(stream=True):
    log = str(line.strip())
    #print(log)
    #sys.stdout.write('\n{}'.format(log))
    i = i + 1
    if "port: 3306  MySQL Community Server - GPL." in log :
      time.sleep(2)
      break

  yield container
  
  containers = client.containers.list()
  for c in containers:
    c.stop()