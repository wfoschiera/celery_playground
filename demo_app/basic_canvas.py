import logging

from celery import signature

from .tasks import add

logger = logging.getLogger("playground")


def signature_example():
    print(signature("tasks.add", args=(2, 2), countdown=10))
    # is the same as
    print(add.signature((2, 2), countdown=10))
    # and using star arguments
    print(add.s(2, 2))


if __name__ == "__main__":
    signature_example()
