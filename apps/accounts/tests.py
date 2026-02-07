from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from .models import Profile
from .forms import RegisterForm, UserUpdateForm


class ProfileSignalTests(TestCase):
    """Test that a Profile is auto-created when a User is created."""

    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123!')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_str(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123!')
        self.assertEqual(str(user.profile), "testuser's profile")


class ProfileModelTests(TestCase):
    """Test Profile model methods and properties."""

    def test_avatar_initial_from_first_name(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123!')
        user.first_name = 'Alice'
        user.save()
        self.assertEqual(user.profile.avatar_initial, 'A')

    def test_avatar_initial_from_username(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123!')
        self.assertEqual(user.profile.avatar_initial, 'T')


class RegisterFormTests(TestCase):
    """Test the registration form."""

    def test_valid_registration(self):
        form = RegisterForm(data={
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertTrue(form.is_valid())

    def test_duplicate_email_rejected(self):
        User.objects.create_user('existing', 'taken@example.com', 'TestPass123!')
        form = RegisterForm(data={
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'taken@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class UserUpdateFormTests(TestCase):
    """Test the user update form."""

    def test_own_email_allowed(self):
        user = User.objects.create_user('testuser', 'me@example.com', 'TestPass123!')
        form = UserUpdateForm(
            data={'first_name': 'Test', 'last_name': 'User', 'email': 'me@example.com'},
            instance=user,
        )
        self.assertTrue(form.is_valid())

    def test_duplicate_email_rejected(self):
        User.objects.create_user('other', 'taken@example.com', 'TestPass123!')
        user = User.objects.create_user('testuser', 'me@example.com', 'TestPass123!')
        form = UserUpdateForm(
            data={'first_name': 'Test', 'last_name': 'User', 'email': 'taken@example.com'},
            instance=user,
        )
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class AuthViewTests(TestCase):
    """Test authentication views."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'TestPass123!')

    def test_home_page_accessible(self):
        response = self.client.get(reverse('accounts:home'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_accessible(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_accessible(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_accessible_when_logged_in(self):
        self.client.login(username='testuser', password='TestPass123!')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)

    def test_register_creates_user(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())


class APIPermissionTests(TestCase):
    """Test API permissions."""

    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user('user1', 'u1@example.com', 'TestPass123!')
        self.user2 = User.objects.create_user('user2', 'u2@example.com', 'TestPass123!')
        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'AdminPass123!')

    def test_unauthenticated_access_denied(self):
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_list_profiles(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_can_update_own_profile(self):
        self.client.force_authenticate(user=self.user1)
        profile = self.user1.profile
        response = self.client.patch(f'/api/profiles/{profile.id}/', {'bio': 'Updated'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_owner_cannot_update_profile(self):
        self.client.force_authenticate(user=self.user2)
        profile = self.user1.profile
        response = self.client.patch(f'/api/profiles/{profile.id}/', {'bio': 'Hacked'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_sees_email_in_user_list(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/users/')
        data = response.json()
        self.assertIn('email', data['results'][0])

    def test_regular_user_no_email_in_user_list(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get('/api/users/')
        data = response.json()
        self.assertNotIn('email', data['results'][0])

    def test_api_pagination(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get('/api/profiles/')
        data = response.json()
        self.assertIn('results', data)
        self.assertIn('count', data)
