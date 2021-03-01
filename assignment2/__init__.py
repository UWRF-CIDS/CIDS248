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
def check_shell1():
    """checking output of shell.c with invalid input"""
    src_file = "shell.c"
    
    commands = ""
    for i in range(random.randint(3,5)):
        commands = commands + "cmd{}\n".format(random.randint(0,100))

    commands = commands + "exit\n"
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
      
@check50.check(shell_compiles)
def check_shell_exit():
    """checking output of shell.c with exit command without exit code"""
    src_file = "shell.c"
    
    commands = "exit\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        

@check50.check(check_shell_exit)
def check_shell_exit_code():
    """checking output of shell.c with exit code"""
    src_file = "shell.c"
    
    commands = "exit " + str(random.randint(2,255)) + "\n";
    
    output = check50.run("echo '{}' | ./shell > /dev/null; echo $?".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln > /dev/null; echo $?".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. After you exit your shell, use \"echo $?\" to check that your exit code is correct.".format(commands.replace("\n", "  ")))
        
@check50.check(shell_compiles)
def check_shell_help():
    """checking output of shell.c with help command"""
    src_file = "shell.c"
    
    commands = "help\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
@check50.check(shell_compiles)
def check_shell_pwd():
    """checking output of shell.c with pwd command"""
    src_file = "shell.c"
    
    commands = "pwd\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
@check50.check(shell_compiles)
def check_shell_cd():
    """checking output of shell.c with cd command and no directory given"""
    src_file = "shell.c"
    
    commands = "cd\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
@check50.check(check_shell_cd)
def check_shell_cd_dir():
    """checking output of shell.c with 'cd /home'"""
    src_file = "shell.c"
    
    commands = "cd /home\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
    
@check50.check(check_shell_cd)
def check_shell_cd_dir_error():
    """checking error output of shell.c with cd and a directory that does not exist"""
    src_file = "shell.c"
    
    commands = "cd dir" + random.randint(0,100)) + "\n";
    
    output = check50.run("echo '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
