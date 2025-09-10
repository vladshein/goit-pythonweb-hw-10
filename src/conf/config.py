class Config:
    DB_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/hw8"
    JWT_SECRET = "your_secret_key"  # Секретний ключ для токенів
    JWT_ALGORITHM = "HS256"  # Алгоритм шифрування токенів
    JWT_EXPIRATION_SECONDS = 3600  # Час дії токена (1 година)


config = Config
