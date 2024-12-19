import json
def func(file, index_quest):
    text = list(file["result"]['alternatives'][0]['message']['text'].split('\n'))

    index_quest = (index_quest - 1) * 2

    if (index_quest + 1 >= len(text)):
        return "index out of range"

    quest_text = text[index_quest]
    quest_concept = text[index_quest + 1]

    f = open("curriculum_qa_step2_answer_questions.txt").read()
    f = f.format(quest_text, quest_concept)
    return f



import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    quest = json.load(file)

g = open("output.txt", "w")
g.write(func(quest, 8))
g.close()
