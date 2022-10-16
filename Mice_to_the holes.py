# Returns minimum time required to place mice in holes using the Greedy approach .
# We can put mouse to its nearest hole to minimize the time.
# This can be done by sorting the positions of mice and holes.


def assign_hole(mice, holes):
    if len(mice) == len(holes):
        mice.sort()
        holes.sort()

        max_diff = 0

        for i in range(len(mice)):
            if max_diff < abs(mice[i] - holes[i]):
                max_diff = abs(mice[i] - holes[i])

        return max_diff
    else:
        return "Number of mice and holes not the same"


MiceNumber = [4, -4, 2]
HolesNumber = [4, 0, 5]

MinimumTime = assign_hole(MiceNumber, HolesNumber)

print(f"The last mouse gets into the holes in time: {MinimumTime}")
