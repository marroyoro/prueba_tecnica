import pandas as pd
from sqlalchemy import create_engine
import logging, glob

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

mysql_url = "mysql+pymysql://root:1234567@localhost:3307/bronze_db"
engine = create_engine(mysql_url)

parquet_files = glob.glob("C:/Users/Arroy/Downloads/recursos_prueba/recursos_prueba/tablas_parquet/*.parquet")

for file in parquet_files:
    try:
        table_name = file.split("\\")[-1].replace(".parquet", "")
        logging.info(f"Iniciando ingesta: {file} → {table_name}")
        df = pd.read_parquet(file)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logging.info(f"✅ {table_name} cargada con {len(df)} registros")
    except Exception as e:
        logging.error(f"❌ Error en {file}: {e}")
