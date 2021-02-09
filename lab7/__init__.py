
import check50
import check50.c
import random



ANALYZE_HASHES = [
    "4dd4d660b98d937c605438faf9bd28b26eb14fc0e8839cb796d44956e09161b0",  # outfile.csv
    ]

STARS_HASHES = [
    "44ce43166b9ec08501e42eeb69a4d5fc3bfbb1de44accb208031e5218ba5c588",
    "ff5d3b96487086155a2bc1c62dfcc8022a31dd97b0adba25dc27007629cc49a0",
    "927e8b4acd8533cb8852f70710a64a5a336c3d7005033ff853d7247280d44299",
    "d763410738f89708bcb09d15b3eb5f337b674ef51a96ba1d9d9469c2f739be59",
    "6eb587bfb85e7c1b8040d76dd0d7ccfdcdbfde7ceaf1e2fad6b5eba9a908e783",
    "7c8dd0d08723de2270749abf47c83023926d4c7a1de9c6fff9a3d6a4d2de8c0e",
    "0ef9f5f4c0b079fc28083a50948c1b80c9d3dc6be26e154ffbc4242328d61399",
    "9a9d0d7822690bb04ed23f17b0d3e49126fa42f55a30d515bec02a6781a1b83b",
    "8c85b0f8a51c92c95af5c2c7d82f3bc00341199df283c036ea056ff8a6b0bfc9",
    "9a90582ef445f25db303566798559d608fbfd74a68920fbcc2851713a95bed39",
    "adf3ddb5a73dffb51874fb81b71a5c7faf08b392613745d4564323da1bbf87c6",
    "b9d4be8b2d2f8c99a2445edaf38f8fc932e70943aa76fdaf3d06baca7720c380",
    "82cf8f85135df8babc797464f33951392392c6b9a2a6e4d60df4eea8a8910009",
    "e37db34046b5952d4d996dcfc095b12aa66c2ab2f36b8fcd7f05ffc531485b72",
    "7371598ff426cdee76d8e9affb67e40766437dac2e19e7a73b43193886db4a96",
    "429f94bd7a76f52afd187552796e1baa9c364a101d86a1d2d26428ee00f2a940",
    "f111fda9fe34f1841089ea03439250538312f031b5b272c2f9c6ff54f4a78343",
    "69923f6c4215b4acd1b62ccbb615d29f7dedb1de15ff07262d963ac69eaa3003",
    "5b8d99e852ac9f0ca4429618c88a3d10ecf4a77c90a6a651cb8de110bfb3f045",
    "6361d6686fb2db8ee60388a178b331b29a48294954579f4ba3e0ca210f900199",
    "10a3733b68fc84e11f24d79232f4787d7b592b70b4bde21ba22153d0418d9759",
    "5b8495be06a2eafbe103165eb1443dc972a94090975244dd2eb027572bc0fe16",
    "f31256a0842b85b1e3ad01f877524228cde9bcedc6191ff00ff2f150b2593436",
    "c445050e8bcfcd6265a54c52eba86c430d36450f0e1e3d92cbfbd23624e9369f",
    "e5f887023f8911bd0adecf5832de085af0520071b80f4897c9c5ac259b91a627",
    "78362d44d44ac67d2f7470331540cbcfa2804310e2140b0a0e4ef8ee26492e66",
    "a34314ccf0338055b6752a974c991910e22a6f2ff04afcebec91e3123c758468",
    "f4a7d73fa7d0332b1492372be9a84c1309171a97465e8e483cd9f13b17532f48",
    "5f61ce059025751b415dd03f36e6cb0faf115ae7c6e5690d934964a5f909dc94",
    "be42b1bdc9da525ed1f1788b61325210638afe52296710e792731f2fc3b02c58",
    "b90834f325164c7bacdf9f82fb997dcf5ea8a3fd77e6a43488764d49b4acb97d",
    "cad45cc653e5bf091909d40bd4ad0d249b8b0445615ff2770563fd871de825c6",
    "e13d5370ef56b56ec820d6f160964a72b07da7b8c7eec67c2de3db1fcf9bc730",
    "7ac7d282f7c2eafda135db70da9ff291682d4f15a9d98548fabfd1059e0369ff",
    "0cc07867d40a78932d4148f441a25648354397bfed34bc84001018fdb7c2b6d9",
    "848ee45f6348f030ec2f87b2e252dba8284d2d8dafad8dc61c982de23141603a",
    "e3d33c33ad136f3c2c5b098f8cee170b0e5ef462bc4498f8c31ec0d9ab5c5241",
    "6c58d95a3c7b9dc608dd9b770373824e13dad688886550f2f18fd4dd6d1e933d",
    "2a3ac342d8da985e16f21f8fc72e75b99dc6e9ace9ab25d57c4252c0233e7cf1",
    "4d7a2f4fd3c06c020fdf7455e7a539dc1afb7447a63746f7099ed8bc8173c327",
    "84b4278ed0e9497890bc27f66e2ad4e6c2a6cab463e77261ba9b9d0001aa0b5c",
    "13e16c0f86ba45c5a31206ab1a12a12a96891a3ec47ec9eb820b7ad0a762c803",
    "f07a12ecd3f3dc4afc5d072cbeb92889654d922c9815c5aaf8605f6dbf3537a4",
    "67aec9c4265d59645a7ecf9842683c464ac1bdab75aa637bc96eb8fdc374ee37",
    "d342ff916abb8236889a94d89dc743c6734bd3f1911a056919ac021123aeff75",
    "b07ea6d9a9004faab8851bd4f506bf800ee89f2e60d1abdf0d3360c47c9aca33",
    "961e228ade56f590e0df864f81427577311f62212ebe930d6370e45dad7387d3",
    "56f4bebaa353849853a766902fc4b9f21ebcf194f10688831064e2614b1ec8f9",
    "b1ebc70295d3ea47b113f17fec3976d212a09bca348a5d9d80415ff5f4dddbe9",
    "f649d020cf0b1788d5ce071ccce31a8fdbe2395cdce79b073c48fed4ace8a236",
    "8a59e3d4107c7bdb0983e15a2102abd76995f1f54e579009b518b62056a913b5",
    ]

@check50.check()
def analyzeExists():
    """Checking if analyze.sh file exists"""
    check50.exists("analyze.sh")
    check50.include("sample.txt")
    output = check50.run("xxd -p -l 1 analyze.sh").stdout()
    if output != "23\n":
        raise check50.Failure("It looks like you tried to submit the solution file. Please make sure you are in the correct directory when you run the checks.")

    
@check50.check()
def calcExists():
    """Checking if calc.sh file exists"""
    check50.exists("calc.sh")
    
@check50.check()
def starsExists():
    """Checking if stars.sh file exists"""
    check50.exists("stars.sh")


@check50.check()
def menuExists():
    """Checking if menu.sh file exists"""
    check50.exists("menu.sh")
    check50.include("menu.sh.x")




@check50.check(analyzeExists)
def check_analyze():
    """Checking analyze.sh"""
    output = check50.run("./analyze.sh sample.txt outfile.csv").stdout()
    if check50.hash("outfile.csv") != ANALYZE_HASHES[0]:
        raise check50.Failure("Tried running ./analyze.sh sample.txt outfile.csv. outfile.csv did not contain the correct data.")
    

@check50.check(calcExists)
def check_calc1():
    """Checking calc.sh"""
    output = check50.run("./calc.sh 10 5 /").stdout()
    if output != "2\n":
        raise check50.Failure("Tried running ./calc.sh 10 5 /. The output was not 2.")


@check50.check(calcExists)
def check_calc2():
    """Checking calc.sh exit code."""
    code = check50.run("./calc.sh 10 5 a &>/dev/null; echo $?").stdout()
    if code != "3\n":
        raise check50.Failure("Tried running ./calc.sh 10 5 a. The exit code was not 3.")

@check50.check(calcExists)
def check_calc3():
    """Checking calc.sh error message."""
    output = check50.run("./calc.sh 10 5 a 2>&1").stdout()
    if output.strip() != "The third argument must be +, -, *, /!":
        raise check50.Failure("Tried running ./calc.sh 10 5 a. The error message is not correct.")
        
        
@check50.check(calcExists)
def check_calc4():
    """Checking calc.sh exit code."""
    code = check50.run("./calc.sh 10 a + &>/dev/null; echo $?").stdout()
    if code != "2\n":
        raise check50.Failure("Tried running ./calc.sh 10 a +. The exit code was not 2.")

@check50.check(calcExists)
def check_calc5():
    """Checking calc.sh error message."""
    output = check50.run("./calc.sh 10 a + 2>&1").stdout()
    if output.strip() != "The first two arguments must be numeric!":
        raise check50.Failure("Tried running ./calc.sh 10 a +. The error message is not correct.")

        
@check50.check(calcExists)
def check_calc6():
    """Checking calc.sh exit code."""
    code = check50.run("./calc.sh 1 2 &>/dev/null; echo $?").stdout()
    if code != "1\n":
        raise check50.Failure("Tried running ./calc.sh 1 2. The exit code was not 1.")

@check50.check(calcExists)
def check_calc7():
    """Checking calc.sh error message."""
    output = check50.run("./calc.sh 1 2 2>&1").stdout()
    if output.strip() != "Incorrect number of arguments!":
        raise check50.Failure("Tried running ./calc.sh 1 2. The error message is not correct.")
        
        
@check50.check(starsExists)
def check_stars():
    """Checking stars.sh output using random input."""
    num = random.randint(5,55)
    output = check50.run("./stars.sh " + str(num) + " > stars.out").stdout()
    
    if check50.hash("stars.out") != STARS_HASHES[num - 5]: #index for STARS_HASHES start at 0
        raise check50.Failure("Tried running ./stars.sh " + str(num) + ". The output is not correct.")
        
        
@check50.check(menuExists)
def check_menu():
    """Checking menu.sh output using each input."""
    output = check50.run('./menu.sh < testinput').stdout()
    correct = check50.run('./menu.sh.x < testinput').stdout()
    
    if output.strip() != correct.strip(): 
        raise check50.Failure('Tried running echo -e "1\\n2\\n3\\n4\\n" | ./menu.sh. The output is not correct.')
