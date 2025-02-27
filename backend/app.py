from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Access environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/api/send-notification", methods=["POST"])
def send_notification():
    data = request.json
    title = data.get("title")
    message = data.get("message")

    # Save notification to Supabase
    supabase.table("notifications").insert({
        "title": title,
        "message": message
    }).execute()

    return jsonify({"status": "success", "message": "Notification sent"})

# Vercel requires a `handler` for serverless functions
handler = app
