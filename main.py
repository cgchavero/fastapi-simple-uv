from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "Hello from fastapi-simple-uv! v5"

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    main()
