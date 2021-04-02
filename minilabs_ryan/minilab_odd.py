"""Fibonacci algorithm contained within a class """


class Odd:
    """Initializer of class takes series parameter and returns Class Object"""
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

    """Algorithm for getting odd numbers sequence, this id called from __init__"""
    def calc_series(self):
        limit = self._series
        for i in range(limit):
            if i % 2 != 0: #odd numbers
                self.set_data(i)
            i = i + 1



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
    n = 50
    '''Constructor of Class object'''
    odd = Odd(n)

    '''Using getters to obtain data from object'''
    print(f"Odd numbers till number for {n} = {odd.number}")
    print(f"Odd numbers series for {n} = {odd.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Odd Number sequence {i + 1} = {odd.get_sequence(i)}")
