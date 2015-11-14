def word_count(words):
  word_count = {}
  word_array = words.lower().split()
  for word in word_array:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  return word_count