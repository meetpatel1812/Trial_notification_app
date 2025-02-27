from flask import Flask, request, jsonify
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY, VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY, VAPID_SUBJECT
app = Flask(__name__)

# Supabase configuration
# SUPABASE_URL = "your-supabase-url"
# SUPABASE_KEY = "your-supabase-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/send-notification", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)