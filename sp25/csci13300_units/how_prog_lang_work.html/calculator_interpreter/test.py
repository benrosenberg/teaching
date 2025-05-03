import interpreter

# dictionary from input to expected output
tests = {
    "1": 1,
    "(1)": 1,
    "1 - 1": 0,
    "1-1": 0,
    "1 * 2": 2,
    "-1 + 3": 2,
    "3 * -1": -3,
    "3*-1": -3,
    "(1 + 2)": 3,
    "(1 + 2) * 3": 9,
    "1 + 2 * 3": 7,
    "1 / 0": None,
    "(": None,
    ")": None,
    "1 + 2": 3,
    "4 - 3 - 1": 0,
    "2 * 3 + 1": 7,
    "2 + 3 * 4": 14,
    "(2 + 3) * 4": 20,
    "-5 + 3": -2,
    "-(2 + 3)": -5,
    "10 / 2": 5,
    "20 / 3": 6,
    "((1 + 2) * (3 + 4))": 21,
    "(((((5)))))": 5,
    "1 + -2": -1,
    "-(1 + -2)": 1,
    "": None,
    "2 +": None,
    "+ 2": None,
    "(1 + 2": None,
    "1 + 2)": None,
    "1 / 0": None,
    "1 + (2 * )": None,
    "3 * (4 + )": None,
    "--5": 5,
    "abc + 1": None,
    "1 + 2 3": None,
    "1 + (2 + 3": None,
}


def run_tests(verbose=False):
    passed_tests = []
    failed_tests = []
    failure_strs = []

    for i, (test, expected) in enumerate(tests.items()):
        if verbose:
            print("Running test {}".format(i))
            print('Test program:', test)
        result = interpreter.interpret(test, verbose=verbose)
        if result != expected:
            failed_tests.append(i)
            failure_str = "Failed test {}: expected {}, got {} on input {}".format(
                i, expected, result, test
            )
            failure_strs.append(failure_str)
            if verbose:
                print(failure_str)
        else:
            if verbose:
                print("Passed test {}".format(i))
            passed_tests.append(i)

    print("Passed {}/{} tests".format(len(passed_tests), len(tests)))
    if failure_strs:
        print("Failures:")
        print("\n".join(failure_strs))
    else:
        print("No failed tests.")
