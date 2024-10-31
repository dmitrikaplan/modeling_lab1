import numpy as np
from scipy.stats import erlang

def generate_erlang_samples(mean, cv, size):
    # Определим параметр k
    k = int(np.round((1 / cv) ** 2))

    # Определим параметр lambda
    lambda_ = k / mean

    # Генерация случайных чисел из распределения Эрланга
    return erlang.rvs(k, scale=1/lambda_, size=size)

mean = 195.635  # Среднее значение
cv = 0.790  # Коэффициент вариации
size = 300  # Количество генерируемых случайных чисел

samples = generate_erlang_samples(mean, cv, size)

# Выводим несколько сгенерированных значений
with open('erlang.txt', 'w') as f:
    f.write(('\n'.join(map(str, samples))).replace('.', ','))