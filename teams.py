import requests
import json
from flask import Flask, request

# Set up authentication
tenant_id = "GMO GlobalSign"
client_id = "joshua.garcia@globalsign.com"
client_secret = "YOUR_CLIENT_SECRET"
scope = "https://graph.microsoft.com/.default"
auth_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
auth_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope,
    "grant_type": "client_credentials"
}
response = requests.post(auth_url, data=auth_data)
access_token = response.json()["access_token"]

# Find the ID of the chat or channel
chat_name = "Site24x7 Alerts"
url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{chat_name}/messages"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url, headers=headers)
response_json = response.json()
channel_id = response_json["id"]

# Set up the webhook
webhook_url = "https://globalsign.webhook.office.com/webhookb2/9d583e02-ec74-464d-aae8-551c47d43a49@8fff67c1-8281-4635-b62f-93106cb7a9a8/IncomingWebhook/e082c86a78104ca2ba6005efca149b7a/ddc81f2a-7d28-4c3c-9ad7-c3bfce95a5ad"
app = Flask(__name__)
@app.route('/', methods=['POST'])
def handle_webhook():
    data = request.json
    message_subject = data["subject"]
    if "SEARCH_TERM" in message_subject:
        # Send a notification to the webhook
        payload = {"text": "Triggered by message subject: {}".format(message_subject)}
        response = requests.post(webhook_url, json=payload)
        return "OK"
    else:
        return "IGNORED"

# Run the webhook server
app.run()