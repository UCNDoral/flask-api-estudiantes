"""Reglas de negocio para estudiantes."""

from api.data.store import store


class ValidationError(Exception):
    pass


REQUIRED_FIELDS = ("nombre", "edad", "carrera")


def _validate_student_payload(data, partial=False):
    if not data:
        raise ValidationError("Se requiere un body JSON con datos del estudiante")

    if not partial:
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            raise ValidationError(
                f"Faltan datos requeridos: {', '.join(missing)}"
            )

    if "nombre" in data and (not isinstance(data["nombre"], str) or not data["nombre"].strip()):
        raise ValidationError("El campo nombre debe ser un texto no vacío")

    if "edad" in data:
        if not isinstance(data["edad"], int):
            raise ValidationError("El campo edad debe ser un número entero")
        if data["edad"] < 15 or data["edad"] > 100:
            raise ValidationError("El campo edad debe estar entre 15 y 100")

    if "carrera" in data and (not isinstance(data["carrera"], str) or not data["carrera"].strip()):
        raise ValidationError("El campo carrera debe ser un texto no vacío")


def list_students(carrera=None, edad_min=None, edad_max=None):
    students = store.all()
    filtered = students

    if carrera:
        filtered = [s for s in filtered if s["carrera"].lower() == carrera.lower()]

    if edad_min is not None:
        filtered = [s for s in filtered if s["edad"] >= edad_min]

    if edad_max is not None:
        filtered = [s for s in filtered if s["edad"] <= edad_max]

    return filtered


def get_student(student_id):
    return store.by_id(student_id)


def create_student(data):
    _validate_student_payload(data)
    payload = {
        "nombre": data["nombre"].strip(),
        "edad": data["edad"],
        "carrera": data["carrera"].strip(),
    }
    return store.add(payload)


def update_student(student_id, data, partial=False):
    _validate_student_payload(data, partial=partial)
    student = get_student(student_id)
    if not student:
        return None

    new_values = {}
    for field in REQUIRED_FIELDS:
        if field in data:
            value = data[field]
            if isinstance(value, str):
                value = value.strip()
            new_values[field] = value

    return store.update(student, new_values)


def delete_student(student_id):
    student = get_student(student_id)
    if not student:
        return None

    store.delete(student)
    return student


def get_summary():
    students = store.all()
    total = len(students)
    if total == 0:
        return {"total": 0, "edad_promedio": 0, "carreras": {}}

    avg_age = round(sum(s["edad"] for s in students) / total, 2)
    carreras = {}
    for student in students:
        carreras[student["carrera"]] = carreras.get(student["carrera"], 0) + 1

    return {"total": total, "edad_promedio": avg_age, "carreras": carreras}


def reset_data():
    store.reset()
