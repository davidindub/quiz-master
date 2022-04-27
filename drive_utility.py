from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from googleapiclient.errors import HttpError
from apiclient import discovery, errors
import json

credentials = service_account.Credentials.from_service_account_file(
    'client_secrets.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/drive'])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

service = discovery.build('drive', 'v3', credentials=scoped_credentials)


def delete_file(file_id):
    """Permanently delete a Google Drive file, skipping the trash.

    Args:
      file_id: ID of the file to delete.
    """
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"📁🗑 File deleted: {file_id}")
    except errors.HttpError as error:
        print(f"🚫 An error occurred: {error}")


def list_all_files():
    """
    List All Files in Google Drive
    """
    try:
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('🗂 Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
                # delete_file(item["id"])
    except HttpError as error:
        print(f'🚫 An error occurred: {error}')


list_all_files()