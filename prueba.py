import generacionNumerosAleatorios
#PRUEBAS
# rnd = [0.49,0.81,0.99,0.67,0.00]
# x = []
# for i in rnd:
#     v = generacionNumerosAleatorios.numeroUniforme(80,95,i)
#     x.append(v)
# print(x)
# rnd2 = [0.32,0.65,0.06,0.50,0.89]
# x2 = []
# x3 = []
# for i in rnd2:
#     a = generacionNumerosAleatorios.numeroExponencial(4,i)
#     x2.append(a)
#     b = generacionNumerosAleatorios.numeroExponencial(float(24/60),i)
#     x3.append(b)
# print(x2)
# print(x3)
# valores = [0.48, 0.82, 0.69, 0.67, 0.01, 0.64, 0.46, 0.16, 0.50, 0.21, 0.34, 0.75]
# x4 = []
# for i in range(len(valores)):
#     for j in range(len(valores)):
#         if i == j:
#             pass
#         else:
#             n1,n2 = generacionNumerosAleatorios.numerosNormalBoxMuller(11,0.3,valores[i],valores[j])
#             x4.append(n1)
#             x4.append(n2)
# #print(x4)
# x5 = generacionNumerosAleatorios.numeroNormalConvolucion(11,0.3,12,valores)
# print(x5)
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
#rnd = [0.36,0.39,0.69,0.59,0.78,0.23,0.98,0.31]
valores = [0.15, 0.22, 0.41, 0.65, 0.84, 0.81, 0.62, 0.45, 0.32, 0.07, 
          0.11, 0.29, 0.58, 0.73, 0.93, 0.97, 0.79, 0.55, 0.35, 0.09, 
0.99, 0.51, 0.35, 0.02, 0.19, 0.24, 0.98, 0.10, 0.31, 0.17]
datos = [
    1.56, 2.21, 3.15, 4.61, 4.18, 5.20, 4.87, 7.71, 5.15, 6.76,
    7.28, 4.23, 3.54, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78,
    2.46, 3.97, 6.09, 6.19, 4.20, 3.48, 5.83, 6.36, 5.90, 5.43,
    3.87, 2.21, 3.74, 4.61, 4.18, 5.20, 4.28, 7.71, 5.15, 6.76,
   7.28, 4.23, 3.21, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78
]
#numeros = [
#    2.21, 3.15, 4.61, 4.18, 5.20, 4.87, 7.71, 5.15, 6.76,
#    7.28, 4.23,1.56, 3.54, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78,
#    2.46, 3.97, 6.09, 6.19, 4.20, 3.48, 5.83, 6.36, 5.90, 5.43,
#    3.87, 2.21, 3.74, 4.61, 4.18, 5.20, 4.28, 7.71, 5.15, 6.76,
#    7.28, 4.23, 3.21, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78
#]
#values = [
#    0.10, 0.25, 1.53, 1.83, 3.50, 4.14, 5.65, 6.96, 3.04, 4.22, 1.20, 5.24, 4.75, 3.96,
#    2.21, 3.15, 2.53, 1.16, 0.32, 0.90, 0.87, 1.34, 1.87, 2.91, 0.71, 1.69, 0.69, 0.55,
#    0.43, 0.26, 0.12, 0.24, 1.52, 2.31, 3.45, 4.12, 4.75, 3.25, 3.99, 8.31, 1.21, 5.28,
#    4.79, 3.61, 2.18, 3.19, 2.19, 1.18, 0.33, 0.94
#]
prueba_uniforme  = [
    0.15, 0.22, 0.41, 0.65, 0.84, 0.81, 0.62, 0.45, 0.32, 0.07,
    0.11, 0.29, 0.58, 0.73, 0.93, 0.97, 0.79, 0.55, 0.35, 0.09,
    0.99, 0.51, 0.35, 0.02, 0.19, 0.24, 0.98, 0.10, 0.31, 0.17
]
prueba_exponencial = [
    0.10, 0.25, 1.53, 1.83, 3.50, 4.14, 5.65, 6.96, 3.04, 4.22,
    1.20, 5.24, 4.75, 3.96, 2.21, 3.15, 2.53, 1.16, 0.32, 0.90,
    0.87, 1.34, 1.87, 2.91, 0.71, 1.69, 0.69, 0.55, 0.43, 0.26,
    0.12, 0.24, 1.52, 2.31, 3.45, 4.12, 4.75, 3.25, 3.99, 8.31,
    1.21, 5.28, 4.79, 3.61, 2.18, 3.19, 2.19, 1.18, 0.33, 0.94
]
prueba_normal = [
    1.56, 2.21, 3.15, 4.61, 4.18, 5.20, 4.87, 7.71, 5.15, 6.76,
    7.28, 4.23, 3.54, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78,
    2.46, 3.97, 6.09, 6.19, 4.20, 3.48, 5.83, 6.36, 5.90, 5.43,
    3.87, 2.21, 3.74, 4.61, 4.18, 5.20, 4.28, 7.71, 5.15, 6.76,
    7.28, 4.23, 3.21, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78
]


prueba_poisson = [
    14, 7, 13, 16, 16, 13, 14, 17, 15, 16,
    13, 15, 10, 15, 16, 14, 12, 17, 14, 12,
    13, 20, 8, 17, 19, 11, 12, 17, 9, 18,
    20, 10, 18, 15, 13, 16, 24, 18, 16, 18,
    12, 14, 20, 15, 10, 13, 21, 23, 15, 18
]






observados,esperados,chi,x_2_calc,x_2_tabla,limites = generacionNumerosAleatorios.testPruebaChiCuadrado(prueba_normal,0.05,"Normal")
print("Observados:", observados)
print("Esperados:", esperados)
print("C:", chi)
print("X^2 Calculado:", x_2_calc)
print("X^2 Tabla:", x_2_tabla)
print(limites)
observados,esperados,prob_obs,prob_esp,apfo,apfe,dif,maximo,x,k_s_tabla,limites = generacionNumerosAleatorios.testPruebaKS(prueba_normal,0.05,"Normal")
print("Observados:", observados)
print("Esperados:", esperados)
print("Probabilidad Observada:", prob_obs)
print("Probabilidad Esperada:", prob_esp)
print("Acumulada FO:", apfo)
print("Acumulada FE:", apfe)
print("Diferencia", dif)
print("Maximo",maximo)
print("D Calculado:", x)
print("D Tabla:", k_s_tabla)
print("Limites",limites)