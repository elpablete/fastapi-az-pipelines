from fastapi import FastAPI, Security

import app.settings as settings
import app.models as models
import app.auth as auth

ROOT_PATH = settings.APP_ROOT_PATH

app = FastAPI(root_path=ROOT_PATH)  # type: ignore


@app.get("/", response_model=models.ApiStatus)
async def get_status():
    return {"status": "ready"}


@app.get("/users/me/", response_model=models.User)
async def read_users_me(
    current_user: models.User = Security(
        auth.get_current_user, scopes=["users.me:read"]
    )
):
    return current_user
