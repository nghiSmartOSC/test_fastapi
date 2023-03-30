import os

import uvicorn
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.curdir)

load_dotenv(os.path.join(BASE_DIR, '.env'))

from app.config.base import start_application, DevSettings


app = start_application(DevSettings())


if __name__ == '__main__':

    uvicorn.run(app, port=8000, host='0.0.0.0', reload=True)
