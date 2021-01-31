
import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")



@check50.check(exists)
def contains_echo():
    """command "echo {A..Z} > alphabet" is present"""
    output = check50.run("grep -c -w 'echo {A..Z} > alphabet' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_xxd1():
    """command "xxd -b" is present"""
    output = check50.run("grep -c -w 'xxd -b' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_xxd2():
    """command "xxd" is present"""
    output = check50.run("grep -c -w 'xxd' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)




@check50.check(exists)
def contains_xxd3():
    """command "xxd -p" is present"""
    output = check50.run("grep -c -w 'xxd -p' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)




@check50.check(exists)
def contains_cat():
    """command "cat hexfile" is present"""
    output = check50.run("grep -c -w 'cat hexfile' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_xxd4():
    """command "xxd -p -r hexfile" is present"""
    output = check50.run("grep -c -w 'xxd -p -r hexfile' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        
        
@check50.check(exists)
def contains_xxd5():
    """command "xxd dog.png | less" is present"""
    output = check50.run("grep -c -w 'xxd dog.png | less' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        
        
        
        
                
@check50.check(exists)
def contains_grep():
    """command "xxd -p data.raw | grep -b 89504e470d0a1a0a" is present"""
    output = check50.run("grep -c -w 'xxd -p data.raw | grep -b 89504e470d0a1a0a' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        


        
@check50.check(exists)
def contains_xxd6():
    """command "xxd -p data.raw | tail -c +183 | xxd -p -r > image.png" is present"""
    output = check50.run("grep -c -w 'xxd -p data.raw | tail -c +183 | xxd -p -r > image.png' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        
        
        
        
        
@check50.check(exists)
def contains_xxd7():
    """command "xxd -l 90 -p /dev/random" is present"""
    output = check50.run("grep -c -w 'xxd -l 90 -p /dev/random' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        

@check50.check(exists)
def contains_xxd8():
    """command "xxd -p -r data.hex > myData.raw" is present"""
    output = check50.run("grep -c -w 'xxd -p -r data.hex > myData.raw' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
        
        
        
