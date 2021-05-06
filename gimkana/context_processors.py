from django.db.models import Count, Sum

from .models import UserQr


def scoring(request):
    if not request.user.is_authenticated:
        return {}

    result = (
        UserQr.objects
        .filter(user=request.user, scan_date__isnull=False)
        .aggregate(
            num_scanned=Count('*'),
            num_shops=Sum('is_shop'),
            num_hints=Sum('hints'),
            score=Sum('value'),
        )
    )

    return {
        'num_qrs': (result['num_scanned'] - result['num_shops']) or 0,
        'num_hints': result['num_hints'] or 0,
        'num_shops': result['num_shops'] or 0,
        'score': result['score'] or 0,
    }
