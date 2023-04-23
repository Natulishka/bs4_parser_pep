from pathlib import Path
from typing import Dict, Tuple

MAIN_DOC_URL: str = 'https://docs.python.org/3/'
BASE_DIR: Path = Path(__file__).parent
DATETIME_FORMAT: str = '%Y-%m-%d_%H-%M-%S'
PEP_DOC_URL: str = 'https://peps.python.org/'
EXPECTED_STATUS: Dict[str, Tuple[str]] = {'A': ('Active', 'Accepted'),
                                          'D': ('Deferred',),
                                          'F': ('Final',),
                                          'P': ('Provisional',),
                                          'R': ('Rejected',),
                                          'S': ('Superseded',),
                                          'W': ('Withdrawn',),
                                          '': ('Draft', 'Active')}
