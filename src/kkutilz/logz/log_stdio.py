import os
import sys

from .base import LGLVL, LOG_RECORD, mk_log_record
from .base import ANSI_GREEN, ANSI_YELLOW, ANSI_RED, ANSI_RESET


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
def _process_log_record(lgr: LOG_RECORD):
    """ Process the log record and print it to stdout or stderr based on the log level. """

    # func_name = lgr.func_name
    fbasename = os.path.basename(lgr.filename)

    # lgr.lgr_time_ns is nanosecond. we need less.
    time_seconds = lgr.lgr_time_ns / 1_000_000_000.0  # convert to seconds
    time_trunc = f"{time_seconds:.6f}"[6:]
    msg_builder = f"{time_trunc}|{fbasename}:{lgr.line_no}|{lgr.msg}"

    if lgr.msg_lvl == LGLVL.DBUG:
        msg_builder = f'DBUG|{msg_builder}'

    if lgr.msg_lvl == LGLVL.INFO:
        msg_builder = f'{ANSI_GREEN}INFO|{msg_builder}{ANSI_RESET}'

    if lgr.msg_lvl == LGLVL.WARN:
        msg_builder = f'{ANSI_YELLOW}WARN|{msg_builder}{ANSI_RESET}'

    if lgr.msg_lvl == LGLVL.ERRR:
        msg_builder = f'{ANSI_RED}ERRR|{msg_builder}{ANSI_RESET}'

    print(msg_builder, file=sys.stderr)


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
