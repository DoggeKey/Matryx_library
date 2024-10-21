if __name__ == "__main__":
    print("этот код не должен запускаться как основной! используйте import для импортирования функций и классов в ваш код.")

class Matryx:

    def set(self,new):
        """сеттер"""
        if type(new) == str:
            self._matryx = self._str_to_list(new)
        elif type(new) == list:
            self._matryx = new
        else:
            self._matryx = new._matryx[:]
        return self
    def get(self):
        """геттер"""
        return self._matryx

    def _str_to_list(self, data):
        """ превращает строку в список"""
        data = data.split("\n") #разделение на строки
        data = [x for x in [y.split() for y in data] if len(x)] # разделение на символы (удаление пустых списков)
        data = [[int(data[x][y]) for y in range(0, len(data[x]))] for x in range(0, len(data))] # перевод символов в цифры
        return data

    def __str__(self):
        """рисует матрицу в консоли"""
        string = str()
        print(f"size:{len(self._matryx)}x{len(self._matryx[0])}")
        MX = -1
        for i in self._matryx:
            s = len(str(max(i)))
            if s > MX:
                MX = s
        for i in self._matryx:
            string += "["
            for j in i:
                s = len(str(j))
                string += str(j) + " " * (MX - s + 1)
            string += "]\n"
        return string

    def __eq__(self, other):
        """сравнивает матрицы (==)"""
        a = self._matryx
        b = other._matryx
        if len(a) == len(b):
            for i in range(0, len(a)):
                for j in range(0, len(a[0])):
                    if a[i][j] != b[i][j]:
                        return False
            return True
        else:
            return False

    def __nq__(self, other):
        """сравнивает матрицы (!=)"""
        a = self._matryx
        b = other._matryx
        if len(a) == len(b):
            for i in range(0, len(a)):
                for j in range(0, len(a[0])):
                    if a[i][j] != b[i][j]:
                        return False
            return False
        else:
            return True

    def __mul__(self, other):
        """умножение матриц"""
        a = self._matryx
        if type(other) == type(self):
            b = other._matryx
        else:
            b = other
        if type(a) == list and type(b) == list:
            if len(a[0]) == len(b):
                c = []
                for i in range(0, len(a)):
                    c.append([])
                    for j in range(0, len(b[0])):
                        s = 0
                        for k in range(0, len(b)):
                            s += a[i][k] * b[k][j]
                        c[i].append(s)
                return c
            else:
                return None
        elif type(a) == list or type(b) == list:
            if type(b) == list:
                a, b = b, a
            c = []
            for i in range(0, len(a)):
                c.append([])
                for j in range(0, len(a[0])):
                    c[i].append(a[i][j] * b)
            return Matryx(c)
        else:
            return None

    def __sub__(self, other):
        """вычитанте матриц"""
        a = self._matryx
        b = other._matryx
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c = []
            for i in range(0, len(a)):
                c.append([])
                for j in range(0, len(a[0])):
                    c[i].append(a[i][j] - b[i][j])
            return Matryx(c)
        else:
            return None

    def __add__(self, other):
        """сложение матриц"""
        a = self._matryx
        b = other._matryx
        c = []
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            for i in range(0, len(a)):
                c.append([])
                for j in range(0, len(a[0])):
                    c[i].append(a[i][j] + b[i][j])
            return Matryx(c)
        else:
            return None

    def __init__(self, matryx):
        """инициализация матрицы"""
        if type(matryx) == str:
            matryx = self._str_to_list(matryx)
        self._matryx = matryx

def M(matryx, i, j):
    skipper = 0
    c = []
    for k in range(0, len(matryx._matryx)):
        if i == k:
            skipper += 1
        else:
            c.append([])
            for n in range(0, len(matryx._matryx[0])):
                if j != n:
                    c[k - skipper].append(matryx._matryx[k][n])
    return Matryx(c)

def det(matryx):
    """ вычисляет определитель матрицы"""
    a = matryx
    k = matryx._matryx
    mt = []
    if len(k) > 2:
        for i in range(1, len(k) + 1):
            g = ((-1) ** (1 + i)) * k[0][i - 1] * det(M(a, 0, i - 1))
            mt.append(g)
        return sum(mt)
    else:
        return k[0][0] * k[1][1] - k[0][1] * k[1][0]

def T(matryx):
        """транспонирует матрицу"""
        a = matryx._matryx
        c = []
        for i in range(0, len(a[0])):
            c.append([])
            for j in range(0, len(a)):
                c[i].append(a[j][i])
        return Matryx(c)

def help():
    """подсказка"""
    h = """
using matryx ver.0.301

matryx добавляет матрицы в Python 3.0 и выше.

Инициализация происходит довольно просто:
вы просто присваеваете её через конструктор Matryx().
Внутри конструктора вы вводите вашу матрицу, ставя пробелы между числами
и переходя на новую строку.
Будьте бдительны, ведь если размеры строк будут разные, интерпретатор
выдаст ошибку.
Примеры инициализации матриц:
A = Matryx(\"\"\"
1 2 3
4 5 6
7 8 9
"\"\"\")

ИЛИ

B = Matryx([[1, 2], [3, 4]])

ИЛИ

C = Matryx(B) - вот даже так

Матрицы также имеют при себе сеттер и геттер.
В сеттер можно указать такие-же данные, что и при инициализации.
Из геттера можно получить только вложенный список.
Примеры использования

A.set(B)

ИЛИ

B.set(\"\"\"0"\"\") - мн из 1 значения (нуля)

А ТАКЖЕ

r = A.get() - возращает список

print(r) - [[1, 2], [3, 4]]

Но вам не обязательно выводить списки на экран, ведь
я позаботился о том, что через функцию print() вы сможете распечатать
матрицу "красиво".

print(A) выведет на экран -
[1 2]
[3 4]

В matryx вы можете решать простые математические операции.
На данный момент вам доступны сложение, вычитание и умножение.
Примеры использования:
C = A + C - C * 2 + A * A
print(C)

[7  10]
[15 22]

НУ ИЛИ

print(A + C)

[2 4]
[6 8]

Среди операторов сравнения - всего 2 (как и у матриц).
"равно" и "не равно".

if A == C:
    print("Amazing!")
else:
    print("oh no")

matryx также позволяет найти минор или определитель матрицы;
для этого вам нужно всего-лишь приравнять вашу переменную к
функции, вставив внутрь нужные параметры.
Также можно транспозировать матрицу.

A = T(A) - транспозиция,
dA = det(A) - определитель,
mA = M(A,0,1) минор по 1-й строке/2-му столбцу.

Работу проделал D.
Приятной вам работы!
"""
    print(h)