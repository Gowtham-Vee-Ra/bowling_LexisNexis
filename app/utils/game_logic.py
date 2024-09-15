def calculate_score(rolls):
    """
    Calculate the total score for a list of rolls in a bowling game.
    """
    score = 0
    roll_index = 0
    for frame in range(10):
        if roll_index >= len(rolls):
            break
        if is_strike(rolls, roll_index):
            score += 10 + strike_bonus(rolls, roll_index)
            roll_index += 1
        elif is_spare(rolls, roll_index):
            score += 10 + spare_bonus(rolls, roll_index)
            roll_index += 2
        else:
            score += sum_of_balls_in_frame(rolls, roll_index)
            roll_index += 2
    return score

def is_strike(rolls, roll_index):
    return rolls[roll_index] == 10

def is_spare(rolls, roll_index):
    if roll_index + 1 >= len(rolls):
        return False
    return rolls[roll_index] + rolls[roll_index + 1] == 10

def strike_bonus(rolls, roll_index):
    bonus = 0
    if roll_index + 1 < len(rolls):
        bonus += rolls[roll_index + 1]
    if roll_index + 2 < len(rolls):
        bonus += rolls[roll_index + 2]
    return bonus

def spare_bonus(rolls, roll_index):
    if roll_index + 2 < len(rolls):
        return rolls[roll_index + 2]
    return 0

def sum_of_balls_in_frame(rolls, roll_index):
    frame_sum = rolls[roll_index]
    if roll_index + 1 < len(rolls):
        frame_sum += rolls[roll_index + 1]
    return frame_sum

def is_valid_roll(rolls, pins):
    """
    Validate if the number of pins knocked down is valid according to the game rules.
    """
    current_frame = get_current_frame(rolls)
    frame_rolls = get_rolls_in_frame(rolls, current_frame)

    if current_frame < 9:
        if len(frame_rolls) == 0:
            return True
        elif len(frame_rolls) == 1:
            if frame_rolls[0] == 10:
                return False  # Strike, frame is complete
            else:
                return frame_rolls[0] + pins <= 10
        else:
            return False  # Frame is complete
    else:
        # 10th frame logic
        if len(frame_rolls) < 2:
            return True
        elif len(frame_rolls) == 2:
            if frame_rolls[0] == 10 or sum(frame_rolls[:2]) == 10:
                return True  # Allow a third roll
            else:
                return False
        elif len(frame_rolls) == 3:
            return False
    return False

def get_current_frame(rolls):
    frame = 0
    roll_index = 0
    while frame < 10 and roll_index < len(rolls):
        if is_strike(rolls, roll_index) and frame < 9:
            roll_index += 1
        else:
            roll_index += 2
        frame += 1
    return frame

def get_rolls_in_frame(rolls, frame_number):
    frame = 0
    roll_index = 0
    while frame < frame_number and roll_index < len(rolls):
        if is_strike(rolls, roll_index) and frame < 9:
            roll_index += 1
        else:
            roll_index += 2
        frame += 1
    frame_rolls = []
    if roll_index < len(rolls):
        frame_rolls.append(rolls[roll_index])
        if roll_index + 1 < len(rolls):
            frame_rolls.append(rolls[roll_index + 1])
        if frame_number == 9 and roll_index + 2 < len(rolls):
            frame_rolls.append(rolls[roll_index + 2])
    return frame_rolls
