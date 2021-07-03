# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Alumnos: Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar 4 gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos 4 gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    fig = plt.figure()
    
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    ax1.plot(x, y1, color='darkblue', marker='1', label='y1 = x^2')
    ax2.plot(x, y2, color='r', marker='o', label='y2 = x^3')
    ax3.plot(x, y3, color='black', marker='^', label='y3 = x^4')
    ax4.plot(x, y4, color='navy', marker='v', label='y4 = raiz_cuadrada(X)')

    ax1.set_facecolor('pink')
    ax2.set_facecolor('pink')
    ax3.set_facecolor('pink')
    ax4.set_facecolor('pink')


    ax1.grid(linestyle='dotted')
    ax2.grid(linestyle='dashed')
    ax3.grid(linestyle='solid')
    ax4.grid(linestyle='dashdot')

    ax1.legend(loc='upper center')
    ax2.legend(loc='upper center')
    ax3.legend(loc='upper center')
    ax4.legend(loc='upper center')

    plt.show()
    print("terminamos")