# How to Authenticate
There are 3 ways to Connect to the Dataloop platform's API, depending on how you wish to use it. These methods are:
- Simple Website Log-in
- M2M (Machine to Machine) Login 
- Swagger UI 
- From an External System

This section will describe how to use each of the above Authentication methods. 

If you are not interesed in the different ways you can log in, just use the "Simple Website Log-in" and move ahead to [the next section](./2.%20SwaggerUI_API-Guide.md)!

## Simple website Log-in
To be able to use our API, you must first create an account on the Dataloop platform and then log in.  To get started, you can create and log into a Free account which you can upgrade to a paid account should you desire.

To create an account you can [click here](https://console.dataloop.ai/welcome). You will be redirected to a Sign up/Login page, which you can use to create an account using your e-mail or Google account. After creating an account, you can go the the same page to log in.

## Python SDK M2M (Machine to Machine) Login 
Long-running Python SDK jobs will require an API authentication to work properly.

The M2M login flow allows machines to obtain a valid, signed JWT (Authentication Token) and automatically refresh it without the need for a web browser login.
M2M login is recommended when you want to run commands on the platform without an ongoing internet connection or to run API commands directly from an 
external system to Dataloop.

To use the M2M login, you first need to create a bot user with a unique name:

```python
import dtlpy as dl
dl.login() # use browser login to create the bot
project = dl.projects.get(project_name='myProject') # get your project
myBot = project.bots.create(name='my-unique-name', return_credentials=True)
```

A Bot User on the Dataloop platform is similar to a User with Developer privileges.  The difference is that it runs in the background vs being an interactive user via the Dataloop UI.  You can view the bot user via the UI under Contributors on the Project Dashboard.



Make sure you save the login credentials of the bot you just created for future logins. You can find them using these lines of code:

```python
print("the bot email is "+myBot.email)
print("the bot password is "+myBot.password)
```

Then, you can log in to the Dataloop platform using the Python SDK and your newly created M2M bot credentials:

```python
import dtlpy as dl
dl.login_m2m(email=email, password=password)
```


M2M Login is recommended when:
- You want to run commands on the platform without an ongoing internet connection;
- You want to run API commands directly from an external system to Dataloop;

## The Dataloop Swagger UI 
Swagger UI allows individuals, whether they are members of the development team or end-users, to view and interact with API resources without requiring any implementation details. The visual documentation is generated automatically from OpenAPI (previously known as Swagger), simplifying both backend implementation and client-side consumption. The Swagger UI offers the ability to perform API requests such as ```GET```, ```POST```, ```PUT```, ```PATCH``` and ```DELETE``` to different endpoints in our backend services like Projects, Datasets, Tasks, etc.

You will need to already be logged in to the Dataloop platform to use the Swagger UI. Authentication will be completed with the logged in user.

You can [find Dataloop's Swagger UI here](https://gate.dataloop.ai/api/v1/docs/#/).

You can also [find examples of how to use the Swagger UI here](https://dataloop.ai/docs/swagger-ui-example).

## From an External System 
If you want to connect to the Dataloop API environment from an external system you need to get a JWT Token. You can then use the JWT Token for every HTTP request to the platform (with bearer authentication).

**Note**: *This is highly recommended if you wish to use your prefered API Platforms like Postman or Insomnia.*
To connect from an external system you need to go through 3 steps:
1. Obtain your API Credentials;
2. Use API credentials to get a JWT Token API Authentication by a "Post" HTTP request;
3. Use the JWT for every HTTP request to the platform (with bearer authentication).

You will now learn how to do each of them in Dataloop.

### 1. Set up your Dataloop account
To obtain your API credentials, you must first register with Dataloop. To do that you can [click this link](https://console.dataloop.ai/welcome).

**Make sure you register using an e-mail and password and not with a Google account**. You can use your Gmail account credentials if you wish, **but don't use the "Log In With Google" button**. 

After you create an account, log in to it using your e-mail and password.

![image](https://user-images.githubusercontent.com/58508793/219412890-b6f75d07-8088-4c69-a270-29eba19e70d3.png)

### 2. Get the JWT Authentication Token
Once you have success logging in, you can use these same credentials to obtain a JWT for Dataloop platform.
The Dataloop API uses an ["Auth" authentication scheme](https://oauth.net/2/bearer-tokens/), where each HTTP request has JWT Token attached to it via the Authorization header.

The basic flow for the authentication is:
- Initiate a HTTP request using your API credentials;
- Get your [JWT (JSON Web Token)](https://jwt.io/introduction) from the platform;
- As long as the JWT has not expired, you can use it as a Bearer authorization header.

You can see a schematic detailing this, below.
As long as the JWT is not expired, you can add it as a Bearer authorization header.
![image](https://user-images.githubusercontent.com/58508793/219415230-84421dbc-be0c-40ad-bb6f-8407bfd17574.png)

The request looks like this:
**POST https://gate.dataloop.ai/token?default**
**Content-Type: application/json**
```json
{
    "username": "<user name>",
    "password": "<user password>",
    "type": "user_credentials"
}
```
Here is an example, using [Postman](https://www.postman.com/downloads/):

![image](https://user-images.githubusercontent.com/58508793/219416875-935ec9c2-cdc4-43b7-b914-3fdbca146fcb.png)

You can click "Send" and you will get a response in the following format:
```json
{
    "access_token": "...",
    "id_token": "...",
    "refresh_token": "...",
}
```
You can use the id_token (the JWT) from the response as your authorization JWT for any future requests you may want to run.

***Important!***
Sometimes, your JWT Token may expire, in which case you need to request a new JWT Token.
There are many tools and libraries to decode JWTs, for example, https://jwt.io/ allows the interactive decoding of JWT Tokens.
A decoded JWT will look like this:
```json
{
  "name": "Name",
  "nickname": "Name",
  "picture": "https://example.com",
  "locale": "he",
  "updated_at": "2025-09-23T06:06:17.641Z",
  "email": "zaphod@dataloop.ai",
  "email_verified": true,
  "iss": "https://dataloop-development.auth0.com/",
  "sub": "google-oauth2|101916523885779176498",
  "aud": "I44w8",
  "iat": 1569218779,
  "exp": 1569283579,
}
```
*Note*:
- In order to obtain the expiration date, you will need to decode the JWT. You will also need to extract the exp field to get your JWT lifetime.
- You will need to refresh your JWT before its expiration date.

### 3. API HTTP Request
The Dataloop API uses Auth authentication scheme, where each HTTP request has JWT attached to it via the Authorization header.
You will now learn how to use your JWT Token to make a simple request using [Postman](https://www.postman.com/downloads/).

In this example we will return details of a specific project. The steps you need to go through are the following:
1. The GET request URL is https://gate.dataloop.ai/api/v1/projects/{id}.
2. For authentication, select the "Bearer Token" and fill in the Token we obtained.
3. Select the "Get" method.
4. Press "Send".

You can see these steps in Postman, in the image below:
![image](https://user-images.githubusercontent.com/58508793/219420355-01e22498-ea82-4548-aa0e-2b1ddecb9632.png)

You can also [explore Swagger UI](https://gate.dataloop.ai/api/v1/docs/) for the full Dataloop API using a UI interface.


Now that you've gone through and understood the different ways in which you can Authenticate in Dataloop, you can move on and [learn how to use Dataloop's API](./2.%20SwaggerUI_API-Guide.md).
