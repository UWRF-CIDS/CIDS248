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
def contains_cd():
    """cd ✓"""
    check50.run("grep -c -w 'cd' typescript").stdout("1")
