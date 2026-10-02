import logging
import os
import threading

from flask import Flask

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def health_check():
    return "OK"


def run_server():
    port = int(os.environ.get("PORT", 8080))

    try:
        from waitress import serve
    except ImportError:
        logger.warning(
            "waitress не установлена, используется встроенный сервер Flask "
            "(dev-сервер, не годится для продакшена)."
        )
        app.run(host='0.0.0.0', port=port)
        return

    logger.info("Health-check сервер слушает 0.0.0.0:%s", port)
    serve(app, host='0.0.0.0', port=port)


def keep_alive():
    """Поднимает health-check сервер в фоновом потоке, чтобы хостинг видел открытый порт."""
    t = threading.Thread(target=run_server, name='health-check', daemon=True)
    t.start()
    return t
