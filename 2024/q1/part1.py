#!/usr/bin/env python3

import argparse

creature_potion_cost = {
    'A': 0,
    'B': 1,
    'C': 3
}

def main(args):
    with open(args.creature_notes, 'r') as f:
        raw_data = [ l.strip() for l in f.readlines() ]
    return sum(list(map(lambda c: creature_potion_cost[c], [ c for c in raw_data[0] ])))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest1-part1', description='Potion Optimization')
    parser.add_argument(
        '--creature-notes',
        type=str,
        default='part1_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
