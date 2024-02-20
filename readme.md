# NoteMaster API
NoteMaster API is a secure and efficient note-taking API. It allows users to create, read, update, and delete personal notes. The API uses JWT for user authentication and provides a robust set of endpoints for managing user accounts and notes.

## Getting Started

### Prerequisites

 - Python 3.6 or higher
 - pip (Python package installer)

## Installation

1. **Clone the repository to your local machine.**
    ```bash
    git clone "https://github.com/srb1998/SecureNoteAPI.git"
    ```

2. **Navigate to the project directory.**
    ```bash
    cd <project_directory>
    ```

3. **Install the required packages.**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application.**
    ```bash
    flask run
    ```

## API Endpoints

### Signup

- **URL**: `/signup`
- **Method**: `POST`
- **Body**: `username`, `email`, `password`
- **Success Response**: `{ id: 12, username: "john", email: "john@example.com" }`
- **Error Response**: `{ message: "<error message>" }`

### Login

- **URL**: `/login`
- **Method**: `POST`
- **Body**: `username`, `password`
- **Success Response**: `{ access_token: "<access token>" }`
- **Error Response**: `{ message: "<error message>" }`

### Create Note

- **URL**: `/notes/create`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <access_token>`
- **Body**: `note`
- **Success Response**: `{ id: 1, note: "example note", user_id: 12 }`
- **Error Response**: `{ message: "<error message>" }`

### Get Note

- **URL**: `/notes/<int:id>`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <access_token>`
- **URL Params**: `id`
- **Success Response**: `{ id: 1, note: "example note", user_id: 12 }`
- **Error Response**: `{ message: "<error message>" }`

### Update Note

- **URL**: `/notes/<int:id>`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <access_token>`
- **URL Params**: `id`
- **Body**: `note`
- **Success Response**: `{ id: 1, note: "updated note", user_id: 12 }`
- **Error Response**: `{ message: "<error message>" }`

## Authorization

Several endpoints require authorization using JWT. After successful login or signup, an access token is returned. This token must be included in the Authorization header for all protected endpoints in the following format:

``` Authorization: Bearer <access_token> ```

## Testing the API

To test the API, you can use any HTTP client like Postman or Thunder Client. Thunder Client is an extension for Visual Studio Code that makes it easy to test HTTP requests directly from your IDE.

For endpoints that require authorization, you need to include the JWT token in the Authorization header. Here's an example of how to do this:

``` app.config['JWT_SECRET_KEY'] = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c ```


## Feedback

If you have any feedback, please reach out to us at srbgupta98@gmail.com
