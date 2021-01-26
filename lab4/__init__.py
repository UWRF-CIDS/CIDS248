
import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")



@check50.check(exists)
def contains_lsqlist():
    """command "ls -l" is present"""
    output = check50.run("grep -c -w 'ls -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "chmod go-rwx" is present"""
    output = check50.run("grep -c -w 'chmod go-rwx' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "chmod a+rw" is present"""
    output = check50.run("grep -c -w 'chmod a+rw' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "ps" is present"""
    output = check50.run("grep -c -w 'ps' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "sleep 10" is present"""
    output = check50.run("grep -c -w 'sleep 10' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "sleep 10 ????" is present"""
    output = check50.run("grep -c -w 'sleep 10 ????' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "sleep 100" is present"""
    output = check50.run("grep -c -w 'sleep 100' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "bg" is present"""
    output = check50.run("grep -c -w 'bg' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "jobs" is present"""
    output = check50.run("grep -c -w 'jobs' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "fg" is present"""
    output = check50.run("grep -c -w 'fg' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "kill" is present"""
    output = check50.run("grep -c -w 'kill' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "kill -l" is present"""
    output = check50.run("grep -c -w 'kill -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


@check50.check(exists)
def contains_lsqlist():
    """command "kill -9" is present"""
    output = check50.run("grep -c -w 'kill -9' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

