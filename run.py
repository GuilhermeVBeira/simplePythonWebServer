import sys

from server import start_server
from app.models import DataBase
from app.settings import CONNECTION_STRING


if __name__ == '__main__':
    server_params = sys.argv[1] if len(sys.argv) > 1 else "0.0.0.0:8080"
    DataBase(CONNECTION_STRING).boot()
    start_server(server_params)
