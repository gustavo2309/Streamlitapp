from TCC_Selenium import *
from TCC_TextBlob_GoogleTrans import *
from TCC_Snscrape import *
from TCC_Flair_AnalySenti import *
from TCC_Azure import *
from time import sleep


#chama arquivo python que pega comentarios do twitter via SELENIUM e salva em CSV dentro da pasta

#1- para Webscrapping em Selenium, 2-para Webscrapping em Snscrape

Selecao = int(input("\nDigite 1 para Webscrapping Selenium\n"
                    "Digite 2 para Webscrapping Snscrape\n"))

if Selecao == 1:
    Parametros_Selenium()
elif Selecao == 2:
    Parametros_Snscrape()
else:
    "ERRO, NENHUMA OPÇÃO SELECIONADA"

sleep(5)
#Pega comentarios do twitter, traduz para ingles e realiza analise de sentimentos na LIB TextBlob
Executa_AnaliseSentimentos_TextBlob()
sleep(5)
# Realiza Analise de sentimentos com a solução da Azure
Executa_AnaliseSentimentos_Azure()
sleep(5)
# Realiza Analise de sentimentos com a lib Flair
Executa_AnaliseSentimentos_Flair()


