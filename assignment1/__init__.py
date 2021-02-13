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
def shell_exists():
    """shell.c exists"""
    check50.exists("shell.c")
    check50.include("shell_soln")
    
@check50.check(shell_exists)
def shell_compiles():
    """shell.c compiles"""
    check50.c.compile("shell.c",cc='gcc', lcs50=False)
      
@check50.check(shell_compiles)
def check_shell():
    """checking output of shell.c"""
    src_file = "shell.c"
    
    commands = ""
    for i in range(random.randint(3,5)):
        commands = commands + "cmd{}\n".format(random.randint(0,100))

    commands = commands + "exit\n"
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  "))
      
