from tracemalloc import Statistic
from turtle import mode
import mysql.connector
import statistics


con = mysql.connector.connect(host='localhost',database='dadoshospitalares',user='root',password='')

cursor = con.cursor()
cursor.execute("select * from janeiro;")
Janeiro = cursor.fetchall();
cursor.execute("select * from fevereiro;")
Fevereiro = cursor.fetchall();
cursor.execute("select * from marco;")
Marco = cursor.fetchall();
cursor.execute("select * from abril;")
Abril = cursor.fetchall();
cursor.execute("select * from maio;")
Maio = cursor.fetchall();
cursor.execute("select * from junho;")
Junho = cursor.fetchall();
cursor.execute("select * from julho;")
Julho = cursor.fetchall();
cursor.execute("select * from agosto;")
Agosto = cursor.fetchall();
cursor.execute("select * from setembro;")
Setembro = cursor.fetchall();
cursor.execute("select * from outubro;")
Outubro = cursor.fetchall();
cursor.execute("select * from novembro;")
Novembro = cursor.fetchall();
cursor.execute("select * from dezembro;")
Dezembro = cursor.fetchall();


dadosn = ["nascidos vivos","nascidos masculinos","nascidos femininos","nascidos gemeos","nascidos de cesaria","nascidos de vaginal","boa vitalidade","RN_baixo peso","RN_peso adequado","RN_pre_maturo"]
for  i in range (1,10) :
    print(Janeiro[0][i],Fevereiro[0][i],Marco[0][i],Abril[0][i],Maio[0][i],Junho[0][i],Julho[0][i],Agosto[0][i],Setembro[0][i],Outubro[0][i],Novembro[0][i],Dezembro[0][i])
    dados = [Janeiro[0][i],Fevereiro[0][i],Marco[0][i],Abril[0][i],Maio[0][i],Junho[0][i],Julho[0][i],Agosto[0][i],Setembro[0][i],Outubro[0][i],Novembro[0][i],Dezembro[0][i]]
    mediaInteira = statistics.mean(dados)
    mediaInteira = round(mediaInteira,2)
    print("Media de ",dadosn[i-1]," ao longo dos 12 meses: ",mediaInteira,"\n")
    mediana_total = statistics.median(dados)
    print("Mediana de ",dadosn[i-1]," ao longo dos 12 meses: ", mediana_total,"\n")
    moda = statistics.mode(dados)
    print ("Moda de ",dadosn[i-1]," ao longo dos 12 meses: ",moda,"\n")
    media_harmonica = statistics.harmonic_mean(dados)
    media_harmonica = round(media_harmonica,2)
    print ("Media harmonica de ",dadosn[i-1]," ao longo dos 12 meses: ",media_harmonica,"\n")
    desvio_padrao = statistics.pstdev(dados)
    desvio_padrao = round(desvio_padrao,3)
    print ("Desvio padrao dos ",dadosn[i-1]," ao longo dos 12 meses: ",desvio_padrao,"\n")
    variancia = statistics.pvariance(dados)
    variancia = round(variancia,2)
    print ("Variancia dos ",dadosn[i-1]," ao longo dos 12 meses: ",variancia,"\n")

cursor.close()
con.close()