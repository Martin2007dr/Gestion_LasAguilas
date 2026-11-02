from django.test import TestCase
from django.urls import reverse

from apps.socios.models import Socio

from .models import Pago_Cuota


class CuotasViewsTests(TestCase):
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

    def test_lista_cuotas_renders(self):
        response = self.client.get(reverse('lista_cuotas'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cuotas/list.html')

    def test_formulario_de_pago_rinde(self):
        response = self.client.get(reverse('registrar_pago'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.socio.DNI)

    def test_registrar_pago(self):
        response = self.client.post(
            reverse('registrar_pago'),
            {
                'socio': self.socio.pk,
                'mes': 10,
                'anio': 2026,
                'monto': '5000.00',
                'medio_pago': 'EF',
            },
        )

        self.assertRedirects(response, reverse('lista_cuotas'))
        pago = Pago_Cuota.objects.get(socio=self.socio)
        self.assertEqual(pago.mes, 10)
        self.assertEqual(pago.anio, 2026)
        self.assertEqual(str(pago.monto), '5000.00')
