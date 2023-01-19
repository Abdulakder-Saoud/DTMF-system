from scipy.io.wavfile import write,read
from scipy.fftpack import fft,fftshift
import numpy as np
import matplotlib.pyplot as plt

matris = [[941,1336],
        [697,1209],[697,1336],[697,1477],
        [770,1209],[770,1336],[770,1477],
        [852,1209],[852,1336],[852,1477]
        ]
numString = ""
def sesOlustur():
    duration = int(8000 * 0.1)
    numString = input("Enter The number |Length must be 11|")
    myNum = [int(x) for x in numString]
    data = []
    for i in myNum:
        f1 = matris[i][0]
        f2 = matris[i][1]
        t = np.arange(duration)
        sin1 = np.sin(2 * np.pi * f1 * t/8000)
        sin2 = np.sin(2 * np.pi * f2 * t/8000)
        sum = (sin1+sin2)*5000 
        empty = np.ones(duration) * 0
        data = np.concatenate((data,sum,empty),axis=None)
    """
    time = np.linspace(0, 22 *duration,num=22 * duration)
    plt.plot(time,data)
    plt.show()
    """
    data = np.int16(data)
    write("num.wav", 8000, data)

def sesOku(sesIsmi):
    samplerateA,tmp = read(f'{sesIsmi}.wav')
    time = np.linspace(0, tmp.shape[0], tmp.shape[0])
    """
    plt.plot(time,tmp)
    plt.show()
    """
    Atell = tmp.reshape(22,800)
    i = 0
    Numara = []
    while i <22:
        X = fft(Atell[i],8000)

        Y = fftshift(X)
        time = np.linspace(-4000,4000,num=8000)
        
        max = np.argmax(np.abs(X), axis=0)
        while (max < 500):
            X[max] = 0
            X[-max] = 0
            max= np.argmax(np.abs(X), axis=0)
        X[max] = 0
        X[-max] = 0
        max2 = np.argmax(np.abs(X), axis=0)
        while(abs(max-max2) < 10):
            max2 = np.argmax(np.abs(X), axis=0)
            X[max2] = 0
            X[-max2] = 0
        
        if (max < max2):
            max,max2 = max2,max
        inde = matris.index([max2,max])
        Numara.append(inde)
        """
        plt.title(f'[{max2},{max}] | {inde}')
        plt.plot(time,  np.abs(Y))
        plt.show()
        """
        i +=2
    print(f'Numara : {Numara}')

z = int(input("0| Exit\n1| Make Sound\n2| Read Example\n3| Read the one you wrote\n"))
while(z!= 0):
    if (z == 1):
        sesOlustur()
    elif(z == 2):
        sesOku("Example")
    elif(z == 3):
        sesOku("num")
    z = int(input("0| Exit\n1| Make Sound\n2| Read Example\n3| Read the one you wrote\n"))
