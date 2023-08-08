
```plaintext
# Django-AuthAPI-with-JWT

Django-AuthAPI-with-JWT is an authentication API for Django applications using Django Rest Framework (DRF) and JSON Web Tokens (JWT). It provides functionality for user registration, login, password management, and password reset via email.

## Features

- User Registration: Allow users to create an account by providing necessary information.
- User Login: Authenticate users and issue JWT tokens upon successful login.
- Change Password: Enable users to change their account passwords.
- Password Reset via Email: Send password reset emails to users for account recovery.

## Installation

1. Clone the repository:

```bash
https://github.com/rifatjamil54/Django-AuthAPI-with-JWT.git
```

2. Change directory:

```bash
cd Django-AuthAPI-with-JWT
```

3. Create a virtual environment (recommended):

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```
6. Change directory:

```bash
cd AuthAPI
```

6. Configure settings:

Edit the `settings.py` file to configure your database, email settings, and other necessary options.

7. Apply migrations:

```bash
python manage.py migrate
```

8. Run the development server:

```bash
python manage.py runserver
```

The authentication API should now be accessible at `http://127.0.0.1:8000/`.

## Usage

1. Registration:

Send a POST request to `http://127.0.0.1:8000/account/register/` with user registration details to create a new account.

2. Login:

Send a POST request to `http://127.0.0.1:8000/account/login/` with login credentials to receive a JWT token for authentication.

3. Change Password:

Send a POST request to `http://127.0.0.1:8000/account/changepass/` with the new password to change the user's password.

4. Password Reset via Email:

Send a POST request to `http://127.0.0.1:8000/account/send-email-rest-password/` with the user's email address to initiate a password reset process. An email with reset instructions will be sent to the user.

4. Profile:

Send a GET request to `http://127.0.0.1:8000/account/profile/` with the user's profile see user details.

4. Rest-Password:

Send a POST request to `http://127.0.0.1:8000/account/rest-password/<uid>/<token>/` with the rest-password to change the user's password.

