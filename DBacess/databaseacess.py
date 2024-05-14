import mysql.connector
import statistics
import numpy as np
from sklearn.linear_model import LinearRegression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

con = mysql.connector.connect(host='localhost', database='dadoshospitalares', user='root', password='')
cursor = con.cursor()

meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
dados = []

for mes in meses:
    cursor.execute("SELECT nascidosVivos FROM {};".format(mes))
    dados_mes = cursor.fetchall()[0][0] 
    dados.append(dados_mes)

X = np.array(dados[:-1]).reshape(-1, 1) 
y = np.array(dados[1:]).reshape(-1, 1) 

model = LinearRegression()
model.fit(X, y)

previsao_proximo_ano = model.predict(np.array([dados[-1]]).reshape(-1, 1))


model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(1,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
model.fit(X, y, epochs=100, batch_size=1, verbose=1)

# Fazer a previsão para dezembro do próximo ano
previsao_proximo_ano = model.predict(np.array([dados[-1]]).reshape(-1, 1))
print("Previsão de nascidos vivos para dezembro de 2024:", previsao_proximo_ano[0][0])

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
