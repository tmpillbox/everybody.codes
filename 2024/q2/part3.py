#!/usr/bin/env python3

import argparse

GREEN = "\033[0;32m"
BOLD = '\033[1;3m'
END = '\033[0m'


class Token:
    def __init__(self, text, positions):
        self.text = text
        self.pos = [ pos for pos in positions ]
    
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return f'Token: {self.text} @ {self.pos}'

class Inscription:
    def __init__(self, insc_lines):
        self.lines = list()
        self.positions = list()
        for r, line in enumerate(insc_lines):
            row = list()
            row_pos = list()
            for c, ch in enumerate(line):
                row.append(ch)
                row_pos.append( (r, c) )
            self.lines.append(row)
            self.positions.append(row_pos)
    
    def tokens(self, length):
        grid = list(zip(*self.lines[::-1]))
        pos_grid = list(zip(*self.positions[::-1]))
        for rot in range(4):
            for rid, row in enumerate(grid):
                pos = list(pos_grid[rid])
                if rot % 2:
                    row = list(row) + [ row[i] for i in range(min(length, len(row))) ]
                    pos = pos + [ pos[i] for i in range(min(length, len(pos))) ]
                for i in range(len(row) - length + 1):
                    yield Token(''.join(row[i:i+length]), pos[i:i+length])
            grid = list(zip(*grid[::-1]))
            pos_grid = list(zip(*pos_grid[::-1]))
 

def main(args):
    with open(args.runic_notes, 'r') as f:
        notes_raw = [ l.strip() for l in f.readlines() ]
    words = [
        token.strip()
        for token in notes_raw[0].split(':')[-1].split(',')
    ]
    inscriptions = Inscription(notes_raw[2:])
    matches = list()
    hilite_pos = set()
    word_lens = set([ len(w) for w in words ])
    for word_len in word_lens:
        for token in inscriptions.tokens(word_len):
            if str(token) in words:
                matches.append(token)
    for match in matches:
        # print(repr(match))
        for pos in match.pos:
            hilite_pos.add(pos)
    result_text = ''
    for r, row in enumerate(inscriptions.lines):
        for c, ch in enumerate(row):
            if (r, c) in hilite_pos:
                result_text = f'{result_text}{GREEN}{ch}{END}'
            else:
                result_text = f'{result_text}{ch}'
        result_text += '\n'
    print(result_text)
    return len(hilite_pos)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='quest2-part3', description='Rune Counter')
    parser.add_argument(
        '--runic-notes',
        type=str,
        default='part3_notes.txt'
    )
    args = parser.parse_args()
    print(main(args))
