from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack
# Create your tests here.

class GamesTest(TestCase):

    def setUp(self):
        self.purchaser = get_user_model().objects.create(username="tester",password="tester")
        self.snack = Snack.objects.create(name="tester", pur2=self.purchaser,desc='abs')

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack/snack-list.html')
        self.assertTemplateUsed(response,'_base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['snack_list']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].name, "tester")
        self.assertEqual(snacks[0].pur2.username, "tester")
        self.assertEqual(snacks[0].desc, 'abs')
        

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack/snack-detail.html')
        self.assertTemplateUsed(response, '_base.html')

        

    def test_create_view(self):
        obj={
            'name':"test2",
            'pur2':self.purchaser.id,
            'desc': "info..."
            
        }

        url = reverse('snack_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('snack_detail',args=[2]))

    def test_update_view(self):
        obj={
            'name':"test3",
            'pur2':self.purchaser.id,
            'desc': "info..."
            
        }

        url = reverse('snack_update',args=[1])
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('snack_detail',args=[1]))

    def test_delete_view(self):

        url = reverse('snack_delete',args=[1])
        response = self.client.post(path=url,follow=True)
        self.assertRedirects(response, reverse('snack_list'))