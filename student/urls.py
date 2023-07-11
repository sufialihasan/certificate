from django.urls import path
from . import views
urlpatterns = [
    path('',views.search,name='search'),
    path('safe',views.safe,name='save'),
    path('update',views.update,name='update'),
    path('update_data',views.update_data,name='update_data'),
    path('delete',views.delete,name='delete'),
    path('dell',views.dell,name='dell'),
    path('home',views.home,name='home'),
    path('fetch',views.fetch,name='fetch'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('prof',views.prof,name='prof'),
    path('showw',views.showw,name='showw'),
    path('show',views.show,name='show'),
    path('record',views.record,name='record')

]