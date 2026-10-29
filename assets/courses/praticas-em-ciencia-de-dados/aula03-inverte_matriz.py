import os
import time
import numpy as np

print("Rodando no nó:", os.uname()[1])
print("Núcleos para o numpy (OMP_NUM_THREADS):", os.environ.get("OMP_NUM_THREADS", "não definido"))

a = np.random.random((4000, 4000))

tic = time.perf_counter()
np.linalg.inv(a)
toc = time.perf_counter()
print(f"O código rodou em {toc - tic:0.4f} segundos")
