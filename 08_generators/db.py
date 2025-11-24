print("Starting script...", flush=True)
import oracledb
import sys

try:
    oracledb.init_oracle_client(lib_dir=r"c:\Users\pulkit.gupta1\OneDrive - Comviva Technologies LTD\C\DevSuiteHome_1\BIN")
except Exception as e:
    print(f"Failed to init Oracle Client: {e}")
    sys.exit(1)

dsn = "(description= (retry_count=20)(retry_delay=3)(transport_connect_timeout=10)(address=(protocol=tcps)(port=1522)(host=adb.ap-hyderabad-1.oraclecloud.com))(connect_data=(service_name=g21bd6f153efbd1_atp23_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"

dsn2 = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=clonedb.comviva.com)(PORT=1522))(CONNECT_DATA=(SID=ebs_TEST)))"

print("Attempting to connect...", flush=True)
# connection = oracledb.connect(user="admin", password="Welcome@1234@", dsn=dsn)
connection = oracledb.connect(user="apps", password="apps143", dsn=dsn2)
print("Successfully connected", flush=True)

# Now you can create a cursor and run SQL queries
cursor = connection.cursor()
cursor.execute("SELECT 1 FROM dual")
for row in cursor:
    print(row)
cursor.close()
connection.close()