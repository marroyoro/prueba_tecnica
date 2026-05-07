# Pipeline de Datos Medallion

Pipeline ETL/ELT basado en arquitectura Medallion (Bronze, Silver y Gold) para procesar, transformar y organizar datasets con el objetivo de generar información confiable y consumible.

# Descripción

Este proyecto implementa una arquitectura Medallion para separar el procesamiento de datos en diferentes capas:

- Bronze → Datos crudos.
- Silver → Datos limpios y transformados.
- Gold → Datos listos para análisis y reporting.

La solución permite mantener trazabilidad, mejorar calidad de datos y facilitar el consumo analítico.

---

# Objetivo

Diseñar un flujo de datos escalable que permita:

- Ingestar datasets originales.
- Limpiar y validar información.
- Transformar datos para análisis.
- Generar tablas optimizadas para BI.
- Mantener separación entre datos raw y analíticos.

---

# Arquitectura Medallion

## Bronze Layer

Capa encargada de almacenar los datos originales sin modificaciones.

### Funciones
- Lectura de datasets.
- Ingesta de información.
- Persistencia de datos raw.
- Conservación del histórico original.

### Archivo principal

```bash
main.py
```

---

## Silver Layer

Capa de transformación y limpieza de datos.

### Funciones
- Eliminación de duplicados.
- Limpieza de columnas.
- Conversión de tipos de datos.
- Validación de registros.

### Archivo principal

```bash
main_silver.py
```

---

##  Gold Layer

Capa analítica enfocada en negocio.

### Funciones
- Creación de métricas.
- Tablas agregadas.
- Modelado para analítica.

### Archivo principal

```sql
golden_schema.sql
```

---

# Tecnologías utilizadas

- Python
- Pandas
- MySQL
- Docker

---

# Instalación

## 1. Clonar repositorio

```bash
git clone <repo_url>
cd project
```

---

## 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
```

### Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Levantar contenedores Docker

```bash
docker-compose up -d
```

---

# Configuración

## Variables de entorno

Crear archivo `.env`

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=medallion_db
DB_USER=root
DB_PASSWORD=password
```

# Resultados esperados

El pipeline genera:

- Datos limpios y estructurados.
- Información confiable para analistas.
- Tablas optimizadas para reporting.
- Separación clara entre capas de procesamiento.
- Mejor trazabilidad de datos.

---

# Casos de uso

Este pipeline puede utilizarse para:

- Business Intelligence.
- Dashboards.
- Reporting.
- Analítica de datos.

---

# Posibles mejoras

- Automatización con Apache Airflow.

---

# Buenas prácticas implementadas

- Separación por capas.
- Modularización del pipeline.
- Reutilización de scripts.
- Validación de datos.
- Escalabilidad.
- Trazabilidad de información.

---

# Requisitos

- Python 3.10+
- Docker
- MySQL

---

# Dependencias principales

```txt
pandas
sqlalchemy
pymysql
python-dotenv
```

---

# Autor

Mariana Arroyo Rocha

---

# Licencia

MIT
