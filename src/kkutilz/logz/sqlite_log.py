"""
A simple logging system with a sqlite backend.
- Switch between views to see different log levels, query logs ....

"""

import os
import sys
from pathlib import Path
import sqlite3

from .base import LGLVL, LOG_RECORD, mk_log_record
from .base import ANSI_GREEN, ANSI_YELLOW, ANSI_RED, ANSI_RESET


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
def _process_log_record(lgr: LOG_RECORD):
    # TODO implementation
    pass


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------- module api
def dbg(msg: str = ''):
    lgr = mk_log_record(msg_lvl=LGLVL.DBUG, msg=msg)
    _process_log_record(lgr)


def info(msg: str = ''):
    lgr = mk_log_record(msg_lvl=LGLVL.INFO, msg=msg)
    _process_log_record(lgr)


def warn(msg: str = ''):
    lgr = mk_log_record(msg_lvl=LGLVL.WARN, msg=msg)
    _process_log_record(lgr)


def err(msg: str = ''):
    lgr = mk_log_record(msg_lvl=LGLVL.ERRR, msg=msg)
    _process_log_record(lgr)
