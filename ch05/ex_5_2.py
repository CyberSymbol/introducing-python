questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

# pair = [
#     "Q: " + questions[0] + "\n" + "A: " + answers[1],
#     "Q: " + questions[1] + "\n" + "A: " + answers[2],
#     "Q: " + questions[2] + "\n" + "A: " + answers[0]
# ]
# for i in pair:
#     print(i + "\n")

q_a = ((0, 1), (1, 2), (2, 0))
for q, a in q_a:
    print("Q:", questions[q])
    print("A:", answers[a])
    print()
