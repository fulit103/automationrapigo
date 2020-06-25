
from app.modules.services.domain import ServiceUpdateRepositoryInterface, Service
#from mysql.connector import (connection)
from databases import Database
from typing import List, Any
import asyncio
from sqlescapy import sqlescape

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

  def __init__(self, database: Database ):
    self.database = database

  async def update_column(self, services: List[Service], atribute: str, value:Any ):    
    references = ",".join([f'"{sqlescape(service.reference.get())}"' for service in services])    
    
    query = f"UPDATE itinerario SET pagado_por_servientrega=1 WHERE referencia IN ( {references} )"
   
    return await self.database.execute(query)
    


  