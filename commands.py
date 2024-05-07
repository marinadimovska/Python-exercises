if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()
        if 'insert' in command:
            my_list.insert(int(command[1]), int(command[2]))
        elif 'print' in command:
            print(my_list)
        elif 'remove' in command:
            my_list.remove(int(command[1]))
        elif 'append' in command:
            my_list.append(int(command[1]))
        elif 'sort' in command:
            my_list.sort()
        elif 'pop' in command:
            my_list.pop()
        elif 'reverse' in command:
            my_list.reverse()
