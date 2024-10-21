jokes = open('jokes.txt', 'r')
answers = open('answers.txt', 'r')

jokes_arr = jokes.readlines()
answers_arr = answers.readlines()

max_joke_count = len(jokes_arr)

json_string = '{\n  "jokes": [\n'

for current_joke in range(max_joke_count):
    joke = jokes_arr[current_joke].strip('\n')
    answer = answers_arr[current_joke].strip('\n')

    json_string = json_string + "    {\n" + f'      "id":{current_joke},\n      "joke": "{joke}",\n      "answer": "{answer}"' + "\n    }"

    if current_joke != max_joke_count - 1:
        json_string = json_string + ','

    json_string = json_string + "\n"

json_string = json_string + "  ]\n}"

jokes.close()
answers.close()

json_file = open('jokes.json', 'a')
json_file.write(json_string)
json_file.close()

