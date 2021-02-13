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
def tictactoe_exists():
    """tictactoe.c exists"""
    check50.exists("tictactoe.c")
    check50.include("tictactoe_soln")
    
@check50.check(tictactoe_exists)
def tictactoe_compiles():
    """tictactoe.c compiles"""
    check50.c.compile("tictactoe.c",cc='gcc', lcs50=False)
      
@check50.check(tictactoe_compiles)
def check_tictactoe():
    """checking output of tictactoe.c"""
    src_file = "tictactoe.c"
    input1 = random.randint(0,8)
    input2 = 9
    output = check50.run("echo '{}\n{}\n' | ./tictactoe".format(input1, input2)).stdout()
    soln = check50.run("echo '{}\n{}\n' | ./tictactoe_soln".format(input1, input2)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + " Test input was {}, {}.".format(input1, input2))
      
