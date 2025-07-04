# 🧪 ETL Users Project

Proceso ETL desarrollado en Python que extrae datos de usuarios desde una API pública, los transforma aplicando reglas de validación y limpieza, y los carga en un archivo CSV.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración](#configuración)
- [Contribuciones](#contribuciones)

## Descripción

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) que automatiza la recolección, limpieza y almacenamiento de datos de usuarios provenientes de una API pública. El resultado se almacena en un archivo CSV listo para análisis o integración en otros sistemas.

## Características

- Extracción de datos desde una API pública de usuarios
- Transformación de datos: validación, limpieza y normalización
- Carga de datos en formato CSV
- Código 100% Python

# 🚀 Instalación y Configuración

## Requisitos

- Python 3.8 o superior
- Paquetes adicionales indicados en `requirements.txt`

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/gquintal/etl_users_project.git
    cd etl_users_project
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal para iniciar el proceso ETL:

    ```bash
    python main.py
    ```

2. El archivo CSV generado estará disponible en la carpeta de salida especificada en el código.

## Estructura del Proyecto

- `main.py`: Orquestador del proceso ETL.
- `etl/`: Módulos para cada fase del ETL.
    - `extract.py`: Extracción de datos.
    - `transform.py`: Transformación y limpieza.
    - `load.py`: Carga a CSV.
- `output/`: Carpeta para archivos generados.
- `requirements.txt`: Dependencias del proyecto.

## Configuración
Configurar Variables de entorno (.env) (puedes agregar valores default en el código)

Ejemplos:

```bash
    # API Configuration
    USERS_API_URL="https://randomuser.me/api/"    #URL de la API (puedes agregar un default en el código)
    USERS_COUNT=100                               

    # Output Configuration  
    ETL_OUTPUT_DIR=output
    ETL_OUTPUT_FILE=users_cleaned.csv
```

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias o mejoras.
