# KYC
<h3>Данный проект, является дипломной работой курса pyton-разработчик онлайн университета SkyPro</h3></br>
<b>Задание:</b></br>
Реализовать сервис по обработке загружаемых данных администратором. То есть сделать API для приема документов со стороны фронтенда. При поступлении документа от зарегистрированного пользователя, необходимо уведомлять по почте администратора платформы. После того, как администратор подтвердил документ, отправлять письмо пользователю, который загружал документ. В Django admin добавить быстрые действия для подтверждения или отклоенения загруженных документов. Для рассылки необходимо использовать работу с очередью.
</br></br>
Проект состоит из двух самостоятельных частей объединенных в один проект:</br>
API написанная на FastAPI https://github.com/ualex90/KYC_api</br>
Admin написанная на Django https://github.com/ualex90/KYC_admin</br>
<h3>Запуск проекта:</h3>
1. Установите Docker Engine и Docker Compose;</br>
2. Клонируйте репозиторий;</br>
3. Создайте в директории api проекта и заполните файл .env.docker:</br>

```
SECRET_KEY='<секретный ключ>'

POSTGRES_DB='kyc'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='123qwe'
POSTGRES_HOST='db'
POSTGRES_PORT='5432'

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=587
EMAIL_USER='<имя пользователя (почта)>'
EMAIL_PASSWORD='<пароль>'
EMAIL_USE_TLS=True

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

4. Создайте в директории admin проекта и заполните файл .env.docker:

```
SECRET_KEY='<секретный ключ>'
DEBUG='on'

POSTGRES_DB='kyc'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='123qwe'
POSTGRES_HOST='db'
POSTGRES_PORT='5432'

DJANGO_ADMIN_EMAIL='django-admin@kyc.pro'
DJANGO_ADMIN_PASSWORD='123qwe'
API_URL='http://api:8002'
```
5. Для первого запуска необходимо собрать образ контейнера. Для этого, находясь в корневой директории проекта
необходимо выполнить команду:

```bash
sudo docker-compose build
```

5. Для запуска проекта:

```bash
sudo docker-compose up
```

Документация API: http://127.0.0.1:8002/docs#/
Панель администратора: http://127.0.0.1:8003/admin/

Для изменения портов, необходимо отредактировать их в командах docker-compose.yaml и .env.docker для admin

<h3>Создание пользователей:</h3>
Первый пользователь, который будет создан в системе, будет иметь права администратора!<br/>
Первый пользователь будет создан автоматически с параметрами прописанными в .env.docker проекта admin

Для регистрации пользователей необходимо отправить post запрос по примеру http://127.0.0.1:8002/docs#/users/register_user_api_users_register_post<br/>

Таким же образом регистрируются остальные пользователи, они уже не будут иметь прав администратора.<br/>
Расширить права пользователей можно при помощи http://127.0.0.1:8002/docs#/users/update_user_api_users__pk__patch или панели Django Admin

<h3>Работа с документами:</h3>
Для загрузки одного документа используется http://127.0.0.1:8002/docs#/files/upload_file_api_files_upload_post 
или http://127.0.0.1:8002/docs#/files/upload_multiple_file_api_files_upload_multiple_post для загрузки 2 и более
<br/>
После успешной загрузки, администраторы получат уведомление на почту
<br/></br>

После рассмотрения документа, администратор меняет статус документа http://127.0.0.1:8002/docs#/files/change_file_status_api_files_status__pk__post или на панели Django Admin
<br/>
Пользователь загрузивший файл получит уведомление о результате проверки документа
