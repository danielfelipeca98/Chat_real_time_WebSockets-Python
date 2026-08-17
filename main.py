from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
from typing import List, Dict

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[Dict] = []  # Lista de {websocket, nombre}
    
    async def connect(self, websocket: WebSocket, nombre: str):
        self.active_connections.append({
            "websocket": websocket,
            "nombre": nombre
        })
        await self.broadcast(f" {nombre} se ha unido al chat")
    
    def disconnect(self, websocket: WebSocket):
        for i, conn in enumerate(self.active_connections):
            if conn["websocket"] == websocket:
                nombre = conn["nombre"]
                self.active_connections.pop(i)
                return nombre
        return None
    
    async def broadcast(self, mensaje: str):
        for conn in self.active_connections:
            try:
                await conn["websocket"].send_text(mensaje)
            except:
                pass
    
    async def send_personal(self, mensaje: str, websocket: WebSocket):
        await websocket.send_text(mensaje)

manager = ConnectionManager()



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    nombre = await websocket.receive_text()
    await manager.connect(websocket, nombre)
    
    try:
        while True:
            data = await websocket.receive_text()            
            await manager.broadcast(f" {nombre}: {data}")
            
    except WebSocketDisconnect:
        nombre = manager.disconnect(websocket)
        if nombre:
            await manager.broadcast(f" {nombre} ha salido del chat")

@app.get("/")
async def get():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())