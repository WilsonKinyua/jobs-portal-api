from django.test import TestCase
from .models import *


# category model test
class CategoryTest(TestCase):
    def test_category_creation(self):
        category = Category(name='Programming')
        category.save()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), 'Programming')

    def test_category_creation_with_icon(self):
        category = Category(name='Programming', icon='fa fa-briefcase')
        category.save()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), 'Programming')
        self.assertEqual(category.icon, 'fa fa-briefcase')


# jobs model test
class JobTest(TestCase):
    def test_job_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='12345',
            first_name='test',
            last_name='user',
            email='john@doe.com',
        )
        category = Category(name='Programming')
        category.save()
        job = Job(
            company_name='Google',
            company_website='https://www.google.com',
            title='Software Engineer',
            slug='software-engineer',
            category=category,
            salary_range='$100k - $200k',
            job_type='Full Time',
            job_description='We are looking for a software engineer to join our team.',
            location='New York',
            application_deadline='2020-01-01',
            experience=1,
            qualification='Bachelor of Engineering',
            link_to_job='https://www.google.com',
            user=user,
        )
        job.save()
        self.assertTrue(isinstance(job, Job))
        self.assertEqual(job.__str__(), 'Software Engineer')
        self.assertEqual(job.company_name, 'Google')
