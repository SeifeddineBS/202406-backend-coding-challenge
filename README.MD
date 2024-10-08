# Translation Service Web Application

This Django-based web application provides translation services using the Google Cloud Translation API. Users can sign up, log in, and access a set of APIs to translate text or HTML content into different languages.

## Features

- **User Authentication**: Sign up, log in, and log out with session and token-based authentication.
- **Translation Services**: Submit plain text or HTML content for translation into supported languages.
- **Translation Management**: View, list, and delete your translation requests.

## API Endpoints

### 1. User Signup

- **URL**: `/signup/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "string",
      "password": "string"
  }
  ```
- **Response**:
  - On success: 
    ```json
    { 
        "token": "your_token", 
        "user": { 
            "username": "string", 
            "email": "string" 
        } 
    }
    ```
  - On failure: Validation errors.

### 2. User Login

- **URL**: `/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "string",
      "password": "string"
  }
  ```
- **Response**:
  - On success: 
    ```json
    { 
        "token": "your_token", 
        "user": { 
            "username": "string", 
            "email": "string" 
        } 
    }
    ```
  - On failure: 
    ```json
    {"missing user"}
    ```

### 3. User Logout

- **URL**: `/logout/`
- **Method**: `GET`
- **Response**:
  ```json
  {"User logged out"}
  ```

### 4. List and Create Translations

- **URL**: `/translations/`
- **Method**: `GET` or `POST`
- **GET Parameters**: 
  - `user` (optional): Filter translations by user ID.
- **POST Request Body**:
  ```json
  {
      "original_text": "string",
      "target_language": "string",
      "type": "HTML" or "PLAIN_TEXT"
  }
  ```
- **Response**:
  - On GET: 
    ```json
    {"Translations": [ { ...translation_data... }, ... ]}
    ```
  - On POST: Created translation object or validation errors.

### 5. Translation Details and Deletion

- **URL**: `/translations/<id>/`
- **Method**: `GET` or `DELETE`
- **Response**:
  - On GET: Translation object.
  - On DELETE: Status 204 (No Content).

### 6. Test Token

- **URL**: `/test-token/`
- **Method**: `GET`
- **Response**: 
  ```json
  "passed!"
  ```

## Environment Setup

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SeifeddineBS/202406-backend-coding-challenge.git
   ```

2. **Navigate into the project directory**:
   ```bash
   cd backendCodingChallenge
   ```

3. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Create a `.env` file in the project root directory.
   - **Note**: The `.env` file can be found at [this link](https://drive.google.com/file/d/14FtzT3nxI4g6JGqINJd6OPZEXDRxIoh9/view?usp=sharing).
   - **Important**: Access to this link is restricted for security reasons. Please request access, and I will approve your request as soon as possible.

6. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```


7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to test the application locally.

## Deployment

The application is deployed at [[Website Link](https://backend-coding-challenge.up.railway.app)]. Access the public APIs and test the application using this link.

## Testing the APIs

You can test the APIs using tools like [Postman](https://www.postman.com/). When testing protected endpoints that require authentication, you must provide the required token in the request headers.

To add the authentication token in Postman:

1. **Go to the Headers tab**: When creating or editing a request in Postman, navigate to the "Headers" tab.

2. **Add the Authorization header**: In the "Key" field, enter `Authorization`.

3. **Enter the token in the "Value" field**: The token should be entered in the following format:
   ```
   Token 952aec962241bcd68698ab484d122698da82d06c
   ```
   Make sure that there is a space between `Token` and the actual token value.

4. **Send the request**: With the `Authorization` header in place, you can proceed to send your request.

## Contact

For any issues or questions, please contact at seifeddine.bensalah@gmail.com.