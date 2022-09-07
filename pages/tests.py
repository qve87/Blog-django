from webbrowser import get
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse


from .models import Page


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        cls.page = Page.objects.create(
            title="testtitle",
            body="testbody",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.page.title, "testtitle")
        self.assertEqual(self.page.body, "testbody")
        self.assertEqual(self.page.author.username, "testuser")
        self.assertEqual(str(self.page), "testtitle")
        self.assertEqual(self.page.get_absolute_url(), "/page/1")


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

    def testLogin(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_url_exists_at_correct_location_detail_view(self):
    #     response = self.client.get("page/1")
    #     self.assertEqual(response.status_code, 200)

    # def test_post_listview(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "testbody")
    #     self.assertTemplateUsed(response, "home.html")

    # def test_post_detailview(self):
    #     response = self.client.get(reverse("pages_detail", kwargs={"pk": self.page.pk}))
    #     no_response = self.client.get("/page/1000")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "testtitle")
    #     self.assertTemplateUsed(response, "pages_detail.html")
