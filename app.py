from flask import Flask, request, make_response
from datetime import datetime,timedelta
import time

app = Flask(__name__)

# Route to Home Page
@app.route('/')
def index():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the current date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return f"Home Page, Current time : {formatted_datetime}"

# Route to set a cookie
@app.route('/set_cookie/<value>')
def set_cookie(value):
    resp = make_response("Cookie set!")
    # Calculate the expiration time using datetime and timedelta
    expires_timestamp = int(time.time()) + 5    
    
    # or we can use below but we need to convert the datetime object to a UNIX timestamp
    
    # expires = datetime.now() + timedelta(seconds=5)
    # expires_timestamp = int(expires.timestamp())
    
    resp.set_cookie(key='sample_cookie', value= value, expires= expires_timestamp)
    print(f"expires : {expires_timestamp}")
    return resp

# Route to retrieve the cookie
@app.route('/get_cookie')
def get_cookie():
    sample_cookie = request.cookies.get('sample_cookie')
    if sample_cookie is not None:
        return f"Value of sample_cookie: {sample_cookie}"
    else:
        return "Cookie not set."

# My Configurations

hostMachine = "127.0.0.1"
portNo = 5000
debugMode = True

# Start application
if __name__ == "__main__":
    app.run(host=hostMachine, port=portNo, debug=debugMode)