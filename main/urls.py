from django.urls import path,include
from rest_framework import routers
from main import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'portfolio', views.PortfolioViewSet)

router.register(r'details', views.DetailsViewSet)


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.signup,name='signup'),
    path('Courses/',views.Courses,name='Courses'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('display/',views.display,name='display'),
    path('logout/',views.logout,name='logout'),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.updateportfolio),
    path('updatedetail/<int:id>',views.updatedetail),
    path('deletedetail/<int:id>',views.deletedetail),
    path('session/',views.session,name='session'),
    path('displayportfolio/<int:id>',views.displayportfolio),
    path('auth-api/', include(router.urls)),
]