def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <= 1:
            return n
        else:
            fibonacci_cache = fibonacci(n-1) + fibonacci(n-2)
            cache [n] = fibonacci_cache
            return fibonacci_cache
    return fibonacci

