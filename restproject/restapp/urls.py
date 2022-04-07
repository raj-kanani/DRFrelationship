from django.conf.urls.i18n import i18n_patterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('singer', views.Singerview, basename='singer')
router.register('song', views.Songview, basename='song')

urlpatterns = [
    # path('', views.apt_root),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]

# urlpatterns = i18n_patterns(
#     format_suffix_patterns(urlpatterns, allowed=['json', 'html']) )

# urlpatterns = format_suffix_patterns(urlpatterns)
