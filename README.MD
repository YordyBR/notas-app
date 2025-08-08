# Aplicación CRUD de Notas (Flask + SQL Server)

## Requisitos
- Python 3.8+
- SQL Server (local o remoto) con ODBC Driver 17
- Instalar dependencias:  
  `pip install -r requirements.txt`

## Configuración
1. Ejecuta el script `sql/creacion_bd.sql` en tu SQL Server para crear las tablas y el usuario de prueba.
2. Configura tu cadena de conexión en `app.py` (variables `server`, `database`, `username`, `password`).

## Uso
```bash
python app.py
```
Navega a [http://localhost:5000](http://localhost:5000)  
Login de prueba: **admin / admin123**

## Funcionalidad
- Login
- CRUD de Notas (Crear, Leer, Actualizar, Eliminar)
- Cada nota está asociada a un usuario

## Para pruebas automatizadas
- Todos los formularios usan inputs y botones estándar (fáciles de automatizar con Selenium).
- Login y CRUD listos para scripts de prueba.
