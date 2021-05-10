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
        'num_qrs': int(result['num_scanned'] or 0) - int(result['num_shops'] or 0),
        'num_hints': int(result['num_hints'] or 0),
        'num_shops': int(result['num_shops'] or 0),
        'score': int(result['score'] or 0),
    }
