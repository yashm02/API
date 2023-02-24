from django.urls import path
from .views import WorkList, ArtistList,register

urlpatterns = [
    path('register/',register,name="register"),
    path('works/', WorkList.as_view()),
    path('artists/', ArtistList.as_view()),
]
