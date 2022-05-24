import os
import re

ABS_PATH_TO_WIKI = r''

def replace_dash_at_index(string: str, index: int) -> str:
    # remove spaces
    return string[:index - 1] + '—' + string[index + 2:]

def replace_dashes_in_line(line: str) -> str:
    iter = re.finditer(r'[A-Za-z0-9\!] - [A-Za-z0-9\!]', line)
    match_indices = []

    for m in iter:
        match_index = {'start': m.start(0), 'end': m.end(0)}
        match_indices.append(match_index)

    for match in match_indices:
        # list all exceptions

        # skip cursive texts (author - title format)
        if line.find('*', 0, match['start']) != -1 and line.find('*', match['end']) != -1:
            continue

        # skip links
        if line.find('[', 0, match['start']) != -1 and line.find(']', match['end']) != -1:
            continue

        # skip highlights
        if line.find('`', 0, match['start']) != -1 and line.find('`', match['end']) != -1:
            continue

        # skip tables
        if line.find('|') != -1:
            continue

        # the dash is at position + 2 from the match start
        # this needs to be changed if the match term changes
        line = replace_dash_at_index(line, match['start'] + 2)

        # indices changed because of deletion of two spaces
        for match in match_indices:
            match['start'] -= 2
            match['end'] -= 2

    return line

def main() -> None:
    for root, dirs, files in os.walk(ABS_PATH_TO_WIKI):
        for file in files:
            lines = []

            with open(root + '/' + file, mode='r', encoding='utf-8') as r:
                if file != 'en.md':
                    continue

                lines = r.readlines()
                for line_index, line in enumerate(lines):
                    new_line = replace_dashes_in_line(line)
                    lines[line_index] = new_line

                with open(root + '/' + file, mode='w', encoding='utf-8', newline='\n') as w:
                    w.writelines(lines)

if __name__ == '__main__':
    main()
