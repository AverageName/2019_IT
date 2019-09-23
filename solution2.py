import numpy as np
import math



def gen_filter(std, kernel_size):
    filt = np.zeros((kernel_size, kernel_size))
    const = 1/(2* std ** 2)
    for i in range(-kernel_size//2, kernel_size//2):
        for j in range(-kernel_size//2, kernel_size//2):
            filt[i + kernel_size//2][j + kernel_size//2] = const/math.pi * math.exp(-(i ** 2 + j ** 2) * const)
    return filt/np.sum(filt)

def patch_conv(patch, filter):
    return np.reshape(patch, -1) @ np.reshape(filter, -1)

def conv2d(pic, filter):
    kernel_size = filter.shape[0]
    ans = []
    for channel in range(pic.shape[2]):
        res = np.zeros((pic.shape[0] - kernel_size + 1, pic.shape[1] - kernel_size + 1))
        for i in range(pic.shape[0] - kernel_size + 1):
            for j in range(pic.shape[1] - kernel_size + 1):
                res[i][j] = patch_conv(pic[i : i + kernel_size, j: j + kernel_size, channel], filter)
        ans.append(res)
    return np.stack(ans, axis=-1)

inputs = np.random.rand(3, 3, 3)
print(inputs.shape)
filter = gen_filter(1, 3)
print(conv2d(inputs, filter))

