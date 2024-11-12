from django.contrib import admin
from django.urls import path, include
# Простой API-ответ для корневого пути
from rest_framework.views import APIView
from rest_framework.response import Response
class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Task Manager API!"})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Подключаем маршруты 'tasks'
    path('', RootView.as_view(), name='root'),
]
