#IMPORTACION DE LIBRERIAS
import math as m
import random as r
from fractions import Fraction
from scipy.stats import chi2,ksone,kstwo
from itertools import accumulate
import logging
from decimal import Decimal, ROUND_HALF_UP

#DEPURACION
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#GENERACION DE VARIABLES CON DISTRIBUCION UNIFORME
def numeroUniforme(a, b, rnd=None):
    if b <= a:
        raise ValueError("El valor de b debe ser mayor que a")
    
    if rnd is None:
        rnd = r.random() 
    
    if not (0 <= rnd <= 1):
        raise ValueError("El valor de RND debe estar entre 0 y 1")
    
    return round((a + (b - a) * rnd),4)
    #PREGUNTAR EL REDONDEO A 4 DIGITOS
#GENERACION DE VARIABLES CON DISTRIBUCION EXPONENCIAL NEGATIVA
def numeroExponencial(param, rnd=None):
    if param == 0:
        raise ValueError("El parametro no puede ser cero")

    if rnd is None:
        rnd = r.random()

    if not (0 <= rnd <= 1):
        raise ValueError("El valor de RND debe estar entre 0 y 1")

    if param >= 1:
        return round((-param * m.log(1 - rnd)),4)
    elif param > 0 and param < 1:  
        return round((-1 / param) * m.log(1 - rnd),4)
    else:
        raise ValueError("El valor debe ser un numero positivo")
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR BOX-MÜLLER
def numerosNormalBoxMuller(media, des, rnd1=None, rnd2=None):

    if des <= 0:
        raise ValueError("La desviacion estandar no puede ser cero o negativa")
    

    if rnd1 is None:
        rnd1 = r.random()
    if rnd2 is None:
        rnd2 = r.random()



    if not (0 <= rnd1 <= 1):
        raise ValueError("El valor de RND1 debe estar entre 0 y 1")
    if not (0 <= rnd2 <= 1):
        raise ValueError("El valor de RND2 debe estar entre 0 y 1")

    z1 = m.sqrt(-2 * m.log(rnd1)) * m.cos(2 * m.pi * rnd2)
    z2 = m.sqrt(-2 * m.log(rnd1)) * m.sin(2 * m.pi * rnd2)

    n1 = round((z1 * des + media),4)
    n2 = round((z2 * des + media),4)

    return [n1, n2]
#GENERACION DE VARIABLES CON DISTRIBUCION NORMAL POR CONVOLUCION
def numeroNormalConvolucion(media, des,n=None,rnd=None):
    if des <= 0:
        raise ValueError("La desviación estándar no puede ser cero o negativa")
    
    if rnd is None:
        if n is None or n <= 0:
            raise ValueError("El valor de n debe ser un entero positivo")
        suma = sum(r.random() for _ in range(n))
    elif isinstance(rnd, list):
        n = len(rnd)
        suma = sum(rnd)
    else:
        raise ValueError("El valor de rnd debe ser una lista de números aleatorios")
    
    z = (suma - n / 2) * des + media
    return round(z,4)
#GENERACION DE VARIABLES CON DISTRIBUCION DE POISSON
def numeroPoisson(lambd):
    if lambd <= 0:
        raise ValueError("El valor de lambda debe ser mayor que cero")
    p = 1
    x = -1
    A = m.exp(-lambd)
    while p >= A:
        rnd = r.random()
        p = p * rnd
        x += 1
    return x
#GENERACION DE VARIABLES CON EL METODO DE CONGRUENCIA LINEAL
def numeroCongruenciaLineal(seed,k,c,g):
    if g < 0:
        raise ValueError("El valor de g debe ser positivo.")
    elif k < 0:
        raise ValueError("El valor de k debe ser positivo.")
    mod = 2**g
    if m.gcd(c,mod) != 1:
        raise ValueError("Los valores de c y m deben ser relativamente primos")
    N = mod
    a = 1+4*k
    rnd = []
    x = []
    for i in range(N):
        if i==0:
            b = a*seed + c
            x_i = round((b % mod),4)
            x.append(x_i)
        else:
            r = round((x[i-1] / (mod-1)),4)
            rnd.append(r)
            b = a*x[i-1] + c
            x_i = round((b % mod),4)
            x.append(x_i)
    v = round((x[N -1] / (mod - 1)),4)
    rnd.append(v)
    return rnd,x
#GENERACION DE VARIABLES CON EL METODO CONGRUENCIAL MULTIPLICATIVO
def numeroCongruencialMultiplicativo(seed,k,g):
    if seed % 2 == 0:
        raise ValueError("La semilla debe ser impar")
    elif k<0 and type(k) != int:
        raise ValueError("EL valor de k debe ser un entero positivo")
    elif g < 0 and type(g) != int:
        raise ValueError("El numero g debe ser un entero positivo")
    mod = 2**g
    a = 3 + 8*k
    N = 2**(g-2)
    rnd = []
    x = []
    for i in range(N):
        if i == 0:
            b = a * seed
            x_i = round((b % mod),4)
            x.append(x_i)
        else:
            y = round((x[i-1] / (mod - 1)),4)
            rnd.append(y)
            b = a * x[i-1]
            x_i = round((b % mod),4)
            x.append(x_i)
    z = round((x[N-1] / (mod - 1)),4)
    rnd.append(z)
    return rnd,x
#FUNCION COMPLEMENTARIA
def agrupar_intervalos(tabla):
    n = len(tabla[0])
    contador = 0
    fe = 0

    # Calcular cuántos intervalos agrupados habrá
    for i in range(n):
        fe += tabla[3][i]
        if fe >= 5:
            contador += 1
            fe = 0

    fe = 0
    fo = 0
    li = tabla[0][0]  # Límite inferior del primer intervalo

    contador = contador if contador > 0 else 1
    tabla_agrupada = [[0.0 for _ in range(contador)] for _ in range(5)]

    contador = 0

    # Agrupar intervalos
    for i in range(n):
        fo += tabla[2][i]  # Frecuencia observada
        fe += tabla[3][i]  # Frecuencia esperada
        if fe >= 5:
            tabla_agrupada[0][contador] = li
            tabla_agrupada[1][contador] = tabla[1][i]  # Límite superior
            tabla_agrupada[2][contador] = fo
            tabla_agrupada[3][contador] = fe
            tabla_agrupada[4][contador] = (fo - fe) ** 2 / fe
            fe = 0
            fo = 0
            contador += 1
            li = tabla[1][i]  # El nuevo límite inferior será el anterior superior

    # En caso de que haya un grupo sin cerrar
    if fe > 0 or fo > 0:
        ultimo_indice = len(tabla_agrupada[0]) - 1
        tabla_agrupada[1][ultimo_indice] = tabla[1][n - 1]
        tabla_agrupada[2][ultimo_indice] += fo
        tabla_agrupada[3][ultimo_indice] += fe
        Fo = tabla_agrupada[2][ultimo_indice]
        Fe = tabla_agrupada[3][ultimo_indice]
        tabla_agrupada[4][ultimo_indice] = (Fo - Fe) ** 2 / Fe

    return tabla_agrupada
def agrupar_intervalos_poisson(tabla):
    # Primera pasada: contar cuántos grupos habrá
    n = len(tabla[0])
    contador = 0
    fe = 0

    for i in range(n):
        fe += tabla[2][i]
        if fe >= 5:
            contador += 1
            fe = 0

    contador = max(contador, 1)
    tabla_agrupada = [[0 for _ in range(contador)] for _ in range(4)]  # x, FO, FE, chi^2

    fe = 0
    fo = 0
    min_x = tabla[0][0]
    grupo_idx = 0

    for i in range(n):
        fo += tabla[1][i]
        fe += tabla[2][i]
        if fe >= 5:
            nombre_grupo = f"{min_x}–{tabla[0][i]}" if min_x != tabla[0][i] else str(min_x)
            tabla_agrupada[0][grupo_idx] = nombre_grupo
            tabla_agrupada[1][grupo_idx] = fo
            tabla_agrupada[2][grupo_idx] = fe
            tabla_agrupada[3][grupo_idx] = (fo - fe) ** 2 / fe if fe > 0 else 0
            grupo_idx += 1
            fe = 0
            fo = 0
            if i + 1 < n:
                min_x = tabla[0][i + 1]

    # En caso de que quede un grupo sin cerrar (por ejemplo, si el último grupo tiene FE < 5)
    if fe > 0 or fo > 0:
        ultimo = grupo_idx - 1 if grupo_idx > 0 else 0
        nombre_grupo = f"{tabla_agrupada[0][ultimo].split('–')[0]}–{tabla[0][-1]}"
        tabla_agrupada[0][ultimo] = nombre_grupo
        tabla_agrupada[1][ultimo] += fo
        tabla_agrupada[2][ultimo] += fe
        Fo = tabla_agrupada[1][ultimo]
        Fe = tabla_agrupada[2][ultimo]
        tabla_agrupada[3][ultimo] = (Fo - Fe) ** 2 / Fe if Fe > 0 else 0

    return tabla_agrupada



def testPruebaChiCuadrado(numeros, a, dist, media=None, varianza=None, lamb=None, li=None, ls=None, x=None):
    import math as m
    from scipy.stats import chi2
    from decimal import Decimal, ROUND_HALF_UP

    def redondear(valor, decimales):
        return float(Decimal(valor).quantize(Decimal('1.' + '0' * decimales), rounding=ROUND_HALF_UP))

    def agrupar_intervalos(tabla):
        li, ls, fo, fe = tabla
        new_li, new_ls, new_fo, new_fe = [], [], [], []

        temp_fo, temp_fe = 0, 0
        current_li = li[0]

        for i in range(len(fe)):
            temp_fo += fo[i]
            temp_fe += fe[i]

            if temp_fe >= 5:
                new_li.append(current_li)
                new_ls.append(ls[i])
                new_fo.append(temp_fo)
                new_fe.append(temp_fe)
                if i + 1 < len(li):
                    current_li = li[i + 1]
                temp_fo, temp_fe = 0, 0

        if temp_fe > 0:
            if new_fe:
                new_fe[-1] += temp_fe
                new_fo[-1] += temp_fo
                new_ls[-1] = ls[-1]
            else:
                new_li.append(current_li)
                new_ls.append(ls[-1])
                new_fo.append(temp_fo)
                new_fe.append(temp_fe)

        return [new_li, new_ls, new_fo, new_fe]

    def agrupar_intervalos_poisson(tabla):
        x, fo, fe = tabla
        new_x, new_fo, new_fe = [], [], []

        temp_fo, temp_fe = 0, 0
        current_x = x[0]

        for i in range(len(fe)):
            temp_fo += fo[i]
            temp_fe += fe[i]

            if temp_fe >= 5:
                new_x.append(f"{current_x}–{x[i]}")
                new_fo.append(temp_fo)
                new_fe.append(temp_fe)
                if i + 1 < len(x):
                    current_x = x[i + 1]
                temp_fo, temp_fe = 0, 0

        if temp_fe > 0:
            if new_fe:
                new_fe[-1] += temp_fe
                new_fo[-1] += temp_fo
                new_x[-1] = f"{new_x[-1].split('–')[0]}–{x[-1]}"
            else:
                new_x.append(f"{current_x}–{x[-1]}")
                new_fo.append(temp_fo)
                new_fe.append(temp_fe)

        return [new_x, new_fo, new_fe]

    resultado = []
    chi_cuadrado = 0
    grados_libertad = 0

    if dist == "Poisson":
        max_x = max(x)
        tabla_x = list(range(0, max_x + 1))
        fe = []
        total = sum(numeros)
        for i in tabla_x:
            p = (m.exp(-lamb) * (lamb ** i)) / m.factorial(i)
            fe.append(p * total)

        tabla = [tabla_x, numeros, fe]
        tabla = agrupar_intervalos_poisson(tabla)
        x_agrupado, fo, fe = tabla
        resultado.append(["x", "fo", "fe", "((fo-fe)^2)/fe"])
        for i in range(len(fo)):
            chi = ((fo[i] - fe[i]) ** 2) / fe[i]
            chi_cuadrado += chi
            resultado.append([x_agrupado[i], fo[i], redondear(fe[i], 2), redondear(chi, 4)])

        grados_libertad = len(fe) - 1 - 1  # -1 por lambda estimado

    else:
        k = int(m.ceil(m.sqrt(len(numeros))))
        rango = (max(numeros) - min(numeros)) / k
        li = [min(numeros) + i * rango for i in range(k)]
        ls = [li[i] + rango for i in range(k)]
        fo = [0] * k

        for n in numeros:
            for i in range(k):
                if li[i] <= n < ls[i] or (i == k - 1 and li[i] <= n <= ls[i]):
                    fo[i] += 1
                    break

        #A ADAPTAR            
        fe = []
        n = len(numeros)

        if dist == "Uniforme":
            fe = [ n / k ] * k
            #for i in range(k):
            #   fe.append(n / k)

        elif dist == "Normal":
            # Calcular media y desviación estándar
            media_m = sum(numeros) / n if media is None else media
            varianza_m = sum((x - media_m) ** 2 for x in numeros) / n if varianza is None else varianza
            desviacion = m.sqrt(varianza_m)
        
            # Validar desviación estándar
            if desviacion <= 0:
                raise ValueError("La desviación estándar debe ser mayor que 0")
        
            fe = []
            for i in range(k):
                # Validar límites del intervalo
                if ls[i] <= li[i]:
                    raise ValueError(f"El límite superior ({ls[i]}) debe ser mayor que el límite inferior ({li[i]}) en el intervalo {i}")
        
                # Calcular la probabilidad usando la CDF
                from scipy.stats import norm
                p = norm.cdf(ls[i], loc=media_m, scale=desviacion) - norm.cdf(li[i], loc=media_m, scale=desviacion)
        
                # Validar probabilidad
                if p < 0 or p > 1:
                    raise ValueError(f"Probabilidad inválida calculada: {p} en el intervalo {i}")
        
                # Calcular frecuencia esperada
                fe.append(p * n)
        
            # Agrupar intervalos con fe < 5
            tabla = [li, ls, fo, fe]
            tabla = agrupar_intervalos(tabla)
            li, ls, fo, fe = tabla
        
            # Depuración
            for i in range(len(fe)):
                print(f"Intervalo {i}: li = {li[i]}, ls = {ls[i]}, fe = {fe[i]}, fo = {fo[i]}")
        
            # Calcular Chi-Cuadrado
            chi_cuadrado = 0
            for i in range(len(fe)):
                if fe[i] > 0:
                    chi_cuadrado += ((fo[i] - fe[i]) ** 2) / fe[i]
        
            # Imprimir resultado final
            print(f"Chi-Cuadrado Calculado: {chi_cuadrado}")

        elif dist == "Exponencial":
            lamb = 1 / (sum(numeros) / n)
            for i in range(k):
                p = m.exp(-lamb * li[i]) - m.exp(-lamb * ls[i])
                fe.append(p * n)

        tabla = [li, ls, fo, fe]
        tabla = agrupar_intervalos(tabla)
        li, ls, fo, fe = tabla
        resultado.append(["li", "ls", "fo", "fe", "((fo-fe)^2)/fe"])
        for i in range(len(fo)):
            chi = ((fo[i] - fe[i]) ** 2) / fe[i]
            chi_cuadrado += chi
            resultado.append([
                redondear(li[i], 2),
                redondear(ls[i], 2),
                fo[i],
                fe[i],
                redondear(chi, 4)
            ])

        # Grados de libertad:
        if dist == "Uniforme":
            grados_libertad = len(fe) - 1
        elif dist == "Normal":
            grados_libertad = len(fe) - 3  # media y varianza estimadas
        elif dist == "Exponencial":
            grados_libertad = len(fe) - 2  # lambda estimado

    valor_critico = chi2.ppf(1 - a, grados_libertad)
    resultado.append(["Chi^2 calculado", redondear(chi_cuadrado, 4)])
    resultado.append(["Chi^2 crítico", redondear(valor_critico, 4)])
    resultado.append(["Grados de libertad", grados_libertad])
    resultado.append(["Resultado", "No se rechaza H0" if chi_cuadrado < valor_critico else "Se rechaza H0"])
    return resultado


#TEST DE PRUEBAS DE KOLMOGOROV SMIRNOV
def testPruebaKS(numeros, alpha,dist, i=None,lambd=None,media=None,des=None):
    if type(numeros) != list or len(numeros) == 0:
        raise ValueError("Debe ser una lista de números")
    n = len(numeros)
    if i is not None:
        if i <= 0:
            raise ValueError("El valor de i debe ser un entero positivo")
        k = i
    else:
        k = m.floor(m.sqrt(n))
    observados = [0] * k
    esperados = [0] * k
    #chi = [0] * k
    limites = []
    prob_obs = [0]*k
    prob_esp = [0]*k
    apfo = [0]*k
    apfe = [0]*k
    diferencia = [0]*k
    maximos = [0]*k
    minimo = min(numeros)
    maximo = max(numeros)
    dif = maximo - minimo
    ancho = m.ceil(dif / k * 100) / 100
    ac = sum(numeros)
    if dist == "Uniforme":
        l_i = 0
        l_s = 1/k
        if round(n/k) == n/k:
            esp = int(n/k)
        else:
            esp = n/k
        esperados = [esp] * k
        for i in range(k):
            for j in numeros:
                if l_i<=j<l_s:
                    observados[i] += 1
            prob_obs[i] = round((observados[i] / n),2)
            prob_esp[i] = round((esperados[i] / n),2)
            if i==0:
                apfo[i] = round(prob_obs[i],2)
                apfe[i] = round(prob_esp[i],2)
                diferencia[i] = round((abs(apfo[i]-apfe[i])),2)
                maximos[i] = diferencia[i]
                limites.append([l_i,round(l_s,2)])
                l_i = l_s
                l_s += 1/k
            else:
                apfo[i] = round((prob_obs[i] + apfo[i-1]),2)
                apfe[i] = round((prob_esp[i] + apfe[i-1]),2)
                diferencia[i] = round((abs(apfo[i]-apfe[i])),2)
                if diferencia[i] >= maximos[i-1]:
                    maximos[i] = diferencia[i]
                else:
                    maximos[i] = maximos[i-1]
                limites.append([round(l_i,2),round(l_s,2)])
                l_i = l_s
                l_s += 1/k
        x = maximos[-1]
        k_s_tabla = kstwo.ppf(1 - alpha,n)
    elif dist == "Exponencial":
        if lambd is None:
                med = ac/n
                lambd = 1/med
        l_i=minimo
        l_s = l_i + ancho
        for i in range(k):
            for j in numeros:
                if l_i <= j < l_s:
                    observados[i] += 1
            prob_obs[i] = observados[i] / n
            prob_esp[i] = (1-m.exp(-lambd*l_s))-(1-m.exp(-lambd*l_i))
            esperados[i] = prob_esp[i] * n
            if i==0:
                apfo[i] = prob_obs[i]
                apfe[i] = prob_esp[i]
                diferencia[i] = abs(apfo[i]-apfe[i])
                maximos[i] = diferencia[i]
                limites.append([round(l_i,2),round(l_s,2)])
                l_i = l_s
                l_s += ancho
            else:
                apfo[i] = prob_obs[i] + apfo[i-1]
                apfe[i] = prob_esp[i] + apfe[i-1]
                diferencia[i] = abs(apfo[i]-apfe[i])
                if diferencia[i] >= maximos[i-1]:
                    maximos[i] = diferencia[i]
                else:
                    maximos[i] = maximos[i-1]
                limites.append([round(l_i,2),round(l_s,2)])
                l_i = l_s
                l_s += ancho
        x = maximos[-1]
        k_s_tabla = kstwo.ppf(1 - alpha,n)
    elif dist == "Normal":
        if media is None:
                media = ac/n
        if des is None:
            b = 0
            for i in numeros:
                    b += (i-media)**2
            y = b/(n-1)
            des = m.sqrt(y)
        l_i = minimo
        l_s = l_i + ancho
        for i in range(k):
            for j in numeros:
                if l_i <= j < l_s:
                    observados[i] += 1
            media_intervalos = (l_i+l_s)/2
            p = (1/(des*m.sqrt(2*m.pi)))*m.exp((-1/2)*(((media_intervalos-media)/des)**2))*(l_s-l_i)
            prob_obs[i] = observados[i] / n
            prob_esp[i] = p
            esperados[i] = prob_esp[i] * n
            if i==0:
                apfo[i] = prob_obs[i]
                apfe[i] = prob_esp[i]
                diferencia[i] = abs(apfo[i]-apfe[i])
                maximos[i] = diferencia[i]
                limites.append([l_i, round(l_s, 2)])
                l_i = l_s
                l_s += ancho
            else:
                apfo[i] = prob_obs[i] + apfo[i-1]
                apfe[i] = prob_esp[i] + apfe[i-1]
                diferencia[i] = abs(apfo[i]-apfe[i])
                if diferencia[i] >= maximos[i-1]:
                    maximos[i] = diferencia[i]
                else:
                    maximos[i] = maximos[i-1]
                limites.append([round(l_i, 2), round(l_s, 2)])
                l_i = l_s
                l_s += ancho
        x = maximos[-1]
        k_s_tabla = kstwo.ppf(1 - alpha,n)
    elif dist == "Poisson":
        raise ValueError("La distribucion de Poisson es discreta.No es aplicable esta prueba")
    else:
        raise ValueError("Debe ingresar correctamente la distribucion")
    
    print(x)
    return (
        observados,
        esperados,
        prob_obs,
        prob_esp,
        apfo,
        apfe,
        diferencia,
        maximos,
        x,
        k_s_tabla,
        limites #Rangos de los intervalos
    )



def agrupar_intervalos_poisson2(tabla):
    # Implementación corregida
    limites = tabla[0]
    observados = tabla[1]
    esperados = tabla[2]
    
    # Convertir todos los límites a strings
    limites_str = [str(lim) for lim in limites]
    
    # Lógica de agrupación corregida
    nuevos_limites = []
    nuevos_obs = []
    nuevos_esp = []
    
    temp_obs = 0
    temp_esp = 0
    
    for i in range(len(limites_str)):
        if esperados[i] < 5:
            if not nuevos_limites:
                nuevos_limites.append(limites_str[i])
            else:
                nuevos_limites[-1] += f",{limites_str[i]}"
            temp_obs += observados[i]
            temp_esp += esperados[i]
        else:
            if temp_obs > 0:
                nuevos_obs.append(temp_obs)
                nuevos_esp.append(temp_esp)
                temp_obs = 0
                temp_esp = 0
            nuevos_limites.append(limites_str[i])
            nuevos_obs.append(observados[i])
            nuevos_esp.append(esperados[i])
    
    # Agregar último grupo si queda pendiente
    if temp_obs > 0:
        nuevos_obs.append(temp_obs)
        nuevos_esp.append(temp_esp)
    
    return [nuevos_limites, nuevos_obs, nuevos_esp]


def testChiCuadradoPoisson(numeros, a, lambd, i=None):
    """
    Realiza la prueba de Chi-Cuadrado para la distribución de Poisson.
    """
    import math as m
    from decimal import Decimal, ROUND_HALF_UP
    from scipy.stats import chi2
    import numpy as np

    # Validaciones iniciales mejoradas
    if not isinstance(numeros, list) or len(numeros) == 0:
        raise ValueError("Debe ser una lista de números no vacía.")
    if lambd <= 0:
        raise ValueError("El parámetro lambda debe ser mayor que 0.")
    if i is not None and i <= 0:
        raise ValueError("El número de intervalos debe ser un entero positivo.")
    if not all(isinstance(x, (int, float)) for x in numeros):
        raise ValueError("Todos los valores deben ser numéricos")

    n = len(numeros)
    if n < 30:
        raise ValueError("La muestra debe contener al menos 30 números.")

    # Calcular frecuencias observadas
    poisson = {}
    for num in numeros:
        num_int = int(round(num))
        poisson[num_int] = poisson.get(num_int, 0) + 1
    poisson_ordenado = dict(sorted(poisson.items()))

    # Calcular frecuencias esperadas con protección contra underflow
    limites = []
    observados = []
    esperados = []
    
    for x, fo in poisson_ordenado.items():
        try:
            # Cálculo más estable numéricamente usando logaritmos
            log_p = x * m.log(lambd) - lambd - sum(m.log(i) for i in range(1, x+1)) if x > 0 else -lambd
            p = m.exp(log_p)
            fe = max(1.0, float(Decimal(p * n).quantize(Decimal('1e-10'), rounding=ROUND_HALF_UP)))
        except:
            # Si hay error en el cálculo, usar aproximación
            fe = max(1.0, (lambd**x * m.exp(-lambd) / m.factorial(x) * n if x < 20 else 0.0))
        
        limites.append(str(x))
        observados.append(fo)
        esperados.append(fe)

    # Agrupar intervalos con frecuencias esperadas < 5
    grupos = []
    current_group = {'limites': [], 'obs': 0, 'esp': 0}
    
    for j in range(len(limites)):
        if esperados[j] < 5 and j != len(limites) - 1:
            current_group['limites'].append(limites[j])
            current_group['obs'] += observados[j]
            current_group['esp'] += esperados[j]
        else:
            if current_group['limites']:
                grupos.append(current_group)
                current_group = {'limites': [], 'obs': 0, 'esp': 0}
            grupos.append({
                'limites': [limites[j]],
                'obs': observados[j],
                'esp': esperados[j]
            })
    
    # Reconstruir listas agrupadas
    limites_agrupados = ['-'.join(g['limites']) for g in grupos]
    obs_agrupados = [g['obs'] for g in grupos]
    esp_agrupados = [g['esp'] for g in grupos]

    # Calcular Chi-Cuadrado con protección
    chi = []
    chi_acumulado = 0
    for obs, esp in zip(obs_agrupados, esp_agrupados):
        if esp <= 0:
            contrib = 0
        else:
            contrib = (obs - esp)**2 / esp
        chi_acumulado += contrib
        chi.append(chi_acumulado)

    # Calcular valor crítico con protección
    grados_libertad = max(1, len(obs_agrupados) - 2)
    try:
        x_2_tabla = chi2.ppf(1 - a, grados_libertad)
        if np.isnan(x_2_tabla):
            x_2_tabla = chi2.ppf(1 - a, 1)  # Valor por defecto para grados=1
    except:
        x_2_tabla = float('inf')

    # Resultado final con protección NaN
    resultado = {
        "observados": obs_agrupados,
        "esperados": [float(round(e, 4)) for e in esp_agrupados],
        "chi": [float(round(c, 4)) for c in chi],
        "x_2_calc": float(round(chi[-1], 4)) if chi else 0.0,
        "x_2_tabla": float(round(x_2_tabla, 4)),
        "limites": limites_agrupados,
        "grados_libertad": grados_libertad,
        "resultado": "No se rechaza H0" if chi and chi[-1] < x_2_tabla else "Se rechaza H0"
    }
    
    # Reemplazar posibles NaN/Inf por valores seguros
    for key in ['x_2_calc', 'x_2_tabla']:
        if not np.isfinite(resultado[key]):
            resultado[key] = 0.0
    
    return resultado