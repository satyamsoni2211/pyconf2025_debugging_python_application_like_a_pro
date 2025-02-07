import debugpy
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    # Start debugpy and listen on port 5678
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for debugger attach...")
    debugpy.wait_for_client()  # Only include this line if you want to pause execution until the debugger is attached

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
