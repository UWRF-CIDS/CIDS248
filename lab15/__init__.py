import check50
import check50.c
import random
import os.path


@check50.check()
def exists():
    """queue.h, queue.c, queue_example.c, and Makefile exist"""
    check50.exists("queue.h")
    check50.exists("queue.c")
    check50.exists("queue_example.c")
    check50.exists("Makefile")


@check50.check(exists)
def compiles():
    """queue_example compiles using your Makefile"""
    output = check50.run("make queue").stdout()
    if not os.path.isfile('./queue_example'):
        raise check50.Failure("Make did not create \"queue_example\" executable! Here is the output from the \"make queue\" command: " + str(output))


