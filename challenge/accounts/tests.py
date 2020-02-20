from django.test import TestCase, Client
from . import models
from . import serializers
import json
from rest_framework import status
from random import randrange

# Create your tests here.
class AccountsTest(TestCase):
    def setUp(self):
        models.Account.objects.create(name="Account1", phone="122434")
        models.Account.objects.create(name="Account2", shipping_city="Havana", shipping_country="Cuba")


    def _decode_response(self, content):
        json_object = content.decode('utf8').replace("'", '"')
        return json.loads(json_object)

    def test_get_all_accounts(self):
        response = self.client.get('http://localhost:8000/api/v1/accounts/')
        data_response = self._decode_response(response.content)['results']

        accounts = models.Account.objects.all()
        serializer = serializers.AccountSerializer(accounts, many=True)

        self.assertEqual(data_response, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_account(self):
        account = models.Account.objects.first()

        response = self.client.put(f'http://localhost:8000/api/v1/accounts/{account.id}/', {
            'phone': '12123',
            'shipping_state': 'state1',
            'shipping_zip': '12331232'
        }, content_type='application/json')
        data_response = self._decode_response(response.content)

        account.phone = '12123'
        account.shipping_state = 'state1'
        account.shipping_zip = '12331232'
        serializer = serializers.AccountSerializer(account)
        self.assertEqual(data_response, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def _fuzzy_function(self, number):
        if number % 15 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return number

    def _get_fuzz_object(self, x = 100):
        return {
            'x': x,
            'fizzbuzz': [self._fuzzy_function(number) for number in range(1, x + 1)]
        }

    def test_fizz_buzz_with_param(self):
        x = randrange(100)
        response = self.client.get(f'http://localhost:8000/api/v1/fizz-buzz/?x={x}')
        data_response = self._decode_response(response.content)

        test_object = self._get_fuzz_object(x)
        self.assertEqual(data_response, test_object)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fizz_buzz_without_param(self):
        response = self.client.get(f'http://localhost:8000/api/v1/fizz-buzz/')
        data_response = self._decode_response(response.content)

        test_object = self._get_fuzz_object()
        self.assertEqual(data_response, test_object)
        self.assertEqual(response.status_code, status.HTTP_200_OK)