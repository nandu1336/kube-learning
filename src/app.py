from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .config import Database

DATABASE_URL = f"postgresql+psycopg2://{Database.db_username}:{Database.db_password}@{Database.db_host}:{Database.db_port}/{Database.db_database}"

engine = create_engine(DATABASE_URL, future=True, pool_pre_ping=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True))

from .model import Base, User
Base.metadata.create_all(bind=engine)

from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.get('/')
def index():
   return "Hello world"

@app.get('/ping')
def ping():
    return {'data': 'pong', 'pod': os.environ.get('POD_NAME')}

@app.get('/linux/<cmd>')
def run_cmd(cmd: str):
    with open('/tmp/stdout.txt', 'w+') as stdout, open('/tmp/stderr.txt', 'w+') as stderr:
        subprocess.run(cmd.split(), stdout=stdout, stderr=stderr)
        
        stdout.seek(0)
        stderr.seek(0)

        return {
            "stdout" :stdout.read().split("\n"),
            "stderr": stderr.read().split('\n'), 
            'pod': os.environ.get('POD_NAME')
            }

@app.post('/user')
def create_user():
    payload = request.get_json()
    print(payload)
    username = payload.get("username")
    email = payload.get("email")

    db = SessionLocal()
    try:
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)  # populate id and timestamps
        return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

@app.get('/user')
def list_users():
    # optional query params
    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", 10)), 1), 100)

    db = SessionLocal()
    try:
        query = db.query(User).order_by(User.id)
        total = query.count()
        users = query.offset((page - 1) * per_page).limit(per_page).all()

        result = [{
            "id": u.id,
            "username": u.username,
            "email": u.email
        } for u in users]

        return jsonify({
            "total": total,
            "page": page,
            "per_page": per_page,
            "users": result
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

def run():
    app.run(host='0.0.0.0', port=8000, debug=True)

if __name__ == "__main__":
    run()