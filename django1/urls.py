from django.contrib import admin
from django.urls import path
from core.views import main_view, contacts_view
# from core.views import test, test2, tests, tests2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('number', contacts_view)

    #___________________________________
    # path('', test),
    # path('custom/', test2),
    # path('tekst/', tests),
    # path('tekst2/', tests2)
]


