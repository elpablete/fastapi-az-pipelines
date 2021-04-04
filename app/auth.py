from fastapi import status, HTTPException, Depends
from fastapi.security import (
    OAuth2PasswordBearer,
    SecurityScopes,
)
from jose import jwt, JWTError

import app.models as models
import app.settings as settings

import logging

logger = logging.getLogger(__name__)

AUTH_TOKEN_URL = settings.AUTH_TOKEN_URL
AUTH_TOKEN_SIGN_SECRET = settings.AUTH_TOKEN_SIGN_SECRET
AUTH_TOKEN_SIGN_ALGORITHM = settings.AUTH_TOKEN_SIGN_ALGORITHM

SCOPES = settings.SCOPES

CREDENTIAL_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=AUTH_TOKEN_URL, scopes=SCOPES)


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    try:
        logger.debug(f"Decode jwt {token}")
        payload = jwt.decode(
            token, AUTH_TOKEN_SIGN_SECRET, algorithms=[AUTH_TOKEN_SIGN_ALGORITHM]
        )
        token_data = models.TokenData(**payload)
        user = token_data.user
        token_scopes = token_data.scopes
    except (JWTError, models.ValidationError):
        raise CREDENTIAL_EXCEPTION

    logger.debug(f"Checking required security scopes {security_scopes.scopes}")
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user
