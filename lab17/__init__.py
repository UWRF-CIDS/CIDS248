import check50
import check50.c
import random
import os.path


@check50.check()
def simple_fork_exists():
    """simple_fork exist"""
    check50.exists("simple_fork.c")

@check50.check(simple_fork_exists)
def simple_fork_compiles():
    """simple_fork compiles"""
    check50.c.compile("simple_fork.c",cc='gcc', lcs50=False)

@check50.check()
def simple_wait_exists():
    """simple_wait exist"""
    check50.exists("simple_wait.c")

@check50.check(simple_wait_exists)
def simple_wait_compiles():
    """simple_wait compiles"""
    check50.c.compile("simple_wait.c",cc='gcc', lcs50=False)
    
@check50.check()
def simple_exec_exists():
    """simple_exec exist"""
    check50.exists("simple_exec.c")

@check50.check(simple_exec_exists)
def simple_exec_compiles():
    """simple_exec compiles"""
    check50.c.compile("simple_exec.c",cc='gcc', lcs50=False)
    
@check50.check()
def fork_exec_wait_exists():
    """fork_exec_wait exist"""
    check50.exists("fork_exec_wait.c")

@check50.check(fork_exec_wait_exists)
def fork_exec_wait_compiles():
    """fork_exec_wait compiles"""
    check50.c.compile("fork_exec_wait.c",cc='gcc', lcs50=False)
    
@check50.check()
def zombie_exists():
    """zombie exist"""
    check50.exists("zombie.c")

@check50.check(zombie_exists)
def zombie_compiles():
    """zombie compiles"""
    check50.c.compile("zombie.c",cc='gcc', lcs50=False)
    
@check50.check()
def orphan_exists():
    """orphan exist"""
    check50.exists("orphan.c")

@check50.check(orphan_exists)
def orphan_compiles():
    """orphan compiles"""
    check50.c.compile("orphan.c",cc='gcc', lcs50=False)
