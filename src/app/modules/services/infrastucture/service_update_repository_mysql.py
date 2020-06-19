
from app.modules.services.domain import ServiceUpdateRepositoryInterface, Service
from mysql.connector import (connection)
from typing import List, Any

# def build_update_sql(cnx: connection.MySQLConnection, ids: List[str], table, column: str, value: str ) -> str:  
#   ids_scapped = ",".join([ f"'%s'" %(cnx.escape_string(id)) for id in ids])    
#   query = f"UPDATE {table} SET {cnx.escape_string(column)}='{cnx.escape_string(value)}' WHERE id IN ( {ids_scapped} )"    
#   return query

class ServiceUpdateRepositoryMysql(ServiceUpdateRepositoryInterface):

  table_name = "itinerarios"
  schema = (
    ("pagado", "pagado_por_servientrega"),
    ("referencia", "referencia"),    
  )

  def __init__(self, cnx: connection.MySQLConnection ):
    self.cnx = cnx

  def update_column(self, services: List[Service], atribute: str, value:Any ):
    cursor = self.cnx.cursor()
    references = [service.reference.get() for service in services]
    
    parameters = ",".join([ '%s' for i in range(len(references))])
    
    query = f"UPDATE itinerarios SET pagado_por_servientrega=1 WHERE referencia IN ( {parameters} )"
    print(query)
    print(references)
    cursor.execute(query,tuple(references) )
    cursor.close()    

  