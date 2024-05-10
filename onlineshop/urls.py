from django.urls import path
from onlineshop.views import OrderView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Backend Online Shop APIS",
        default_version='1.0.0',
        description="This is swagger for our apis."

    ),
    public=True,
)

urlpatterns = [
     path('', views.index, name="index"),
    path('order/', OrderView.as_view(), name="Order"),
        path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
