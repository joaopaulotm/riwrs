#!-*- coding: utf8 -*-
import json
import re
import csv

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

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

def GravaLocalidades(arquivo_texto):
    tweets_data = []
    tweets_file = open(arquivo_texto, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    saida = open('localidades.csv', 'w')
    saida.writelines('país;quantidade')
    for tweet in tweets_data:
        try:
            saida.writelines('\n' +tweet['place']['country'].replace('Brazil', 'Brasil').replace('\n', ' ').replace(';', ' ') + ';' + '')
        except:
            continue
    saida.close()

def GravaCandidatos(arquivo_texto):
    tweets_data = []
    tweets_file = open(arquivo_texto, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    saida = open('candidatos.csv', 'w')
    saida.writelines('nome;quantidade')
    JairBolsonaro = {'Contagem': 0}
    MarinaSilva = {'Contagem': 0}
    RodrigoMaia = {'Contagem': 0}
    GeraldoAlckmin = {'Contagem': 0}
    CiroGomes = {'Contagem': 0}
    Indeterminado = {'Contagem': 0}

    for tweet in tweets_data:
        if 'text' in tweet:
            if word_in_text('Jair Bolsonaro', tweet['text']):
                JairBolsonaro['Contagem'] += 1
                #candidatos.append('Jair Bolsonaro')
            elif word_in_text('Marina Silva', tweet['text']):
                MarinaSilva['Contagem'] += 1
                #candidatos.append('Marina Silva')
            elif word_in_text('Rodrigo Maia', tweet['text']):
                RodrigoMaia['Contagem'] += 1
                #candidatos.append('Rodrigo Maia')
            elif word_in_text('Geraldo Alckmin', tweet['text']):
                GeraldoAlckmin['Contagem'] += 1
                #candidatos.append('Geraldo Alckmin')
            elif word_in_text('Alckmin', tweet['text']):
                GeraldoAlckmin['Contagem'] += 1
                #candidatos.append('Geraldo Alckmin')
            elif word_in_text('Ciro Gomes', tweet['text']):
                CiroGomes['Contagem'] += 1
                #candidatos.append('Ciro Gomes')
            elif word_in_text('Bolsonaro', tweet['text']):
                JairBolsonaro['Contagem'] += 1
                #candidatos.append('Jair Bolsonaro')
            else:
                #candidatos.append('(ruído)')
                Indeterminado['Contagem'] += 1
                continue

    saida.writelines('\n' + 'Jair Bolsonaro;' + str(JairBolsonaro['Contagem']))
    saida.writelines('\n' + 'Marina Silva;' + str(MarinaSilva['Contagem']))
    saida.writelines('\n' + 'Geraldo Alckmin;' + str(GeraldoAlckmin['Contagem']))
    saida.writelines('\n' + 'Ciro Gomes;' + str(CiroGomes['Contagem']))
    saida.writelines('\n' + 'Rodrigo Maia;' + str(RodrigoMaia['Contagem']))
    saida.writelines('\n' + 'Indeterminado;' + str(Indeterminado['Contagem']))
    saida.close()


def CriaVocabulario(arquivo_texto):
    tweets_data = []
    tweets_file = open(arquivo_texto, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    dicionario = {}

    for tweet in tweets_data:
        if word_in_text('Bolsonaro', tweet['text']):
            textoPuro = tweet['text']
            textoQuebrado = textoPuro.lower().split(' ')
            for lista in textoQuebrado:
                if lista in dicionario:
                    dicionario[lista] += 1
                else:
                    dicionario.update({lista: 1})

    saida = open('palavras_JairBolsonaro.csv', 'w', encoding="utf-8")
    for chave, valor in dicionario.items():
        saida.writelines('\n' + str(chave) + ';' + str(valor))
    saida.close()

    dicionario = {}

    for tweet in tweets_data:
        if word_in_text('Marina Silva', tweet['text']):
            textoPuro = tweet['text']
            textoQuebrado = textoPuro.lower().split(' ')
            for lista in textoQuebrado:
                if lista in dicionario:
                    dicionario[lista] += 1
                else:
                    dicionario.update({lista: 1})

    saida = open('palavras_Marina_Silva.csv', 'w', encoding="utf-8")
    for chave, valor in dicionario.items():
        saida.writelines('\n' + str(chave) + ';' + str(valor))
    saida.close()

    dicionario = {}

    for tweet in tweets_data:
        if word_in_text('Rodrigo Maia', tweet['text']):
            textoPuro = tweet['text']
            textoQuebrado = textoPuro.lower().split(' ')
            for lista in textoQuebrado:
                if lista in dicionario:
                    dicionario[lista] += 1
                else:
                    dicionario.update({lista: 1})

    saida = open('palavras_Rodrigo_Maia.csv', 'w', encoding="utf-8")
    for chave, valor in dicionario.items():
        saida.writelines('\n' + str(chave) + ';' + str(valor))
    saida.close()

    dicionario = {}

    for tweet in tweets_data:
        if word_in_text('Alckmin', tweet['text']):
            textoPuro = tweet['text']
            textoQuebrado = textoPuro.lower().split(' ')
            for lista in textoQuebrado:
                if lista in dicionario:
                    dicionario[lista] += 1
                else:
                    dicionario.update({lista: 1})

    saida = open('palavras_Alckmin.csv', 'w', encoding="utf-8")
    for chave, valor in dicionario.items():
        saida.writelines('\n' + str(chave) + ';' + str(valor))
    saida.close()

    dicionario = {}

    for tweet in tweets_data:
        if word_in_text('Ciro Gomes', tweet['text']):
            textoPuro = tweet['text']
            textoQuebrado = textoPuro.lower().split(' ')
            for lista in textoQuebrado:
                if lista in dicionario:
                    dicionario[lista] += 1
                else:
                    dicionario.update({lista: 1})

    saida = open('palavras_Ciro_Gomes.csv', 'w', encoding="utf-8")
    for chave, valor in dicionario.items():
        saida.writelines('\n' + str(chave) + ';' + str(valor))
    saida.close()