from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

router = InferringRouter()

from app.controllers.accounts.user import *  # noqa
