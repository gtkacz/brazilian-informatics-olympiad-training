import os
import sys
from timeit import default_timer as timer

import pandas as pd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    dir_separator = '\\' if sys.platform.startswith('win') else '/'

    tests = {
        '2022': {
            'chuva': {'input': ['6', '2', '0 2 0 1 0 1'], 'expected_output': ['6']},
            'hotel': {'input': ['100', '20', '15'], 'expected_output': ['6460']},
            'magico': {'input': ['4', '11 8 5 0', '14 1 4 15', '2 13 16 3', '7 12 9 6'], 'expected_output': ['10', '1', '4']},
            'maior': {'input': ['80', '500', '12'], 'expected_output': ['480']},
        },
        '2021': {
            'baralho': {'input': ['01C02C03C04C05C07C09C10C11C02E02E03E11U'], 'expected_output': ['4', 'erro', '12', '13']},
            'torneio': {'input': ['P', 'P', 'P', 'P', 'P', 'P'], 'expected_output': ['-1']},
            'zero': {'input': ['10', '1', '3', '5', '4', '0', '0', '7', '0', '0', '6'], 'expected_output': ['7']},
            # 'tempo': {'input': [], 'expected_output': []},
        },
    }

    os.system('rm -rf tests')
    os.system('rm -f tests.md')
    os.system('mkdir tests')

    raw_df = []

    for year, problems in tests.items():
        os.system(f'mkdir tests{dir_separator}{year}')

        print(f'{bcolors.WARNING}{bcolors.UNDERLINE}Year: {year}{bcolors.ENDC}')
        for problem, test in problems.items():
            with open(f'tests{dir_separator}{year}{dir_separator}{problem}.in', 'w+') as f:
                f.write('\n'.join(test['input']))

            start = timer()
            os.system(
                f'python {year}{dir_separator}{problem}.py < tests{dir_separator}{year}{dir_separator}{problem}.in > tests{dir_separator}{year}{dir_separator}{problem}.out')
            end = timer()

            with open(f'tests{dir_separator}{year}{dir_separator}{problem}.out', 'r') as f:
                test['output'] = f.read().splitlines()

            result = True if test['output'] == test['expected_output'] else False

            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\tProblem: {problem}.py{bcolors.ENDC}')
            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\t\t\tInput: {test["input"]}{bcolors.ENDC}')
            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\t\t\tExpected output: {test["expected_output"]}{bcolors.ENDC}')
            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\t\t\tOutput: {test["output"]}{bcolors.ENDC}')
            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\t\t\tElapsed in: {end - start}s{bcolors.ENDC}')
            print(
                f'{bcolors.OKGREEN if result else bcolors.FAIL}\t\t\tResult: {"OK" if result else "FAIL"}{bcolors.ENDC}')

            raw_df.append({'Year': year, 'Problem': problem,
                          'Result': 'OK' if result else 'FAIL', 'Elapsed (s)': end - start})

        print()

    os.system('rm -rf tests')
    pd.DataFrame(raw_df).sort_values('Year', ascending=False).to_html(
        '.tests.html', index=False, justify='center')

    with open('README.md', 'r') as f:
        readme = f.readlines()

    with open('.tests.html', 'r') as f:
        tests = f.read()

    with open('README.md', 'w+') as f:
        for index, line in enumerate(readme):
            if '<!-- TESTS START -->' in line:
                start_idx = index

            elif '<!-- TESTS END -->' in line:
                end_idx = index
                break

        f.writelines(readme[:start_idx + 1])
        f.write(tests.replace('<table ', '<table align="center" '))
        f.write('\n')
        f.writelines(readme[end_idx:])

    os.system('rm -f .tests.html')


if __name__ == '__main__':
    main()
