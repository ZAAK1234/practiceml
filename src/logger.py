import logging
import os
from datetime import datetime
import src.exception

import sys


LOG_FILE=f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
log_path=os.path.join(os.getcwd(),'logs', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)
'''if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info(f'Divided by zero error at {datetime.now()}')
        raise CustomException(e,sys)'''