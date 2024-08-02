# 1/4
def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return "{}{}{}".format(open_tag, msg, close_tag)

        # Return the decorated function
        return wrapper

    # Return the decorator
    return decorator


# 2/4
# Make hello() return bolded text
@html("<b>", "</b>")
def hello(name):
    return "Hello {}!".format(name)


print(hello("Alice"))


# 3/4
# Make goodbye() return italicized text
@html("<i>", "</i>")
def goodbye(name):
    return "Goodbye {}.".format(name)


print(goodbye("Alice"))


# 4/4
# Wrap the result of hello_goodbye() in <div> and </div>
@html("<div>", "</div>")
def hello_goodbye(name):
    return "\n{}\n{}\n".format(hello(name), goodbye(name))


print(hello_goodbye("Alice"))
