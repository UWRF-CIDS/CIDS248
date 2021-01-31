
import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")



@check50.check(exists)
def contains_lsl():
    """command "ls -l" is present"""
    output = check50.run("grep -c -w 'ls -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_chmod1():
    """command "chmod go-rwx" is present"""
    output = check50.run("grep -c -w 'chmod go-rwx' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_chmod2():
    """command "chmod a+rw" is present"""
    output = check50.run("grep -c -w 'chmod a+rw' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_ps():
    """command "ps" is present"""
    output = check50.run("grep -c -w 'ps' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_sleep():
    """command "sleep" is present"""
    output = check50.run("grep -c -w 'sleep' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_sleep2():
    """command "sleep 100 &" is present"""
    output = check50.run("grep -c -w 'sleep 100 &' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_jobs():
    """command "jobs" is present"""
    output = check50.run("grep -c -w 'jobs' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_fg():
    """command "fg" is present"""
    output = check50.run("grep -c -w 'fg' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_kill():
    """command "kill" is present"""
    output = check50.run("grep -c -w 'kill' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_kill2():
    """command "kill -l" is present"""
    output = check50.run("grep -c -w 'kill -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


