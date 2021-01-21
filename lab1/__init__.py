import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")

@check50.check(exists)
def contains_ls():
    """command "ls" is present"""
    output = check50.run("grep -c -w 'ls' typescript").stdout()
    raise check50.Failure("DB '" + output + "'")
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

@check50.check(exists)
def contains_lsa():
    """command "ls -a" is present"""
    output = check50.run("grep -c -w 'ls -a' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
  
@check50.check(exists)
def contains_mkdir():
    """command "mkdir" is present"""
    output = check50.run("grep -c -w 'mkdir' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_cd():
    """command "cd" is present"""
    output = check50.run("grep -c -w 'cd' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_cdtilde():
    """command "cd ~" is present"""
    output = check50.run("grep -c -w 'cd ~' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
    
@check50.check(exists)
def contains_cddotdot():
    """command "cd .." is present"""
    output = check50.run("grep -c -w 'cd ..' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

    
@check50.check(exists)
def contains_pwd():
    """command "pwd" is present"""
    output = check50.run("grep -c -w 'pwd' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
