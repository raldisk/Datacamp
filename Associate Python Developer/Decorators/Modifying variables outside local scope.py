# 2/3
def read_files():
    file_contents = None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents = []
        with open(filename) as fin:
            file_contents.append(fin.read())

    for filename in ["1984.txt", "MobyDick.txt", "CatsEye.txt"]:
        save_contents(filename)

    return file_contents


print("\n".join(read_files()))


# 3/3
def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print("Work done? {}".format(done))
