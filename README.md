# Effective Mobile - DevOps Test Task

Простое веб-приложение с nginx reverse proxy в Docker-контейнерах.

## Архитектура

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Client    │──────│    Nginx    │──────│   Backend   │
│             │ :80  │  (proxy)    │ :8080│  (Python)   │
└─────────────┘      └─────────────┘      └─────────────┘
                           │                     │
                           └─────────────────────┘
                              Docker Network
                              (app-network)
```

**Поток запроса:**
1. Клиент отправляет HTTP-запрос на `localhost:80`
2. Nginx принимает запрос и проксирует его на backend-сервис
3. Backend (Python HTTP-сервер) обрабатывает запрос и возвращает ответ
4. Nginx передаёт ответ клиенту

## Структура проекта

```
├── backend/
│   ├── Dockerfile      # Образ Python-приложения
│   └── app.py          # HTTP-сервер
├── nginx/
│   └── nginx.conf      # Конфигурация reverse proxy
├── docker-compose.yml  # Оркестрация контейнеров
├── .env                # Переменные окружения (не в git)
├── .env.example        # Пример переменных окружения
├── .gitignore
└── README.md
```

## Требования

- Docker 20.10+
- Docker Compose 2.0+

## Запуск

```bash
# Клонировать репозиторий
git clone https://github.com/<user>/<repo>.git
cd <repo>

# Запустить контейнеры
docker-compose up -d --build

# Проверить статус
docker-compose ps
```

## Проверка работоспособности

```bash
curl http://localhost
```

**Ожидаемый ответ:**
```
Hello from Effective Mobile!
```

## Остановка

```bash
# Остановить контейнеры
docker-compose down

# Остановить и удалить volumes
docker-compose down -v
```

## Технологии

| Компонент | Технология | Версия |
|-----------|------------|--------|
| Backend | Python | 3.12-alpine |
| Reverse Proxy | Nginx | 1.25-alpine |
| Контейнеризация | Docker | 20.10+ |
| Оркестрация | Docker Compose | 2.0+ |

## Особенности реализации

- **Безопасность**: Backend запускается от непривилегированного пользователя
- **Health Checks**: Оба сервиса имеют проверки работоспособности
- **Изоляция**: Backend недоступен с хоста, только через nginx
- **Отдельная сеть**: Сервисы общаются через выделенную Docker-сеть
- **Минимальные образы**: Использованы alpine-версии для уменьшения размера
