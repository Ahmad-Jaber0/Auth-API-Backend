# API-Server-Auth  

A Django-based back-end API designed for user authentication and management. This repository provides a secure, extensible, and production-ready authentication system using Django REST Framework (DRF). The system includes core features like token-based authentication, user registration, profile management, and personalized dashboards.  

---

## Features  

- **Secure Authentication**  
  Token-based authentication for secure access.  

- **User Management**  
  Includes user registration, login, logout, profile management, and password change functionalities.  

- **Dashboard Access**  
  A personalized dashboard accessible only by authenticated users.  

- **Error Handling**  
  Comprehensive validation and error responses to ensure smooth user experience.  

---

## Testing the API with test.rest  

To test this back-end API, you can use the **test.rest** file in your project. This allows you to define HTTP requests and test them directly within VS Code. Below is an example of how you can use `test.rest` to interact with the back-end:  


---
## API Endpoints and Descriptions

### **Authentication Endpoints**

#### 1. **Signup**
- **URL**: `/signup/`
- **Method**: `POST`
- **Description**: Creates a new user account with a unique email and username. Returns a token upon successful registration.
- **Request Body**:  
  ```json
  {
    "username": "Ahmad",
    "password": "123",
    "email": "Ahmad@mail.com"
    "first_name": "Ahmad",
    "last_name": "jaber"
  }
- **Response**: 
  ```json
  {
  "token": "949332b44dd671cb407db4ffb2d032594242ccc4",
  "user": {
    "id": 1,
    "username": "Ahmad",
    "password": "pbkdf2_sha256$720000$Jlw8lu6Ucm4HmPJ1Yz7hYl$g4TqANd7zW9zBAgiPrCoKrNlkXIlerwRnYWgMXsBEZI=",
    "email": "Ahmad@mail.com",
    "first_name": "Ahmad",
    "last_name": "Jaber",
    "is_active": true,
    "date_joined": "2024-11-18T11:59:14.730979Z"
  }
  }



#### 2. **Login**
- **URL**: `/login/`
- **Method**: `POST`
- **Description**: Authenticates a user and provides a token for subsequent requests.
- **Request Body**:  
  ```json
  {
  "username": "Ahmad",
  "password": "123"
  }
- **Response**: 
  ```json
  {
  "token": "949332b44dd671cb407db4ffb2d032594242ccc4",
  "user": {
    "id": 1,
    "username": "Ahmad",
    "password": "pbkdf2_sha256$720000$Jlw8lu6Ucm4HmPJ1Yz7hYl$g4TqANd7zW9zBAgiPrCoKrNlkXIlerwRnYWgMXsBEZI=",
    "email": "Ahmad@mail.com",
    "first_name": "Ahmad",
    "last_name": "Jaber",
    "is_active": true,
    "date_joined": "2024-11-18T11:59:14.730979Z"
  }
  }

#### 3. **logout**
- **URL**: `/logout/`
- **Method**: `POST`
- **Description**: Logs out the user by invalidating their token.
- **Headers**:  
  ```http
  Authorization: Token your_token

- **Response**: 
  ```json
  
  {
  "detail": "Successfully logged out."
  }

#### 4. **view_profile**
- **URL**: `/view_profile/`
- **Method**: `POST`
- **Description**: Retrieves the profile of the authenticated user.
- **Headers**:  
  ```http
  Authorization: Token your_token
- **Response**:
  ```json
  {
  "profile": {
    "username": "Ahmad",
    "email": "Ahmad@mail.com",
    "first_name": "Ahmad",
    "last_name": "Jaber"
  }
  }

#### 5. **change_password**
- **URL**: `/change_password/`
- **Method**: `POST`
- **Description**: Allows an authenticated user to change their password.
- **Headers**:  
  ```http
  Authorization: Token your_token
- **Request body**:
  ```json
  {
  "old_password": "123",
  "new_password": "1234"
  }


- **Response**:
  ```json
  {
  "detail": "Password successfully updated."
  }

#### 6. **dashboard**
- **URL**: `/dashboard/`
- **Method**: `POST`
- **Description**: Provides a personalized dashboard for authenticated users.
- **Request Body**:  
- **Headers**:  
  ```http
  Authorization: Token your_token
- **Response**:
  ```json
  {
  "message": "Welcome to your dashboard, Ahmad!"
  }
