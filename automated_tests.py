import optparse
from contextlib import suppress
from os import listdir
from os import system as execute
from sys import argv, platform
from timeit import default_timer as timer

from pyperclip import copy

SLASH = '\\' if platform.startswith('win') else '/'


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


def run_tests(year: str, problems: list[str], options: dict) -> None:
    print(f'{bcolors.WARNING}{bcolors.UNDERLINE}Year: {year}{bcolors.ENDC}')

    problems = [
        problem for problem in problems if not options.problems or problem in options.problems.split(',')]
    problem_times = {problem: [] for problem in problems}

    for problem in problems:
        with suppress(FileNotFoundError):
            dir_problem_suites = sorted(
                listdir(f'.{SLASH}tests{SLASH}{year}{SLASH}{problem}'))
            print(f'{bcolors.OKBLUE}\tProblem: {problem}{bcolors.ENDC}')

            for raw_dir in dir_problem_suites:
                dir = f'.{SLASH}tests{SLASH}{year}{SLASH}{problem}{SLASH}{raw_dir}'

                number_of_problems = len(listdir(dir)) // 2

                for t in range(1, number_of_problems+1):
                    start = timer()
                    execute(
                        f'python {year}{SLASH}{problem}.py < {dir}{SLASH}{t}.in > {dir}{SLASH}{t}.out')
                    elapsed = timer() - start
                    problem_times[problem].append(elapsed)

                    with open(f'{dir}{SLASH}{t}.out', 'r') as f:
                        output = f.read()

                    with open(f'{dir}{SLASH}{t}.sol', 'r') as f:
                        solution = f.read()

                    if output != solution:
                        print(
                            f'\t\t{bcolors.FAIL}Failed test {t} in {dir}{bcolors.ENDC}')
                        print(
                            f'\t\tOutput: {output}\t\tSolution: {solution}\n')

                    else:
                        print(
                            f'\t\t{bcolors.OKGREEN}Passed test {t} in {dir}{bcolors.ENDC}\n')

                    execute(f'del {dir}{SLASH}{t}.out')

            print(
                f'\t\t{bcolors.OKCYAN}Average time: {sum(problem_times[problem]) / len(problem_times[problem])} seconds{bcolors.ENDC}\n')


def main():
    p = optparse.OptionParser()
    p.add_option('-y', '--years')
    p.add_option('-p', '--problems')
    options, arguments = p.parse_args()

    years = [year for year in sorted(
        listdir('.')) if year.isdigit() and len(year) == 4] if not options.years else options.years.split(',')

    problems_per_year = {year: [problem.replace('.py', '') for problem in sorted(listdir(
        f'.{SLASH}{year}')) if problem.endswith('.py') and problem != 'tests.py'] for year in years}

    for year, problems in problems_per_year.items():
        run_tests(year, problems, options)


if __name__ == '__main__':
    main()
