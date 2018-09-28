from A_Star import A_Star
from Problem import SyntaxProblem
from heuristic import Heuristic
from genetic import Genetic
import text_utils

print("Which search do you want?")
print("1. A*")
print("2. Genetic")
option = int(input())
problem = None

if option == 1:
    vocabulary = text_utils.import_text("GameOfThrones")
    heuristic = Heuristic("GameOfThronesClassifier")
    problem = A_Star(heuristic, SyntaxProblem(6), vocabulary)
elif option == 2:
    vocabulary = text_utils.genetic_import_text("ThreeLittlePigs")
    heuristic = Heuristic("ThreeLittlePigsClassifier", "ThreeLittlePigs")
    problem = Genetic(heuristic, SyntaxProblem(6), vocabulary)
problem.execute()