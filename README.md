# Proyecto 4: Sistema de Recomendaciones E-Commerce (Batch Inference)

Bienvenido al repositorio oficial del motor de recomendaciones distribuido, desarrollado como proyecto integrador de Big Data. Este sistema procesa interacciones a gran escala para generar sugerencias personalizadas (Top-20) para 1 millón de usuarios simulados.

## Equipo de Desarrollo (Arquitectura Multi-Nodo)

* **Evans Martínez (@EvansMS)** - Líder Técnico / Arquitecta de Pipeline
* **Blanca S.** - Ingeniera de Infraestructura (SRE) / Spark Master
* **Gamaliel C. (@Castro3003)** - Ingeniero de Datos (ETL)

## Arquitectura y Stack Tecnológico

El proyecto opera sobre un clúster **Apache Spark (Standalone)** distribuido en 3 nodos físicos (1 Master, 2 Workers) procesando datos alojados en un Data Lake local.

* **Procesamiento Distribuido:** Apache Spark 3.5.8 / PySpark (Python 3.10)
* **Algoritmo de Machine Learning:** Alternating Least Squares (ALS) nativo de Spark MLlib
* **Data Lakehouse (Almacenamiento Raw):** MinIO (S3-Compatible)
* **Persistencia Dual:** PostgreSQL 15 (Histórico Analítico) + Redis 7 (Caché de Baja Latencia)

## Estructura del Repositorio

El proyecto sigue una convención estándar para pipelines de datos:

```text
proyecto-ecommerce-bigdata/
├── conf/                 # Archivos de configuración de Spark y variables de entorno
├── data/                 # Directorio local (ignorado en Git) para output de ETL
├── docs/                 # Documentación técnica, diseño de arquitectura y diagramas
├── models/               # Modelos serializados de ALS
├── notebooks/            # Jupyter Notebooks para EDA y pruebas de amplificación
├── scripts/              # Shell scripts para levantar el clúster y utilidades
├── src/                  # Código fuente principal (PySpark)
│   ├── etl_features.py   # Fase 1: Limpieza y cálculo de rating implícito
│   ├── batch_inference.py # Fase 2: Entrenamiento y predicción ALS
│   └── persistence.py    # Fase 3: Escritura en PostgreSQL y Redis
├── docker-compose.yml    # Orquestación de MinIO, PostgreSQL y Redis
└── README.md             # Documentación principal del proyecto

## Volumen de Datos (MovieLens 25M Amplificado)

* **Usuarios Activos:** 1,000,000+
* **Interacciones (Ratings implícitos):** ~175,000,000
* **Catálogo de Ítems:** 62,423 productos
* **Peso Total de la Semilla:** 2.79 GB

## Requisitos y Ejecución Local (Workers)

Para que un nodo se una al clúster, debe cumplir con las siguientes dependencias:
1. Java Development Kit (JDK) 17.
2. Apache Spark 3.5.8 configurado en `SPARK_HOME`.
3. Entorno Anaconda con Python 3.10 y librerías base (`pyspark`, `pandas`, `numpy`).

*Nota: La ejecución del pipeline requiere que el nodo Master esté activo y los servicios de MinIO inicializados.*