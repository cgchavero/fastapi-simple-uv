from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "Hello from fastapi-simple-uv!"

if __name__ == "__main__":
    main()
