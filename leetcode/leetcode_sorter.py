import os

def leetcode_sorter():
    if os.getcwd().split('/')[-1].lower() != 'leetcode':
        print('Please run this script in the LeetCode directory')
        return

    dirs = os.listdir()
    dirs = [d for d in dirs if d != 'README.md' and d != '.git']

    range_dirs = [d for d in dirs if '(' in d]
    problem_dirs = [d for d in dirs if '-' in d]

    for p in problem_dirs:
        problem_number = int(p.split('-')[0])
        range_number = problem_number // 200 * 200 + 1
        range_dirs.append(f'({range_number}, {range_number + 199})')
        range_dir = range_dirs[-1]
        for r in range_dirs:
            range_numbers = r[1:-2].split(', ')
            if problem_number >= int(range_numbers[0]) and problem_number <= int(range_numbers[1]):
                range_dir = r
                break
        if not os.path.exists(range_dir):
            os.mkdir(f'({range_number}, {range_number + 199})')
        os.rename(p, f'({range_number}, {range_number + 199})/{p}')

if __name__ == '__main__':
    leetcode_sorter()
