import sys
sys.stdin = open("C:\\Users\\USER\\Downloads\\input.txt", "r")
T = int(input())
score_dictionary = {}
for i in range(T):
    number = int(input())
    for j in range(0,101): score_dictionary[j] = 0
    score = list(map(int,input().split()))
    for j in range(len(score)):
        if score[j] in score_dictionary.keys(): score_dictionary[score[j]] += 1
    mode_students = max(score_dictionary.values()); mode_score = []
    for key,value in score_dictionary.items():
        if value == mode_students: mode_score.append(key)
    print("#{} {}".format(i+1, max(mode_score)))