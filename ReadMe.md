
## Cookie Handling with Flask Application

### Overview

The "Cookie Handling with Flask" application is a Flask-based web service designed to illustrate how to work with cookies in a web application. It provides the following functionality:

1.  Displays the current date and time on the home page.
2.  Allows you to set a cookie with a specified value that expires after 5 seconds.
3.  Retrieves and displays the value of the previously set cookie.

### Code Structure

The code consists of several parts, each serving a specific purpose:

1.  **Importing Required Modules:**

-   `Flask`: This module is used for creating the web application.
-   `request`: It is used for handling incoming HTTP requests.
-   `make_response`: Used to create an HTTP response.
-   `datetime`: Provides functions for working with dates and times.
-   `time`: Helps in managing time-related operations.
2.  **Creating the Flask App:**

    ``` python 
    app = Flask(__name__) 
    ```

    This line initializes the Flask application.

3.  **Routes:**

-   **Home Page:**
    
    ```python
    @app.route('/')
    def index():
    ```

    This route displays the current date and time. It fetches the current date and time, formats it, and returns it as a response.
    
-   **Set Cookie:**
    
    ```python    
    @app.route('/set_cookie/<value>')
    def set_cookie(value):
    ```
    
    This route sets a cookie with a specified value. It calculates the expiration time as a UNIX timestamp and sets the cookie with the provided value.
    
-   **Get Cookie:**
    
    ```python    
    @app.route('/get_cookie')
    def get_cookie():
    ```
    This route retrieves and displays the value of the previously set cookie.
    
4.  **Configuration:**

```python
hostMachine = "127.0.0.1"
portNo = 5000
debugMode = True
```

These variables store the configuration settings for the Flask application, such as the host, port, and debug mode.

5.  **Starting the Application:**

``` Python
if __name__ == "__main__":
```

This conditional block starts the Flask application with the specified host, port, and debug mode if the script is run directly.


### Usage

1.  To run this application, make sure you have Flask installed. You can install Flask using `pip`:

```    bash
pip install Flask
```

2.  Run the script, and the Flask application will start.

```    bash
python your_script_name.py
```

3.  Access the application in a web browser:

-   Home Page: `http://127.0.0.1:5000/`
-   Set Cookie: `http://127.0.0.1:5000/set_cookie/your_cookie_value`
-   Get Cookie: `http://127.0.0.1:5000/get_cookie`

### Note

-   The cookie set using the `/set_cookie` route will expire after 5 seconds.