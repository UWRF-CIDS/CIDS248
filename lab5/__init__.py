
import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")



@check50.check(exists)
def contains_cat1():
    """command "cat /etc/passwd" is present"""
    output = check50.run("grep -c -w 'cat /etc/passwd' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)




#cat /etc/passwd | head -n 1
@check50.check(exists)
def contains_cat2():
    """command "cat /etc/passwd | head -n 1" is present"""
    output = check50.run("grep -c -w 'cat /etc/passwd | head -n 1' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
        

#cut
@check50.check(exists)
def contains_cut():
    """command "cut" is present"""
    output = check50.run("grep -c -w 'cut' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

#tr
@check50.check(exists)
def contains_tr():
    """command "tr" is present"""
    output = check50.run("grep -c -w 'tr' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


#awk '{ print length }'
@check50.check(exists)
def contains_awk():
    """command "awk" is present"""
    output = check50.run("grep -c -w 'awk' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

#sort -n | uniq -c
@check50.check(exists)
def contains_su():
    """command "sort -n | uniq -c" is present"""
    output = check50.run("grep -c -w 'sort -n | uniq -c' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

#> data.csv
@check50.check(exists)
def contains_redir():
    """command "> data.csv" is present"""
    output = check50.run("grep -c -w '> data.csv' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

#wget
@check50.check(exists)
def contains_wget():
    """command "wget" is present"""
    output = check50.run("grep -c -w 'wget' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


#unzip
@check50.check(exists)
def contains_unzip():
    """command "unzip" is present"""
    output = check50.run("grep -c -w 'unzip' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)
