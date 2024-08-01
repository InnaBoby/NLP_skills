_NLP skills presentation_

**PET-проект "Анализ и классификация отзывов на рестораны"**

*Данные - отзывы о ресторанах в формате jsonl (47139 строк, 6 столбцов, 6 классов в основной оценке). Датасет взят на HuggingFace (blinoff/restaurants_reviews)

*модели классификации - 1) градиентный бустинг над эмбеддингами w2v с весами TF-IDF 2) fine-tuned ruBERT

**Файлы:**

-app.py -приложение на Streamlit (https://nlp-skills-presentation.streamlit.app/)

-Chat_Bot_Func.py - функция для генерации ответа чат-бота с использованием MistralAPI

-restaurants_reviews.jsonl - исходный датасет

-preproc_resturants.csv - датасет после предобработки

-презентация.pdf - результаты обучения моделей классификации

-word2v.model - обученная модель word2vec

-weights_ruBERT - веса дообученного ruBert

-requirements.txt - список зависимостей для приложения
