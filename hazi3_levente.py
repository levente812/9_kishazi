#!/usr/bin/env python
# coding: utf-8

# 3. Kisházi - Pandas alapok
# 
# Írj egy olyan függvényt, amely bemenetként kap egy elérési útvonalat, beolvassa az itt található file-t egy DataFrame-be, elvégzi rajta a szükséges transzformációkat és visszaad egy listát, ami tartalmazza az eredményként kapott DataFrame indexeit.
# 
# Az adat amivel dolgozni kell a feladat során megegyezik az órákon is használt ingatlanos adathalmazzal. Ez megtalálható az ADA2018/data mappában.
# 
# Részletes leírás:
# 
# Számoljuk ki azoknak a lakásoknak az átlagos négyzetméterárát, amelyek az I. kerületben vannak és nem 2 szobásak
# Határozzuk meg ennek segítségével azokat az I. kerületi 2 szobás lakásokat, amelyeknek négyzetméterára ennél nagyobb
# Sorrendezzük az így kapott lakásokat négyzetméterár szerint növekvő sorrendbe
# Adjuk vissza egy listában az így kapott DataFrame első 5 elemének indexét (fontos, hogy megtartsuk az eredeti indexelést valamilyen módon)
#  
# 
# Ellenőrző példát most nem adunk ki a feladathoz.



import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


import pandas as pd

def olyan(eleresiut):   # 'dataset_lakasp.csv'
    
    df = pd.read_csv(eleresiut)
    df['index_eredeti'] = df.index.values
    
    df_filter_1 = df['city'] == 'Budapest I.'     # első kerületi
    df2 = df[df_filter_1]
    df2['negyzetmeter_ar'] = df2['price_created_at'] * 1000000 / df2['property_area']

    df_filter_2 = df2['room_cnt'] != 2.0           # nem kétszobás
    df_filter_3 = df2['room_cnt'] == 2.0           # kétszobás
    
    
    df3 = df2[df_filter_2]                        # nem kétszobás
    df4 = df2[df_filter_3]
    #átlagos négyzetméterár:
    atlagar = df3['negyzetmeter_ar'].mean()
    #print("Átlagár az I.kerületben, nem kétszobás:", atlagar)
    df_filter_4 = df4['negyzetmeter_ar'] > df3['negyzetmeter_ar'].mean()
    df5 = df4[df_filter_4]
    #[74833, 69615, 56585, 57993, 35325]
    
    return list(df5.sort_values('negyzetmeter_ar', ascending=True).reset_index().loc[0:4, 'index'] )




#akkor fog lefutni ha ez a foprogi
if __name__ == '__main__':
    print("Az elso 5 indexe:")
    print(olyan('dataset_lakasp.csv'))
	




