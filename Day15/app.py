import sys
from typing import Any


"""
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
"""

def get_ascii_code(char):
    return ord(char)

def increase_current_value(ascii_code, current_value):
    return int(current_value + ascii_code)

def multiply_current_value(current_value):
    return int(current_value * 17)

def remainder_current_value(current_value):
    return int(current_value % 256)

def process_char(char, current_value):
    ascii_code = int(get_ascii_code(char))
    current_value = remainder_current_value(multiply_current_value(increase_current_value(ascii_code, current_value)))
    return current_value

def extract_input():
    input_file = open(sys.argv[1], 'r')
    return input_file.read()


# Part 1
hashes = []
split_sequence = extract_input().split(',')
for sequence in split_sequence:
    current_value = 0
    for char in sequence:
        current_value = process_char(char, current_value)
    hashes.append(current_value)

print(sum(hashes))

# Answer is 507291

def get_correct_box(label):
    current_value = 0
    for char in label:
        current_value = process_char(char, current_value)
    return current_value

def process_step(step, boxes):
    if '-' in step:
        label = step.split('-')[0]
        box_number = get_correct_box(label)
        box = boxes[box_number]
        process_dash(box, label)
    elif '=' in step:

        label = step.split('=')[0]
        focal_length = step.split('=')[1]
        box_number = get_correct_box(label)
        box = boxes[box_number]
        process_equals(box, label, focal_length)


def process_dash(box, label):
    """
        If the operation character is a dash (-), go to the relevant box and remove the lens with the given label if it is present in the box.
        Then, move any remaining lenses as far forward in the box as they can go without changing their order, 
        filling any space made by removing the indicated lens. (If no lens in that box has the given label, nothing happens.)
    """
    has_already, idx = box.has_lens(label)
    if has_already:
        box.remove_lens(idx)

def process_equals(box, label, focal_length):
    """
        If the operation character is an equals sign (=), 
        it will be followed by a number indicating the focal length of the lens that needs to go into the relevant box;
        be sure to use the label maker to mark the lens with the label given in the beginning of the step so you can find it later.

        There are two possible situations:

        If there is already a lens in the box with the same label, 
            replace the old lens with the new lens: 
            remove the old lens and put the new lens in its place, 
            not moving any other lenses in the box.
        If there is not already a lens in the box with the same label, 
            add the lens to the box immediately behind any lenses already in the box. 
            Don't move any of the other lenses when you do this. 
            If there aren't any lenses in the box, 
            the new lens goes all the way to the front of the box.
    """
    has_already, idx = box.has_lens(label)
    if has_already:
        box.swap_lens(idx, Lens(label, focal_length))
    else:
        box.add_lens(Lens(label, focal_length))


"""
Lenses have labels and focal lengths.
"""
class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length
    
    def __str__(self):
        return self.label + " " + str(self.focal_length)
    
    def __repr__(self):
        return self.__str__()
    
"""
You have 256 boxes, each of which can hold any number of lenses.
"""
class Box:
    def __init__(self, number):
        self.number = number
        self.lenses = []

    def add_lens(self, lens):
        self.lenses.append(lens)

    def remove_lens(self, idx):
        del self.lenses[idx]

    def move_lens(self, lens, new_position):
        self.remove_lens(lens)
        self.lenses.insert(new_position, lens)

    def has_lens(self, label):
        for idx in range(len(self.lenses)):
            if self.lenses[idx].label == label:
                return True, idx
        return False, None
    
    def swap_lens(self, idx, lens):
        self.lenses[idx] = lens

    def should_examine(self):
        return len(self.lenses) > 0

    def calculate_focusing_power(self, box_number, slot_number, focal_length):
        """
        The focusing power of a single lens is the result of multiplying together:
        
        One plus the box number of the lens in question.
        The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
        The focal length of the lens.
        """
        focusing_power = int(box_number + 1) * int(slot_number) * int(focal_length)
        
        return int(focusing_power)

    def get_focusing_power(self):
        """
        Returns the total focusing power of all the lenses in the box.
        """
        total_focusing_power = 0
        for index, lens in enumerate(self.lenses):
            total_focusing_power += self.calculate_focusing_power(self.number, (index + 1), lens.focal_length)
        return total_focusing_power

    def __str__(self):
        return "Box " + str(self.number) + ": " + str(self.lenses)

def create_initial_boxes():
    boxes = []
    for i in range(256):
        boxes.append(Box(i))
    return boxes


# Part 2

boxes = create_initial_boxes()
for step in split_sequence:
    process_step(step, boxes)

total_focusing_power = 0
for box in boxes:
    if box.should_examine():
        print("Calculating focusing power for box " + str(box.number) + " with lenses " + str(box.lenses))
        total_focusing_power += box.get_focusing_power()
    
print(total_focusing_power)

# The answer is 296921