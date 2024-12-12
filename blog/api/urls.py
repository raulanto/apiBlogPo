from django.urls import path
from .routers import router

urlpatterns = [
    # path('post/registro/', PostCreateViewSet.as_view(), name='postregistro'),

]

urlpatterns += router.urls
