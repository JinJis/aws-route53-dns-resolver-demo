import pytest

from demo_app.apps.users.models import User

pytestmark = pytest.mark.django_db


def test_user_profile_detail(user: User):
    pass
