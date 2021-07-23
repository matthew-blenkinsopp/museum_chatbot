import os

from django.contrib import admin, messages
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
# Register your models here.
from chat_bot.models import Question, QuestionCorpus, Keyword


class QuestionCorpusAdmin(admin.ModelAdmin):

    def getWordCurrentCount(self, i, w):
        try:
            count = keywordsDf.loc[i, w]
            if str(count) == 'nan':
                count = 0
        except:
            count = 0

        return count

    def removeExistingKeywords(self, addedWords, originalWords):
        resultWords = originalWords
        for i in range(len(addedWords)):
            if addedWords[i] not in originalWords:
                resultWords.append(addedWords[i])
        return resultWords

    def learn(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        keywords = Keyword.objects.all().values_list('word', flat=True)
        keywords = list(dict.fromkeys(keywords))
        pairedFAQs = pd.DataFrame(list(QuestionCorpus.objects.all().values()))

        keywordsDf = pd.DataFrame(columns=keywords)
        index = 0
        for question in pairedFAQs['question']:
            for word in keywords:
                if str(word).lower() in str(question).lower():

                    wordCurrentCount = self.getWordCurrentCount(index, word)
                    keywordsDf.loc[index, word] = wordCurrentCount + 1

                else:
                    keywordsDf.loc[index, word] = self.getWordCurrentCount(index, word)
            index += 1

        for colName in pairedFAQs.columns:
            keywordsDf[colName] = pairedFAQs[colName]
        keywordsDf.to_csv(BASE_DIR + '/chat_bot/model_data/keyPhrasesVectorizer.csv', index=False)
        vectorizedData = keywordsDf
        randomizedData = vectorizedData.sample(frac=1).reset_index(drop=True)

        y = randomizedData[['index_id']]

        columnNames = randomizedData.columns.tolist()

        columnNames.remove('index_id')
        columnNames.remove('question')
        columnNames.remove('created_at')
        columnNames.remove('id')
        X = randomizedData[columnNames]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, )

        X_train = np.array(preprocessing.scale(X_train)).tolist()
        y_train = np.array(y_train).tolist()
        X_test = np.array(preprocessing.scale(X_test)).tolist()
        y_test = np.array(y_test).tolist()

        nn = 150
        lrate = 0.001
        ep = 50

        result = []

        model = models.Sequential([
            layers.Dense(nn, activation='relu', input_shape=(len(keywords),)),
            layers.Dense(Question.objects.count()+1, activation='softmax'),
        ])

        model.compile(optimizer=Adam(lr=lrate),
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.fit(X_train, y_train, epochs=ep, validation_data=(X_test, y_test))

        predicted = np.argmax(model.predict(X_test, verbose=0), axis=-1)
        accuracy = accuracy_score(y_test, predicted)
        precision = precision_score(y_test, predicted, average='macro')
        recall = recall_score(y_test, predicted, average='macro')
        f1 = f1_score(y_test, predicted, average='macro')
        r = 'nn: {}\nrate: {}\nacc: {} \nprec: {}\nrecall: {}\nf1: {}\n' \
            .format(nn, lrate, accuracy, precision, recall, f1)
        result.append(r)

        model.save(os.path.join(BASE_DIR, 'bot_model11'))

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.learn()
        messages.add_message(request, messages.SUCCESS, "The model has been updated")


admin.site.register(Question)
admin.site.register(QuestionCorpus, QuestionCorpusAdmin)
admin.site.register(Keyword)
