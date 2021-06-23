from flask import *  
import io

app = Flask(__name__)  

@app.route('/')
def home():
    return "Welcome to the test page"

@app.route('/numberguesser', methods=['GET'])
def num_guess_game():
    return render_template("index.html")

if __name__ == '__main__':  
   app.run(debug = True)  