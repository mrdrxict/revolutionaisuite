python
     from googleapiclient.discovery import build
     from googleapiclient.http import MediaFileUpload
     from google.oauth2 import service_account

     SCOPES = ['https://www.googleapis.com/auth/drive']
     SERVICE_ACCOUNT_FILE = 'credentials.json'

     credentials = service_account.Credentials.from_service_account_file(
         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

     drive_service = build('drive', 'v3', credentials=credentials)

     def upload_file_to_drive(file_path, file_name):
         file_metadata = {'name': file_name}
         media = MediaFileUpload(file_path, resumable=True)
         file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
         return file.get('id')