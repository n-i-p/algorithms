def run_tests(func):
    import os
    import sys
    problem_path = os.path.dirname(sys.argv[0])
    tests_path = os.path.join(problem_path, 'tests')
    infiles = [fn for fn in os.listdir(tests_path) if fn.endswith('.in')]
    for infile in infiles:
        outfile = infile.replace('.in', '.out')
        with open(os.path.join(tests_path, infile), 'r') as fin:
            with open(os.path.join(tests_path, outfile), 'r') as fout:
                din = fin.read()
                dout = fout.read()
                func_ret = func(din)
                if dout != func_ret:
                    print(f'FAILED {infile}:\n{din}\n')
                    print(f'EXPECTED {outfile}:\n{dout}\n')
                    print(f'FUNCTION RETURNED:\n{func_ret}\n')
                else:
                    print(f'OK: {infile}')
    print(f'Tests Run: {len(infiles)}')
