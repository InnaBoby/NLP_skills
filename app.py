import streamlit as st
import torch
from PIL import Image
import pandas as pd
from gensim.models import Word2Vec

from transformers import AutoTokenizer, AutoModelForSequenceClassification

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tokenizer = AutoTokenizer.from_pretrained('ai-forever/ruBert-base')
#декоратор для загрузки модели в кэш
@st.cache_resource
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained('ai-forever/ruBert-base')
    model.load_state_dict(torch.load('weights_ruBERT', map_location=torch.device(DEVICE)))
    if torch.cuda.is_available():
        model.cuda()
    return model

#model = load_model()

#Загрузка данных
df=pd.read_json('restaurants_reviews.jsonl', lines=True)
data=pd.read_csv('preproc_resturants.csv')

add_selectbox = st.sidebar.selectbox(
    "Выберите скилл",
    ("Главная", "Data Preprocessing", "Chat-bot", "Classification"))

if add_selectbox == "Главная":
    st.subheader('NLP skills presentation')
    st.title('Анализ и классификация отзывов на рестораны')
    img = Image.open('img.jpg')
    st.image(img)

elif add_selectbox == 'Data Preprocessing':

    if st.toggle("Показать исходный датасет"):
        st.subheader('Датасет с отзывами на рестораны')
        st.text('47139 строк, 6 столбцов, 6 классов в общей оценке')
        df5=df.head()
        st.table(df5)

    st.subheader('Этапы предобработки')
    st.text('1) Пропуски, дубликаты, аномалии \n2) Проверка баланса классов \n3) Форматирование текста: приведение к нижнему регистру, удаление знаков препинания (исключение “! : - ( )“)\n4) Исправление грамматических ошибок\n5) Удаление стоп-слов (гипотеза проверена-отклонена)\n6) Лемматизация')

    if st.toggle("Показать датасет после препроцессинга"):
        st.text('Данные после препроцессинга')
        data5 = data.head()
        st.table(data5)

    if st.toggle('Визуализация пространства слов (W2V)'):
        st.write(':green[Зеленым] - ТОП-100 слов из :green[позитивных] отзывов (4 и 5 звезд)')
        st.write(':red[Красным] - ТОР-100 слов из :red[негативных] отзывов (оценка 3 и ниже)')
        visual = Image.open('bokeh_plot.jpg')
        st.image(visual)


elif add_selectbox == "Chat-bot":
    st.text('Раздел в разработке')
    #prompt = st.chat_input("Введите вопрос")
    #if prompt:
    #    st.write(prompt)

elif add_selectbox == "Classification":
    st.text('Раздел в разработке')
    #input_text=st.text_area('Введите отзыв:', 'Текст отзыва...')
    #model_w2v = Word2Vec.load("word2v.model")


