from math import sin, pi
import random
import sins
import time



if __name__ == '__main__':
    samples = []
    for loop in range(10**6):
        samples.append(
            (random.random()-.5)*pi*2
            )
    subsamples = samples[:1000]
    repeated_samples = []
    for loop in range(10**3):
        random.shuffle(subsamples)
        repeated_samples += subsamples
    print(len(samples), len(repeated_samples))
    # outputTrue=map(sin, samples[:5])
    # outputOurs=map(sins.sin1, samples[:5])
    # print(list(outputTrue))
    # print(list(outputOurs))
    # print([outputOurs])
    # start1 = time.time()
    # output = list(map(sins.sin1, repeated_samples))
    # end1 = time.time()
    # print('trial 1 took duration of time ', end1-start1)
    # start2 = time.time()
    # output = list(map(sins.sin2, repeated_samples))
    # end2 = time.time()
    # print('trial 2 took duration of time ', end2-start2)
    start3 = time.time()
    calcObj = sins.sin3()
    output = list(map(calcObj.sin, repeated_samples))
    end3 = time.time()
    print('trial 3 took duration of time ', end3-start3)
    start4 = time.time()
    calcObj = sins.sin4()
    output = list(map(calcObj.sin, repeated_samples))
    end4 = time.time()
    print('trial 4 took duration of time ', end4-start4)
