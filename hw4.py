# PART A
"""
Q1
"""


def fibonacci_chars(n, k):
    return helper_fibonacci_chars(n)[k]


def helper_fibonacci_chars(n):
    if n == 0:
        return "a"
    elif n == 1:
        return "bc"
    else:
        Sn = helper_fibonacci_chars(n - 2) + helper_fibonacci_chars(n - 1)
        return Sn


"""
Q2
"""


def drainage_basins(n):
    lindex = []
    lvalue = []
    count = -1
    lindex = helper_drainage_basins(n, lindex, lvalue, count)
    return lindex


def helper_drainage_basins(elevation_histogram, lindex, lvalue, count):
    lvalue.append(elevation_histogram[0]) #שומר את המספרים שהוא עומד למחוק
    count += 1
    if len(elevation_histogram) > 1: #תנאי עצירה
        if elevation_histogram[0] < elevation_histogram[1]: #אם הנוכחי קטן מהבא
            if len(lindex) < 1:
                lindex.append(count)
            elif elevation_histogram[0] < lvalue[-2]: # בודק את הנוכחי ביחס לאלו שנמחקו
                lindex.append(count)
        elif len(elevation_histogram) == 2: #אם האורך הוא 2
            if elevation_histogram[0] > elevation_histogram[1]: #אם האחרון קטן יותר
                count += 1 #תעדכן אינדקס
                lindex.append(count) #תוסיף אינדקס לרשימת האינדקסים של האגנים
        helper_drainage_basins(elevation_histogram[1:], lindex, lvalue, count) #תקרא מחדש לפונקציה ללא האיבר הראשון
    return lindex


# PART B
"""
Q1
"""


def is_legit_track(grid, i1, j1, i2, j2, current_weight):
    return is_legit_track_2(grid, i1, j1, i2, j2, current_weight)


def is_legit_track_2(grid, i1, j1, i2, j2, current_weight):
    if i2 < 0 or j2 < 0:
        return False
    row = len(grid)
    if i2 >= row:
        return False
    col = len(grid[i2])
    if j2 >= col:
        return False
    if i1 < i2 and j1 < j2:
        return False
    if current_weight + grid[i2][j2] < 2 * grid[i2][j2]:
        return True
    return False


"""
Q2
"""


def get_number_legit_tracks(grid, i1, j1):
    return helper_get_number_legit_tracks(grid, i1, j1, 0)


def helper_get_number_legit_tracks(grid, i, j, current_weight):
    if i == len(grid) - 1 and j == len(grid[len(grid) - 1]) - 1:
        return 1
    count = 0
    new_current_weight = current_weight + grid[i][j]
    if is_legit_track_2(grid, i, j, i - 1, j, new_current_weight):
        count += helper_get_number_legit_tracks(grid, i - 1, j, new_current_weight)
    if is_legit_track_2(grid, i, j, i, j - 1, new_current_weight):
        count += helper_get_number_legit_tracks(grid, i, j - 1, new_current_weight)
    if is_legit_track_2(grid, i, j, i, j + 1, new_current_weight):
        count += helper_get_number_legit_tracks(grid, i, j + 1, new_current_weight)
    if is_legit_track_2(grid, i, j, i + 1, j, new_current_weight):
        count += helper_get_number_legit_tracks(grid, i + 1, j, new_current_weight)
    return count


# PART C
"""
Q1
"""


def optimize_flowers_selection(flowers, budget):
    return helper_optimize_flowers_selection(flowers, 0, budget)


def helper_optimize_flowers_selection(flowers, sum_aesthetic_value, budget):
    if len(flowers) == 0:
        return (sum_aesthetic_value, budget)
    flower = flowers[0]
    flower_name = flower[0]
    aesthetic_value = int(flower[1])
    cost = int(flower[2])
    if cost <= budget:
        option_B = helper_optimize_flowers_selection(flowers[1:], sum_aesthetic_value + aesthetic_value, budget - cost)
    else:
        option_B = (0, 0)
    option_A = helper_optimize_flowers_selection(flowers[1:], sum_aesthetic_value, budget)
    A_aesthetic_value = option_A[0]
    B_aesthetic_value = option_B[0]
    if A_aesthetic_value > B_aesthetic_value:
        return (option_A[0], option_A[1])
    elif A_aesthetic_value == B_aesthetic_value and option_A[1] > option_B[1]:
        return (option_A[0], option_A[1])
    else:
        return (option_B[0], option_B[1])


"""
Q2
"""


def get_plants_to_buy_faster(flowers, budget):
    return helper_get_plants_to_buy_faster(flowers, 0, budget, {})


def helper_get_plants_to_buy_faster(flowers, sum_aesthetic_value, budget, memo):
    if len(flowers) == 0:
        return (sum_aesthetic_value, budget)
    flower = flowers[0]
    flower_name = flower[0]
    aesthetic_value = int(flower[1])
    cost = int(flower[2])
    key = (flower_name, sum_aesthetic_value, budget, len(flowers))
    if key not in memo:
        if cost <= budget:
            option_B = helper_get_plants_to_buy_faster(flowers[1:], sum_aesthetic_value + aesthetic_value,
                                                       budget - cost, memo)
        else:
            option_B = (sum_aesthetic_value, budget)
        option_A = helper_get_plants_to_buy_faster(flowers[1:], sum_aesthetic_value, budget, memo)
        A_aesthetic_value = option_A[0]
        B_aesthetic_value = option_B[0]
        if A_aesthetic_value > B_aesthetic_value:
            memo[key] = (option_A[0], option_A[1])
        elif A_aesthetic_value == B_aesthetic_value and option_A[1] > option_B[1]:
            memo[key] = (option_A[0], option_A[1])
        else:
            memo[key] = (option_B[0], option_B[1])
    return memo[key]

