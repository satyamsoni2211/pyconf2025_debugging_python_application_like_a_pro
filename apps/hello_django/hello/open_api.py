from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Debugging Python applications like a Pro",
        default_version='1',
        description="A hands-on Python workshop covering advanced topics and best practices.",
        terms_of_service="https://2025.pyconfhyd.org/code-of-conduct",
        contact=openapi.Contact(email="kr.pratik@ymail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
