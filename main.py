from A_Star import A_Star
from Problem import SyntaxProblem
from heuristic import Heuristic
from genetic import Genetic
import text_utils

vocabulary = text_utils.import_text("BaseText")

#Only needed when classifier was not created (it's expensive)
#text_utils.create_classifier("BaseTextClassifier", vocabulary)

heuristic = Heuristic("BaseTextClassifier")

print("Which search do you want?")
print("1. A*")
print("2. Genetic")

option = int(input())

problem = None
if option == 1:
    problem = A_Star(heuristic, SyntaxProblem(6), vocabulary)
elif option == 2:
    problem = Genetic(heuristic, SyntaxProblem(6), vocabulary)
problem.execute()