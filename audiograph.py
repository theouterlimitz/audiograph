import time
import numpy as np
import matplotlib.pyplot as plt
import requests
from mpl_toolkits.mplot3d import Axes3D

def audio_stream(url):
    response = requests.get(url, stream=True)
    data = np.frombuffer(response.content, dtype=np.int16, count=1024)
    return data



def plot_audio(data):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(data, zs=range(len(data)), ys=data, label="Amplitude")
    ax.set_ylabel("Time")
    ax.set_xlabel("Frequency")
    ax.legend()
    plt.show()

def aggregate_sum(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    return sum

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=0jspaMLxBig"
    data = audio_stream(url)
    plot_audio(data)
    sum = aggregate_sum(data)
    print("The aggregate sum is:", sum)
