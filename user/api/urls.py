
from rest_framework.routers import DefaultRouter
from user.api.views import CustomerViewSet


router = DefaultRouter()

router.register(r"customer", CustomerViewSet)

urlpatterns = router.urls
