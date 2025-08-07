from flask import Flask
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1)
        },
        key="minhachave",
        algorithm="HS256"
    )
    return(token)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)