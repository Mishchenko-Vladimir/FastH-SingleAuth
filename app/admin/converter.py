from typing import Any
from sqlalchemy.orm import ColumnProperty
from sqladmin.forms import converts, ModelConverter as ModelConverterGeneric
from sqladmin.fields import DateTimeField


class ModelConverter(ModelConverterGeneric):
    """Конвертер для полей created_at, что бы отображать как календарь с выбором времени, а не как строка"""

    @converts("TIMESTAMPAware")
    def conv_timestamp_aware(
        self,
        model: type,
        prop: ColumnProperty,
        kwargs: dict[str, Any],
    ):
        return DateTimeField(**kwargs)
