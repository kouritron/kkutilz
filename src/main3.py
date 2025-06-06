import os
import time
from kkutilz.logz import log_stdio as log


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
def main():
    log.info("Hi")

    # i = 0
    # for _ in range(3):
    #     i *= 4242

    log.info("Hi again")

    print("--------------------")
    print("--------------------")

    log.set_log_level(log.LGLVL.WARN)
    log.dbg("this is dbg")
    log.info("this is info")
    log.warn("This is a warning")
    log.err("This is an error")

    print("--------------------")
    print("--------------------")
    log.set_log_level(log.LGLVL.DBUG)
    log.dbg("this is dbg")
    log.info("this is info")
    log.warn("This is a warning")
    log.err("This is an error")


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
if '__main__' == __name__:
    main()
