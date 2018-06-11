# edX python-social-auth Example

This is a sample Django project which demonstrates using the edX LMS as an OAuth2 authentication provider using python-social-auth. This repository uses Docker to enable you to quickly fire up a container running the sample Django application and see the OAuth2 flow in action with an external sandbox running the edX LMS (the sandbox currently configured is https://auth.sandbox.edx.org).

The sample Django project makes use of the OAuth2 authentication backend provided by https://github.com/edx/auth-backends (See the [auth-backends](https://github.com/edx/auth-backends) README for details about setting things up in your own Django project).

## Demo Installation Steps
1. [Install](https://docs.docker.com/install/) Docker.
2. Run `docker-compose up`.
3. Visit http://localhost:8000/login.
4. This will redirect you to the login page on https://auth.sandbox.edx.org where you can login as verifed@example.com/edx.
5. After logging in, and accepting the sharing of data with the sample app you will be redirected back to http://localhost:8000/courses.

## Setting up auth-backends with your own Django project
1. Make sure `social_django` is listed in `INSTALLED_APPS`.
2. Configure the `AUTHENTICATION_BACKENDS` setting:
```
AUTHENTICATION_BACKENDS = (
    'auth_backends.backends.EdXOAuth2',
)
```
3. Configure `auth-backends` settings:
```
SOCIAL_AUTH_EDX_OAUTH2_KEY = 'PROVIDED_BY_EDX'
SOCIAL_AUTH_EDX_OAUTH2_SECRET = 'PROVIDED_BY_EDX'
SOCIAL_AUTH_EDX_OAUTH2_ENDPOINT = 'https://auth.sandbox.edx.org/oauth2'
SOCIAL_AUTH_EDX_OAUTH2_LOGIN_REDIRECT_URL = 'http://localhost:8000/courses'
SOCIAL_AUTH_STRATEGY = 'auth_backends.strategies.EdxDjangoStrategy'
JWS_HMAC_SIGNING_KEY = 'SET-ME-PLEASE'
```
