import numpy as np

path = 'data/combined_processed_text.txt'
data = list(np.loadtxt(path, dtype=str, encoding='utf8', delimiter ='\n',))

#Goal is to get 5651 neutrals remaining 
counter = 0
i=0
while counter < (55037 - 5651):
    data_emo = data[i].split(';')
    act_emo = data_emo[len(data_emo)-1]
    if 'neutral' in act_emo:
        data[i] = ''
        counter+=1
    i+=1

data = [ele for ele in data if ele.strip()]

with open('cut_down_data.txt', 'w', encoding='utf8') as f:
    for line in data:
        f.write(line)
        f.write('\n')
