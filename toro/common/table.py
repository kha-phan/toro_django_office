import itertools
from django_tables2 import Table, columns


class CounterColumnTableMixin(Table):
    row_number = columns.Column(verbose_name='No.', empty_values=(), orderable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return f'{next(self.counter) + 1}'


class UpdatedAtFormattedTableMixin(Table):
    updated_at = columns.DateTimeColumn(format='Y-m-d H:i:s ', verbose_name='Updated At')
