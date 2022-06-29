import pytest
from django.test import RequestFactory

from demo_app.apps.users.api.views import UserProfileViewSet
from demo_app.apps.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserProfileViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()
