import psycopg2
from sshtunnel import SSHTunnelForwarder
from ssh_params import get_params

try:
    params = get_params()
    with SSHTunnelForwarder(
         (params['ip'], 22),
         #ssh_private_key="</path/to/private/ssh/key>",
         
         ssh_username=params['username'],
         ssh_password=params['password'], 
         remote_bind_address=('localhost', 5432)) as server:
         
         server.start()
         print("server connected")

         pg_params = {
             'database': params['db_name'],
             'user': params['username'],
             'password': params['password'],
             'host': 'localhost',
             'port': server.local_bind_port
             }

         conn = psycopg2.connect(**pg_params)
         curs = conn.cursor()
         print("database connected")

except:
    print("Connection Failed")
