from A_Star import A_Star
from Problem import SyntaxProblem
from heuristic import Heuristic
import text_utils

vocabulary = text_utils.import_text("BaseText")

#Only needed when classifier was not created (it's expensive)
#text_utils.create_classifier("BaseTextClassifier", vocabulary)

heuristic = Heuristic("BaseTextClassifier")

problem = A_Star(heuristic, SyntaxProblem(6), vocabulary)
problem.execute()