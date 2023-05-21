import numpy as np
""" 
    Функция fft_add принимает две строки a и b, содержащие числа,
    которые необходимо сложить. Алгоритм преобразует строки a и b в массивы комплексных чисел,
    затем дополняет нулями до ближайшей степени двойки для выполнения ФФТ.
"""
def fft_add(a, b):
    a_complex = np.array([complex(int(digit), 0) for digit in a], dtype=np.complex_)
    b_complex = np.array([complex(int(digit), 0) for digit in b], dtype=np.complex_)

    N = 2**(int(np.log2(len(a) + len(b) - 1)) + 1)
    a_complex = np.pad(a_complex, (0, N - len(a)), mode='constant')
    b_complex = np.pad(b_complex, (0, N - len(b)), mode='constant')

    fft_a = np.fft.fft(a_complex)
    fft_b = np.fft.fft(b_complex)
    fft_result = fft_a + fft_b
    result = np.absolute(np.fft.ifft(fft_result)).astype(int)

    return ''.join([str(int(np.real(digit))) for digit in result])
"""
    После выполнения ФФТ массивы a_complex и b_complex складываются,
    а затем выполняется обратное преобразование Фурье (iFFT).
    Результат преобразования передается в функцию numpy.absolute,
    которая возвращает абсолютное значение элементов массива, и метод astype(int),
    который преобразует все элементы массива в тип данных int.
    Результат сложения строк является строкой, полученной из функции join().
"""

def main():
    a = input('Enter 1 number:')
    b = input('Enter 2 number:')
    print(fft_add(a, b))


if __name__ == "__main__":
    main()
