from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
estudiantes = [
    {"id": 1, "nombre": "Juan Pérez", "edad": 20, "carrera": "Ingeniería"},
    {"id": 2, "nombre": "María García", "edad": 22, "carrera": "Medicina"},
    {"id": 3, "nombre": "Carlos López", "edad": 21, "carrera": "Derecho"}
]

# Endpoint 1: GET - Obtener todos los estudiantes
@app.route('/api/estudiantes', methods=['GET'])
def obtener_estudiantes():
    """
    Endpoint para obtener la lista de todos los estudiantes
    """
    return jsonify({
        "success": True,
        "data": estudiantes,
        "total": len(estudiantes)
    }), 200

# Endpoint 2: POST - Agregar un nuevo estudiante
@app.route('/api/estudiantes', methods=['POST'])
def agregar_estudiante():
    """
    Endpoint para agregar un nuevo estudiante
    Espera un JSON con: nombre, edad, carrera
    """
    datos = request.get_json()
    
    # Validación básica
    if not datos or 'nombre' not in datos or 'edad' not in datos or 'carrera' not in datos:
        return jsonify({
            "success": False,
            "error": "Faltan datos requeridos: nombre, edad, carrera"
        }), 400
    
    # Crear nuevo estudiante
    nuevo_estudiante = {
        "id": len(estudiantes) + 1,
        "nombre": datos['nombre'],
        "edad": datos['edad'],
        "carrera": datos['carrera']
    }
    
    estudiantes.append(nuevo_estudiante)
    
    return jsonify({
        "success": True,
        "message": "Estudiante agregado exitosamente",
        "data": nuevo_estudiante
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
