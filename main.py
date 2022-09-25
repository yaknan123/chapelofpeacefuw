#Importing the Flask class libraries
from flask import Flask, render_template

#Creating an app instance
app = Flask(__name__)


#Creating a route
@app.route("/")
#Defining a function to be called
def home():
    return render_template('index.html')

#Creating a route
@app.route("/about")
#Defining a function to be called
def home():
    return render_template('about.html')

print("__name__")
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
