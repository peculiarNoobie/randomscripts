from imaplib import IMAP4
import email

# Connect to the email server
mail = IMAP4('imap.example.com')
mail.login('username', 'password')

# Select the subfolder
mail.select('MyFolder')

# Search for messages with a specific subject line
status, messages = mail.search(None, 'SUBJECT "example subject"')

# Get the message ID of the first matching message
message_ids = messages[0].split()
if len(message_ids) > 0:
    message_id = message_ids[0]
else:
    print("No messages found")
    exit()

# Retrieve the message contents
status, data = mail.fetch(message_id, '(RFC822)')
message_contents = data[0][1]
message = email.message_from_bytes(message_contents)

# Print the message body
print(message.get_payload())