from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView

from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name="login"),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name="logout"),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),

    url(r'^', TemplateView.as_view(template_name='index.html'), name='index'),
)
