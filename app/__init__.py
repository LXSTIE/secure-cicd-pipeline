from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify({"status": "ok"})

    @app.route("/health")
    def health():
        return jsonify({"healthy": True})

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000)  # nosec B104
