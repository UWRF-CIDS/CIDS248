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
def check_shell_echo_outfile():
    """checking output of shell.c with command echo hello > outfile"""
    src_file = "shell.c"
    
    commands = "echo hello > outfile\ncat outfile\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        

@check50.check(check_shell_echo_outfile)
def check_shell_cat_infile():
    """checking output of shell.c with command cat < outfile"""
    src_file = "shell.c"
    
    commands = "cat < outfile\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        

@check50.check(check_shell_cat_infile)
def check_shell_cat_in_out_file():
    """checking output of shell.c with command cat < outfile > outfile2"""
    src_file = "shell.c"
    
    commands = "cat < outfile > outfile2\ncat outfile2\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        

