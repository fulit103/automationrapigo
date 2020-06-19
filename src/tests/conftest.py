# import docker
# import time


# def pytest_configure(config):
#   """ called after command line options have been parsed
#       and all plugins and initial conftest files been loaded.
#   """  
#   try:  
#     client = docker.from_env()
#     container = client.containers.run("mysql", environment=
#       {
#         "MYSQL_ROOT_PASSWORD": "secret",
#         "MYSQL_DATABASE": "automation",
#         "MYSQL_USER": "admin",
#         "MYSQL_PASSWORD": "example"
#       }, 
#       ports = {
#         '3306/tcp':'3306/tcp'
#       },    
#       detach=True
#     )
#     i = 0
#     for line in container.logs(stream=True):
#       log = str(line.strip())
#       print(log)
#       i = i + 1
#       if "port: 3306  MySQL Community Server - GPL." in log :
#         time.sleep(2)
#         break
#   except:
#     print("Error docker")

# def pytest_unconfigure(config):
#   """ called before test process is exited.  """
#   print("exit")
#   client = docker.from_env()
#   containers = client.containers.list()
#   for c in containers:
#     c.stop()
  