from fastapi import FastAPI, APIRouter

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
