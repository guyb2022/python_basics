class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        # Add some pre-processing code
        print("Before function execution")
        # Call the original function
        self.func()
        # Add some post-processing code
        print("After function execution")

@DecoratorClass
def greeting():
    print("Hello, world!")

# Call the decorated function
greeting()
