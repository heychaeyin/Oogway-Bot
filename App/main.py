# Run by typing python3 main.py

# **IMPORTANT:** only collaborators on the project where you run
# this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

# import basics
import os

# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url
# import stuff for our models
from aitextgen import aitextgen

#import stuff for data...
import random as rd
import numpy as np

path = 'new_fortunes.txt'
data = list(np.loadtxt(path, dtype=str, encoding='utf8', delimiter ='\n',))
emo_list = ['admiration','amusement','anger','annoyance','approval','caring','confusion',
            'curiosity','desire','disappointment','disapproval','disgust','embarrassment','excitement',
            'fear','gratitude','grief','joy','love','nervousness','optimism','pride','realization','relief',
            'remorse','sadness','surprise','neutral']
advice_data = {}
for emo in emo_list:
    advice_data['{emotion}'.format(emotion = emo)] = []

startIndex = 0
endIndex = 10
for emo in advice_data.keys():
    advice_data[emo] = data[startIndex:endIndex]
    startIndex+= 10
    endIndex +=10

def get_advice(target_emo):
    for emo in advice_data.keys():
        if emo in target_emo:
            advice_list = advice_data[emo]
            advice = advice_list[rd.randint(0, 9)]
            return advice
# load up a model from memory. Note you may not need all of these options.
ai = aitextgen(model_folder="model/", to_gpu=False)

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 11420
base_url = get_base_url(port)


# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

app.secret_key = os.urandom(64)

# set up the routes and logic for the webserver


# ROUTES FOR THE MAIN PAGES
# -------------------------
@app.route(f'{base_url}')
def home():
    return render_template('index.html', generated=None)

@app.route(f'{base_url}', methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route(f'{base_url}/index.html')
def index():
    return render_template('index.html')

@app.route(f'{base_url}/about.html')
def about():
    return render_template('about.html')

@app.route(f'{base_url}/demo.html')
def demo():
    return render_template('demo.html')

@app.route(f'{base_url}/journey.html')
def journey():
    return render_template('journey.html')

@app.route(f'{base_url}/data.html')
def data():
    return render_template('data.html')


# REDIRECTS
#----------

@app.route(f'{base_url}/results/index.html')
def redirect_home():
    return redirect(url_for('home'))

@app.route(f'{base_url}/results/about.html')
def redirect_about():
    return redirect(url_for('about'))

@app.route(f'{base_url}/results/demo.html')
def redirect_demo():
    return redirect(url_for('demo'))

@app.route(f'{base_url}/results/journey.html')
def redirect_journey():
    return redirect(url_for('journey'))

@app.route(f'{base_url}/results/data.html')
def redirect_data():
    return redirect(url_for('data'))


# OTHER STUFF
# -----------
@app.route(f'{base_url}/results/')
def results():
    if 'data' in session:
        data = session['data']
        return render_template('demo.html', generated=data)
    else:
        return render_template('demo.html', generated=None)


@app.route(f'{base_url}/generate_text/', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text.
    """

    prompt = request.form['prompt'] + "%"


    #Checks if last charecter is alpha, if so isNotLetter becomes false
    isNotLetter = True
    while isNotLetter:
        l = len(prompt[0])
        if prompt[0][-1].isalpha():
            isNotLetter = False
        else:
            prompt[0] = prompt[0][:l-1]

    if prompt is not None:
        generated = ai.generate(
            n=1,
            batch_size=3,
            prompt=str(prompt),
            temperature=0.9,
            return_as_list = True
        )



    generated[0] = generated[0] + ";"
    emotion = generated[0].split(";")[1].split(" ")
    output = 'Master Oogway senses that you are feeling: ' + emotion[0]  + '\nMaster Oogway advises: ' + get_advice(emotion[0])

    data = {'generated_ls': emotion}
    session['data'] = output
    return redirect(url_for('results'))

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page


if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc19.ai-camp.dev'

    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host='0.0.0.0', port=port, debug=True)
