lst = [1, 2, 3, 4, 5]
lt = iter(lst)

# print(next(lt))


def custom_for(iterable, func):
    lt = iter(iterable)

    while True:
        try:
            func(next(lt))
        except StopIteration:
            print("End of loop")
            return


custom_for(lst, print)
