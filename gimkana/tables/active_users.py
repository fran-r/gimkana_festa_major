from django_tables2 import Column
from django_tables2.tables import Table

from gimkana.models.userqr import UserQr


class UsersTable(Table):
    user__username = Column(verbose_name='Usuario')
    user__email = Column(verbose_name='email', visible=False)
    score = Column(verbose_name='Puntos')
    num_qrs = Column(verbose_name='QRs')
    num_shops = Column(verbose_name='Comercios')
    num_hints = Column(verbose_name='Pistas')

    class Meta:
        model = UserQr
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('user__username', 'user__email', 'score', 'num_qrs', 'num_shops', 'num_hints')
        ordering = ['score', 'num_scanned']
