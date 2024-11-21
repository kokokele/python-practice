import random

answer = random.randint(1, 100);
print(answer)
count = 0


while True:
        guess =  input(' 请输入你要猜的数字： ')
        # print(guess, type(int(guess)), type(answer))
        count += 1
        if int(guess) == answer:
            print('恭喜你猜对的了，共猜了', count, '次')
            break;
            

            