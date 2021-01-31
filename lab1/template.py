
@check50.check(exists)
def contains_lsqlist():
    """command "????" is present"""
    output = check50.run("grep -c -w '????' typescript").stdout()
    if output == "0\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

