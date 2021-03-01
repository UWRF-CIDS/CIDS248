import check50
import check50.c
import random



@check50.check()
def stat_example1_exists():
    """stat_example1.c exists"""
    check50.exists("stat_example1.c")
    
@check50.check(stat_example1_exists)
def stat_example1_compiles():
    """stat_example1.c compiles"""
    check50.c.compile("stat_example1.c",cc='gcc -D _BSD_SOURCE', lcs50=False)

@check50.check()
def stat_example2_exists():
    """stat_example2.c exists"""
    check50.exists("stat_example2.c")
    
@check50.check(stat_example2_exists)
def stat_example2_compiles():
    """stat_example2.c compiles"""
    check50.c.compile("stat_example2.c",cc='gcc', lcs50=False)

@check50.check()
def file_io_exists():
    """file_io.c exists"""
    check50.exists("file_io.c")
    
@check50.check(file_io_exists)
def file_io_compiles():
    """file_io.c compiles"""
    check50.c.compile("file_io.c",cc='gcc', lcs50=False)
