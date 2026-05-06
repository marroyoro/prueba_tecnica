import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

bronze_engine = create_engine("mysql+pymysql://root:1234567@localhost:3307/bronze_db")
silver_engine = create_engine("mysql+pymysql://root:1234567@localhost:3307/silver_db")

def limpiar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    for col in df.select_dtypes(include=["object", "string"]).columns:
        if "fec" in col or "fecha" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def cargar_a_silver(df: pd.DataFrame, table_name: str):
    try:
        df.to_sql(table_name, con=silver_engine, if_exists="replace", index=False)
        logging.info(f"✅ {table_name} cargada en Silver con {len(df)} registros")
    except Exception as e:
        logging.error(f"❌ Error cargando {table_name} en Silver: {e}")

# --- Proceso Silver ---
bronze_tables = ["hotcli", "hotcag", "hotvta"]

for table in bronze_tables:
    try:
        logging.info(f"Iniciando transformación de {table}")
        df = pd.read_sql(f"SELECT * FROM {table}", con=bronze_engine)
        df_clean = limpiar_dataframe(df)

        if table == "hotcli":
            # Crear dimensión de clientes con columnas clave
            dim_clients = df_clean[["c_cve_cxc", "c_nombre", "c_ciudad", "c_estado", "c_pais"]].drop_duplicates()
            cargar_a_silver(dim_clients, "silver_dim_clients")

            # Tabla de hechos (todo lo demás)
            fact_clients = df_clean.drop(columns=["c_nombre", "c_ciudad", "c_estado", "c_pais"])
            cargar_a_silver(fact_clients, "silver_fact_clients")
        else:
            cargar_a_silver(df_clean, f"silver_{table}")

    except Exception as e:
        logging.error(f"❌ Error procesando {table}: {e}")

