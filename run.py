import main
from config import APP_HOST, APP_PORT, DEVEL

if __name__ == "__main__":
    main.init_blueprints()
    main.init_db()
    main.main.run(host=APP_HOST, port=APP_PORT, debug=DEVEL)
