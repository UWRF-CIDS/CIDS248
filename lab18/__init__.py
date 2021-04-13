import check50
import check50.c
import random
import os.path


@check50.check()
def io_example_exists():
    """simple_fork exist"""
    check50.exists("io_example.c")

@check50.check(io_example_exists)
def io_example_compiles():
    """io_example compiles"""
    check50.c.compile("io_example.c",cc='gcc', lcs50=False)

@check50.check()
def dup_example_exists():
    """dup_example exist"""
    check50.exists("dup_example.c")

@check50.check(dup_example_exists)
def dup_example_compiles():
    """dup_example compiles"""
    check50.c.compile("dup_example.c",cc='gcc', lcs50=False)
    
@check50.check()
def in_file_exists():
    """in_file exist"""
    check50.exists("in_file.txt")
