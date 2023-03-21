from typing import Dict
from datasets.parameter_options import group_by_options
import squirrels as sq


def main() -> Dict[str, sq.Parameter]:
    return {
        'group_by': sq.SingleSelectParameter('Group By', group_by_options),
    }
