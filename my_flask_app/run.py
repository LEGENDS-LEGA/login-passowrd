from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Պետք է համոզվեք, որ MongoDB-ն աշխատում է ստեղեկների այս URI-ին
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = {
            "username": username,
            "password": password
        }
        try:
            collection.insert_one(user_data)
            return "Օգտատիրոջ տվյալները հաջողությամբ պահպանված են"
        except Exception as e:
            return f"Տվյալների ավելացման սխալ՝ {e}"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
