import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face 

def mse(ref: np.ndarray , noise: np.ndarray) -> np.float:
    assert ref.ndim == noise.ndim, "Dimentions are not equal"
    diff = np.sum((ref - noise)**2)
    return(diff / ref.size )

def psnr(ref: np.ndarray , noise: np.ndarray) -> np.float:
    m = mse(ref, noise)
    return(20 * np.log10(np.max(ref) / m ** 0.5))
    
def salt_and_pepper_noise(image: np.ndarray, n: int) -> np.ndarray:
    noised = image.copy()
    coords = []
    
    for i in range(image.ndim):
        coords.append(np.random.randint(0, img.shape[i], n)) 
    
    noise_vals = np.random.randint(0, 1000, n)
    
    noised[tuple(coords)] = noise_vals
    return(noised)     


img = face(gray = False)

noised = salt_and_pepper_noise(img, 700000)


print(psnr(img, noised))

fig = plt.figure()
plt.subplot(121)
plt.title("original", size = 20)
plt.imshow(img, cmap = 'hot')
plt.subplot(122)
plt.title("noised", size = 20)
plt.imshow(noised, cmap = 'hot')

plt.show()