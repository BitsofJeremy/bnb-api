from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
# router.register(r'users', api_views.UserViewSet)
# router.register(r'groups', api_views.GroupViewSet)
router.register(r'auctions', api_views.AuctionsViewSet)
router.register(r'comments', api_views.CommentsViewSet)
router.register(r'bids', api_views.BidsViewSet)

urlpatterns = [
    # Set the main route to api
    path('', include('api.urls')),
    # Set the admin route
    path('admin/', admin.site.urls),
    # API stuff
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
