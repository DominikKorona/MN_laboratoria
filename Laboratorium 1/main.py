import unittest
import numpy as np
import pandas as pd
import math
import scipy


def cylinder_area(r:float,h:float):
    if r > 0 and h > 0:
        base_area = 2 * math.pi * r ** 2
        wall_area = 2 * math.pi * r * h
        return float(wall_area + base_area)
    else:
        return float('NaN')


def fib(n:int):
    if isinstance(n, int):
        if n < 0:
            return None
        elif n == 0:
            return None
        elif n == 1 or n == 2:
            return np.array([1])
        elif n > 2:
            wyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisalem w krotce
            a, b = wyrazy  # przypisanie wielokrotne, rozpakowanie krotki
            vec = np.array([[1]])
            while n > 1:
                a, b = b, a + b  # przypisanie wielokrotne
                n -= 1
                vec = np.append(vec, float(b))
            return np.array([vec])
    return None

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    m = np.array(([[a, 1, -a], [0, 1, 1], [-a, a, 1]]))
    # Inverse of Matrix m
    if np.linalg.det(m) != 0:  # Napisalem warunek na to, aby wyznacznik byl rozny od zera
        m_inv = np.linalg.inv(m)
    else:
        m_inv = float('NaN')  # gdyby wyznacznik byl rowny zero, przypisano by wartosc nan
    # Transpose a Matrix m
    m_t = m.T
    # determinant of the matrix
    m_det = np.linalg.det(m)
    return m_inv, m_t, m_det
    # nie mam pewnosci dlaczego tak mi rzad macierzy wychodzi

def custom_matrix(m:int, n:int):
    if isinstance(m, int) and isinstance(n, int):
        """Funkcja zwraca macierz o wymiarze mxn zgodnie 
        z opisem zadania 7.  

        Parameters:
        m (int): ilość wierszy macierzy
        n (int): ilość kolumn macierzy  

        Returns:
        np.ndarray: macierz zgodna z opisem z zadania 7.
        """
        data = (m, n)
        if m <= 0 or n <= 0:
            return None
        else:
            a = np.zeros(data)
            for row in range(m):
                for col in range(n):
                    if row > col:
                        a[row, col] = row
                    else:
                        a[row, col] = col
        return a
    return None
