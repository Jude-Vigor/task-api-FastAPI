# def wrapper_decorator_(func):
#     def wrapped():
#         print("Wrapping before the gift")
#         func()
#         print("Wrapping after the gift")

#     return wrapped


# @wrapper_decorator_
# def say_hello():
#     print("Hello!")


# # say_hello()


# # 2. Decorator with argument


# def gift_wrapper(message):
#     def decorator(func):
#         def wrapped():
#             print(f"Before: {message}")
#             func()
#             print("After: Gift delivered")

#         return wrapped

#     return decorator


# @gift_wrapper("Happy Birthday!")
# def give_gift():
#     print("Here is your gift!")


# # give_gift()

# # 3. Preserving metadata with functools.wraps

# # This is very important.

# # Without special handling, when you wrap a function, Python forgets some info about the original gift.

from functools import wraps


def wrapper_decorator(func):
    @wraps(func)
    def wrapped():
        print("Before")
        func()

    return wrapped


@wrapper_decorator
def Jude_hello():
    """This function says hello"""
    print("Hello")


print(Jude_hello.__name__)
print(Jude_hello.__doc__)
