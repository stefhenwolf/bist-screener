from telnetlib import PRAGMA_HEARTBEAT
from turtle import listen
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
import talib
import pandas as pd
import time



candle_names = talib.get_function_groups()['Pattern Recognition']

tablo = pd.read_excel("output1.xlsx")

tablo.rename({"Unnamed: 0":"HISSE"}, axis="columns", inplace=True)

df = pd.read_excel (r"C:\Users\umbra\Desktop\yeni çalışma\tumhisse.xlsx")
tickers = df["HISSE"]
tickers_list = tickers.to_list()
tum_hisse = []

for a in tickers_list:
    tum_hisse.append(a[0:-38]+".IS")
 
def liste_olustur(candlename):
    print(tablo[candlename])   
    tablo1 = pd.DataFrame(tablo, columns= [candlename])
    tablo1.drop(tablo1.index[tablo1[candlename] == 0], inplace=True)
    print(tablo1)
    

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token="5160382392:AAGut-nGfKpbDDGSfsoRcWOW0iK7WvjbjUs", use_context=True)

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    
    start = time.time()
    context.bot.send_message(chat_id=update.effective_chat.id, text="BIST mum çubuğu tarama işlemi başlatıldı!"'\n' "Yaklaşık 4-5 dakika bekleyiniz!" '\n' "Formasyon isimleri için: /liste")
    exec(open("bist.py").read())
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tarama işlemi tamamlandı!")
    end = time.time()
    b = end-start
    c = "Geçen zaman: "+str(b)+ "saniye"
    context.bot.send_message(chat_id=update.effective_chat.id, text=c)

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
def liste(update: Update, context: CallbackContext):
    
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Aramak istediğiniz mum çubuğu dizilimini seçiniz!")
    for (i, item) in enumerate(candle_names, start=1):
        a =str(i)+" "+"/"+item
        context.bot.send_message(chat_id=update.effective_chat.id, text=a)   
    
def CDL2CROWS(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL2CROWS = tablo[['HISSE', 'CDL2CROWS']]
    CDL2CROWS = CDL2CROWS[CDL2CROWS['CDL2CROWS'] != 0]
    CDL2CROWS = CDL2CROWS[CDL2CROWS['CDL2CROWS'] > 0]
    
    liste = CDL2CROWS["HISSE"].to_list()
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)  
def CDL3BLACKCROWS(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3BLACKCROWS = tablo[['HISSE', 'CDL3BLACKCROWS']]
    CDL3BLACKCROWS = CDL3BLACKCROWS[CDL3BLACKCROWS['CDL3BLACKCROWS'] != 0]
    CDL3BLACKCROWS = CDL3BLACKCROWS[CDL3BLACKCROWS['CDL3BLACKCROWS'] > 0]
    
    liste = CDL3BLACKCROWS["HISSE"].to_list()
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
              
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)  
def CDL3INSIDE(update: Update, context: CallbackContext):   
     
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3INSIDE = tablo[['HISSE', 'CDL3INSIDE']]
    CDL3INSIDE = CDL3INSIDE[CDL3INSIDE['CDL3INSIDE'] != 0]
    CDL3INSIDE = CDL3INSIDE[CDL3INSIDE['CDL3INSIDE'] > 0]
    
    liste = CDL3INSIDE["HISSE"].to_list()
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
              
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)  
def CDL3LINESTRIKE(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3LINESTRIKE = tablo[['HISSE', 'CDL3LINESTRIKE']]
    CDL3LINESTRIKE = CDL3LINESTRIKE[CDL3LINESTRIKE['CDL3LINESTRIKE'] != 0]
    CDL3LINESTRIKE = CDL3LINESTRIKE[CDL3LINESTRIKE['CDL3LINESTRIKE'] > 0]
    
    liste = CDL3LINESTRIKE["HISSE"].to_list()
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
              
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)  
def CDL3OUTSIDE(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3OUTSIDE = tablo[['HISSE', 'CDL3OUTSIDE']]
    CDL3OUTSIDE = CDL3OUTSIDE[CDL3OUTSIDE['CDL3OUTSIDE'] != 0]
    CDL3OUTSIDE = CDL3OUTSIDE[CDL3OUTSIDE['CDL3OUTSIDE'] > 0]
    
    liste = CDL3OUTSIDE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDL3OUTSIDE)
              
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDL3STARSINSOUTH(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3STARSINSOUTH = tablo[['HISSE', 'CDL3STARSINSOUTH']]
    CDL3STARSINSOUTH = CDL3STARSINSOUTH[CDL3STARSINSOUTH['CDL3STARSINSOUTH'] != 0]
    CDL3STARSINSOUTH = CDL3STARSINSOUTH[CDL3STARSINSOUTH['CDL3STARSINSOUTH'] > 0]
    
    liste = CDL3STARSINSOUTH["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDL3STARSINSOUTH)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)     
def CDL3WHITESOLDIERS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDL3WHITESOLDIERS = tablo[['HISSE', 'CDL3WHITESOLDIERS']]
    CDL3WHITESOLDIERS = CDL3WHITESOLDIERS[CDL3WHITESOLDIERS['CDL3WHITESOLDIERS'] != 0]
    CDL3WHITESOLDIERS = CDL3WHITESOLDIERS[CDL3WHITESOLDIERS['CDL3WHITESOLDIERS'] > 0]
    
    liste = CDL3WHITESOLDIERS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDL3WHITESOLDIERS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDLABANDONEDBABY(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLABANDONEDBABY = tablo[['HISSE', 'CDLABANDONEDBABY']]
    CDLABANDONEDBABY = CDLABANDONEDBABY[CDLABANDONEDBABY['CDLABANDONEDBABY'] != 0]
    CDLABANDONEDBABY = CDLABANDONEDBABY[CDLABANDONEDBABY['CDLABANDONEDBABY'] > 0]
    
    liste = CDLABANDONEDBABY["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLABANDONEDBABY)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDLADVANCEBLOCK(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLADVANCEBLOCK = tablo[['HISSE', 'CDLADVANCEBLOCK']]
    CDLADVANCEBLOCK = CDLADVANCEBLOCK[CDLADVANCEBLOCK['CDLADVANCEBLOCK'] != 0]
    CDLADVANCEBLOCK = CDLADVANCEBLOCK[CDLADVANCEBLOCK['CDLADVANCEBLOCK'] > 0]
    
    liste = CDLADVANCEBLOCK["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLADVANCEBLOCK)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)    
def CDLBELTHOLD(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLBELTHOLD = tablo[['HISSE', 'CDLBELTHOLD']]
    CDLBELTHOLD = CDLBELTHOLD[CDLBELTHOLD['CDLBELTHOLD'] != 0]
    CDLBELTHOLD = CDLBELTHOLD[CDLBELTHOLD['CDLBELTHOLD'] > 0]
    
    liste = CDLBELTHOLD["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLBELTHOLD)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)  
def CDLBREAKAWAY(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLBREAKAWAY = tablo[['HISSE', 'CDLBREAKAWAY']]
    CDLBREAKAWAY = CDLBREAKAWAY[CDLBREAKAWAY['CDLBREAKAWAY'] != 0]
    CDLBREAKAWAY = CDLBREAKAWAY[CDLBREAKAWAY['CDLBREAKAWAY'] > 0]
    
    liste = CDLBREAKAWAY["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLBREAKAWAY)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLCLOSINGMARUBOZU(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLCLOSINGMARUBOZU = tablo[['HISSE', 'CDLCLOSINGMARUBOZU']]
    CDLCLOSINGMARUBOZU = CDLCLOSINGMARUBOZU[CDLCLOSINGMARUBOZU['CDLCLOSINGMARUBOZU'] != 0]
    CDLCLOSINGMARUBOZU = CDLCLOSINGMARUBOZU[CDLCLOSINGMARUBOZU['CDLCLOSINGMARUBOZU'] > 0]
    
    liste = CDLCLOSINGMARUBOZU["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLCLOSINGMARUBOZU)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDLCONCEALBABYSWALL(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLCONCEALBABYSWALL = tablo[['HISSE', 'CDLCONCEALBABYSWALL']]
    CDLCONCEALBABYSWALL = CDLCONCEALBABYSWALL[CDLCONCEALBABYSWALL['CDLCONCEALBABYSWALL'] != 0]
    CDLCONCEALBABYSWALL = CDLCONCEALBABYSWALL[CDLCONCEALBABYSWALL['CDLCONCEALBABYSWALL'] > 0]
    
    liste = CDLCONCEALBABYSWALL["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLCONCEALBABYSWALL)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDLCOUNTERATTACK(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLCOUNTERATTACK = tablo[['HISSE', 'CDLCOUNTERATTACK']]
    CDLCOUNTERATTACK = CDLCOUNTERATTACK[CDLCOUNTERATTACK['CDLCOUNTERATTACK'] != 0]
    CDLCOUNTERATTACK = CDLCOUNTERATTACK[CDLCOUNTERATTACK['CDLCOUNTERATTACK'] > 0]
    
    liste = CDLCOUNTERATTACK["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLCOUNTERATTACK)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)      
def CDLDARKCLOUDCOVER(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLDARKCLOUDCOVER = tablo[['HISSE', 'CDLDARKCLOUDCOVER']]
    CDLDARKCLOUDCOVER = CDLDARKCLOUDCOVER[CDLDARKCLOUDCOVER['CDLDARKCLOUDCOVER'] != 0]
    CDLDARKCLOUDCOVER = CDLDARKCLOUDCOVER[CDLDARKCLOUDCOVER['CDLDARKCLOUDCOVER'] > 0]
    
    liste = CDLDARKCLOUDCOVER["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLDARKCLOUDCOVER)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)       
def CDLDOJI(update: Update, context: CallbackContext):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLDOJI = tablo[['HISSE', 'CDLDOJI']]
    CDLDOJI = CDLDOJI[CDLDOJI['CDLDOJI'] != 0]
    CDLDOJI = CDLDOJI[CDLDOJI['CDLDOJI'] > 0]
    
    liste = CDLDOJI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLDOJI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)    
def CDLDOJISTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLDOJISTAR = tablo[['HISSE', 'CDLDOJISTAR']]
    CDLDOJISTAR = CDLDOJISTAR[CDLDOJISTAR['CDLDOJISTAR'] != 0]
    CDLDOJISTAR = CDLDOJISTAR[CDLDOJISTAR['CDLDOJISTAR'] > 0]
    
    liste = CDLDOJISTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLDOJISTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)   
def CDLDRAGONFLYDOJI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLDRAGONFLYDOJI = tablo[['HISSE', 'CDLDRAGONFLYDOJI']]
    CDLDRAGONFLYDOJI = CDLDRAGONFLYDOJI[CDLDRAGONFLYDOJI['CDLDRAGONFLYDOJI'] != 0]
    CDLDRAGONFLYDOJI = CDLDRAGONFLYDOJI[CDLDRAGONFLYDOJI['CDLDRAGONFLYDOJI'] > 0]
    
    liste = CDLDRAGONFLYDOJI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLDRAGONFLYDOJI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLENGULFING(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLENGULFING = tablo[['HISSE', 'CDLENGULFING']]
    CDLENGULFING = CDLENGULFING[CDLENGULFING['CDLENGULFING'] != 0]
    CDLENGULFING = CDLENGULFING[CDLENGULFING['CDLENGULFING'] > 0]
    
    liste = CDLENGULFING["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLENGULFING)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLEVENINGDOJISTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLEVENINGDOJISTAR = tablo[['HISSE', 'CDLEVENINGDOJISTAR']]
    CDLEVENINGDOJISTAR = CDLEVENINGDOJISTAR[CDLEVENINGDOJISTAR['CDLEVENINGDOJISTAR'] != 0]
    CDLEVENINGDOJISTAR = CDLEVENINGDOJISTAR[CDLEVENINGDOJISTAR['CDLEVENINGDOJISTAR'] > 0]
    
    liste = CDLEVENINGDOJISTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLEVENINGDOJISTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLEVENINGSTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLEVENINGSTAR = tablo[['HISSE', 'CDLEVENINGSTAR']]
    CDLEVENINGSTAR = CDLEVENINGSTAR[CDLEVENINGSTAR['CDLEVENINGSTAR'] != 0]
    CDLEVENINGSTAR = CDLEVENINGSTAR[CDLEVENINGSTAR['CDLEVENINGSTAR'] > 0]
    
    liste = CDLEVENINGSTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLEVENINGSTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLGAPSIDESIDEWHITE(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLGAPSIDESIDEWHITE = tablo[['HISSE', 'CDLGAPSIDESIDEWHITE']]
    CDLGAPSIDESIDEWHITE = CDLGAPSIDESIDEWHITE[CDLGAPSIDESIDEWHITE['CDLGAPSIDESIDEWHITE'] != 0]
    CDLGAPSIDESIDEWHITE = CDLGAPSIDESIDEWHITE[CDLGAPSIDESIDEWHITE['CDLGAPSIDESIDEWHITE'] > 0]
    
    liste = CDLGAPSIDESIDEWHITE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLGAPSIDESIDEWHITE)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLGRAVESTONEDOJI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLGRAVESTONEDOJI = tablo[['HISSE', 'CDLGRAVESTONEDOJI']]
    CDLGRAVESTONEDOJI = CDLGRAVESTONEDOJI[CDLGRAVESTONEDOJI['CDLGRAVESTONEDOJI'] != 0]
    CDLGRAVESTONEDOJI = CDLGRAVESTONEDOJI[CDLGRAVESTONEDOJI['CDLGRAVESTONEDOJI'] > 0]
    
    liste = CDLGRAVESTONEDOJI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLGRAVESTONEDOJI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHAMMER(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHAMMER = tablo[['HISSE', 'CDLHAMMER']]
    CDLHAMMER = CDLHAMMER[CDLHAMMER['CDLHAMMER'] != 0]
    CDLHAMMER = CDLHAMMER[CDLHAMMER['CDLHAMMER'] > 0]
    
    liste = CDLHAMMER["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHAMMER)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHANGINGMAN(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHANGINGMAN = tablo[['HISSE', 'CDLHANGINGMAN']]
    CDLHANGINGMAN = CDLHANGINGMAN[CDLHANGINGMAN['CDLHANGINGMAN'] != 0]
    CDLHANGINGMAN = CDLHANGINGMAN[CDLHANGINGMAN['CDLHANGINGMAN'] > 0]
    
    liste = CDLHANGINGMAN["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHANGINGMAN)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHARAMI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHARAMI = tablo[['HISSE', 'CDLHARAMI']]
    CDLHARAMI = CDLHARAMI[CDLHARAMI['CDLHARAMI'] != 0]
    CDLHARAMI = CDLHARAMI[CDLHARAMI['CDLHARAMI'] > 0]
    
    liste = CDLHARAMI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHARAMI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHARAMICROSS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHARAMICROSS = tablo[['HISSE', 'CDLHARAMICROSS']]
    CDLHARAMICROSS = CDLHARAMICROSS[CDLHARAMICROSS['CDLHARAMICROSS'] != 0]
    CDLHARAMICROSS = CDLHARAMICROSS[CDLHARAMICROSS['CDLHARAMICROSS'] > 0]
    
    liste = CDLHARAMICROSS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHARAMICROSS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHIGHWAVE(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHIGHWAVE = tablo[['HISSE', 'CDLHIGHWAVE']]
    CDLHIGHWAVE = CDLHIGHWAVE[CDLHIGHWAVE['CDLHIGHWAVE'] != 0]
    CDLHIGHWAVE = CDLHIGHWAVE[CDLHIGHWAVE['CDLHIGHWAVE'] > 0]
    
    liste = CDLHIGHWAVE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHIGHWAVE)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHIKKAKE(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHIKKAKE = tablo[['HISSE', 'CDLHIKKAKE']]
    CDLHIKKAKE = CDLHIKKAKE[CDLHIKKAKE['CDLHIKKAKE'] != 0]
    CDLHIKKAKE = CDLHIKKAKE[CDLHIKKAKE['CDLHIKKAKE'] > 0]
    
    liste = CDLHIKKAKE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHIKKAKE)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHIKKAKEMOD(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHIKKAKEMOD = tablo[['HISSE', 'CDLHIKKAKEMOD']]
    CDLHIKKAKEMOD = CDLHIKKAKEMOD[CDLHIKKAKEMOD['CDLHIKKAKEMOD'] != 0]
    CDLHIKKAKEMOD = CDLHIKKAKEMOD[CDLHIKKAKEMOD['CDLHIKKAKEMOD'] > 0]
    
    liste = CDLHIKKAKEMOD["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHIKKAKEMOD)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLHOMINGPIGEON(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLHOMINGPIGEON = tablo[['HISSE', 'CDLHOMINGPIGEON']]
    CDLHOMINGPIGEON = CDLHOMINGPIGEON[CDLHOMINGPIGEON['CDLHOMINGPIGEON'] != 0]
    CDLHOMINGPIGEON = CDLHOMINGPIGEON[CDLHOMINGPIGEON['CDLHOMINGPIGEON'] > 0]
    
    liste = CDLHOMINGPIGEON["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLHOMINGPIGEON)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLIDENTICAL3CROWS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLIDENTICAL3CROWS = tablo[['HISSE', 'CDLIDENTICAL3CROWS']]
    CDLIDENTICAL3CROWS = CDLIDENTICAL3CROWS[CDLIDENTICAL3CROWS['CDLIDENTICAL3CROWS'] != 0]
    CDLIDENTICAL3CROWS = CDLIDENTICAL3CROWS[CDLIDENTICAL3CROWS['CDLIDENTICAL3CROWS'] > 0]
    
    liste = CDLIDENTICAL3CROWS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLIDENTICAL3CROWS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLINNECK(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLINNECK = tablo[['HISSE', 'CDLINNECK']]
    CDLINNECK = CDLINNECK[CDLINNECK['CDLINNECK'] != 0]
    CDLINNECK = CDLINNECK[CDLINNECK['CDLINNECK'] > 0]
    
    liste = CDLINNECK["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLINNECK)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLINVERTEDHAMMER(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLINVERTEDHAMMER = tablo[['HISSE', 'CDLINVERTEDHAMMER']]
    CDLINVERTEDHAMMER = CDLINVERTEDHAMMER[CDLINVERTEDHAMMER['CDLINVERTEDHAMMER'] != 0]
    CDLINVERTEDHAMMER = CDLINVERTEDHAMMER[CDLINVERTEDHAMMER['CDLINVERTEDHAMMER'] > 0]
    
    liste = CDLINVERTEDHAMMER["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLINVERTEDHAMMER)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLKICKING(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLKICKING = tablo[['HISSE', 'CDLKICKING']]
    CDLKICKING = CDLKICKING[CDLKICKING['CDLKICKING'] != 0]
    CDLKICKING = CDLKICKING[CDLKICKING['CDLKICKING'] > 0]
    
    liste = CDLKICKING["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLKICKING)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLKICKINGBYLENGTH(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLKICKINGBYLENGTH = tablo[['HISSE', 'CDLKICKINGBYLENGTH']]
    CDLKICKINGBYLENGTH = CDLKICKINGBYLENGTH[CDLKICKINGBYLENGTH['CDLKICKINGBYLENGTH'] != 0]
    CDLKICKINGBYLENGTH = CDLKICKINGBYLENGTH[CDLKICKINGBYLENGTH['CDLKICKINGBYLENGTH'] > 0]
    
    liste = CDLKICKINGBYLENGTH["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLKICKINGBYLENGTH)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLLADDERBOTTOM(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLLADDERBOTTOM = tablo[['HISSE', 'CDLLADDERBOTTOM']]
    CDLLADDERBOTTOM = CDLLADDERBOTTOM[CDLLADDERBOTTOM['CDLLADDERBOTTOM'] != 0]
    CDLLADDERBOTTOM = CDLLADDERBOTTOM[CDLLADDERBOTTOM['CDLLADDERBOTTOM'] > 0]
    
    liste = CDLLADDERBOTTOM["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLLADDERBOTTOM)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLLONGLEGGEDDOJI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLLONGLEGGEDDOJI = tablo[['HISSE', 'CDLLONGLEGGEDDOJI']]
    CDLLONGLEGGEDDOJI = CDLLONGLEGGEDDOJI[CDLLONGLEGGEDDOJI['CDLLONGLEGGEDDOJI'] != 0]
    CDLLONGLEGGEDDOJI = CDLLONGLEGGEDDOJI[CDLLONGLEGGEDDOJI['CDLLONGLEGGEDDOJI'] > 0]
    
    liste = CDLLONGLEGGEDDOJI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLLONGLEGGEDDOJI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLLONGLINE(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLLONGLINE = tablo[['HISSE', 'CDLLONGLINE']]
    CDLLONGLINE = CDLLONGLINE[CDLLONGLINE['CDLLONGLINE'] != 0]
    CDLLONGLINE = CDLLONGLINE[CDLLONGLINE['CDLLONGLINE'] > 0]
    
    liste = CDLLONGLINE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLLONGLINE)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLMARUBOZU(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLMARUBOZU = tablo[['HISSE', 'CDLMARUBOZU']]
    CDLMARUBOZU = CDLMARUBOZU[CDLMARUBOZU['CDLMARUBOZU'] != 0]
    CDLMARUBOZU = CDLMARUBOZU[CDLMARUBOZU['CDLMARUBOZU'] > 0]
    
    liste = CDLMARUBOZU["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLMARUBOZU)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLMATCHINGLOW(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLMATCHINGLOW = tablo[['HISSE', 'CDLMATCHINGLOW']]
    CDLMATCHINGLOW = CDLMATCHINGLOW[CDLMATCHINGLOW['CDLMATCHINGLOW'] != 0]
    CDLMATCHINGLOW = CDLMATCHINGLOW[CDLMATCHINGLOW['CDLMATCHINGLOW'] > 0]
    
    liste = CDLMATCHINGLOW["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLMATCHINGLOW)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLMATHOLD(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLMATHOLD = tablo[['HISSE', 'CDLMATHOLD']]
    CDLMATHOLD = CDLMATHOLD[CDLMATHOLD['CDLMATHOLD'] != 0]
    CDLMATHOLD = CDLMATHOLD[CDLMATHOLD['CDLMATHOLD'] > 0]
    
    liste = CDLMATHOLD["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLMATHOLD)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLMORNINGDOJISTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLMORNINGDOJISTAR = tablo[['HISSE', 'CDLMORNINGDOJISTAR']]
    CDLMORNINGDOJISTAR = CDLMORNINGDOJISTAR[CDLMORNINGDOJISTAR['CDLMORNINGDOJISTAR'] != 0]
    CDLMORNINGDOJISTAR = CDLMORNINGDOJISTAR[CDLMORNINGDOJISTAR['CDLMORNINGDOJISTAR'] > 0]
    
    liste = CDLMORNINGDOJISTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLMORNINGDOJISTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLMORNINGSTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLMORNINGSTAR = tablo[['HISSE', 'CDLMORNINGSTAR']]
    CDLMORNINGSTAR = CDLMORNINGSTAR[CDLMORNINGSTAR['CDLMORNINGSTAR'] != 0]
    CDLMORNINGSTAR = CDLMORNINGSTAR[CDLMORNINGSTAR['CDLMORNINGSTAR'] > 0]
    
    liste = CDLMORNINGSTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLMORNINGSTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLONNECK(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLONNECK = tablo[['HISSE', 'CDLONNECK']]
    CDLONNECK = CDLONNECK[CDLONNECK['CDLONNECK'] != 0]
    CDLONNECK = CDLONNECK[CDLONNECK['CDLONNECK'] > 0]
    
    liste = CDLONNECK["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLONNECK)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLPIERCING(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLPIERCING = tablo[['HISSE', 'CDLPIERCING']]
    CDLPIERCING = CDLPIERCING[CDLPIERCING['CDLPIERCING'] != 0]
    CDLPIERCING = CDLPIERCING[CDLPIERCING['CDLPIERCING'] > 0]
    
    liste = CDLPIERCING["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLPIERCING)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLRICKSHAWMAN(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLRICKSHAWMAN = tablo[['HISSE', 'CDLRICKSHAWMAN']]
    CDLRICKSHAWMAN = CDLRICKSHAWMAN[CDLRICKSHAWMAN['CDLRICKSHAWMAN'] != 0]
    CDLRICKSHAWMAN = CDLRICKSHAWMAN[CDLRICKSHAWMAN['CDLRICKSHAWMAN'] > 0]
    
    liste = CDLRICKSHAWMAN["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLRICKSHAWMAN)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLRISEFALL3METHODS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLRISEFALL3METHODS = tablo[['HISSE', 'CDLRISEFALL3METHODS']]
    CDLRISEFALL3METHODS = CDLRISEFALL3METHODS[CDLRISEFALL3METHODS['CDLRISEFALL3METHODS'] != 0]
    CDLRISEFALL3METHODS = CDLRISEFALL3METHODS[CDLRISEFALL3METHODS['CDLRISEFALL3METHODS'] > 0]
    
    liste = CDLRISEFALL3METHODS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLRISEFALL3METHODS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSEPARATINGLINES(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSEPARATINGLINES = tablo[['HISSE', 'CDLSEPARATINGLINES']]
    CDLSEPARATINGLINES = CDLSEPARATINGLINES[CDLSEPARATINGLINES['CDLSEPARATINGLINES'] != 0]
    CDLSEPARATINGLINES = CDLSEPARATINGLINES[CDLSEPARATINGLINES['CDLSEPARATINGLINES'] > 0]
    
    liste = CDLSEPARATINGLINES["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSEPARATINGLINES)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSHOOTINGSTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSHOOTINGSTAR = tablo[['HISSE', 'CDLSHOOTINGSTAR']]
    CDLSHOOTINGSTAR = CDLSHOOTINGSTAR[CDLSHOOTINGSTAR['CDLSHOOTINGSTAR'] != 0]
    CDLSHOOTINGSTAR = CDLSHOOTINGSTAR[CDLSHOOTINGSTAR['CDLSHOOTINGSTAR'] > 0]
    
    liste = CDLSHOOTINGSTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSHOOTINGSTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSHORTLINE(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSHORTLINE = tablo[['HISSE', 'CDLSHORTLINE']]
    CDLSHORTLINE = CDLSHORTLINE[CDLSHORTLINE['CDLSHORTLINE'] != 0]
    CDLSHORTLINE = CDLSHORTLINE[CDLSHORTLINE['CDLSHORTLINE'] > 0]
    
    liste = CDLSHORTLINE["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSHORTLINE)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSPINNINGTOP(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSPINNINGTOP = tablo[['HISSE', 'CDLSPINNINGTOP']]
    CDLSPINNINGTOP = CDLSPINNINGTOP[CDLSPINNINGTOP['CDLSPINNINGTOP'] != 0]
    CDLSPINNINGTOP = CDLSPINNINGTOP[CDLSPINNINGTOP['CDLSPINNINGTOP'] > 0]
    
    liste = CDLSPINNINGTOP["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSPINNINGTOP)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSTALLEDPATTERN(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSTALLEDPATTERN = tablo[['HISSE', 'CDLSTALLEDPATTERN']]
    CDLSTALLEDPATTERN = CDLSTALLEDPATTERN[CDLSTALLEDPATTERN['CDLSTALLEDPATTERN'] != 0]
    CDLSTALLEDPATTERN = CDLSTALLEDPATTERN[CDLSTALLEDPATTERN['CDLSTALLEDPATTERN'] > 0]
    
    liste = CDLSTALLEDPATTERN["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSTALLEDPATTERN)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLSTICKSANDWICH(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLSTICKSANDWICH = tablo[['HISSE', 'CDLSTICKSANDWICH']]
    CDLSTICKSANDWICH = CDLSTICKSANDWICH[CDLSTICKSANDWICH['CDLSTICKSANDWICH'] != 0]
    CDLSTICKSANDWICH = CDLSTICKSANDWICH[CDLSTICKSANDWICH['CDLSTICKSANDWICH'] > 0]
    
    liste = CDLSTICKSANDWICH["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLSTICKSANDWICH)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLTAKURI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLTAKURI = tablo[['HISSE', 'CDLTAKURI']]
    CDLTAKURI = CDLTAKURI[CDLTAKURI['CDLTAKURI'] != 0]
    CDLTAKURI = CDLTAKURI[CDLTAKURI['CDLTAKURI'] > 0]
    
    liste = CDLTAKURI["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLTAKURI)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLTASUKIGAP(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLTASUKIGAP = tablo[['HISSE', 'CDLTASUKIGAP']]
    CDLTASUKIGAP = CDLTASUKIGAP[CDLTASUKIGAP['CDLTASUKIGAP'] != 0]
    CDLTASUKIGAP = CDLTASUKIGAP[CDLTASUKIGAP['CDLTASUKIGAP'] > 0]
    
    liste = CDLTASUKIGAP["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLTASUKIGAP)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLTHRUSTING(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLTHRUSTING = tablo[['HISSE', 'CDLTHRUSTING']]
    CDLTHRUSTING = CDLTHRUSTING[CDLTHRUSTING['CDLTHRUSTING'] != 0]
    CDLTHRUSTING = CDLTHRUSTING[CDLTHRUSTING['CDLTHRUSTING'] > 0]
    
    liste = CDLTHRUSTING["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLTHRUSTING)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLTRISTAR(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLTRISTAR = tablo[['HISSE', 'CDLTRISTAR']]
    CDLTRISTAR = CDLTRISTAR[CDLTRISTAR['CDLTRISTAR'] != 0]
    CDLTRISTAR = CDLTRISTAR[CDLTRISTAR['CDLTRISTAR'] > 0]
    
    liste = CDLTRISTAR["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLTRISTAR)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLUNIQUE3RIVER(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLUNIQUE3RIVER = tablo[['HISSE', 'CDLUNIQUE3RIVER']]
    CDLUNIQUE3RIVER = CDLUNIQUE3RIVER[CDLUNIQUE3RIVER['CDLUNIQUE3RIVER'] != 0]
    CDLUNIQUE3RIVER = CDLUNIQUE3RIVER[CDLUNIQUE3RIVER['CDLUNIQUE3RIVER'] > 0]
    
    liste = CDLUNIQUE3RIVER["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLUNIQUE3RIVER)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLUPSIDEGAP2CROWS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLUPSIDEGAP2CROWS = tablo[['HISSE', 'CDLUPSIDEGAP2CROWS']]
    CDLUPSIDEGAP2CROWS = CDLUPSIDEGAP2CROWS[CDLUPSIDEGAP2CROWS['CDLUPSIDEGAP2CROWS'] != 0]
    CDLUPSIDEGAP2CROWS = CDLUPSIDEGAP2CROWS[CDLUPSIDEGAP2CROWS['CDLUPSIDEGAP2CROWS'] > 0]
    
    liste = CDLUPSIDEGAP2CROWS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLUPSIDEGAP2CROWS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
def CDLXSIDEGAP3METHODS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bu formasyona sahip olan hisseler:")
    
    CDLXSIDEGAP3METHODS = tablo[['HISSE', 'CDLXSIDEGAP3METHODS']]
    CDLXSIDEGAP3METHODS = CDLXSIDEGAP3METHODS[CDLXSIDEGAP3METHODS['CDLXSIDEGAP3METHODS'] != 0]
    CDLXSIDEGAP3METHODS = CDLXSIDEGAP3METHODS[CDLXSIDEGAP3METHODS['CDLXSIDEGAP3METHODS'] > 0]
    
    liste = CDLXSIDEGAP3METHODS["HISSE"].to_list()
    
    slash = "/"
    i = 0
    for s in liste:
        s = s[:len(s)-3]
        liste[i] = slash+s
        i = i + 1
    print(CDLXSIDEGAP3METHODS)             
    context.bot.send_message(chat_id=update.effective_chat.id, text=liste)
    
    
 
    
liste_handler = CommandHandler("liste", liste)
start_handler = CommandHandler('start', start)


CDL3BLACKCROWS_handler = CommandHandler('CDL3BLACKCROWS', CDL3BLACKCROWS)
CDL2CROWS_handler = CommandHandler('CDL2CROWS', CDL2CROWS)
CDL3INSIDE_handler = CommandHandler('CDL3INSIDE', CDL3INSIDE)
CDL3LINESTRIKE_handler = CommandHandler('CDL3LINESTRIKE', CDL3LINESTRIKE)
CDL3OUTSIDE_handler = CommandHandler('CDL3OUTSIDE', CDL3OUTSIDE)
CDL3STARSINSOUTH_handler = CommandHandler('CDL3STARSINSOUTH', CDL3STARSINSOUTH)
CDL3WHITESOLDIERS_handler = CommandHandler('CDL3WHITESOLDIERS', CDL3WHITESOLDIERS)
CDLABANDONEDBABY_handler = CommandHandler('CDLABANDONEDBABY', CDLABANDONEDBABY)
CDLADVANCEBLOCK_handler = CommandHandler('CDLADVANCEBLOCK', CDLADVANCEBLOCK)
CDLBELTHOLD_handler = CommandHandler('CDLBELTHOLD', CDLBELTHOLD)
CDLBREAKAWAY_handler = CommandHandler('CDLBREAKAWAY', CDLBREAKAWAY)
CDLCLOSINGMARUBOZU_handler = CommandHandler('CDLCLOSINGMARUBOZU', CDLCLOSINGMARUBOZU)
CDLCONCEALBABYSWALL_handler = CommandHandler('CDLCONCEALBABYSWALL', CDLCONCEALBABYSWALL)
CDLCOUNTERATTACK_handler = CommandHandler('CDLCOUNTERATTACK', CDLCOUNTERATTACK)
CDLDARKCLOUDCOVER_handler = CommandHandler('CDLDARKCLOUDCOVER', CDLDARKCLOUDCOVER)
CDLDOJI_handler = CommandHandler('CDLDOJI', CDLDOJI)
CDLDOJISTAR_handler = CommandHandler('CDLDOJISTAR', CDLDOJISTAR)
CDLDRAGONFLYDOJI_handler = CommandHandler('CDLDRAGONFLYDOJI', CDLDRAGONFLYDOJI)
CDLENGULFING_handler = CommandHandler('CDLENGULFING', CDLENGULFING)
CDLEVENINGDOJISTAR_handler = CommandHandler('CDLEVENINGDOJISTAR', CDLEVENINGDOJISTAR)
CDLEVENINGSTAR_handler = CommandHandler('CDLEVENINGSTAR', CDLEVENINGSTAR)
CDLGAPSIDESIDEWHITE_handler = CommandHandler('CDLGAPSIDESIDEWHITE', CDLGAPSIDESIDEWHITE)
CDLGRAVESTONEDOJI_handler = CommandHandler('CDLGRAVESTONEDOJI', CDLGRAVESTONEDOJI)
CDLHAMMER_handler = CommandHandler('CDLHAMMER', CDLHAMMER)
CDLHANGINGMAN_handler = CommandHandler('CDLHANGINGMAN', CDLHANGINGMAN)
CDLHARAMI_handler = CommandHandler('CDLHARAMI', CDLHARAMI)
CDLHARAMICROSS_handler = CommandHandler('CDLHARAMICROSS', CDLHARAMICROSS)
CDLHIGHWAVE_handler = CommandHandler('CDLHIGHWAVE', CDLHIGHWAVE)
CDLHIKKAKE_handler = CommandHandler('CDLHIKKAKE', CDLHIKKAKE)
CDLHIKKAKEMOD_handler = CommandHandler('CDLHIKKAKEMOD', CDLHIKKAKEMOD)
CDLHOMINGPIGEON_handler = CommandHandler('CDLHOMINGPIGEON', CDLHOMINGPIGEON)
CDLIDENTICAL3CROWS_handler = CommandHandler('CDLIDENTICAL3CROWS', CDLIDENTICAL3CROWS)
CDLINNECK_handler = CommandHandler('CDLINNECK', CDLINNECK)
CDLINVERTEDHAMMER_handler = CommandHandler('CDLINVERTEDHAMMER', CDLINVERTEDHAMMER)
CDLKICKING_handler = CommandHandler('CDLKICKING', CDLKICKING)
CDLKICKINGBYLENGTH_handler = CommandHandler('CDLKICKINGBYLENGTH', CDLKICKINGBYLENGTH)
CDLLADDERBOTTOM_handler = CommandHandler('CDLLADDERBOTTOM', CDLLADDERBOTTOM)
CDLLONGLEGGEDDOJI_handler = CommandHandler('CDLLONGLEGGEDDOJI', CDLLONGLEGGEDDOJI)
CDLLONGLINE_handler = CommandHandler('CDLLONGLINE', CDLLONGLINE)
CDLMARUBOZU_handler = CommandHandler('CDLMARUBOZU', CDLMARUBOZU)
CDLMATCHINGLOW_handler = CommandHandler('CDLMATCHINGLOW', CDLMATCHINGLOW)
CDLMATHOLD_handler = CommandHandler('CDLMATHOLD', CDLMATHOLD)
CDLMORNINGDOJISTAR_handler = CommandHandler('CDLMORNINGDOJISTAR', CDLMORNINGDOJISTAR)
CDLMORNINGSTAR_handler = CommandHandler('CDLMORNINGSTAR', CDLMORNINGSTAR)
CDLONNECK_handler = CommandHandler('CDLONNECK', CDLONNECK)
CDLPIERCING_handler = CommandHandler('CDLPIERCING', CDLPIERCING)
CDLRICKSHAWMAN_handler = CommandHandler('CDLRICKSHAWMAN', CDLRICKSHAWMAN)
CDLRISEFALL3METHOD_handler = CommandHandler('CDLRISEFALL3METHODS', CDLRISEFALL3METHODS)
CDLSEPARATINGLINES_handler = CommandHandler('CDLSEPARATINGLINES', CDLSEPARATINGLINES)
CDLSHOOTINGSTAR_handler = CommandHandler('CDLSHOOTINGSTAR', CDLSHOOTINGSTAR)
CDLSHORTLINE_handler = CommandHandler('CDLSHORTLINE', CDLSHORTLINE)
CDLSPINNINGTOP_handler = CommandHandler('CDLSPINNINGTOP', CDLSPINNINGTOP)
CDLSTALLEDPATTERN_handler = CommandHandler('CDLSTALLEDPATTERN', CDLSTALLEDPATTERN)
CDLSTICKSANDWICH_handler = CommandHandler('CDLSTICKSANDWICH', CDLSTICKSANDWICH)
CDLTAKURI_handler = CommandHandler('CDLTAKURI', CDLTAKURI)
CDLTASUKIGAP_handler = CommandHandler('CDLTASUKIGAP', CDLTASUKIGAP)
CDLTHRUSTING_handler = CommandHandler('CDLTHRUSTING', CDLTHRUSTING)
CDLTRISTAR_handler = CommandHandler('CDLTRISTAR', CDLTRISTAR)
CDLUNIQUE3RIVER_handler = CommandHandler('CDLUNIQUE3RIVER', CDLUNIQUE3RIVER)
CDLUPSIDEGAP2CROWS_handler = CommandHandler('CDLUPSIDEGAP2CROWS', CDLUPSIDEGAP2CROWS)
CDLXSIDEGAP3METHODS_handler = CommandHandler('CDLXSIDEGAP3METHODS', CDLXSIDEGAP3METHODS)


dispatcher.add_handler(liste_handler)
dispatcher.add_handler(start_handler)

dispatcher.add_handler(CDL3BLACKCROWS_handler)
dispatcher.add_handler(CDL2CROWS_handler)
dispatcher.add_handler(CDL3INSIDE_handler)
dispatcher.add_handler(CDL3LINESTRIKE_handler)
dispatcher.add_handler(CDL3OUTSIDE_handler)
dispatcher.add_handler(CDL3STARSINSOUTH_handler)
dispatcher.add_handler(CDL3WHITESOLDIERS_handler)
dispatcher.add_handler(CDLABANDONEDBABY_handler)
dispatcher.add_handler(CDLADVANCEBLOCK_handler)
dispatcher.add_handler(CDLBELTHOLD_handler)
dispatcher.add_handler(CDLBREAKAWAY_handler)
dispatcher.add_handler(CDLCLOSINGMARUBOZU_handler)
dispatcher.add_handler(CDLCONCEALBABYSWALL_handler)
dispatcher.add_handler(CDLCOUNTERATTACK_handler)
dispatcher.add_handler(CDLDARKCLOUDCOVER_handler)
dispatcher.add_handler(CDLDOJI_handler)
dispatcher.add_handler(CDLDOJISTAR_handler)
dispatcher.add_handler(CDLDRAGONFLYDOJI_handler)
dispatcher.add_handler(CDLENGULFING_handler)
dispatcher.add_handler(CDLEVENINGDOJISTAR_handler)
dispatcher.add_handler(CDLEVENINGSTAR_handler)
dispatcher.add_handler(CDLGAPSIDESIDEWHITE_handler)
dispatcher.add_handler(CDLGRAVESTONEDOJI_handler)
dispatcher.add_handler(CDLHAMMER_handler)
dispatcher.add_handler(CDLHANGINGMAN_handler)
dispatcher.add_handler(CDLHARAMI_handler)
dispatcher.add_handler(CDLHARAMICROSS_handler)
dispatcher.add_handler(CDLHIGHWAVE_handler)
dispatcher.add_handler(CDLHIKKAKE_handler)
dispatcher.add_handler(CDLHIKKAKEMOD_handler)
dispatcher.add_handler(CDLHOMINGPIGEON_handler)
dispatcher.add_handler(CDLIDENTICAL3CROWS_handler)
dispatcher.add_handler(CDLINNECK_handler)
dispatcher.add_handler(CDLINVERTEDHAMMER_handler)
dispatcher.add_handler(CDLKICKING_handler)
dispatcher.add_handler(CDLKICKINGBYLENGTH_handler)
dispatcher.add_handler(CDLLADDERBOTTOM_handler)
dispatcher.add_handler(CDLLONGLEGGEDDOJI_handler)
dispatcher.add_handler(CDLLONGLINE_handler)
dispatcher.add_handler(CDLMARUBOZU_handler)
dispatcher.add_handler(CDLMATCHINGLOW_handler)
dispatcher.add_handler(CDLMATHOLD_handler)
dispatcher.add_handler(CDLMORNINGDOJISTAR_handler)
dispatcher.add_handler(CDLMORNINGSTAR_handler)
dispatcher.add_handler(CDLONNECK_handler)
dispatcher.add_handler(CDLPIERCING_handler)
dispatcher.add_handler(CDLRICKSHAWMAN_handler)
dispatcher.add_handler(CDLRISEFALL3METHOD_handler)
dispatcher.add_handler(CDLSEPARATINGLINES_handler)
dispatcher.add_handler(CDLSHOOTINGSTAR_handler)
dispatcher.add_handler(CDLSHORTLINE_handler)
dispatcher.add_handler(CDLSPINNINGTOP_handler)
dispatcher.add_handler(CDLSTALLEDPATTERN_handler)
dispatcher.add_handler(CDLSTICKSANDWICH_handler)
dispatcher.add_handler(CDLTAKURI_handler)
dispatcher.add_handler(CDLTASUKIGAP_handler)
dispatcher.add_handler(CDLTHRUSTING_handler)
dispatcher.add_handler(CDLTRISTAR_handler)
dispatcher.add_handler(CDLUNIQUE3RIVER_handler)
dispatcher.add_handler(CDLUPSIDEGAP2CROWS_handler)
dispatcher.add_handler(CDLXSIDEGAP3METHODS_handler)

updater.start_polling()

