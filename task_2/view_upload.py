from googleapiclient.discovery import build
from google.oauth2 import service_account


# Установка доступа (scopes),ключа сервисного аккаунта и идентификатора папки
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "1-lK9sghF51C7or46UpIKi9Qzucqz6OQG"

# Функция для аутентификации
def authenticate():
    # Загрузка учетных данных из файла сервисного аккаунта
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds


# Функция для загрузки графиков на Google drive
def upload_photo(file_path, name):
    # Получение учетных данных через функцию аутентификации
    creds = authenticate()
    # Построение объекта сервиса Google Диск
    service = build('drive', 'v3', credentials=creds)

    # Данные файла: имя файла и родительская папка
    file_metadata = {
        'name': name,
        'parents': [PARENT_FOLDER_ID]
    }

    # Запрос на загрузку файла на Google drive с указанными данными
    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
