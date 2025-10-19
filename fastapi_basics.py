import uvicorn
from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, Depends, status
from pydantic import BaseModel

# Создаём главное приложение
app = FastAPI(title="basics")

# Настраиваем роутер с префиксом и тегом
router = APIRouter(
    prefix="/api/v1",             # общий префикс для всех путей в этом роутере
    tags=["Basics"]               # в Swagger UI группа будет помечена тегом "Basics"
)

# Pydantic-модель для входящих данных
class User(BaseModel):
    username: str
    email: str
    age: int

# Модель для ответа
class UserResponse(BaseModel):
    username: str
    email: str
    message: str

# Зависимость: проверка минимального возраста
def validate_min_age(min_age: int = 18):
    def checker(user: User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User must be at least {min_age} years old"
            )
        return user

    return checker

@router.get("/basics/{item_id}")
async def get_basics(
        name: str = Query("Alise", description="Имя пользователя"),
        item_id: int = Path(..., description="Идентификатор элемента")
):
    return {
        "message": f"Hello, {name}!",
        "description": f"Item number {item_id}"
    }

@router.post("/basics/users", response_model=UserResponse)
async def create_user(user: User = Body(..., description="Данные нового пользователя")):
    return UserResponse(
        username=user.username,
        email=user.email,
        message="User created successfully!"
    )


# Эндпоинт использует Depends для валидации возраста
@router.post("/basics/register", summary="Регистрация пользователя с проверкой возраста")
async def register_user(
        user: User = Depends(validate_min_age(min_age=21))  # внедряем зависимость
):
    return {
        "message": f"User {user.username} registered successfully",
        "email": user.email,
        "age": user.age
    }

# Подключаем роутер к основному приложению
app.include_router(router)

# --------------------------------------------------------
# Программный запуск приложения
# --------------------------------------------------------
if __name__ == "__main__":
    # Запускаем Uvicorn с указанием:
    # - имя модуля и объекта приложения (fastapi_basics:app)
    # - адрес и порт (host, port)
    # - авто-перезагрузка при изменении кода (reload=True)
    uvicorn.run(
        "fastapi_basics:app",  # "<module_name>:<app_instance>"
        host="127.0.0.1",  # адрес, на котором слушаем входящие подключения
        port=8000,  # порт
        reload=True,  # перезагрузка при изменении файлов
        log_level="info"  # уровень логирования
    )