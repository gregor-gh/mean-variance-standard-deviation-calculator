import numpy as np

def calculate(list):

    # check we have 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # create numpy array
    a = np.array(list, dtype=np.int8)
    b = np.reshape(a, (3, 3))

    mean = []
    mean.append(np.mean(b, axis=0).tolist())
    mean.append(np.mean(b, axis=1).tolist())
    mean.append(np.mean(b))

    var = []
    var.append(np.var(b, axis=0).tolist())
    var.append(np.var(b, axis=1).tolist())
    var.append(np.var(b))

    std = []
    std.append(np.std(b, axis=0).tolist())
    std.append(np.std(b, axis=1).tolist())
    std.append(np.std(b))

    max = []
    max.append(np.max(b, axis=0).tolist())
    max.append(np.max(b, axis=1).tolist())
    max.append(np.max(b))

    min = []
    min.append(np.min(b, axis=0).tolist())
    min.append(np.min(b, axis=1).tolist())
    min.append(np.min(b))

    sum = []
    sum.append(np.sum(b, axis=0).tolist())
    sum.append(np.sum(b, axis=1).tolist())
    sum.append(np.sum(b))

    calculations = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum
    }

    return calculations