import check50
import check50.c

@check50.check()
def exists():
    """typescript exists"""
    check50.exists("typescript")

@check50.check(exists)
def contains_ls():
    """ls ✓"""
    check50.run("grep -c -w 'ls' typescript").stdout("1")

@check50.check(exists)
def contains_lsa():
    """ls -a ✓"""
    check50.run("grep -c -w 'ls -a' typescript").stdout("1")
  
@check50.check(exists)
def contains_mkdir():
    """mkdir ✓"""
    check50.run("grep -c -w 'mkdir' typescript").stdout("1")
   
@check50.check(exists)
def contains_cd():
    """cd ✓"""
    check50.run("grep -c -w 'cd' typescript").stdout("1")
   
@check50.check(exists)
def contains_cdtilde():
    """cd ~ ✓"""
    check50.run("grep -c -w 'cd ~' typescript").stdout("1")
    
@check50.check(exists)
def contains_cddotdot():
    """cd .. ✓"""
    check50.run("grep -c -w 'cd ..' typescript").stdout("1")   
    
@check50.check(exists)
def contains_pwd():
    """pwd ✓"""
    check50.run("grep -c -w 'pwd' typescript").stdout("1")
