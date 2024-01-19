from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests



app = Flask(__name__)

URL1 = 'https://api.genderize.io'
URL2 = 'https://api.agify.io'
yyy = datetime.now().year


@app.route('/')
def home():
    random_number = random.randint(1, 100)
    return render_template('index.html', num=random_number, yr=yyy)


@app.route('/username/<name>')
def greet(name):
    name = name.capitalize()
    response = requests.get(url=URL1, params='name='+name)
    #print(response.status_code)
    data = response.json()
    #print(data)
    gender = data['gender']
    #print(gender)

    response2 = requests.get(url=URL2, params='name='+name)
    data2 = response2.json()
    age = data2['age']

    return render_template('greet.html', name=name, sex=gender, ppp=data['probability'], yyy=age)

@app.route('/xxx/<num>')
def get_blog(num):
    resp = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    #print(resp.status_code)
    texts = resp.json()
    print(num)
    #print(texts)

    return render_template('blog.html', texts=texts)






if __name__ == "__main__":
    app.run(debug=True)


