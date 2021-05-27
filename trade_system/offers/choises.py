from django.utils.translation import ugettext_lazy as _


BUY = 1
SALE = 2

OrderType = [
    (BUY, _('BUY')),
    (SALE, _('SALE'))
]