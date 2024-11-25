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
    for i in range(0, len(data), 3):
        r = 0
        a, b, c = data[i], data[i + 1], data[i + 2]
        if a == 'x' and b == 'x' and c == 'x':
            pass
        elif a == 'x':
            if b == 'x':
                r += creature_potion_cost[c]
            elif c == 'x':
                r += creature_potion_cost[b]
            else:
                r += 1 + creature_potion_cost[b]
                r += 1 + creature_potion_cost[c]
        elif b == 'x':
            if c == 'x':
                r += creature_potion_cost[a]
            else:
                r += 1 + creature_potion_cost[a]
                r += 1 + creature_potion_cost[c]
        elif c == 'x':
            r += 1 + creature_potion_cost[a]
            r += 1 + creature_potion_cost[b]
        else:
            r += 2 + creature_potion_cost[a]
            r += 2 + creature_potion_cost[b]
            r += 2 + creature_potion_cost[c]
        count += r
            
    return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest1-part3', description='Potion Optimization')
    parser.add_argument(
        '--creature-notes',
        type=str,
        default='part3_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
