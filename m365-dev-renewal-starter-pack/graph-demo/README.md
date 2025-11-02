# Microsoft Graph Demo

This folder contains example Microsoft Graph API queries and Python scripts used to test user data, emails, and calendar events.

### How to use:
1. Go to https://developer.microsoft.com/en-us/graph/graph-explorer  
2. Sign in with your dev tenant account.  
3. Run and save the following queries:
   - `GET /users`
   - `GET /me/messages`
   - `GET /me/events`

### Files
- `queries/users.http` – GET users example  
- `queries/events.http` – GET events example  
- `get_users.py` – Python example for calling Graph API
