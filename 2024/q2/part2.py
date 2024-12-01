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
    inscriptions = notes_raw[2:]
    rune_count = 0
    for inscription in inscriptions:
        hilite_pos = set()
        for rune in words:
            r_len = len(rune)
            enur = rune[::-1]
            for i in range(0, len(inscription) - r_len + 1):
                if inscription[i:i+r_len] in [ rune, enur ]:
                    #print(f'# DEBUG: RUNE: {rune} insc_word slice: {inscription[i:i+r_len]}')
                    for j in range(i, i + r_len):
                        hilite_pos.add(j)
        result_text = ''
        for i in range(len(inscription)):
            if i in hilite_pos:
                result_text = f'{result_text}{GREEN}{BOLD}{inscription[i]}{END}'
            else:
                result_text = f'{result_text}{inscription[i]}'
        print(result_text + ': ' + str(len(hilite_pos)))
        rune_count += len(hilite_pos)
    return rune_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest2-part2', description='Rune Counter')
    parser.add_argument(
        '--runic-notes',
        type=str,
        default='part2_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
