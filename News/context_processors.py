
from django.utils import timezone

import pytz  # импортируем стандартный модуль для работы с часовыми поясами


def get_var(request):
    context = {
        'current_time': timezone.localtime(timezone.now()),
        'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
    }

    return context
