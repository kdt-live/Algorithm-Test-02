T = int(input())
mirror_dictionary = {"b":"d", "d":"b", "p":"q", "q":"p"}
for i in range(T):
    sentence = input(); mirror_sentence = ""
    for j in range(len(sentence)-1,-1,-1):
        if sentence[j] in mirror_dictionary.keys(): mirror_sentence += mirror_dictionary[sentence[j]]
    print("#{} {}".format(i+1, mirror_sentence))