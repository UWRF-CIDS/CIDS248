import check50
import check50.c
import random



@check50.check()
def leaky_exists():
    """leaky.c exists"""
    check50.exists("leaky.c")
    
@check50.check(leaky_exists)
def leaky_compiles():
    """leaky.c compiles"""
    check50.c.compile("leaky.c",cc='gcc -D _BSD_SOURCE', lcs50=False)

@check50.check(leaky_compiles)
def leaky_check():
    """leaky.c contains no memory leaks"""
    output = check50.run("valgrind ./leaky".stdout()
    if not "All heap blocks were freed -- no leaks are possible" in output:
        raise check50.Failure("According to valgrind, the program still contains leaks.")

