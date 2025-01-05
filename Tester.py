import nltk
import numpy as np
from aitextgen import aitextgen
from nltk.corpus import stopwords
import urllib
import bs4 as bs
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


#Scraping from Website
url = 'discord/groups/Degenerates/user/monogata#3992'
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,"html.parser") 
text = ""
for paragraph in soup.find_all('p'): #The <p> tag defines a paragraph in the webpages
    text += paragraph.text
#Pre Processing    
text = re.sub(r'\[[0-9]*\]',' ',text) # [0-9]* --> Matches zero or more repetitions of any digit from 0 to 9
text = text.lower() #everything to lowercase
text = re.sub(r'\W^.?!',' ',text) # \W --> Matches any character which is not a word character except (.?!)
text = re.sub(r'\d',' ',text) # \d --> Matches any decimal digit
text = re.sub(r'\s+',' ',text) # \s --> Matches any characters that are considered whitespace (Ex: [\t\n\r\f\v].)


#Pulling text from Custom Textfile
path = 'myData.txt'
data = np.loadtxt(path, dtype = str, delimiter = '\n')

#Removing Stopwords from Data
def removeStop(list_of_lists):
    temp = []
    for s in list_of_lists:
        tokenWord = nltk.word_tokenize(s)
        filtered_words = [word for word in tokenWord if word not in stopwords.words('english')]
        filtered_sentence = ' '.join(filtered_words)
        temp.append(filtered_sentence)
    return temp

#Removing Puncuation from Data
def removePunct(list_of_lists):
    temp = []
    for s in list_of_lists:
        filler = re.sub(r'[^\w\s]','',s)
        temp.append(filler)
    return temp

