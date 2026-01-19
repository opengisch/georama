import math
from typing import TypeVar

from django.db import models

ModelType = TypeVar("ModelType", bound=models.Model)


class Service:
    models: list[models.Model]

    def count(self) -> int:
        count = 0
        for model in self.models:
            count += model.objects.count()
        return count

    def get(self, pk) -> list[ModelType]:
        items = []
        for model in self.models:
            items.append(model.objects.get(pk=pk))
        return items

    def get_list(self) -> list[ModelType]:
        items = []
        for model in self.models:
            items += model.objects.all()
        return items

    def get_list_page(self, start=0, offset=100) -> list[ModelType]:
        items = []
        for model in self.models:
            items += model.objects.all()[start : (start + offset)]
        return items

    def amount_of_pages(self, offset=100) -> int:
        return math.ceil(self.count() / offset)

    def pages_list(self, offset=100):
        page_numbers = list(range(1, self.amount_of_pages(offset) + 1))
        pages = []
        for page_number in page_numbers:
            pages.append([page_number, (page_number - 1) * offset])
        return pages
