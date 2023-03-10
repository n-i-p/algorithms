import os
import re
import sys

import bs4
import requests


def run_tests(func):
    problem_path = os.path.dirname(sys.argv[0])
    tests_path = os.path.join(problem_path, 'tests')
    infiles = [fn for fn in os.listdir(tests_path) if fn.endswith('.in')]
    for infile in infiles:
        outfile = infile.replace('.in', '.out')
        with open(os.path.join(tests_path, infile), 'r') as fin:
            with open(os.path.join(tests_path, outfile), 'r') as fout:
                din = fin.read()
                dout = fout.read()
                fret = func(din.split('\n')[:-1])
                if dout.strip() == fret.strip():
                    print(f'-OK-: {infile}')
                else:
                    print(f'FAIL: {infile}:')
                    print(f'CHCK <expected_value> <returned_value>')
                    dout_lines = dout.split('\n')
                    fret_lines = fret.split('\n')
                    max_len = max([len(dout_line) for dout_line in dout_lines])
                    for dout_line, fret_line in zip(dout_lines, fret_lines):
                        msg = '-ok-'
                        if dout_line == '':
                            continue
                        if dout_line != fret_line:
                            msg = 'DIFF'
                        log = '{{msg}} {{dout_line:{max_len}}} {{fret_line:{max_len}}}'
                        print(log.format(max_len=max_len).format(msg=msg, dout_line=dout_line, fret_line=fret_line))
    print(f'Tests Run: {len(infiles)}')


def generate(problem_id):
    problem_number, problem_letter = re.match('([0-9]+)(.+)', problem_id).groups()
    url = f'https://codeforces.com/problemset/problem/{problem_number}/{problem_letter}'
    soup = bs4.BeautifulSoup(requests.get(url).content, features='html.parser')
    ins = soup.find_all('div', {'class': "input"})
    outs = soup.find_all('div', {'class': "output"})
    assert len(ins) == len(outs)

    def _convert(bs4_elem_tag):
        for br in bs4_elem_tag.find_all('br'):
            br.replace_with('\n')
        return ''.join(bs4_elem_tag.find('pre').contents)

    def _save(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    tests_folder = f'{problem_id}/tests'
    os.makedirs(tests_folder, exist_ok=True)

    for number, (i, o) in enumerate(zip(ins, outs)):
        _save(f'{tests_folder}/{problem_id}_{number + 1:>02}.in', _convert(i))
        _save(f'{tests_folder}/{problem_id}_{number + 1:>02}.out', _convert(o))

    with open(f'template.py', 'r') as f:
        _save(f'{problem_id}/{problem_id}.py', f.read().replace('/?/?', f'/{problem_number}/{problem_letter}'))


if __name__ == '__main__':
    generate(input("Problem id: "))
