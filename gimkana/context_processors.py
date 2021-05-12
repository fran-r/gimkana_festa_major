from django.db.models import Count, Sum, Case, When, F

from .models import UserQr


def scoring(request):
    if not request.user.is_authenticated:
        return {}

    result = (
        UserQr.objects
        .filter(user=request.user, scan_date__isnull=False)
        .exclude(value=0)
        .aggregate(
            score=Sum('value'),
            num_qrs=Count(Case(When(is_shop=False, then=1))),
            num_shops=Count(Case(When(is_shop=True, then=1))),
            num_hints=Sum('hints'),
        )
    )

    return {
        'score': int(result['score'] or 0),
        'num_qrs': int(result['num_qrs'] or 0),
        'num_shops': int(result['num_shops'] or 0),
        'num_hints': int(result['num_hints'] or 0),
    }
