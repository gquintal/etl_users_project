## 📋 Descripción

Proceso ETL (Extract, Transform, Load) desarrollado en Python que extrae datos de usuarios desde la API pública de RandomUser.me, los transforma aplicando reglas de validación y limpieza, y los carga en un archivo CSV.

## 🏗️ Estructura del Proyecto

```
etl_users_project/
├── etl/
│   ├── __init__.py
│   ├── extract.py          # Módulo de extracción de datos
│   ├── transform.py        # Módulo de transformación y limpieza
│   └── load.py            # Módulo de carga a CSV
├── tests/
│   ├── test_extract.py    # Pruebas de extracción
│   ├── test_transform.py  # Pruebas de transformación
│   └── test_load.py       # Pruebas de carga
├── output/
│   └── users_cleaned.csv  # Archivo de salida (generado)
├── main.py               # Punto de entrada principal
├── requirements.txt      # Dependencias del proyecto
├── README.md            # Documentación
└── etl.log             # Log del proceso (generado)
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)