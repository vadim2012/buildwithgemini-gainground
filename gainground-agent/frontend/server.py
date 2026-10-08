import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env before initializing google-genai / ADK
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
os.environ["GOOGLE_CLOUD_PROJECT"] = "qwiklabs-gcp-04-6a336254df75"
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Add parent path so we can import app.agent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

app = FastAPI(title="GainGround Civic Action Platform")

# Setup ADK Runner for local execution
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    session_service=session_service,
    app_name="gainground_app"
)

SESSION_ID = "gainground-default-session"
USER_ID = "champion-user"

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        session = await session_service.get_session(app_name="gainground_app", user_id=USER_ID, session_id=SESSION_ID)
        if not session:
            session = await session_service.create_session(app_name="gainground_app", user_id=USER_ID, session_id=SESSION_ID)

        content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=req.message)]
        )
        
        reply_texts = []
        async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        reply_texts.append(part.text)

        full_reply = "".join(reply_texts) if reply_texts else "Action recorded."
        return {"reply": full_reply}
    except Exception as e:
        print("Error during chat processing:", e)
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files
static_dir = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/")
async def root():
    return FileResponse(static_dir / "index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8085)
