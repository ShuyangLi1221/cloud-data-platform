from sqlalchemy import create_engine

from common.config import DB_CONFIG

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['username']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
    f"/{DB_CONFIG['database']}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"options": "-c timezone=utc"},
)