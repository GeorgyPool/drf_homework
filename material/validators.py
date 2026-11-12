import re

from rest_framework.serializers import ValidationError


class CheckingUrl:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = dict(value).get(self.field)
        if url is not None:
            pattern = r"https://www.youtube.com/"

            if not bool(re.match(pattern, url, flags=0)):
                raise ValidationError(
                    "Нельзя ссылаться на сторонние источники, мы поддерживаем только ссылки на youtube"
                )
