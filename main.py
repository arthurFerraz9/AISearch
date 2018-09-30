from Algorithms.A_Star import A_Star
from Problems.SyntaxProblem import SyntaxProblem
from Evaluation.heuristic import Heuristic
from Algorithms.genetic import Genetic
from Utils import text_utils

print("Which search do you want?")
print("1. A*")
print("2. Genetic")
option = int(input())
problem = None

if option == 1:
    vocabulary = text_utils.import_text("Texts/GameOfThrones")
    heuristic = Heuristic("Classifiers/GameOfThronesClassifier")
    problem = A_Star(heuristic, SyntaxProblem(6), vocabulary)
elif option == 2:
    vocabulary = text_utils.genetic_import_text("Texts/ThreeLittlePigs")
    heuristic = Heuristic("Classifiers/ThreeLittlePigsClassifier", "Texts/ThreeLittlePigs")
    problem = Genetic(heuristic, SyntaxProblem(6), vocabulary)
problem.execute()