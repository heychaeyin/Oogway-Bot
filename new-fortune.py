import numpy as np

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
    
print(advice_data['neutral'])

