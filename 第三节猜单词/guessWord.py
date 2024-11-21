import random

guessWords = ['hello', 'world', 'choice', 'letter', 'love']

word = random.choice(guessWords)
l = len(word)
default = list("?" * l)
print(word)

live = 9
gc = 0
while gc < l:
    guess = input('请猜出word：')
    if len(guess) > 1:
        print('每次只能猜一个字母')
        continue
    ds = ''.join(default)

    # 从右边开始查找，用来判断重复字母
    startIndex = ds.rfind(guess)
    print('startindex:', startIndex)
    if startIndex == -1:
        startIndex = 0
    else:
        startIndex = startIndex + 1 # 判断是从 start >= 计算的

    pos = word.find(guess, startIndex)
    if pos != -1:
        gc += 1
        default[pos] = guess
        print(default)

    live -= 1
    if live < 1:
        print('你猜的次数超出了次数')
        break


if live > 0:
    print('恭喜你猜对了！！！')