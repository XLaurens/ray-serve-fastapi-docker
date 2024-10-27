import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ray import serve

app = FastAPI()
logger = logging.getLogger("ray.serve")


@serve.deployment(num_replicas=1)
@serve.ingress(app)
class API:
    def __init__(self, models_dict):
        self._warmup(models_dict)

    @app.get("/healthy")
    async def health_check(self):
        return JSONResponse(content={"status": "UP"})

    def _warmup(self, models_dict):
        for model_tasks, models_list in models_dict.items():
            for model_params in models_list:
                model_name = model_params["name"]
                logger.info(f'"{model_name}": warmup complete.')


def app_builder(args: dict) -> API:
    return API.bind(args["llms"])
