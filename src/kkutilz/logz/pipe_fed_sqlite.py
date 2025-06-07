import os
import json

from .base import LOG_RECORD, LGLVL, mk_log_record
from .base import ANSI_GREEN, ANSI_YELLOW, ANSI_RED, ANSI_RESET


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
class PipeFedSqliteLogger:

    def __init__(self):

        # --- default log level
        self.current_log_level = LGLVL.INFO

        # --- fork off child using os.pipe and os.fork (unix only is fine)
        # child will be the log sink, parent will be the log source
        self.log_pipe_read_fd, self.log_pipe_write_fd = os.pipe()
        self.child_pid = os.fork()
        if self.child_pid == 0:
            # Child process
            os.close(self.log_pipe_write_fd)
            child_entry(self.log_pipe_read_fd)
        else:
            # Parent process
            os.close(self.log_pipe_read_fd)

    # --------------------------------------------------------------------------------------------------------------------------
    def set_log_level(self, level):

        if not isinstance(level, LGLVL):
            raise ValueError(f"Expected an instance of LGLVL, got {type(level)}")

        self.current_log_level = level
        self.info(f"Log level changed to {level}")

    # --------------------------------------------------------------------------------------------------------------------------
    def dbg(self, msg: str = ''):
        lgr = mk_log_record(msg_lvl=LGLVL.DBUG, msg=msg)
        self._process_log_record(lgr)

    def info(self, msg: str = ''):
        lgr = mk_log_record(msg_lvl=LGLVL.INFO, msg=msg)
        self._process_log_record(lgr)

    def warn(self, msg: str = ''):
        lgr = mk_log_record(msg_lvl=LGLVL.WARN, msg=msg)
        self._process_log_record(lgr)

    def err(self, msg: str = ''):
        lgr = mk_log_record(msg_lvl=LGLVL.ERRR, msg=msg)
        self._process_log_record(lgr)

    # --------------------------------------------------------------------------------------------------------------------------
    def _process_log_record(self, lgr: LOG_RECORD):

        # serialize the log record to a string and hex encode it, then send it through the pipe
        lgr_dict = {
            'lgr_time_ns': lgr.lgr_time_ns,
            'msg': lgr.msg,
            'msg_lvl': lgr.msg_lvl.name,  # convert enum to string
            'filename': lgr.filename,
            'line_no': lgr.line_no,
            'func_name': lgr.func_name,
        }
        lgr_dict_json_str_hex = json.dumps(lgr_dict).encode('utf-8').hex().encode('ascii')

        os.write(self.log_pipe_write_fd, lgr_dict_json_str_hex)

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------- Child process (log sink)
def child_entry(log_pipe_read_fd):
    
    for line in log_pipe_read_fd:
        line = line.strip()
        if not line:
            continue
        print(f"Child received: {line}")

    # loop ends when EOF is reached
    print("Child: EOF, exiting.")
