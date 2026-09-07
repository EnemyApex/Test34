import numpy as np

def pagerank(A, d=0.85, max_iter=100, tol=1e-6):
    N = A.shape[0]
    out_degree = A.sum(axis=0)
    M = np.copy(A).astype(float)

    for j in range(N):
        if out_degree[j] > 0:
            M[:, j] /= out_degree[j]
        else:
            M[:, j] = 1.0 / N

    r = np.ones(N) / N
    history = [r.copy()]

    for i in range(max_iter):
        r_new = d * M @ r + (1 - d) / N
        if np.linalg.norm(r_new - r, 1) < tol:
            break
        r = r_new
        history.append(r.copy())

    return r, i+1, np.array(history)
