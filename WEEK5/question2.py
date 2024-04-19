def num():
    total = 0
    count = 0
    while True:
        user = input('Enter a number: ')
        if user.lower() == 'done':
            break
        try:
            num = float(user)
            total += num
            count += 1
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    average = total / count
    print(f'Total: {total}, Count: {count}, Average: {average}')

num()