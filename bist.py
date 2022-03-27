
from numpy import append
import yfinance as yf
import pandas as pd
import talib
import xlsxwriter


candle_names = talib.get_function_groups()['Pattern Recognition']

df = pd.read_excel (r"C:\Users\umbra\Desktop\yeni çalışma\tumhisse.xlsx")

tickers = df["HISSE"]

tickers_list = tickers.to_list()
tum_hisse = []

for a in tickers_list:
    tum_hisse.append(a[0:-38]+".IS")
    

sablon_tablo = pd.DataFrame(columns= candle_names)

data = yf.download(tickers = tum_hisse, period = "20d", interval = "1d", group_by = 'ticker', auto_adjust = True, prepost = True, threads = True ,proxy = None )

try:
    
    for hisse in tum_hisse:

        skor1 = talib.CDL2CROWS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor2 = talib.CDL3BLACKCROWS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor3 = talib.CDL3INSIDE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor4 = talib.CDL3LINESTRIKE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor5 = talib.CDL3OUTSIDE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor6 = talib.CDL3STARSINSOUTH(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor7 = talib.CDL3WHITESOLDIERS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor8 = talib.CDLABANDONEDBABY(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor9 = talib.CDLADVANCEBLOCK(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])    
        skor10 = talib.CDLBELTHOLD(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor11 = talib.CDLBREAKAWAY(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor12 = talib.CDLCLOSINGMARUBOZU(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor13 = talib.CDLCONCEALBABYSWALL(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor14 = talib.CDLCOUNTERATTACK(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor15 = talib.CDLDARKCLOUDCOVER(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])    
        skor16 = talib.CDLDOJI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor17 = talib.CDLDOJISTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor18 = talib.CDLDRAGONFLYDOJI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor19 = talib.CDLENGULFING(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor20 = talib.CDLEVENINGDOJISTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor21 = talib.CDLEVENINGSTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor22 = talib.CDLGAPSIDESIDEWHITE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor23 = talib.CDLGRAVESTONEDOJI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor24 = talib.CDLHAMMER(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor25 = talib.CDLHANGINGMAN(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor26 = talib.CDLHARAMI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor27 = talib.CDLHARAMICROSS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor28 = talib.CDLHIGHWAVE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor29 = talib.CDLHIKKAKE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor30 = talib.CDLHIKKAKEMOD(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor31 = talib.CDLHOMINGPIGEON(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor32 = talib.CDLIDENTICAL3CROWS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor33 = talib.CDLINNECK(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor34 = talib.CDLINVERTEDHAMMER(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor35 = talib.CDLKICKING(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor36 = talib.CDLKICKINGBYLENGTH(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor37 = talib.CDLLADDERBOTTOM(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor38 = talib.CDLLONGLEGGEDDOJI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor39 = talib.CDLLONGLINE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor40 = talib.CDLMARUBOZU(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor41 = talib.CDLMATCHINGLOW(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor42 = talib.CDLMATHOLD(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor43 = talib.CDLMORNINGDOJISTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor44 = talib.CDLMORNINGSTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor45 = talib.CDLONNECK(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor46 = talib.CDLPIERCING(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor47 = talib.CDLRICKSHAWMAN(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor48 = talib.CDLRISEFALL3METHODS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor49 = talib.CDLSEPARATINGLINES(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor50 = talib.CDLSHOOTINGSTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor51 = talib.CDLSHORTLINE(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor52 = talib.CDLSPINNINGTOP(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor53 = talib.CDLSTALLEDPATTERN(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor54 = talib.CDLSTICKSANDWICH(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor55 = talib.CDLTAKURI(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor56 = talib.CDLTASUKIGAP(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor57 = talib.CDLTHRUSTING(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor58 = talib.CDLTRISTAR(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor59 = talib.CDLUNIQUE3RIVER(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor60 = talib.CDLUPSIDEGAP2CROWS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])
        skor61 = talib.CDLXSIDEGAP3METHODS(data[hisse]['Open'], data[hisse]['High'], data[hisse]['Low'], data[hisse]['Close'])

        tablo = pd.DataFrame({'CDL2CROWS': skor1[-1],
                                'CDL3BLACKCROWS': skor2[-1], 
                                'CDL3INSIDE': skor3[-1],
                                'CDL3LINESTRIKE': skor4[-1],
                                'CDL3OUTSIDE': skor5[-1],
                                'CDL3STARSINSOUTH': skor6[-1],
                                'CDL3WHITESOLDIERS': skor7[-1],
                                'CDLABANDONEDBABY': skor8[-1],
                                'CDLADVANCEBLOCK': skor9[-1],
                                'CDLBELTHOLD': skor10[-1],
                                'CDLBREAKAWAY': skor11[-1],
                                'CDLCLOSINGMARUBOZU': skor12[-1],
                                'CDLCONCEALBABYSWALL': skor13[-1],
                                'CDLCOUNTERATTACK': skor14[-1],
                                'CDLDARKCLOUDCOVER': skor15[-1],
                                'CDLDOJI': skor16[-1],
                                'CDLDOJISTAR': skor17[-1],
                                'CDLDRAGONFLYDOJI': skor18[-1],
                                'CDLENGULFING': skor19[-1],
                                'CDLEVENINGDOJISTAR': skor20[-1],
                                'CDLEVENINGSTAR': skor21[-1],
                                'CDLGAPSIDESIDEWHITE': skor22[-1],
                                'CDLGRAVESTONEDOJI': skor23[-1],
                                'CDLHAMMER': skor24[-1],
                                'CDLHANGINGMAN': skor25[-1],
                                'CDLHARAMI': skor26[-1],
                                'CDLHARAMICROSS': skor27[-1],
                                'CDLHIGHWAVE': skor28[-1],
                                'CDLHIKKAKE': skor29[-1],
                                'CDLHIKKAKEMOD': skor30[-1],
                                'CDLHOMINGPIGEON': skor31[-1],
                                'CDLIDENTICAL3CROWS': skor32[-1],
                                'CDLINNECK': skor33[-1],
                                'CDLINVERTEDHAMMER': skor34[-1],
                                'CDLKICKING': skor35[-1],
                                'CDLKICKINGBYLENGTH': skor36[-1],
                                'CDLLADDERBOTTOM': skor37[-1],
                                'CDLLONGLEGGEDDOJI': skor38[-1],
                                'CDLLONGLINE': skor39[-1],
                                'CDLMARUBOZU': skor40[-1],
                                'CDLMATCHINGLOW': skor41[-1],
                                'CDLMATHOLD': skor42[-1],
                                'CDLMORNINGDOJISTAR': skor43[-1],
                                'CDLMORNINGSTAR': skor44[-1],
                                'CDLONNECK': skor45[-1],
                                'CDLPIERCING': skor46[-1],
                                'CDLRICKSHAWMAN': skor47[-1],
                                'CDLRISEFALL3METHODS': skor48[-1],
                                'CDLSEPARATINGLINES': skor49[-1],
                                'CDLSHOOTINGSTAR': skor50[-1],
                                'CDLSHORTLINE': skor51[-1],
                                'CDLSPINNINGTOP': skor52[-1],
                                'CDLSTALLEDPATTERN': skor53[-1],
                                'CDLSTICKSANDWICH': skor54[-1],
                                'CDLTAKURI': skor55[-1],
                                'CDLTASUKIGAP': skor56[-1],
                                'CDLTHRUSTING': skor57[-1],
                                'CDLTRISTAR': skor58[-1],
                                'CDLUNIQUE3RIVER': skor59[-1],
                                'CDLUPSIDEGAP2CROWS': skor60[-1],
                                'CDLXSIDEGAP3METHODS': skor61[-1]}, index=[hisse])
        a = tablo.iloc[0].to_frame().T

        sablon_tablo = sablon_tablo.append(a)
        print(hisse)
 
except:
    
    print("Bir hata oluştu!")
    
    pass
       
print(sablon_tablo)

sablon_tablo.to_excel('output1.xlsx', engine='xlsxwriter')
