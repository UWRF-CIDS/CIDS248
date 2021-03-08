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
    check50.include("queue_example_soln")

@check50.check(exists)
def compiles():
    """queue_example compiles using your Makefile"""
    output = check50.run("make queue").stdout()
    if not os.path.isfile('./queue_example'):
        raise check50.Failure("Make did not create \"queue_example\" executable! Check your spelling. Here is the output from the \"make queue\" command: " + str(output))


@check50.check(compiles)
def check_queue_example():
    """checking output of queue_example"""
    output = check50.run("./queue_example".stdout()
    soln = check50.run("./queue_example_soln".stdout()
    if output != soln:
        raise check50.Failure("Your output did not match the solution output. \n\nExpected:\n{}\n\nYour output:\n{}\n\n".format(soln, output))
      
