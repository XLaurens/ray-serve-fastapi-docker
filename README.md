# ray-serve-fastapi-docker

## Run the Ray Serve x FastAPI in Docker
```
docker build -t ray-serve-app .
docker run --shm-size=2.26gb -p=8080:8080  ray-serve-app
curl "http://127.0.0.1:8080/healthy"
```
