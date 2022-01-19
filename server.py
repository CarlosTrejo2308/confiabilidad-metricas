import time
import random
from wsgiref.simple_server import ServerHandler

def serverMock():
    """
    This function is used to mock a server.

    :return: A boolean representing if the server is up or down.
    """
    status = False
    duration = random.randint(1, 10)

    while True:
        for i in range(duration):
            yield status
        duration = random.randint(1, 10)
        status = random.random() < 0.67

        print("Duration: {}".format(duration))


def main():
    """
    This function is used to run the server.
    """
    for status in serverMock():
        print("Server is {}".format("up" if status else "down"))
        time.sleep(.1)

if __name__ == "__main__":
    main()