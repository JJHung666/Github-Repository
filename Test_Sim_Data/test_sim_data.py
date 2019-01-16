# Name: Justin Lin -- Title of simulation: Simulation and Data Sets
# Date: 1/13/2019
# Description:
# Source: none


#Option #1:

# Create a Monte-Carlo simulation of your choice that helps to determine the most probable outcomes in your chosen scenario. You can run any simulation at all; please explain your reasoning for the ranges that you choose, and why your simulation setup resembles possible situations in real life. Explain your simulation and results in a humorous but serious way, a la What If from XKCD (Links to an external site.)Links to an external site.. You may build your presentation in any format that makes sense for you; poster, PDF, web site, slideshow, whatever program you are comfortable with. Any charts you make can be done with the basics of Matplotlib, with minimal research if any.


# Test Scores.

import random as r
import math as m
# from collections import Counter
import matplotlib.pyplot as mat

def Assessment_scores(amount_of_test, subject, affinity):
	test_score = []
	if subject.lower() == "math":
		for x in range(amount_of_test):
			if affinity.lower() == "bad":
				lowest_possible = 60
				highest_possible = 95
				duration_of_studying = r.uniform(1.5,3.5)
			elif affinity.lower() == "normal":
				lowest_possible = 70
				highest_possible = 100
				duration_of_studying = r.uniform(1.25,3)
			elif affinity.lower() == "great":
				lowest_possible = 75
				highest_possible = 102.5
				duration_of_studying = r.uniform(1,2.5)
			grade = r.uniform(lowest_possible, highest_possible)
			studying_multiplyer = (grade*(1+0.1)**(duration_of_studying))//1
			if studying_multiplyer > 102.5:
				studying_multiplyer = 102.5
			test_score.append(studying_multiplyer)


	elif subject.lower() == "english":
		for x in range(amount_of_test):
			if affinity.lower() == "bad":
				lowest_possible = 30
				highest_possible = 47.5
				duration_of_studying = r.uniform(1.5,3.5)
			elif affinity.lower() == "normal":
				lowest_possible = 35
				highest_possible = 50
				duration_of_studying = r.uniform(1.25,3)
			elif affinity.lower() == "great":
				lowest_possible = 75/2
				highest_possible = 102.5/2
				duration_of_studying = r.uniform(1,2.5)
			grade = r.uniform(lowest_possible, highest_possible)
			studying_multiplyer = (grade*(1+0.075)**(duration_of_studying))//1
			if studying_multiplyer > 102.5/2:
				studying_multiplyer = 102.5/2
			test_score.append(studying_multiplyer)


	elif subject.lower() == "computer science" or subject.lower() == "comp scie":
		for x in range(amount_of_test):
			if affinity.lower() == "bad":
				lowest_possible = 3
				highest_possible = 4.85
				duration_of_studying = r.uniform(1.5,3.5)
			elif affinity.lower() == "normal":
				lowest_possible = 3.5
				highest_possible = 5
				duration_of_studying = r.uniform(1.25,3)
			elif affinity.lower() == "great":
				lowest_possible = 3.85
				highest_possible = 5.1
				duration_of_studying = r.uniform(1,2.5)
			grade = r.uniform(lowest_possible, highest_possible)
			studying_multiplyer = (grade*(1+0.05)**(duration_of_studying))//1
			if studying_multiplyer > 5.1:
				studying_multiplyer = 5.1
			test_score.append(studying_multiplyer)


	elif subject.lower() == "language" or subject.lower() == "spanish":
		for x in range(amount_of_test):
			if affinity.lower() == "bad":
				lowest_possible = 60
				highest_possible = 95
				duration_of_studying = r.uniform(1.5,3.5)
			elif affinity.lower() == "normal":
				lowest_possible = 70
				highest_possible = 100
				duration_of_studying = r.uniform(1.25,3)
			elif affinity.lower() == "great":
				lowest_possible = 75
				highest_possible = 102.5
				duration_of_studying = r.uniform(1,2.5)
			grade = r.uniform(lowest_possible, highest_possible)
			studying_multiplyer = (grade*(1+0.1)**(duration_of_studying))//1
			if studying_multiplyer > 102.5:
				studying_multiplyer = 100
			test_score.append(studying_multiplyer)
	return test_score


def math(n, affinity):
	amount_of_test = n
	math = Assessment_scores(amount_of_test, "math", affinity)
	r = [x for x in range(1, 1+amount_of_test)]
	mat.bar(r, math, color=(.6,.2,.4,1.0))
	mat.ylabel("Scores")
	mat.xlabel("amount of math tests")
	mat.savefig("math_test_bar_charts.png")
	mat.show()

def spanish(n, affinity):
	amount_of_test = n
	spanish = Assessment_scores(amount_of_test, "spanish", affinity)
	r = [x for x in range(1, 1+amount_of_test)]
	mat.bar(r, spanish, color=(.6,.2,.4,1.0))
	mat.ylabel("Scores")
	mat.xlabel("amount of spanish tests")
	mat.savefig("spanish_test_bar_charts.png")
	mat.show()

def computer_science(n, affinity):
	amount_of_test = n
	computer_science = Assessment_scores(amount_of_test, "computer science", affinity)
	r = [x for x in range(1, 1+amount_of_test)]
	mat.bar(r, computer_science, color=(.6,.2,.4,1.0))
	mat.ylabel("Scores")
	mat.xlabel("amount of computer science tests")
	mat.savefig("cs_test_bar_charts.png")
	mat.show()

def english(n, affinity):
	amount_of_test = n
	english = Assessment_scores(amount_of_test, "english", affinity)
	r = [x for x in range(1, 1+amount_of_test)]
	mat.bar(r, english, color=(.6,.2,.4,1.0))
	mat.ylabel("Scores")
	mat.xlabel("amount of english tests")
	mat.savefig("english_test_bar_charts.png")
	mat.show()

math(9, "great")
english(4, "great")
computer_science(1, "normal")
spanish(11, "normal")