if __name__ == '__main__':
    import random
    N = int(input())
    my_list = []
    dict_of_actions = {
        1: my_list.insert(int(input()), int(input())),
        2: my_list.remove(int(input())),
        3: print(my_list),
        4: my_list.append(int(input)),
        5: my_list.sort(),
        6: my_list.pop(),
        7: my_list.reverse()
    }
    for i in range(0, N):
        random.choice([dict_of_actions.keys()])


# the other solution
if __name__ == '__main__':
    my_list = []
    N = int(input())
    for i in range(N):
        command = map(str, raw_input().split())
        if command[0] == "sort":
            my_list.sort()
        elif command[0] == "print":
            print(my_list())
        elif command[0] == "reverse":
            my_list.reverse()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
