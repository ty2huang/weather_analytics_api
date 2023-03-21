from typing import Dict
from datasets.parameter_options import trend_type_options, filter_by_options, time_period_options
import squirrels as sq


def main() -> Dict[str, sq.Parameter]:
    return {
        'trend_type': sq.SingleSelectParameter('Trend Type', trend_type_options),
        'filter_by': sq.SingleSelectParameter('Filter Time Period By', filter_by_options, trigger_refresh=True),
        'time_period': sq.DataSourceParameter(sq.WidgetType.MultiSelect, 'Time Period of', time_period_options, parent='filter_by')
    }
