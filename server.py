import time
import random

def serverMock():
    """
    This function is used to mock a server.

    :return: A boolean representing if the server is up or down.
    """
    return random.random() < 0.7


def main():
    """
    This function is used to run the server.
    """
    while True:
        if serverMock():
            print("Server is up!")
        else:
            print("Server is down!")
        time.sleep(1)

if __name__ == "__main__":
    main()