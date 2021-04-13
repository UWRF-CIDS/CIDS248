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
    
    output = check50.run("echo -n '{}' | ./shell 1>/dev/null".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln 1>/dev/null".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. Make sure to print errors to stderr and not strout.".format(commands.replace("\n", "  ")))
      
@check50.check(shell_compiles)
def check_shell_exit():
    """checking output of shell.c with exit command without exit code"""
    src_file = "shell.c"
    
    commands = "exit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        

@check50.check(check_shell_exit)
def check_shell_exit_code():
    """checking output of shell.c with exit code"""
    src_file = "shell.c"
    
    commands = "exit " + str(random.randint(2,255)) + "\n";
    
    output = check50.run("echo -n '{}' | ./shell > /dev/null; echo $?".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln > /dev/null; echo $?".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. After you exit your shell, use \"echo $?\" to check that your exit code is correct.".format(commands.replace("\n", "  ")))
        
        
@check50.check(check_shell_exit)
def check_shell_exit_code_nonnumeric():
    """checking output of shell.c with exit and non-numeric exit code"""
    src_file = "shell.c"
    
    commands = "exit random" + str(random.randint(2,255)) + "\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell 1>/dev/null".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln 1>/dev/null".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. Make sure errors are printed to stderr and not stdout.".format(commands.replace("\n", "  ")))
                
@check50.check(check_shell_exit)
def check_shell_exit_code_outofrange():
    """checking output of shell.c with exit and exit code out of range"""
    src_file = "shell.c"
    
    commands = "exit " + str(random.randint(256,500)) + "\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell 1>/dev/null".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln 1>/dev/null".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. Make sure errors are printed to stderr and not stdout.".format(commands.replace("\n", "  ")))
               

        
@check50.check(check_shell_exit)
def check_shell_help():
    """checking output of shell.c with help command"""
    src_file = "shell.c"
    
    commands = "help\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
@check50.check(check_shell_exit)
def check_shell_pwd():
    """checking output of shell.c with pwd command"""
    src_file = "shell.c"
    
    commands = "pwd\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
@check50.check(check_shell_exit)
def check_shell_cd():
    """checking output of shell.c with cd command and no directory given"""
    src_file = "shell.c"
    
    commands = "cd\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
@check50.check(check_shell_cd)
def check_shell_cd_dir():
    """checking output of shell.c with 'cd /home'"""
    src_file = "shell.c"
    
    commands = "cd /home\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
    
    
@check50.check(check_shell_cd)
def check_shell_cd_dir_error():
    """checking error output of shell.c with cd and a directory that does not exist"""
    src_file = "shell.c"
    
    commands = "cd dir" + str(random.randint(0,100)) + "\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell 1>/dev/null".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln 1>/dev/null".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}. Make sure errors are printed to stderr.".format(commands.replace("\n", "  ")))


@check50.check(shell_compiles)
def check_shell_echo():
    """checking output of shell.c with command echo"""
    src_file = "shell.c"
    
    commands = "echo\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
@check50.check(check_shell_echo)
def check_shell_echo_hello():
    """checking output of shell.c with command echo hello"""
    src_file = "shell.c"
    
    commands = "echo hello\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
@check50.check(check_shell_echo_hello)
def check_shell_echo_hello_no_newline():
    """checking output of shell.c with command echo hello"""
    src_file = "shell.c"
    
    commands = "echo -n hello\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
@check50.check(check_shell_echo_hello)
def check_shell_echo_abcdefg():
    """checking output of shell.c with command echo a b c d e f g"""
    src_file = "shell.c"
    
    commands = "echo a b c d e f g\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))


@check50.check(check_shell_echo_hello)
def check_shell_abcdefg():
    """checking output of shell.c with command abcdefg"""
    src_file = "shell.c"
    
    commands = "abcdefg\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))



@check50.check(check_shell_echo_hello)
def check_shell_pipe1():
    """checking output of shell.c with command echo "this is a test" | wc"""
    src_file = "shell.c"
    
    commands = "echo \"this is a test\" | wc\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))


@check50.check(check_shell_pipe1)
def check_shell_pipe2():
    """checking output of shell.c with command echo "this is a test" | grep -o t | wc"""
    src_file = "shell.c"
    
    commands = "echo \"this is a test\" | grep -o t | wc\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))

@check50.check(check_shell_pipe1)
def check_shell_pipe_built_in():
    """checking output of shell.c with command pwd | wc -c"""
    src_file = "shell.c"
    
    commands = "pwd | wc -c\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))

@check50.check(check_shell_pipe2)
def check_shell_pipe3():
    """checking output of shell.c with command ls -l | tail -n 3 | grep -o - | wc -l"""
    src_file = "shell.c"
    
    commands = "ls -l | tail -n 3 | grep -o - | wc -l\nexit\n";
    
    output = check50.run("echo -n '{}' | ./shell".format(commands)).stdout()
    soln = check50.run("echo -n '{}' | ./shell_soln".format(commands)).stdout()
    if output != soln:
        raise check50.Failure(help_msg.format(src_file, soln, output) + "Test input was {}.".format(commands.replace("\n", "  ")))
        
