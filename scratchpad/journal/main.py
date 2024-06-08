date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10: ")
thought = input("Let your thoughts flow: ")

with open(f'{date}.txt', 'w') as file:
    file.write(mood)
    file.write(thought)