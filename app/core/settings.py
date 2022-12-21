from pydantic import BaseSettings

class Settings(BaseSettings):
    USER: str
    PASSWORD: str = ''
    HOST: str
    PORT: str
    DB_NAME: str

    @property
    def db(self):
        return 'postgresql://{name}:{password}@{host}:{port}/{db_name}'.format(
            name=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            db_name=self.DB_NAME
        )

    class Config:
        env_file = './.env'

settings = Settings()
