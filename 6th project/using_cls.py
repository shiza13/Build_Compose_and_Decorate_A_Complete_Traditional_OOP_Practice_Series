class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

    @classmethod
    def show_count(cls):
        print("Total Counter objects created:", cls.count)

o1 = Counter()
o2 = Counter()
o3 = Counter()

Counter.show_count()
