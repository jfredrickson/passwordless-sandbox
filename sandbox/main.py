from fastapi import FastAPI, status
from mangum import Mangum
import secrets
from sandbox.schemas import UserSchema
from sandbox.email import send_magic_link
import sandbox.database as db

app = FastAPI(title="Passwordless Sandbox")

@app.get("/", status_code=status.HTTP_200_OK, summary="Return a basic test message")
def root():
    return {"message": "Hello!"}

@app.post("/sessions", status_code=status.HTTP_200_OK, summary="Initiate a login session and send an email with a login link")
def create_session(user: UserSchema):
    session_id = generate_session_id()
    db.create_session(session_id, user.email)
    send_magic_link(session_id, user.email)
    return {"message": "Email sent"}

handler = Mangum(app)

def generate_session_id():
    return secrets.token_urlsafe(40)
