from django.urls import path
from vision import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('courses', views.courses),
    path('contact', views.contact),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('book',views.book),
    path('que',views.que),
    path('notes',views.notes),
    path('search',views.search),
    path('productdetail/<pid>',views.productdetail),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.remove),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
