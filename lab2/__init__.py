import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")

@check50.check(exists)
def contains_cp():
    """command "cp" is present"""
    output = check50.run("grep -c -w 'cp' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

@check50.check(exists)
def contains_mv():
    """command "mv" is present"""
    output = check50.run("grep -c -w 'mv' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

@check50.check(exists)
def contains_rm():
    """command "rm" is present"""
    output = check50.run("grep -c -w 'rm' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_rmdir():
    """command "rmdir" is present"""
    output = check50.run("grep -c -w 'rmdir' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_cat():
    """command "cat" is present"""
    output = check50.run("grep -c -w 'cat' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
    
@check50.check(exists)
def contains_more():
    """command "more" is present"""
    output = check50.run("grep -c -w 'more' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

    
@check50.check(exists)
def contains_head():
    """command "head" is present"""
    output = check50.run("grep -c -w 'head' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
@check50.check(exists)
def contains_tail():
    """command "tail" is present"""
    output = check50.run("grep -c -w 'tail' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_grep():
    """command "grep" is present"""
    output = check50.run("grep -c -w 'grep' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        

@check50.check(exists)
def contains_wc():
    """command "wc" is present"""
    output = check50.run("grep -c -w 'wc' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        

@check50.check(exists)
def contains_man():
    """command "man" is present"""
    output = check50.run("grep -c -w 'man' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        
@check50.check(exists)
def contains_whatis():
    """command "whatis" is present"""
    output = check50.run("grep -c -w 'whatis' typescript").stdout()   
    if output == "0\n":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
