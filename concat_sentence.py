def longest_match(s1, list_of_sentences):
    best_match_count = -1
    best_sentence = -1
    s1_size = len(s1)
    for i in range(len(list_of_sentences)):
        s2 = list_of_sentences[i]
        counter =0
        s2_size = len(s2)
        min_size = min(s1_size, s2_size)

        for k in range(min_size,0,-1):
            if s1.endswith(s2[:k]):
                counter = k
                break

        if counter > best_match_count:
            best_match_count = counter
            best_sentence = i

    new_sentence = s1+ list_of_sentences[best_sentence][best_match_count:]
    return [new_sentence,best_sentence]

num_words = int(input())

words = [input().strip() for _ in range(num_words)]

start_id = 0
for i in range(num_words):
    if words[i][0].isupper():
        start_id = i
        break
result = words[i]
words.pop(i)
for i in range(1, num_words):
    result,idx = longest_match(result, words)
    words.pop(idx)

print(result)