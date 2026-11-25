import os
import socket

from fastapi import FastAPI

# Имя экземпляра — потом по нему будем видеть, какой воркер ответил
INSTANCE = os.getenv("INSTANCE_NAME") or socket.gethostname()

app = FastAPI(title="Мини-магазин")


@app.get("/")
async def index():
    return {"service": "mini-shop", "instance": INSTANCE}