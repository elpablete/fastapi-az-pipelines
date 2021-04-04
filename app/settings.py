import os
import pathlib
import json

import logging

logger = logging.getLogger(__name__)

scopes_path = pathlib.Path("./scopes.json")

APP_ROOT_PATH = os.getenv("ROOT_PATH", None)
AUTH_TOKEN_URL = os.environ["AUTH_TOKEN_URL"]
AUTH_TOKEN_SIGN_SECRET = os.environ["AUTH_TOKEN_SIGN_SECRET"]
AUTH_TOKEN_SIGN_ALGORITHM = os.environ["AUTH_TOKEN_SIGN_ALGORITHM"]

logger.info(f"Reading scopes from path {scopes_path}")
with open(scopes_path) as src:
    logger.info(f"Reading scopes from path {scopes_path}")
    SCOPES = json.load(src)
