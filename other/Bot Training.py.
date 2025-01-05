import nltk
import numpy as np
from aitextgen import aitextgen
import pandas as pd
import random as rd

path = "data/cut_down_data.txt"
data = np.loadtxt(path, dtype=str, delimiter = "\n", encoding = 'utf8')

fortune_list = list(np.loadtxt('data/Fortune.txt', dtype=str, delimiter = '. ', encoding = 'utf8'))

#ai = aitextgen()
#ai.train(path, line_by_line = True, learning_rate = 1e-3, num_steps = 100)
    
ai = aitextgen(model_folder = 'trained_model')

path = 'data/new_fortunes.txt'
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
        if target_emo in emo:
            advice_list = advice_data[emo]
            advice = advice_list[rd.randint(0, 9)]
            return advice

prompt = input('The universe questions how one is feeling... ')
result = ai.generate_one(prompt = prompt, temperature = 0.7)
cut = result.split(';')
emo = cut[len(cut)-1]
clean_emo = emo[:len(emo)-1]
print('Master Oogway senses that you are feeling: {}'.format(clean_emo))   
print('Master Oogway advises: ' + get_advice(clean_emo))#

