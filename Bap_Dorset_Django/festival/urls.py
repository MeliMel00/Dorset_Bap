from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import add_to_cart, cart, delete_cart, index, plan_agenda, ticket_office
from accounts.views import login_user, signup, logout_user

from festival import settings

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('plan-agenda/', plan_agenda, name="plan-agenda"),
    path('ticket-office/', ticket_office, name="ticket-office"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('cart/', cart, name="cart"),
    path('cart/delete/', delete_cart, name="delete-cart"),
    # path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
