from math import factorial
def sin1(x):
    #sum (-1)**(n-1)*x**(2n-1)/(2n-1)!
    n=1
    output=0
    while n < 6:
        output += (-1)**(n-1) * x**(2*n-1)/factorial(2*n-1)
        n+=1
    return output

def sin2(x, sigfig=10**-12):
    current = x
    last_term = x
    n=2
    while abs(last_term) > sigfig:
        last_term = (-1)**(n-1) * x**(2*n-1)/factorial(2*n-1)
        current += last_term
        n+=1
    return current

class sin3:
    def __init__(self):
        #memoization
        #caching
        self.results = {}

    def sin(self, x, sigfig=10**-12):
        if x in self.results:
            return self.results[x]
        current = x
        last_term = x
        n=2
        while abs(last_term) > sigfig:
            last_term = (-1)**(n-1) * x**(2*n-1)/factorial(2*n-1)
            current += last_term
            n+=1
        self.results[x] = current
        return current

class sin4:
    def __init__(self):
        #shitty memoization
        self.results = []

    def sin(self, x, sigfig=10**-12):
        for pair in self.results:
            if pair[0]==x:
                return pair[1]
        current = x
        last=0
        n=2
        while current-last > sigfig:
            last= current
            current += (-1)**(n-1) * x**(2*n-1)/factorial(2*n-1)
            n+=1
        self.results += [(x, current)]
        return current
