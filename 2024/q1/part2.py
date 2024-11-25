#!/usr/bin/env python3

import argparse

creature_potion_cost = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
}

def main(args):
    with open(args.creature_notes, 'r') as f:
        raw_data = [ l.strip() for l in f.readlines() ]
    count = 0
    data = raw_data[0]
    for i in range(0, len(data), 2):
        a, b = data[i], data[i + 1]
        if a == 'x' and b == 'x':
            pass
        elif a == 'x':
            count += creature_potion_cost[b]
        elif b == 'x':
            count += creature_potion_cost[a]
        else:
            count += 1 + creature_potion_cost[a]
            count += 1 + creature_potion_cost[b]
            
    return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest1-part2', description='Potion Optimization')
    parser.add_argument(
        '--creature-notes',
        type=str,
        default='part2_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
