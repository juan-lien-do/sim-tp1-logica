import generacionNumerosAleatorios
#PRUEBAS
rnd = [0.49,0.81,0.99,0.67,0.00]
x = []
for i in rnd:
    v = generacionNumerosAleatorios.numeroUniforme(80,95,i)
    x.append(v)
print(x)
rnd2 = [0.32,0.65,0.06,0.50,0.89]
x2 = []
x3 = []
for i in rnd2:
    a = generacionNumerosAleatorios.numeroExponencial(4,i)
    x2.append(a)
    b = generacionNumerosAleatorios.numeroExponencial(float(24/60),i)
    x3.append(b)
print(x2)
print(x3)
valores = [0.48, 0.82, 0.69, 0.67, 0.01, 0.64, 0.46, 0.16, 0.50, 0.21, 0.34, 0.75]
x4 = []
for i in range(len(valores)):
    for j in range(len(valores)):
        if i == j:
            pass
        else:
            n1,n2 = generacionNumerosAleatorios.numerosNormalBoxMuller(11,0.3,valores[i],valores[j])
            x4.append(n1)
            x4.append(n2)
#print(x4)
x5 = generacionNumerosAleatorios.numeroNormalConvolucion(11,0.3,12,valores)
print(x5)
#rnd = [0.15, 0.22, 0.41, 0.65, 0.84, 0.81, 0.62, 0.45, 0.32, 0.07, 0.11, 0.29, 0.58, 0.73, 0.93, 0.97, 0.79, 0.55, 0.35, 0.09, 0.99, 0.51, 0.35, 0.02, 0.19, 0.24, 0.98, 0.10, 0.31, 0.17]
#obs,esp,c,x,x_2 = testPruebaChiCuadrado(rnd,0.05)
#print(obs)
#print(esp)
#print(c)
#print(x)
#print(x_2)    
#observados,esperados,prob_obs,prob_esp,apfo,apfe,x,k_s_tabla = generacionNumerosAleatorios.testPruebaKS(rnd,0.05)
#print(observados)
#print(esperados)
#print(prob_obs)
#print(prob_esp)
#print(apfo)
#print(apfe)
#print(x)
#print(k_s_tabla)
