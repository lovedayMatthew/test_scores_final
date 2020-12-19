#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score_1 = int(input("Enter test score: "))
score_2 = int(input("Enter test score: "))
score_3 = int(input("Enter test score: "))

total_score = score_1+score_2+score_3
# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Your Score:  ", score_1,score_2,score_3,
      "\nTotal Score: ",total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")


