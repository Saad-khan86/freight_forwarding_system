from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")

except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret, default='postgresql://neondb_owner:npg_qDEdU8IlTW9w@ep-dry-glade-a125mkdw-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')
# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)
