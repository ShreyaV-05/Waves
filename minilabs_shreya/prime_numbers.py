"""Fibonacci algorithm contained within a class """


class PrimeNum:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 2 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for getting prime numbers sequence, this id called from __init__"""
    def calc_series(self):
        limit = self._series
        f = [0, 2]
        for num in range(0,n+1):
            if all(num%i!=0 for i in range(2,num)):
                print (num)

    """Method/Function to set prime numbers data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 20
    '''Constructor of Class object'''
    primenum = PrimeNum(n)

    '''Using getters to obtain data from object'''
    print(f"Prime numbers till number for {n} = {primenum.number}")
    print(f"Prime numbers series for {n} = {primenum.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Prime Number sequence {i + 1} = {primenum.get_sequence(i)}")
