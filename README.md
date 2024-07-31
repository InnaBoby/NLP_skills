_NLP skills presentation_

**PET-проект "Анализ и классификация отзывов на рестораны"**

*данные - отзывы о ресторанах в формате jsonl (47139 строк, 6 столбцов, 6 классов в основной оценке). Датасет взят на HuggingFace (blinoff/restaurants_reviews)

*модели классификации - 1) градиентный бустинг над эмбеддингами w2v с весами TF-IDF 2) fine-tuned ruBERT

*приложение на Streamlit (https://nlp-skills-presentation.streamlit.app/)
