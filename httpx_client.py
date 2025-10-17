import time

import httpx

# Инициализируем клиент с base_url и timeout
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=100  # Таймаут в секундах
)

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем POST-запрос
response = client.post("/api/v1/users", json=payload)
print(response.text)
