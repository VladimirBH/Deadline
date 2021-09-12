#from tensorflow import keras
#from tensorflow.keras.layers import Dense
#from tensorflow.keras import layers
import os
from os import listdir
from os.path import isfile, join, isdir
import nltk
from keras_preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import pymorphy2
from sklearn.feature_extraction.text import CountVectorizer
import docx
import string


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


def tokenizer_words(name_folder: str, file_name: str, path: str):
    main_folder = os.listdir(path)
    print("Загрузка файлов...")
    list_of_files = []
    for folders in main_folder:  # Шарим по папкам с названием региона
        sub_path = join(path, folders)

        if isdir(join(sub_path, name_folder)):
            # Получили список содержимого Алтайский край/3_2 и тому подобное
            list_folders = listdir(join(path, folders, name_folder))

            if not len(list_folders):
                continue

            # Шарим по папкам, название которых - токены
            for sub_folders in list_folders:

                sub_sub_path = join(path, folders, name_folder, sub_folders)

                if isfile(sub_sub_path):
                    list_of_files.append([join(path, folders, name_folder, sub_folders1)
                                          for sub_folders1 in list_folders if (sub_folders1[:2] != '~$')
                                          and (sub_folders1[:7].lower() == "edition") and
                                          ((sub_folders1[-4:] == "docx") or (sub_folders1[-3:] == "doc"))])
                    continue
                # Список содержимого
                # Получаем список содержимого папки-токена
                list_sub_folders = [f for f in listdir(sub_sub_path) if isdir(join(sub_sub_path, f))]
                for sub_sub_sub_folders in list_sub_folders:
                    list_files = listdir(join(path, folders, name_folder, sub_folders, sub_sub_sub_folders))

                    list_of_files.append([join(path, folders, name_folder, sub_folders, sub_sub_sub_folders, curr_file)
                                          for curr_file in list_files if (curr_file[:2] != '~$')
                                          and (curr_file[:len(file_name)].lower() == file_name) and
                                          ((curr_file[-4:] == "docx") or (curr_file[-3:] == "doc"))])

        else:
            continue

    list_of_files = [f for f in list_of_files if f]
    # for i in range(len(list_of_files)):
    #     if not list_of_files[i]:
    #         list_of_files.pop(i)
    print("Файлы загружены")
    text_documents = []
    print("Чтение файлов и токенизация слов...")
    for document in list_of_files:
        doc = docx.Document(document[0])
        text = ""
        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                for run in paragraph.runs:
                    if run.font.highlight_color:
                        text += run.text
        text_documents.append(text)

    formatted_text = []
    stop_words = stopwords.words("russian")
    # Приведение всех слов к первоначальной форме
    for text_document in text_documents:

        text_token = nltk.word_tokenize(text_document)
        morph = pymorphy2.MorphAnalyzer()

        for i in range(len(text_token)):
            p = morph.parse(text_token[i])[0]
            text_token[i] = p.normal_form
            if (text_token[i] not in string.punctuation) and (text_token[i] not in stop_words):
                formatted_text.append(text_token[i])

    formatted_text_without_punc = []
    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(formatted_text)
    formatted_text = vectorizer.get_feature_names()

    print(formatted_text)

    # encoded_text = tokenizer.texts_to_matrix(formatted_text, mode="binary")


tokenizer_words("4_2", "edition", "C:\\dataset\\DataSet_Razmetra")
