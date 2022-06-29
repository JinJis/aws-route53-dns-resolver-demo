from django.urls import path

from demo_app.apps.users.api.views import UserProfileViewSet

app_name = "users"

user_profile_detail = UserProfileViewSet.as_view()

urlpatterns = [
    path("profile/", user_profile_detail, name="user-profile-detail"),
]
