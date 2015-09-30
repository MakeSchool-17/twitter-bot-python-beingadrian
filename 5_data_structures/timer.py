import cProfile


def time_function(function):
    cProfile.run(function)
