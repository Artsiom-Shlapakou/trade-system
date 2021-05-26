from django.utils.translation import ugettext_lazy as _


# USD = 'USD'
# BYN = 'BYN'
# RUB = 'RUB'

# = [
#     (USD, _('USD')),
#     (BYN, _('BYN')),
#     (RUB, _('RUB'))
#     ]

BUY = 1
SALE = 2


OrderType = [
    BUY, _(BUY),
    SALE, _(SALE)
]
