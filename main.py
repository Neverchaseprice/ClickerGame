from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Разрешаем доступ с этого origin
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

def get_counter():
    try:
        with open("count.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def write_counter(count):
    with open("count.txt", "w") as f:
        f.write(str(count))

@app.post("/increment-counter")
async def increment_counter(request: Request):
    count = get_counter()
    count += 1
    write_counter(count)
    return {"message": "Counter updated successfully"}

@app.get("/get-counter")
async def get_counter_api():
    count = get_counter()
    response = PlainTextResponse(str(count))
    return response
