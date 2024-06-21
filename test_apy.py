import random
import time
import uuid

import httpx

ENDPOINTS = ["temperature", "battery"]
SATELLITE_IDS = [uuid.uuid4() for _ in range(10)]
SERVER_DEMO_BASE_URL = "http://localhost:8090"


def main():
    while True:
        satellite_id = random.choice(SATELLITE_IDS)
        endpoint = random.choice(ENDPOINTS)
        final_endpoint = f"{SERVER_DEMO_BASE_URL}/{endpoint}/{satellite_id}"
        value = random.randrange(0, 30)
        httpx.post(final_endpoint, json={endpoint: value})
        time.sleep(0.1)


if __name__ == "__main__":
    main()
