from app import create_app
import os
app = create_app(env_config=os.getenv("ENV") or "production")


