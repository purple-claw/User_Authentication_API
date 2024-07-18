# README

## Table of Contents
1. [Secure User Authentication and Authorization API with JWT]
    - [Introduction](#introduction-1)
    - [Features](#features-1)
    - [Installation](#installation-1)
    - [Usage](#usage-1)
    - [Endpoints](#endpoints-1)

## Project 1: Secure User Authentication and OTP Verification API with JWT

### Introduction

This project provides a secure user authentication and authorization API using Python DJANGO Framework and JSON Web Tokens (JWT). JWT is used to ensure secure transmission of user data.


### Features

- User registration with Email
- OTP generation - 6 Digit OTP
- JWT generation for authentication
- OTP Expries Every 5 Minutes
- Protected routes accessible only with valid tokens
  
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/purple-claw/User_Authentication_API.git
    cd User_Authentication_API
    ```
2. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```
3. Apply Migrations:
    ```bash
    python3 manage.py makemigrations
    ```
    ```bash
    python3 manage.py migrate
    ```

### Usage

The API runs on `http://localhost:8000`. Use tools like POSTMAN to interact with the endpoints and send Requests to Server.

### Endpoints

- **POST api/register**
    - Registers a new user.
    - Body parameters:
        ```json
        
            "email": "your-email"
        }
        ```
    - Response:
        ```json
        {
            "message": "User registered successfully"
        }
        ```

- **POST api/request-otp**
    - Genarates an OTP for the Registered Email
    - Body parameters:
        ```json
        {
          "email" : "test@email.com"
        }
        ```
    - Response:
        ```json
        {
            "message": "OTP Generated Succesfully and Sent to your Email"
        }
        ```

- **POST api/verify-otp**
    - Verifies the Generated OTP and Grants Access
    - Response:
        ```json
        {
            "email" : "test@email.com",
            "otp" : 123456
        }
        ```
  ## Images and Working Screenshots
  ![Screenshot](https://github.com/purple-claw/User_Authentication_API/blob/master/WhatsApp%20Image%202024-07-18%20at%206.56.44%20AM.jpeg)
  ![Screenshot](https://github.com/purple-claw/User_Authentication_API/blob/master/WhatsApp%20Image%202024-07-18%20at%206.57.02%20AM.jpeg)
  ![Screenshot](https://github.com/purple-claw/User_Authentication_API/blob/master/WhatsApp%20Image%202024-07-18%20at%206.56.22%20AM.jpeg)
  ![Screenshot](https://github.com/purple-claw/User_Authentication_API/blob/master/WhatsApp%20Image%202024-07-18%20at%206.57.18%20AM.jpeg)

---
