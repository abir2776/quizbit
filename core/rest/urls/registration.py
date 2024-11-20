from django.urls import path

from core.rest.views import registration

urlpatterns = [
    path(
        "register",
        registration.PublicUserRegistration.as_view(),
        name="user-registration",
    )
]
