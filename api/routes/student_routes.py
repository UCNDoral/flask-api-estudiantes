from flask import Blueprint, jsonify, request

from api.services.student_service import (
    ValidationError,
    create_student,
    delete_student,
    get_student,
    get_summary,
    list_students,
    update_student,
)

students_bp = Blueprint("students", __name__, url_prefix="/api")


@students_bp.get("/health")
def health_check():
    return jsonify({"success": True, "status": "ok"}), 200


@students_bp.get("/estudiantes")
def obtener_estudiantes():
    carrera = request.args.get("carrera")
    edad_min = request.args.get("edad_min", type=int)
    edad_max = request.args.get("edad_max", type=int)

    students = list_students(carrera=carrera, edad_min=edad_min, edad_max=edad_max)
    return jsonify({"success": True, "data": students, "total": len(students)}), 200


@students_bp.get("/estudiantes/resumen")
def resumen_estudiantes():
    return jsonify({"success": True, "data": get_summary()}), 200


@students_bp.get("/estudiantes/<int:student_id>")
def obtener_estudiante(student_id):
    student = get_student(student_id)
    if not student:
        return jsonify({"success": False, "error": "Estudiante no encontrado"}), 404

    return jsonify({"success": True, "data": student}), 200


@students_bp.post("/estudiantes")
def agregar_estudiante():
    data = request.get_json(silent=True)
    try:
        student = create_student(data)
    except ValidationError as err:
        return jsonify({"success": False, "error": str(err)}), 400

    return (
        jsonify(
            {
                "success": True,
                "message": "Estudiante agregado exitosamente",
                "data": student,
            }
        ),
        201,
    )


@students_bp.put("/estudiantes/<int:student_id>")
def reemplazar_estudiante(student_id):
    data = request.get_json(silent=True)
    try:
        student = update_student(student_id, data, partial=False)
    except ValidationError as err:
        return jsonify({"success": False, "error": str(err)}), 400

    if not student:
        return jsonify({"success": False, "error": "Estudiante no encontrado"}), 404

    return jsonify({"success": True, "message": "Estudiante actualizado", "data": student}), 200


@students_bp.patch("/estudiantes/<int:student_id>")
def actualizar_parcial_estudiante(student_id):
    data = request.get_json(silent=True)
    try:
        student = update_student(student_id, data, partial=True)
    except ValidationError as err:
        return jsonify({"success": False, "error": str(err)}), 400

    if not student:
        return jsonify({"success": False, "error": "Estudiante no encontrado"}), 404

    return jsonify({"success": True, "message": "Estudiante actualizado", "data": student}), 200


@students_bp.delete("/estudiantes/<int:student_id>")
def eliminar_estudiante(student_id):
    deleted = delete_student(student_id)
    if not deleted:
        return jsonify({"success": False, "error": "Estudiante no encontrado"}), 404

    return jsonify({"success": True, "message": "Estudiante eliminado", "data": deleted}), 200
