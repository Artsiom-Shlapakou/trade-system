from django.utils.translation import gettext_lazy as _


OPEN = 1
CLOSE = 2 


STATUSES = [
    (OPEN, _('OPEN')),
    (CLOSE, _('CLOSE'))
]