# Words Counter and Paragraphs Counter Flask App using Python

from flask import Flask,request,render_template
from datetime import date

#### Defining Flask App
app = Flask(__name__)


#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

def replace_multiple_newlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

################## ROUTING FUNCTIONS #########################

#### Our main page
@app.route('/')
def wordcount():
    return render_template('wordcount.html',datetoday2=datetoday2) 

#### This function will run when we add a new user
@app.route('/count', methods=['POST'])
def count():
    text = request.form['text']
    action = request.form.get('action')

    if action == 'save':
    # Save the text to a file
        with open(f'text_{datetoday}.txt', 'w') as file:
            file.write(text)
        return render_template('wordcount.html', datetoday2=datetoday2, message="Text has been saved to a file!")

    words = len(text.split())
    paras = replace_multiple_newlines(text)

    text = text.replace('\r','')
    text = text.replace('\n','')

    chars = len(text)
    return render_template('wordcount.html',words=words,paras=paras,chars=chars,datetoday2=datetoday2) 


#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)