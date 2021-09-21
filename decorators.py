# # Passing postional arguments to decorators
# def accept_the_arguments(function_to_decorator):
#     def inner_function(*args, **kwargs):
#         print("The positional arguments are: ", args)
#         print("The keyword arguments are", kwargs)
#         function_to_decorator(*args)
#
#     return inner_function
#
#
# @accept_the_arguments
# def function_with_args(a, b, c):
#     print(a, b, c)
#
#
# function_with_args(10, 20, 30)

# passing kwargs based arguments
# def accepting_kwargs(function_to_decorator):
#     def inner_function(*args, **kwargs):
#         print(f"args: {args}")
#         print(f"kwargs: {kwargs}")
#         function_to_decorator(args, kwargs)
#     return inner_function
#
# @accepting_kwargs
# def function_with_args(*args, **kwargs):
#     print(f"Inside functions_with_args, args: {args}")
#     print(f"Inside functions_with_args, kwargs: {kwargs}")
#
# function_with_args(1, 2, 3, name="Pedri", address="Barcelona")

# passing argument to decorator

def decorator_with_args(decorator_args1, decorator_args2, decorator_args3):
    def decorator(func):
        def wrapper(function_args1, function_args2, function_args3):
            print(f"The wrapper can access all the variables\n"
                  f"\t from the decorator maker: {decorator_args1} {decorator_args2} {decorator_args3}\n"
                  f"\t from the function call: {function_args1} {function_args2} {function_args3}\n"
                  f"and pass them into decorator function")

            return func(function_args1, function_args2, function_args3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_with_args(pandas, "Numpy", "Scikit-learn")
def actual_function(function_args1, function_args2, function_args3):
    print(f"This is decorated function and it only knows about its args: {function_args1} {function_args2} {function_args3}")


actual_function("John", "Science", "Tools")