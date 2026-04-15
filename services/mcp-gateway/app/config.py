from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "SoberFuture MCP Gateway"
    version: str = "0.1.0"
    host: str = "0.0.0.0"
    port: int = 8100
    debug: bool = False

    # Auth
    api_key: str = "changeme"  # overridden by env MCP_GATEWAY_API_KEY
    jwt_secret: str = "changeme"

    # Downstream services
    api_base_url: str = "http://localhost:8000"

    # AWS
    aws_region: str = "us-east-1"

    # Meeting sources
    meeting_guide_api: str = "https://api.meetingguide.org/meetings"
    bmlt_root_server: str = "https://bmlt.app/main_server"

    # Geo
    default_radius_miles: float = 10.0


settings = Settings()
