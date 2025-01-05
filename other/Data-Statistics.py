import numpy as np
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt

path = 'data/cut_down_data.txt'
data = list(np.loadtxt(path, dtype=str, encoding='utf8', delimiter ='\n',))

emo_list = ['admiration','amusement','anger','annoyance','approval','caring','confusion',
            'curiosity','desire','disappointment','disapproval','disgust','embarrassment','excitement',
            'fear','gratitude','grief','joy','love','nervousness','optimism','pride','realization','relief',
            'remorse','sadness','surprise','neutral']

#Creates a dictionary with the keys being the different emotions possible, and their values being 0; will serve as a counter for how many occurences each emotions comes up
counter = {}
for emo in emo_list:
    counter['{emotion}'.format(emotion = emo)] = 0

#loops through each sentence 
for i in range(len(data)):
    #splits each sentence by the semicolon, as the emotion tag is after the semicolon
    data_emo = data[i].split(';')
    #takes the last item in the list, in case there are already semicolons in the original sentence
    act_emo = data_emo[len(data_emo)-1]
    #goes through each emotion in the list, and if the emotion from the sentence matches the emotion from the list, +1 on the counter
    for emo in emo_list:
        if emo in data_emo:
            counter[emo] += 1


#Never used Matplotlib pray for me
#I copied all this code online @ https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
emotions = list(counter.keys())
occurences = list(counter.values())
                
occ_series = pd.Series(occurences)

plt.figure(figsize = (12, 8))
ax = occ_series.plot(kind='barh')
ax.set_title('Occurences of Emotions in Dataset')
ax.set_ylabel('Emotions')
ax.set_xlabel('Occurences')
ax.set_yticklabels(emotions)

rects = ax.patches
    
for rect in rects:
    x_val = rect.get_width()
    y_val = rect.get_y() + rect.get_height() / 2    
     
    label = '{}'.format(x_val)
    
    plt.annotate(
        label,
        (x_val, y_val), 
        xytext=(2, 0),
        textcoords = 'offset points',
        va='center',
        ha = 'left'
    )
    
plt.show()
    

