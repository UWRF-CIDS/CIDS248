
import check50
import check50.c


@check50.check()
def exists():
    """files exist"""
    check50.exists("redir.c")
    check50.exists("input.txt")

@check50.check(exists)
def compiles():
    """redir.c compiles"""
    check50.c.compile("redir.c", lreadline=True, lcs50=True)

@check50.check(compiles)
def emma():
    check50.run("./redir").exit()

@check50.check(compiles)
def contains_cat():
    """Reads input.txt and outputs first line to tmp.txt"""
    check50.run("./redir")
    with open("input.txt", "w") as f1:
        with open("tmp.txt", "w") as f2:
            if f1.readline() != f2.readline():
		          help = "no bueno"
                raise check50.Failure(help)