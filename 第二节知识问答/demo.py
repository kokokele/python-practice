#coding=utf-8
questions = [{'question': '下面哪些不是计算机语言? \n A)abc \n B)c- \n C)python \n D)java \n', 'answer': 'b'},
             {'question': '下面哪些是计算机语言? \n A)abc \n B)c- \n C)python \n D)java \n', 'answer': 'c'}]
score = 0
for q in questions:
    guess = input(q['question'])
    if guess.lower() == q['answer'].lower():
        print('回答正确')
        score += 10
    else:
        print('回答错误')
print('你的得分是:', score)