import requests
import base64

issue_key= "SOC-186234"
url = f"https://intranet.internal.globalsign.com/jira/rest/api/2/issue/{issue_key}"

# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual personal access token
api_token = 'NzcxNjA4NjYxNzM0OlbBE86uFCOB3qi2uteS20FTDQY4'
# credentials = f"{personal_access_token}:"
base64_credentials = base64.b64encode(f'username:{api_token}'.encode()).decode()
print(url)
headers = {
    "Authorization": f"Bearer {base64_credentials}",
    "Content-Type": "application/json"
}

# Get current issue details
response = requests.get(url, headers=headers)
issue_details = response.json()

# Prepare the transition data
transition_data = {
    "transition": {"id": 442211}
}

# Send a PUT request to update the issue
response = requests.post(url, json=transition_data, headers=headers)

if response.status_code == 204:
    print("Progress started successfully!")
else:
    print(f"Failed to start progress. Status code: {response.status_code}")






# Prepare the assignee data
assignee_data = {
    "fields": {"assignee": {"name": "sheryl.patalen"}}  # Replace with the assignee's username
}

# Send a PUT request to assign the issue
response = requests.put(url, json=assignee_data, headers=headers)

if response.status_code == 204:
    print("Issue assigned successfully!")
else:
    print(f"Failed to assign issue. Status code: {response.status_code}")




# Jira API endpoint for adding a comment to an issue
comment_url = f"https://your-jira-instance.atlassian.net/rest/api/2/issue/{issue_key}/comment"
# Prepare the comment content
comment_content = {
    "body": "This is a comment added via API."
}

# Send a POST request to add the comment
comment_response = requests.post(comment_url, json=comment_content, headers=headers)

if comment_response.status_code == 201:
    print("Comment added successfully!")
else:
    print(f"Failed to add comment. Status code: {comment_response.status_code}")


print(response.text)