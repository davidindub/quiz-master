from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from googleapiclient.errors import HttpError
from apiclient import discovery, errors
import json
from termcolor import colored, cprint
from helpers import ask_any_key, ask_yes_no, clear, is_quit

CREDS = service_account.Credentials.from_service_account_file('creds.json')

SCOPED_CREDENTIALS = CREDS.with_scopes(
    ['https://www.googleapis.com/auth/drive'])

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=SCOPED_CREDENTIALS)


def delete_file(file_id):
    """Permanently delete a Google Drive file, skipping the trash.

    Args:
      file_id: ID of the file to delete.
    """
    try:
        DRIVE_SERVICE.files().delete(fileId=file_id).execute()
        print(f"📁🗑 File deleted: {file_id}")
    except errors.HttpError as error:
        print(f"🚫 An error occurred: {error}")


def list_all_files():
    """
    List All Files in Google Drive
    """
    try:
        # Call the Drive v3 API
        results = DRIVE_SERVICE.files().list(
            pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])

        if not items:
            cprint("No files found.", "red")
        else:
            print("🗂 Files:")
            for item in items:
                print(u"{0} ({1})".format(item["name"], item["id"]))
                # delete_file(item["id"])
    except HttpError as error:
        print(f"🚫 An error occurred: {error}")


def delete_all_files():
    """
    Deletes all files in Google Drive!
    """
    try:
        results = DRIVE_SERVICE.files().list(
            pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])

        if not items:
            cprint("No files found.", "red")

        else:
            print("🗂 Files:")
            for item in items:
                delete_file(item["id"])

    except HttpError as error:
        print(f"🚫 An error occurred: {error}")


def insert_permission(service, file_id, value, role):
    """
    Insert a new permission.
    Args:
        service: Drive API service instance.
        file_id: ID of the file to insert permission for.
        value:
        User or group e-mail address, domain name or None for 'default' type.
        role: The value 'owner', 'writer' or 'reader'.
    """
    new_permission = {
        "emailAddress": value,
        "role": role,
        "type": "user"
    }
    try:
        return service.permissions().create(
            fileId=file_id, body=new_permission).execute()
    except errors.HttpError as error:
        print(f"An error occurred: {error}")
        return


def run():
    """
    Displays a terminal menu for managing Google
    Drive Files
    """
    menu_options = ["(1) List All Files",
                    "(2) Delete a File based on ID",
                    "(3) Delete ALL Files"]

    while True:
        try:
            cprint("Welcome to the Google Drive Management Utility \n", "blue")

            for option in menu_options:
                print(option)

            if is_quit(response):
                return

            response = int(input("What would you like to do?\n"))

        except ValueError:
            continue
        if response not in [1, 2, 3]:
            continue
        if response == 1:
            list_all_files()
            continue
        if response == 2:
            print("Permanently delete a file. You cannot undo this!")
            file_id = input("File ID to be deleted: \n")
            delete_file(file_id)
        if response == 3:
            cprint("❌ WARNING ❌", "red")
            print("This will instantly deleted all files permanently!")
            delete_all_response = ask_yes_no(
                "Are you sure you want to continue?")
            if delete_all_response:
                delete_all_files()
                continue
            else:
                continue