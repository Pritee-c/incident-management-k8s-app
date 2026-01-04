from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/incidents", methods=["GET"])
def get_incidents():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM incidents ORDER BY created_at DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@app.route("/incidents", methods=["POST"])
def create_incident():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO incidents (title, severity, status) VALUES (%s, %s, %s)",
        (data["title"], data["severity"], "OPEN")
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Incident created"}, 201

@app.route("/incidents/<int:id>/status", methods=["PUT"])
def update_status(id):
    status = request.json["status"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE incidents SET status=%s WHERE id=%s", (status, id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Status updated"}

@app.route("/incidents/<int:id>/comments", methods=["POST"])
def add_comment(id):
    comment = request.json["comment"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO incident_comments (incident_id, comment) VALUES (%s, %s)",
        (id, comment)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Comment added"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

