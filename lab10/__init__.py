import check50
import check50.c
import random



help_msg = '''Output of {} does not match the solution.

Expected: 
{}

Found: 
{}
'''



@check50.check()
def myStrlen_exists():
    """myStrlen.c exists"""
    check50.exists("myStrlen.c")
    check50.include("myStrlen_soln")
    
@check50.check(myStrlen_exists)
def myStrlen_compiles():
    """myStrlen.c compiles"""
    check50.c.compile("myStrlen.c",cc='gcc', lcs50=False)
      
@check50.check(myStrlen_compiles)
def check_myStrlen():
    """checking output of myStrlen.c"""
    src_file = "myStrlen.c"
    input1 = random.randint(1,100000)
    output = check50.run("./myStrlen {}".format(input1)).stdout()
    soln = check50.run("./myStrlen_soln {}".format(input1)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + " Test input was {}.".format(input1))
      



@check50.check()
def myStrchr_exists():
    """myStrchr.c exists"""
    check50.exists("myStrchr.c")
    check50.include("myStrchr_soln")
    
@check50.check(myStrchr_exists)
def myStrchr_compiles():
    """myStrchr.c compiles"""
    check50.c.compile("myStrchr.c",cc='gcc', lcs50=False)
      
@check50.check(myStrchr_compiles)
def check_myStrchr():
    """checking output of myStrchr.c"""
    src_file = "myStrchr.c"
    input1 = random.randint(1,100000)
    input2 = random.randint(0,10)
    
    output = check50.run("./myStrchr {} {}".format(input1, input2)).stdout()
    soln = check50.run("./myStrchr_soln {} {}".format(input1, input2)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + " Test input was {} {}.".format(input1, input2))
        
        
        
@check50.check()
def myAtoi_exists():
    """myAtoi.c exists"""
    check50.exists("myAtoi.c")
    check50.include("myAtoi_soln")
    
@check50.check(myAtoi_exists)
def myAtoi_compiles():
    """myAtoi.c compiles"""
    check50.c.compile("myAtoi.c",cc='gcc', lcs50=False)
      
@check50.check(myAtoi_compiles)
def check_myAtoi():
    """checking output of myAtoi.c"""
    src_file = "myAtoi.c"
    sign = random.randint(0, 1) == 0 ? -1 : 1; 
        input1 = random.randint(1,100000) * sign
    output = check50.run("./myAtoi {}".format(input1)).stdout()
    soln = check50.run("./myAtoi_soln {}".format(input1)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + " Test input was {}.".format(input1))
      
