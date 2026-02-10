# API Flask - Sistema de Estudiantes

API REST simple desarrollada con Flask para gestionar información de estudiantes.

## 📋 Descripción

Esta API proporciona endpoints para consultar y agregar estudiantes a una base de datos en memoria. Es ideal para demostraciones y propósitos educativos.

## 🚀 Endpoints Disponibles

### 1. Obtener todos los estudiantes
- **URL**: `/api/estudiantes`
- **Método**: `GET`
- **Respuesta exitosa**: 
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "nombre": "Juan Pérez",
      "edad": 20,
      "carrera": "Ingeniería"
    }
  ],
  "total": 1
}
```

### 2. Agregar un nuevo estudiante
- **URL**: `/api/estudiantes`
- **Método**: `POST`
- **Body (JSON)**:
```json
{
  "nombre": "Ana Martínez",
  "edad": 23,
  "carrera": "Arquitectura"
}
```
- **Respuesta exitosa**:
```json
{
  "success": true,
  "message": "Estudiante agregado exitosamente",
  "data": {
    "id": 4,
    "nombre": "Ana Martínez",
    "edad": 23,
    "carrera": "Arquitectura"
  }
}
```

## 💻 Instalación y Ejecución Local

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos para ejecutar localmente

1. **Clonar o descargar el proyecto**
```bash
cd API
```

2. **Crear un entorno virtual** (recomendado)
```bash
python -m venv env
```

3. **Activar el entorno virtual**
   - Windows:
   ```bash
   env\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source env/bin/activate
   ```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar la aplicación**
```bash
python app.py
```

6. **Probar la API**
   - La aplicación estará disponible en: `http://localhost:5000`
   - Prueba el endpoint GET: `http://localhost:5000/api/estudiantes`

## 🌐 Despliegue en Render

### Paso 1: Preparar el repositorio

1. **Crear un repositorio en GitHub**
   - Ve a [GitHub](https://github.com) y crea una cuenta si no tienes una
   - Haz clic en el botón "New repository"
   - Dale un nombre (ejemplo: `flask-api-estudiantes`)
   - Selecciona "Public" o "Private" según prefieras
   - Haz clic en "Create repository"

2. **Subir tu código a GitHub**
   
   Abre una terminal en la carpeta de tu proyecto y ejecuta:
   
   ```bash
   # Inicializar git (si no lo has hecho)
   git init
   
   # Agregar todos los archivos
   git add .
   
   # Hacer el primer commit
   git commit -m "Initial commit - Flask API"
   
   # Conectar con tu repositorio de GitHub
   git remote add origin https://github.com/TU_USUARIO/flask-api-estudiantes.git
   
   # Subir el código
   git branch -M main
   git push -u origin main
   ```
   
   > **Nota**: Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub

### Paso 2: Crear cuenta en Render

1. Ve a [Render.com](https://render.com)
2. Haz clic en "Get Started" o "Sign Up"
3. Puedes registrarte con tu cuenta de GitHub (recomendado) o con email
4. Completa el proceso de registro

### Paso 3: Crear un nuevo Web Service

1. **Desde el Dashboard de Render**:
   - Haz clic en el botón "New +" en la esquina superior derecha
   - Selecciona "Web Service"

2. **Conectar tu repositorio**:
   - Si es la primera vez, Render te pedirá autorización para acceder a tus repositorios de GitHub
   - Busca y selecciona el repositorio `flask-api-estudiantes` (o el nombre que le hayas dado)
   - Haz clic en "Connect"

### Paso 4: Configurar el Web Service

Completa el formulario con la siguiente información:

| Campo | Valor |
|-------|-------|
| **Name** | `flask-api-estudiantes` (o el nombre que prefieras) |
| **Region** | Selecciona la región más cercana (ejemplo: Oregon - USA) |
| **Branch** | `main` |
| **Root Directory** | Dejar vacío (a menos que tu app esté en una subcarpeta) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

### Paso 5: Configurar el plan

1. **Selecciona un plan**:
   - Para pruebas, selecciona el plan **"Free"**
   - El plan gratuito tiene algunas limitaciones pero es perfecto para demos

2. **Variables de entorno** (opcional):
   - Por ahora no necesitas agregar ninguna
   - Haz clic en "Create Web Service"

### Paso 6: Despliegue automático

1. Render comenzará a construir y desplegar tu aplicación automáticamente
2. Verás los logs en tiempo real
3. El proceso puede tomar 2-5 minutos
4. Cuando veas el mensaje **"Your service is live 🎉"**, tu API estará disponible

### Paso 7: Probar tu API desplegada

1. **Obtener la URL**:
   - En la parte superior de tu servicio verás una URL como: `https://flask-api-estudiantes.onrender.com`

2. **Probar el endpoint GET**:
   - Abre tu navegador y visita: `https://TU-APP.onrender.com/api/estudiantes`
   - Deberías ver la lista de estudiantes en formato JSON

3. **Probar el endpoint POST** (usando curl o Postman):
   ```bash
   curl -X POST https://TU-APP.onrender.com/api/estudiantes \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Pedro Sánchez","edad":24,"carrera":"Informática"}'
   ```

## 🔄 Actualizaciones Automáticas

Una vez configurado, cada vez que hagas `git push` a tu repositorio de GitHub:

1. Render detectará los cambios automáticamente
2. Reconstruirá la aplicación
3. Desplegará la nueva versión

```bash
# Hacer cambios en tu código
# Luego:
git add .
git commit -m "Descripción de los cambios"
git push
```

## ⚠️ Consideraciones Importantes

### Plan Gratuito de Render
- ✅ Perfecto para demos y proyectos educativos
- ⚠️ La aplicación se "duerme" después de 15 minutos de inactividad
- ⚠️ La primera petición después de dormir puede tardar 30-60 segundos
- ⚠️ 750 horas de uso gratuito al mes

### Datos en Memoria
- ⚠️ Esta API usa una lista en memoria para almacenar estudiantes
- ⚠️ Los datos se reinician cada vez que el servicio se reinicia
- 💡 Para datos persistentes, considera usar una base de datos (PostgreSQL, MongoDB, etc.)

## 📚 Recursos Adicionales

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de Render](https://render.com/docs)
- [Guía de despliegue de Flask en Render](https://render.com/docs/deploy-flask)

## 🛠️ Solución de Problemas

### Error: "Application failed to start"
- Verifica que `gunicorn` esté en `requirements.txt`
- Asegúrate de que el comando de inicio sea exactamente: `gunicorn app:app`

### Error 502 Bad Gateway
- Espera unos minutos, el servicio puede estar iniciándose
- Revisa los logs en el dashboard de Render

### La aplicación está lenta
- En el plan gratuito, la primera petición después de inactividad es lenta
- Considera actualizar a un plan de pago si necesitas mejor rendimiento

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.
