from django.test import TestCase
from django.urls import reverse

from .models import Socio


class SocioViewsTests(TestCase):
    def setUp(self):
        self.socio = Socio.objects.create(
            nombre='Ana',
            apellido='Perez',
            DNI='12345678',
            Fecha_nacimiento='2000-01-02',
            Telefono='1112345678',
            email='ana@example.com',
            categoria='M14',
        )

    def test_lista_socios_renders(self):
        response = self.client.get(reverse('lista_socios'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.socio.apellido)

    def test_formularios_de_crear_editar_y_eliminar_rinden(self):
        for url_name, args in (
            ('crear_socio', ()),
            ('editar_socio', (self.socio.pk,)),
            ('eliminar_socio', (self.socio.pk,)),
        ):
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name, args=args))
                self.assertEqual(response.status_code, 200)

    def test_crear_socio(self):
        response = self.client.post(
            reverse('crear_socio'),
            {
                'nombre': 'Luis',
                'apellido': 'Gomez',
                'DNI': '87654321',
                'Fecha_nacimiento': '2001-03-04',
                'Telefono': '1198765432',
                'email': 'luis@example.com',
                'categoria': 'M16',
                'activo': 'on',
            },
        )

        self.assertRedirects(response, reverse('lista_socios'))
        self.assertTrue(Socio.objects.filter(DNI='87654321').exists())

    def test_editar_socio_actualiza_campos_del_modelo(self):
        response = self.client.post(
            reverse('editar_socio', args=[self.socio.pk]),
            {
                'nombre': 'Ana Maria',
                'apellido': 'Perez',
                'DNI': self.socio.DNI,
                'Fecha_nacimiento': '2000-01-02',
                'Telefono': '1199999999',
                'email': self.socio.email,
                'categoria': 'M18',
                'apto_medico_al_dia': 'on',
                'activo': 'on',
            },
        )

        self.assertRedirects(response, reverse('lista_socios'))
        self.socio.refresh_from_db()
        self.assertEqual(self.socio.nombre, 'Ana Maria')
        self.assertEqual(self.socio.Telefono, '1199999999')
        self.assertEqual(self.socio.categoria, 'M18')
