import check50
import check50.c
import random





@check50.check()
def table_exists():
    """table.c exists"""
    check50.exists("table.c")
    check50.include("table_soln")

@check50.check(exists)
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
      
