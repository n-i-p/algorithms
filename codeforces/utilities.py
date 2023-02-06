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
                fret = func(din)
                if dout == fret:
                    print(f'-OK-: {infile}')
                else:
                    print(f'FAIL: {infile}:')
                    dout_lines = dout.split('\n')
                    fret_lines = fret.split('\n')
                    max_len = max([len(dout_line) for dout_line in dout_lines])
                    for dout_line, fret_line in zip(dout_lines, fret_lines):
                        msg = '-ok-'
                        if dout_line != fret_line:
                            msg = 'DIFF'
                        log = '{{msg}} {{dout_line:{max_len}}} {{fret_line:{max_len}}}'
                        print(log.format(max_len=max_len).format(msg=msg, dout_line=dout_line, fret_line=fret_line))
    print(f'Tests Run: {len(infiles)}')


def generate(problem_id, number_of_tests):
    import os
    os.makedirs(f'{problem_id}/tests', exist_ok=True)
    for number in range(1, number_of_tests + 1):
        open(f'{problem_id}/tests/{problem_id}_{number:>02}.in', 'w').close()
        open(f'{problem_id}/tests/{problem_id}_{number:>02}.out', 'w').close()
    with open(f'template.py', 'r') as f:
        with open(f'{problem_id}/{problem_id}.py', 'w') as g:
            g.write(f.read().replace('/?/?', f'/{problem_id[:-1]}/{problem_id[-1]}'))


if __name__ == '__main__':
    generate(input("Problem id: "), int(input('Number of tests: ')))
