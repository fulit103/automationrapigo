import docker

client = docker.from_env()
container = client.containers.run("mysql", environment=
  {
    "MYSQL_ROOT_PASSWORD": "secret",
    "MYSQL_DATABASE": "automation",
    "MYSQL_USER": "admin",
    "MYSQL_PASSWORD": "example"
  }, 
  ports = {
    "3306":"3306"
  },
  detach=True
)