import check50
import check50.c
import random



@check50.check()
def typedef_exists():
    """typedef.c exists"""
    check50.exists("typedef.c")
    
@check50.check(typedef_exists)
def typedef_compiles():
    """typedef.c compiles"""
    check50.c.compile("typedef.c",cc='gcc', lcs50=False)

@check50.check()
def struct1_exists():
    """struct1.c exists"""
    check50.exists("struct1.c")
    
@check50.check(struct1_exists)
def struct1_compiles():
    """struct1.c compiles"""
    check50.c.compile("struct1.c",cc='gcc', lcs50=False)

@check50.check()
def struct2_exists():
    """struct2.c exists"""
    check50.exists("struct2.c")
    
@check50.check(struct2_exists)
def struct2_compiles():
    """struct2.c compiles"""
    check50.c.compile("struct2.c",cc='gcc', lcs50=False)
    
@check50.check()
def struct3_exists():
    """struct3.c exists"""
    check50.exists("struct3.c")
    
@check50.check(struct3_exists)
def struct3_compiles():
    """struct3.c compiles"""
    check50.c.compile("struct3.c",cc='gcc', lcs50=False)

@check50.check()
def struct4_exists():
    """struct4.c exists"""
    check50.exists("struct4.c")
    
@check50.check(struct4_exists)
def struct4_compiles():
    """struct4.c compiles"""
    check50.c.compile("struct4.c",cc='gcc', lcs50=False)
