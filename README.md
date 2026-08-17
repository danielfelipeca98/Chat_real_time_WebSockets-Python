Chat en tiempo real con FastAPI y WebSockets.

##  Características

-  Comunicación en tiempo real
-  Múltiples usuarios conectados
-  Notificaciones de entrada y salida
-  Interfaz simple y moderna
-  WebSockets con FastAPI

##  Tecnologías

- **FastAPI** → API y WebSockets
- **WebSockets** → Comunicación bidireccional
- **HTML/CSS** → Interfaz de usuario
- **JavaScript** → Cliente WebSocket

##  Estructura del proyecto

```
chat-websocket/
├── main.py # Servidor FastAPI + WebSocket
├── static/
│ └── index.html # Interfaz del chat
├── requirements.txt # Dependencias
├── .gitignore # Archivos ignorados
└── README.md # Documentación
```


##  Cómo ejecutar

```bash
# 1. Clonar
git clone https://github.com/TU-USUARIO/chat-websocket.git
cd chat-websocket

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar
uvicorn main:app --reload

##  Autor

**Daniel Felipe Castro**
- [GitHub]https://github.com/danielfelipeca98