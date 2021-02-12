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

@check50.check(strings1_exists)
def strings1_compiles():
    """strings1.c compiles"""
    check50.c.compile("strings1.c", lcs50=False)

@check50.check(strings2_exists)
def strings2_compiles():
    """strings2.c compiles"""
    check50.c.compile("strings2.c", lcs50=False)
    
@check50.check(strings3_exists)
def strings3_compiles():
    """strings3.c compiles"""
    check50.c.compile("strings3.c", lcs50=False)
    
@check50.check(input_exists)
def input_compiles():
    """input.c compiles"""
    check50.c.compile("input.c", lcs50=False)
    
    
@check50.check(table_compiles)
def check_table():
    """checking output of table.c"""
    output = check50.run("./table").stdout()
    soln = check50.run("./table_soln").stdout()
    if output != soln:
        raise check50.Failure("Output of table.c does not match the solution.")
      

@check50.check(strings1_compiles)
def check_strings1():
    """checking output of strings1.c"""
    output = check50.run("./strings1").stdout()
    soln = check50.run("./strings1_soln").stdout()
    if output != soln:
        raise check50.Failure("Output of strings1.c does not match the solution.")

@check50.check(strings2_compiles)
def check_strings2():
    """checking output of strings2.c"""
    output = check50.run("./strings2").stdout()
    soln = check50.run("./strings2_soln").stdout()
    if output != soln:
        raise check50.Failure("Output of strings2.c does not match the solution.")
        
@check50.check(strings3_compiles)
def check_strings3():
    """checking output of strings3.c"""
    output = check50.run("./strings3").stdout()
    soln = check50.run("./strings3_soln").stdout()
    if output != soln:
        raise check50.Failure("Output of strings3.c does not match the solution.")
        
@check50.check(input_compiles)
def check_input():
    """checking output of input.c"""
    rand = random.uniform(0, 1)*50
    output = check50.run("echo '{}' | ./input".format(rand)).stdout()
    soln = check50.run("echo '{}' | ./input_soln".format(rand)).stdout()
    if output != soln:
        raise check50.Failure("Output of input.c does not match the solution. Test input used is {}".format(rand))
