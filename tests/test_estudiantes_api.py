import unittest

from api import create_app
from api.services.student_service import reset_data


class EstudiantesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        reset_data()

    def test_get_estudiantes(self):
        response = self.client.get('/api/estudiantes')
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertTrue(body['success'])
        self.assertEqual(body['total'], 3)

    def test_get_estudiante_por_id(self):
        response = self.client.get('/api/estudiantes/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['data']['nombre'], 'Juan Pérez')

    def test_crear_actualizar_y_eliminar_estudiante(self):
        created = self.client.post(
            '/api/estudiantes',
            json={'nombre': 'Ana Martinez', 'edad': 23, 'carrera': 'Arquitectura'},
        )
        self.assertEqual(created.status_code, 201)
        student_id = created.get_json()['data']['id']

        updated = self.client.patch(
            f'/api/estudiantes/{student_id}',
            json={'carrera': 'Diseño'},
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.get_json()['data']['carrera'], 'Diseño')

        deleted = self.client.delete(f'/api/estudiantes/{student_id}')
        self.assertEqual(deleted.status_code, 200)

        not_found = self.client.get(f'/api/estudiantes/{student_id}')
        self.assertEqual(not_found.status_code, 404)

    def test_resumen(self):
        response = self.client.get('/api/estudiantes/resumen')
        self.assertEqual(response.status_code, 200)
        body = response.get_json()['data']
        self.assertEqual(body['total'], 3)
        self.assertIn('Ingeniería', body['carreras'])


if __name__ == '__main__':
    unittest.main()
