# https://codeforces.com/problemset/problem/2/A

def func_sol(raw_data):
    lines = raw_data.split('\n')

    rounds = []
    for line in lines[1:-1]:
        name, score_str = line.split()
        rounds.append((name, int(score_str)))

    player_score_map = {}
    for name, score in rounds:
        player_score_map[name] = player_score_map.get(name, 0) + score

    max_score = max(player_score_map.values())

    player_score_remap = {}
    for name, score in rounds:
        player_score_remap[name] = player_score_remap.get(name, 0) + score
        if player_score_remap[name] >= max_score and player_score_map[name] == max_score:
            return name


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
