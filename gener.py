class GeneratorIterator:
    def __init__(self, generator_func, n):
        self.generator_func = generator_func
        self.n = n
        self.current = 0

    def __iter__(self):
        return self.generator_func(self.n)

def my_generator(n):
    for i in range(n):
        yield i

gen_iterator = GeneratorIterator(my_generator, 5)

for item in gen_iterator:
    print(item)