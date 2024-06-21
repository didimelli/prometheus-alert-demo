from uuid import UUID

from fastapi import FastAPI
from prometheus_client import Gauge, make_asgi_app
from pydantic import BaseModel

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
temperature_gauge = Gauge(
    "satellite_temperature", "Satellite temperature in C", labelnames=["satellite_id"]
)
battery_gauge = Gauge(
    "satellite_battery_percentage", "Satellite battery %", labelnames=["satellite_id"]
)


class Temperature(BaseModel):
    temperature: float


class Battery(BaseModel):
    battery: float


@app.post("/temperature/{satellite_id}")
async def temperature(satellite_id: UUID, temp: Temperature):
    temperature_gauge.labels(satellite_id).set(temp.temperature)


@app.post("/battery/{satellite_id}")
async def battery(satellite_id: UUID, batt: Battery):
    temperature_gauge.labels(satellite_id).set(batt.battery)
