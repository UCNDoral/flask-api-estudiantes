# API Flask - Sistema de Estudiantes

API REST desarrollada con Flask para gestionar estudiantes en memoria, ahora con arquitectura modular (rutas, servicios y capa de datos).

## 🚀 Estructura del proyecto

```text
.
├── api/
│   ├── __init__.py           # Factory de Flask
│   ├── data/store.py         # Almacenamiento en memoria
│   ├── services/student_service.py  # Reglas de negocio y validaciones
│   └── routes/student_routes.py     # Endpoints REST
├── tests/test_estudiantes_api.py    # Pruebas con unittest
├── app.py                    # Punto de entrada (gunicorn app:app)
└── requirements.txt
```

## 📌 Endpoints disponibles

### Salud de la API
- `GET /api/health`

### Estudiantes
- `GET /api/estudiantes` → lista todos los estudiantes
- `GET /api/estudiantes?carrera=Medicina&edad_min=20&edad_max=24` → lista con filtros
- `GET /api/estudiantes/<id>` → obtiene un estudiante por ID
- `POST /api/estudiantes` → crea un estudiante
- `PUT /api/estudiantes/<id>` → reemplaza todos los datos de un estudiante
- `PATCH /api/estudiantes/<id>` → actualización parcial de un estudiante
- `DELETE /api/estudiantes/<id>` → elimina un estudiante
- `GET /api/estudiantes/resumen` → métricas (total, edad promedio, cantidad por carrera)

## Ejemplo de payload para crear/actualizar

```json
{
  "nombre": "Ana Martínez",
  "edad": 23,
  "carrera": "Arquitectura"
}
```

Reglas básicas:
- `nombre`: texto no vacío
- `edad`: entero entre 15 y 100
- `carrera`: texto no vacío

## ▶️ Ejecución local

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
pip install -r requirements.txt
python app.py
```

## ✅ Pruebas

```bash
python -m unittest discover -s tests
```

## 🌐 Despliegue en Render

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
