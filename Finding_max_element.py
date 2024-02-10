def find_max_element(n):
    if not n:
        return None
    else:
        max_element = n[0]
        for num in n:
            if num > max_element:
                max_element = num
        return max_element


number = [10, 5, 20, 3, 2, 8, 20, 2]
maximum = find_max_element(number)
print("Maximum element in the list:", maximum)