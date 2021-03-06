import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import httplib2
from oauth2client.client import GoogleCredentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly '
          'https://www.googleapis.com/auth/classroom.coursework.me.readonly '
          'https://www.googleapis.com/auth/classroom.announcements.readonly '
          'https://www.googleapis.com/auth/classroom.coursework.students.readonly '
          'https://www.googleapis.com/auth/classroom.coursework.students '
          'https://www.googleapis.com/auth/classroom.coursework.me']
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
def get_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds = GoogleCredentials(access_token=None, client_id=creds.client_id, client_secret=creds.client_secret,
                                      refresh_token=creds.refresh_token, token_expiry=None, token_uri=creds.token_uri,
                                      user_agent=None)
            http = creds.authorize(httplib2.Http())
            creds.refresh(http)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080, prompt='consent', access_type='offline')
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)
    return service
