from .base import LGLVL
from .log2stdio import StdioLogger
from .pipe_fed_sqlite import PipeFedSqliteLogger

# default_logger = StdioLogger()
default_logger = PipeFedSqliteLogger()
