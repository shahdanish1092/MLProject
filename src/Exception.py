import sys
import logging
from src.Logger import logging as project_logging


def error_msg_detail(error_msg, error_detail:sys):

    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred at Python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error_msg)
    )

    return error_message




class CustomException(Exception):

    def __init__(self, error_message, error_detail):
        # build a formatted message first so it's used as the Exception message
        self.error_message = error_msg_detail(error_message, error_detail=error_detail)
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message



