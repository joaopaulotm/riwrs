#!-*- coding: utf8 -*-
import functions
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

class MyListener(StreamListener):
    def __init__(self, file):
        global the_file
        self.the_file = open(file, 'a')

    def on_data(self, data):
        self.the_file.write(data)
        return True

    def on_error(self, status):
        print(status)

    def file_close(self):
        self.the_file.close()

def Principal():
    count = 0 #' + str(count) + '
    file = 'tweets_usar.json'
    # setup security
    access_token = ''
    access_token_secret = ''
    consumer_key = ''
    consumer_secret = ''
    while count <= 20000:
        listener = MyListener(file)
        oauth = OAuthHandler(consumer_key, consumer_secret)
        oauth.set_access_token(access_token, access_token_secret)
        max_time = 20  # in seconds
        start_time = time.time()
        stream = Stream(oauth, listener)

        stream.filter(track=['Jair Bolsonaro', 'Bolsonaro', 'Marina Silva', 'Rodrigo Maia',
                             'Geraldo Alckmin', 'Alckmin' 'Ciro Gomes', 'jair bolsonaro', 'bolsonaro',
                             'marina silva', 'rodrigo maia', 'geraldo alckmin', 'ciro gomes'], async=True)
#, languages=['pt']
        elapsed_time = (time.time() - start_time)
        while elapsed_time < max_time:
            elapsed_time = (time.time() - start_time)

        stream.disconnect()
        listener.file_close()
        if count == 200:
            print('-> Coleta: ' + str(count))
        if count == 500:
            print('-> Coleta: ' + str(count))
        if count == 1000:
            print('-> Coleta: ' + str(count))
        if count == 5000:
            print('-> Coleta: ' + str(count))
        count += 1
        time.sleep(60)

def GravaArquivoLegivel(arquivo_texto):
    saida = open('limpos_teste_ml.csv', 'w')
    saida2 = open('palavras.csv', 'w')
    saida2.writelines('frase;sentimento')
    for linha in arquivo_texto:
        try:                        #linha['user']['screen_name']     linha['id_str']
            saida.writelines('\n' + linha['user']['screen_name'] + ';' + linha['text'].replace('\n', ' ').replace(';', ' '))
            saida2.writelines('\n' +linha['text'].replace('\n', ' ').replace(';', ' ') + ';' + '')
        except:
            continue
    saida.close()
    saida2.close()

def Imprime(arquivo):
    tweets_data = []
    tweets_file = open(arquivo, "r")
    saida = []
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    for line in tweets_data:
        saida.append(line)
    #functions.GravaArquivoLegivel(saida)
    #functions.GravaCandidatos(arquivo)
    #functions.GravaLocalidades(arquivo)
    #functions.GravaLocalidades(arquivo)
    functions.CriaVocabulario(arquivo)

Imprime('tweets_usar.json')
#Principal()
print('**Fim**')
