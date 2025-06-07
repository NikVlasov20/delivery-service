
# id - 139004822
def min_count_platform(weight: tuple, limit: int):
    weight = tuple(sorted(weight))
    result: int = 0
    left_pointer: int = 0
    right_pointer: int = len(weight) - 1
    while left_pointer <= right_pointer:
        if weight[left_pointer] + weight[right_pointer] <= limit:
            left_pointer += 1
        right_pointer -= 1
        result += 1 
    return result


if __name__ == '__main__':
    weight: tuple = tuple(int(number) for number in input().split())
    limit: int = int(input())
    print(min_count_platform(weight, limit))