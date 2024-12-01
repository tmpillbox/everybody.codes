#!/usr/bin/env python3

import argparse

GREEN = "\033[0;32m"
BOLD = '\033[1;3m'
END = '\033[0m'


def main(args):
    with open(args.runic_notes, 'r') as f:
        notes_raw = [ l.strip() for l in f.readlines() ]
    words = [
        token.strip()
        for token in notes_raw[0].split(':')[-1].split(',')
    ]
    inscription = notes_raw[-1]
    inscription_len = len(inscription)
    hilite_pos = set()
    rune_count = 0
    for rune in words:
        r_len = len(rune)
        for i in range(0, inscription_len - r_len + 1):
            if inscription[i:i+r_len] == rune:
                print(f'# DEBUG: RUNE: {rune} insc_word slice: {inscription[i:i+r_len]}')
                rune_count += 1
                for j in range(i, i + r_len):
                    hilite_pos.add(j)
    result_text = ''
    for i in range(inscription_len):
        if i in hilite_pos:
            result_text = f'{result_text}{GREEN}{BOLD}{inscription[i]}{END}'
        else:
            result_text = f'{result_text}{inscription[i]}'
    print(result_text)
    return rune_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest2-part1', description='Rune Counter')
    parser.add_argument(
        '--runic-notes',
        type=str,
        default='part1_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
