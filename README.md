# Oogway Bot: Sentiment Analysis & Philosophical Advice

This project is a sentiment analysis tool that detects emotions in user-provided text and returns a piece of philosophical advice tailored to those emotions. It was created in the Summer of 2022 as a part of [**AI Camp's**](https://www.ai-camp.org/) summer session along with five other teammates and a mentor to guide us. 

---

## Table of Contents
1. [Credits](#credits)
2. [Overview](#overview) 
3. [Demo](#demo)  
4. [How It Works](#how-it-works)  
5. [Libraries & Technologies](#libraries--technologies)  
6. [Dataset Used](#dataset-used)

---

## Credits
- **Hyrum Hansen** – Dictator and Overlord (Mentor)  
- **Nathan Tran** – Product Manager & Data Scientist  
- **Harrison Butler** – Data Scientist & Website Developer  
- **Logan Kilinski** – Website Designer & Developer  
- **Gerald Aguirre** – Website Designer  
- **Vraj Prajapati** – Website Designer  
- **Shae Sihock** – Data Scientist

---

## Overview
During a summer camp program, our team set out to build a machine learning model that could:
1. **Identify emotions** (e.g., grief, sadness, excitement, approval, desire) from a user’s input text.  
2. **Offer targeted advice** by providing short, philosophical quotes or suggestions tailored to the detected emotion.

We aimed to combine **sentiment analysis** with **creative, uplifting responses** to demonstrate how AI can both recognize and respond to human emotions in a meaningful way.

---

## Demo
A video presentation of the project can be found on **YouTube**:

[**Oogway Bot Presentation**](https://www.youtube.com/watch?v=WbypRp6fyeI&list=PLbuomA3vEYEenEzaAvOCrnqae2QVDVaF8&index=8)

In this video, we:
- Introduce our team roles.
- Walk through various example inputs and outputs.
- Showcase data exploration pages and visualizations.
- Discuss our methodology, data collection, and future plans.

---

## How It Works
1. **Data Collection & Processing**  
   - We compiled a large dataset of text snippets labeled with various emotions.  
   - Additional “fortune cookie”–style quotes were generated (with help from OpenAI) for each emotion.  
   - The data was cleaned, formatted, and balanced so that the model could learn equally from each emotion category.

2. **Model Training**  
   - We used **AI TextGen** (built on PyTorch) to train a model that maps an input text to the most likely emotion.  
   - After extensive tuning (reducing loss from ~3.6 to under 1.0), the model began producing coherent and \*somewhat\* accurate emotion predictions.

3. **Advice Generation**  
   - Once the model identifies the user’s emotion, the system returns a piece of philosophical or uplifting advice from our “fortune cookie” data.  
   - Each emotion has multiple possible advice snippets to keep responses fresh and varied.

4. **Website Frontend**  
   - We created a web interface where users could type in a sentence and instantly receive a predicted emotion plus advice.  
   - This site also showcased our data exploration (word clouds, charts, and embeddings) and provided links to external resources.

---

## Libraries & Technologies

### Libraries
- **NumPy**  
- **NLTK**  
- **Pandas**  
- **Matplotlib**  
- **Word2vec**  
- **PyPi**  
- **Plotly**  
- **TensorFlow**  

### Tech Stack
- **Python**, **OpenAI**  
- **aitextgen**, **GPT-2**  
- **Flask**, **Bootstrap**  
- **HTML**, **CSS**, **JavaScript**

---

## Dataset Used
We used the **Emotions Dataset for NLP** from Kaggle, which can be found here:  
[**Emotions Dataset (Kaggle)**](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)

---

**Additional Note:**  
The `other` folder in this repository contains data and various support files used to pre-process and train the model.
