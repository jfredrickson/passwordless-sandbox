from pathlib import Path
import uvicorn

def local_server():
    env_path = Path(__file__).parent.parent.joinpath(".env")
    uvicorn.run("sandbox.main:app", port=3000, env_file=env_path, reload=True)

if __name__ == "__main__":
    local_server()
