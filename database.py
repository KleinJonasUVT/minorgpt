import os
import pymysql
import pandas as pd

# Connect to TiDB database function
def connect_to_db():
    connection = pymysql.connect(
        host = "gateway01.eu-central-1.prod.aws.tidbcloud.com",
        port = 4000,
        user = os.environ.get("TIDB_USER"),
        password = os.environ.get("TIDB_PASSWORD"),
        database = "minor",
        ssl_verify_cert = True,
        ssl_verify_identity = True,
        ssl_ca = "/etc/ssl/certs/ca-certificates.crt"
        )
    return connection

def load_minors_from_db():
    connection = connect_to_db()
    minors_df = pd.read_sql(f"SELECT * FROM minor_details", con=connection)
    return minors_df