from django.test import TestCase

from core.models import User


class UserTest(TestCase):

    def test_user_list_get_1(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [])

    def test_user_list_get_2(self):
        u1 = User.objects.create(name='Виноградов Артур')
        u2 = User.objects.create(name='Степанова Анастасия')
        u3 = User.objects.create(name='Носырев Андрей')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'id': u1.pk,
                    'name': u1.name
                },
                {
                    'id': u2.pk,
                    'name': u2.name
                },
                {
                    'id': u3.pk,
                    'name': u3.name
                },
            ]
        )

    def test_user_create_1(self):
        response = self.client.post('/api/users/', {'name': 'ФИО 1'})
        user = User.objects.get(pk=response.json()['id'])
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'id': user.id,
                'name': user.name
            }
        )

    def test_user_create_2(self):
        response = self.client.post('/api/users/', {'name': ''})
        self.assertEqual(response.status_code, 400)

    def test_user_create_3(self):
        response = self.client.post('/api/users/')
        self.assertEqual(response.status_code, 400)

    def test_user_create_update_1(self):
        response = self.client.post('/api/users/', {'name': 'Старое ФИО'})
        user_id = response.json()['id']
        self.assertEqual(response.status_code, 201)

        response = self.client.patch(f'/api/users/{user_id}/',
                                     {'name': 'Новое ФИО'},
                                     content_type='application/json'
                                     )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'id': user_id,
                'name': 'Новое ФИО'
            }
        )

    def test_user_get_1(self):
        response = self.client.post('/api/users/', {'name': 'Какое-то ФИО'})
        user_id = response.json()['id']
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'/api/users/{user_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'id': user_id,
                'name': 'Какое-то ФИО'
            }
        )

    def test_user_get_2(self):
        response = self.client.post('/api/users/', {'name': 'Какое-то ФИО1'})
        user_id = response.json()['id']
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'/api/users/{user_id + 10}/')
        self.assertEqual(response.status_code, 404)
        self.assertIn('detail', response.json())

    def test_user_delete_1(self):
        response = self.client.post('/api/users/', {'name': 'Я тебя удалю'})
        user_id = response.json()['id']
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'/api/users/{user_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'id': user_id,
                'name': 'Я тебя удалю'
            }
        )
        response = self.client.delete(f'/api/users/{user_id}/')
        self.assertEqual(response.status_code, 204)

        response = self.client.get(f'/api/users/{user_id}/')
        self.assertEqual(response.status_code, 404)
        self.assertIn('detail', response.json())
