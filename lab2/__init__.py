import check50
import check50.c

cp file1 file2 	copy file1 and call it file2
mv file1 file2 	move or rename file1 to file2
rm file 	remove a file
rmdir directory 	remove a directory
cat file 	display a file
more file 	display a file a page at a time
head file 	display the first few lines of a file
tail file 	display the last few lines of a file
grep 'keyword' file 	search a file for keywords
wc file


@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")

@check50.check(exists)
def contains_cp():
    """command "cp" is present"""
    output = check50.run("grep -c -w 'cp' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

@check50.check(exists)
def contains_mv():
    """command "mv" is present"""
    output = check50.run("grep -c -w 'mv' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
  
@check50.check(exists)
def contains_rm():
    """command "rm" is present"""
    output = check50.run("grep -c -w 'rm' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_rmdir():
    """command "rmdir" is present"""
    output = check50.run("grep -c -w 'rmdir' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
   
@check50.check(exists)
def contains_cat():
    """command "cat" is present"""
    output = check50.run("grep -c -w 'cat' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
    
@check50.check(exists)
def contains_more():
    """command "more" is present"""
    output = check50.run("grep -c -w 'more' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

    
@check50.check(exists)
def contains_head():
    """command "head" is present"""
    output = check50.run("grep -c -w 'head' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        
@check50.check(exists)
def contains_tail():
    """command "tail" is present"""
    output = check50.run("grep -c -w 'tail' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_grep():
    """command "grep" is present"""
    output = check50.run("grep -c -w 'grep' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        

@check50.check(exists)
def contains_wc():
    """command "wc" is present"""
    output = check50.run("grep -c -w 'wc' typescript").stdout()   
    if output == "0":
        help = "Make sure that you have tried all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
