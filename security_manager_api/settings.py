import os


ALLOW_EXTERNAL_DATA = bool(os.getenv("ALLOW_EXTERNAL_DATA", 1))


# SQL TAP PROFILER

ENABLE_SQL_TAP_MIDDLEWARE = False
SQL_TAP_REPORT_SETTINGS = dict(filename="sql-tap-report.html", format="html")


# DATABASE CONNECTIONS

DATABASES = {
    "postgres": {
        "DATABASE_URI": os.getenv(
            "DATABASE_URL",
            "postgres://postgres:symphony001@localhost:5432/cpqdb?sslmode=disable",
        ),
        "DATABASE_SCHEMA": os.getenv("DATABASE_SCHEMA", "kube_dev_schema"),
    },
    "test": {
        "DATABASE_URI": "sqlite:///./test.db",
        "DATABASE_SCHEMA": None,
    },
}


# CACHE

CACHE_PARAMS = {
    "cache_type": os.getenv("CACHE_TYPE", "REDIS"),
    "cache_url": os.getenv("CACHE_URL", "IP_CACHE_DEFAULT_VALUE"),
    "cache_port": os.getenv("CACHE_PORT", 6379),
    "cache_password": os.getenv("CACHE_PASSWORD", "PASS_CACHE_DEFAULT_VALUE"),
    "cache_disabled": bool(os.getenv("CACHE_DISABLED", 1)),
}

# keycloak
KEYCLOAK_SERVER = os.getenv("KEYCLOAK_SERVER", "http://localhost:8080") + "/auth/"
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", None)
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", None)
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", None)
KEYCLOAK_SKIP_SSL_VALIDATION = bool(int(os.getenv("KEYCLOAK_SKIP_SSL_VALIDATION", 0)))

# AMQP
RABBITMQ_BROKER_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/%2f")
RABBITMQ_Q_ORM_REFRESH = "b2worm"
