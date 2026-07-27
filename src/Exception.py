import sys
import logging
import Logger


def error_msg_detail(error_msg, error_detail:sys):

    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred at Python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error_msg)
    )

    return error_message




class CustomException(Exception):

    def __init__(self, error_message, error_detail):

        super().__init__(error_message)

        self.error_message = error_msg_detail(error_message, error_detail=error_detail)






if __name__ == "__main__":

    try:
        a = 1/0

    except Exception as e:

        logging.info("Start Process...")
        logging.exception("An exception occurred")
        raise CustomException(e, sys)
