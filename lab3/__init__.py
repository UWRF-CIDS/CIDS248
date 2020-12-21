
import check50
import check50.c


@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")


@check50.check(exists)
def contains_cat():
    """command "cat" is present"""
    output = check50.run("grep -c -w 'cat' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_catolist1():
    """command "cat > list1" is present"""
    output = check50.run("grep -c -w 'cat > list1' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_pear():
    """command "pear" is present"""
    output = check50.run("grep -c -w 'pear' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_banana():
    """command "banana" is present"""
    output = check50.run("grep -c -w 'banana' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_apple():
    """command "apple" is present"""
    output = check50.run("grep -c -w 'apple' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_list2():
    """command "list2" is present"""
    output = check50.run("grep -c -w 'list2' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_orange():
    """command "orange" is present"""
    output = check50.run("grep -c -w 'orange' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_plum():
    """command "plum" is present"""
    output = check50.run("grep -c -w 'plum' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_mango():
    """command "mango" is present"""
    output = check50.run("grep -c -w 'mango' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_grapefruit():
    """command "grapefruit" is present"""
    output = check50.run("grep -c -w 'grapefruit' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_catoolist1():
    """command "cat >> list1" is present"""
    output = check50.run("grep -c -w 'cat >> list1' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_catlist1():
    """command "cat list1" is present"""
    output = check50.run("grep -c -w 'cat list1' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_catlist1list2obiglist():
    """command "cat list1 list2 > biglist" is present"""
    output = check50.run("grep -c -w 'cat list1 list2 > biglist' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_catbiglist():
    """command "cat biglist" is present"""
    output = check50.run("grep -c -w 'cat biglist' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_sort():
    """command "sort" is present"""
    output = check50.run("grep -c -w 'sort' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_artichoke():
    """command "artichoke" is present"""
    output = check50.run("grep -c -w 'artichoke' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_beetroot():
    """command "beetroot" is present"""
    output = check50.run("grep -c -w 'beetroot' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_carrot():
    """command "carrot" is present"""
    output = check50.run("grep -c -w 'carrot' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_sortibiglist():
    """command "sort < biglist" is present"""
    output = check50.run("grep -c -w 'sort < biglist' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_sortibiglistoslist():
    """command "sort < biglist > slist" is present"""
    output = check50.run("grep -c -w 'sort < biglist > slist' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lsl():
    """command "ls -l" is present"""
    output = check50.run("grep -c -w 'ls -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lslotmptxt():
    """command "ls -l > tmp.txt" is present"""
    output = check50.run("grep -c -w 'ls -l > tmp.txt' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_sortitmptxt():
    """command "sort < tmp.txt" is present"""
    output = check50.run("grep -c -w 'sort < tmp.txt' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lslpsort():
    """command "ls -l | sort" is present"""
    output = check50.run("grep -c -w 'ls -l | sort' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lslrwcl():
    """command "ls -l | wc -l" is present"""
    output = check50.run("grep -c -w 'ls -l | wc -l' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lslists():
    """command "ls list*" is present"""
    output = check50.run("grep -c -w 'ls list*' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lsslist():
    """command "ls *list" is present"""
    output = check50.run("grep -c -w 'ls *list' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_lsqlist():
    """command "ls ?list" is present"""
    output = check50.run("grep -c -w 'ls ?list' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_manwc():
    """command "man wc" is present"""
    output = check50.run("grep -c -w 'man wc' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_whatiswc():
    """command "whatis wc" is present"""
    output = check50.run("grep -c -w 'whatis wc' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)



@check50.check(exists)
def contains_aproposcopy():
    """command "apropos copy" is present"""
    output = check50.run("grep -c -w 'apropos copy' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)


