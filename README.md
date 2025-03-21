# 🚀 AI-CHATBOT MULTISERVICES

Una API disenada para usar una LLM en diferentes entornos como correos, web App, redes sociales, ejecutada con Docker Compose y utilizando Alembic 
para gestionar migraciones de la base de datos.

## 🛠️ REQUISITOS PREVIOS

Antes de iniciar, asegurate de tener intalado
- Docker 4.37.0
- Docker compose v1
- PastgreSQL (si no usas Docker para la base de datos)

## 📦 INSTALACION

1. Clona el repositorio:
``` bash
  git clone  https://github.com/Joalink/chatbot-ai-backend.git 
```


## 🏗️ CONSTRUCCION Y EJECUCION CON DOCKER

Para levantar los servicios con Docker Compose, usa: 
``` bash
  docker-compose up --build 
```

Esto ejecutara la API en ``` http://127.0.0.1:8000``` y luego levantara los servicios necesarios (como PostgreSQL si esta en  ```docker-compose.yml```).

Para correr en segundo plano: 
``` bash 
  docker-compose up -d
```

para detener los contenedores: 
``` bash
  docker-compose down
```

## 🛢️ MIGRACIONES DE BASE DE DATOS CON ALEMBIC

Generar una nueva migracion: 
``` bash 
  docker-compose exec fastapi_app alembic revision --autogenerate -m "Mensaje de la migracion" 
```

Aplica las migraciones: 

``` bash 
  docker-compose exec fastapi_app alembic upgrade head 
```

Revertir la ultima migracion (opcional): 

``` bash 
  docker-compose exec fastapi_app alembic downgrade -1 
```

[//]: # (Si uvicorn se estancan, verificar los procesos: ```tasklist /FI "IMAGENAME eq python.exe"``` y remplaza el nombre en el siguiente comando para eliminar d manualmente```taskkill /PID <PID_ID_REPLACE_HERE>  /F``` ``` )
[//]: # (alembic manual migrations ```)

## 📖 DOCUMENTACION DE LA API

Una vez el servidor este corriendo , puedes acceder a la documentacion interactiva de FASDT

- **Swagger UI** → http://127.0.0.1:8000/docs
- **Redoc** → http://127.0.0.1:8000/redoc


## 📂 ESTRUCTURA DEL PROYECTO

la estructura del proyeto esta basada en tipo de servicio lo cual la hace util si se desea trabajar con microservicios




## 📝 EJEMPLOS DE USO

### obtener lista de items

``` bash  
  curl -X 'GET' \ 'http://localhost:8000/items/' \ 'accept: application/json'
```
