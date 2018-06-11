import os
import json

from django.test import TestCase
from django.conf import settings

from .utils import header_to_field
from .models import Pulse


class ManagePulsesTestCase(TestCase):

    def setUp(self):
        for i in range(10):
            Pulse.objects.create(
                name='A Test Pulse',
                type='cinsk',
                maximum_rabi_rate=34,
                polar_angle=0.165)

    def test_create_new_pulse(self):
        """
        - Create a new pulse

        """
        data = {
            "data": {
                "type": "pulse",
                "attributes": {
                    "name": "A New Pulse",
                    "type": "cinsk",
                    "maximum_rabi_rate": 34,
                    "polar_angle": 0.165
                }
            }
        }
        response = self.client.post(
            '/api/pulse/',
            json.dumps(data),
            content_type='application/vnd.api+json')

        self.assertEquals(response.status_code, 201)

        self.assertEquals(
            Pulse.objects.filter(name='A New Pulse').count(), 1)

    def test_list_pulses(self):
        """
        - List all pulses (five per page)

        """
        response = self.client.get('/api/pulse/')
        self.assertEquals(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEquals(len(data['data']), 5)

    def test_get_pulse(self):
        """
        - Get a specific pulse

        """
        pulse = Pulse.objects.all()[0]

        response = self.client.get('/api/pulse/{}/'.format(pulse.pk))
        self.assertEquals(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEquals(data['data']['id'], str(pulse.pk))

    def test_update_pulse(self):
        """
        - Update a specific pulse

        """
        pulse = Pulse.objects.all()[0]

        new_name = "Dr. Evil's Pulse"
        old_polar_angle = pulse.polar_angle

        patch_data = {
            "data": {
                "type": "pulse",
                "id": str(pulse.pk),
                "attributes": {
                    "name": new_name,
                }
            }
        }

        response = self.client.patch(
            '/api/pulse/{}/'.format(pulse.pk),
            data=json.dumps(patch_data),
            content_type='application/vnd.api+json')

        self.assertEquals(response.status_code, 200)

        data = json.loads(response.content)
        updated_pulse = data['data']

        self.assertEquals(updated_pulse['id'], str(pulse.pk))
        self.assertEquals(updated_pulse['attributes']['name'], new_name)
        self.assertEquals(updated_pulse['attributes']['polar_angle'], old_polar_angle)

    def test_delete_pulse(self):
        """
        - Delete a specific pulse

        """
        pulse = Pulse.objects.all()[0]

        response = self.client.delete('/api/pulse/{}/'.format(pulse.pk))
        self.assertEquals(response.status_code, 204)

        with self.assertRaises(Pulse.DoesNotExist):
            Pulse.objects.get(pk=pulse.pk)


class UploadPulsesTestCase(TestCase):

    def get_pulses_data(self, filename=None):
        if filename is None:
            filename = 'pulses.csv'

        path = os.path.join(settings.BASE_DIR, 'doc/files/', filename)

        data = ""
        with open(path, 'rb', buffering=0) as fh:
            data = fh.read()

        return data

    def get_upload_response(self, data):
        return self.client.post(
            '/api/pulse/upload/',
            data,
            content_type='text/csv')

    def test_invalid_headers(self):
        data = self.get_pulses_data(filename='pulses_invalid.csv')
        response = self.get_upload_response(data)
        self.assertEquals(response.status_code, 400)

    def test_upload_pulses(self):
        """
        Implement an endpoint that can accept a CSV file where each row
        represents a pulse.

        """
        data = self.get_pulses_data()
        response = self.get_upload_response(data)
        self.assertEquals(response.status_code, 200)

        self.assertEquals(Pulse.objects.count(), 4)

    def test_downlad_pulses(self):
        """
        Implement an endpoint that returns all pulses in CSV format. The CSV
        should not include a header row.

        """
        for i in range(5):
            Pulse.objects.create(
                name='A Test Pulse',
                type='cinsk',
                maximum_rabi_rate=34,
                polar_angle=0.165)

        response = self.client.get('/api/pulse/download/')

        self.assertTrue('Content-Disposition' in response)
        self.assertEquals(len(response.content.decode('utf-8').splitlines()), 5)


class UtilsTestCase(TestCase):

    def setUp(self):
        self.field = 'maximum_rabi_rate'

    def test_header_to_field_1(self):
        self.assertEquals(
            header_to_field('Maximum Rabi Rate'),
            self.field)

    def test_header_to_field_2(self):
        self.assertEquals(
            header_to_field('MaximumRabiRate'),
            self.field)

    def test_header_to_field_3(self):
        self.assertEquals(
            header_to_field('maximum rabi rate'),
            self.field)

    def test_header_to_field_4(self):
        self.assertEquals(
            header_to_field('Maximum_Rabi_Rate'),
            self.field)