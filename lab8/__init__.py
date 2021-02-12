import check50
import check50.c
import random





@check50.check()
def table_exists():
    """table.c exists"""
    check50.exists("table.c")
    check50.include("table_soln")
    
@check50.check()
def strings1_exists():
    """strings1.c exists"""
    check50.exists("strings1.c")
    check50.include("strings1_soln")
    
@check50.check()
def strings2_exists():
    """strings2.c exists"""
    check50.exists("strings2.c")
    check50.include("strings2_soln")

@check50.check()
def strings3_exists():
    """strings3.c exists"""
    check50.exists("strings3.c")
    check50.include("strings3_soln")
    
@check50.check()
def input_exists():
    """input.c exists"""
    check50.exists("input.c")
    check50.include("input_soln")

@check50.check(table_exists)
def table_compiles():
    """table.c compiles"""
    check50.c.compile("table.c", lcs50=False)

@check50.check(table_compiles)
def check_table():
    """checking output of table.c"""
    output = check50.run("./table").stdout()
    soln = check50.run("./table_soln").stdout()
    if output != soln:
        raise check50.Failure("Output of table.c does not match the solution.")
      