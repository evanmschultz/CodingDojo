local_val = "magical unicorns"


def square(x):
    return x * x


class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"


# if __name__ == '__main__': # code I ran before I saw the part of the assignment written below
#     print(__name__)
#     print(locals())
#     print(square(5))
#     user = User("Anna")
#     print(user.name)
#     print(user.say_hello())

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
