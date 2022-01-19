import time
import random
from wsgiref.simple_server import ServerHandler

def serverMock(maxi = None):
    """
    This function is used to mock a server.

    :return: A boolean representing if the server is up or down.
    """
    status = False
    duration = random.randint(1, 10)
    iteration = 0

    while not maxi or maxi > iteration:
        for i in range(duration):
            yield status
            iteration += 1
        duration = random.randint(1, 10)
        status = random.random() < 0.67


def main():
    """
    This function is used to run the server.
    """
    for status in serverMock():
        print("Server is {}".format("up" if status else "down"))
        time.sleep(.1)

if __name__ == "__main__":
    main()