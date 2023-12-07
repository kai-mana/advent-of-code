words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def create_tree(words):
    tree = {'start': {}}
    for word, number in words.items():
        current = tree['start']
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['end'] = number
    return tree

def process_line(tree, line):
    detected_numbers = []
    active_paths = [tree['start']]

    for char in line:
        if char in tree['start']:
            active_paths.append(tree['start'])

        new_active_paths = []
        for path in active_paths:
            if char in path:
                next_node = path[char]
                new_active_paths.append(next_node)
                if 'end' in next_node:
                    detected_numbers.append(next_node['end'])
            elif char.isdigit() and char in '123456789':
                detected_numbers.append(int(char))
                # Reset active paths after detecting a digit
                new_active_paths = [tree['start']]

        active_paths = new_active_paths if new_active_paths else [tree['start']]

    return detected_numbers

tree = create_tree(words)

sum_of_numbers = 0

with open('day01_trebuchet/calibration.txt', 'r') as file:
    for line in file:
        numbers_in_line = process_line(tree, line.lower().strip())
        if numbers_in_line:
            first_last_concat = str(numbers_in_line[0]) + str(numbers_in_line[-1])
            print(f"Number from line: {int(first_last_concat)}")
            sum_of_numbers += int(first_last_concat)

print(f"Sum of numbers: {sum_of_numbers}")