from django.urls import path,register_converter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .utils import FloatConverter

# register_converter(converters.RomanNumeralConverter, 'roman')
register_converter(FloatConverter, 'float')

urlpatterns = [
    path("addtocart/<int:pk>",addToCart,name="addtocart"),
    path("api/v1/customer/order/add/",CartAddView.as_view(),name="addtocartapi"),
    path("ordersummary/",cartCheckoutPageView,name="cartview"),
    path("removesingleitemfromcart/<int:pk>",removeSingleItemFromCart,name="removesingleitemfromcart"),
    path("payment/checkout/<float:amount>",orderPaymentRequest,name="paymentcheckout"),
    path("paymentstatusupdate",paymentStatusAndOrderStatusUpdate,name="paymentstatusupdate"),
    path("cart/delete/item/<int:pk>",deleteItemFromCart,name="delete-from-cart"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)