#Importing the Flask class libraries
from flask import Flask

#Creating an app instance
app = Flask(__name__)

#Creating a route
@app.route("/")

#Defining a function to be called
def home():
    return "Chapel Home Page"

print("__name__")
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
