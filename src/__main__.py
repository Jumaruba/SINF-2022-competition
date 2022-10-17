import os
import sys 
from .p1 import P1
from .p2 import P2
from .p3 import P3
from .p4 import P4
from .p5 import P5
from .p6 import P6

from .Solution import Solution

problem_map = {
    "p1": P1,
    "p2": P2,
    "p3": P3,
    "p4": P4,
    "p5": P5, 
    "p6": P6 
}


problem_id = ""
test_input_path = ""
test_output_path = ""


def check_args():
    global problem_id
    global test_input_path
    global test_output_path 

    if len(sys.argv) > 2:
        print(  "WRONG ARGUMENTS:\n"
                "USAGE: python -m src <problem>\n"
                "<problem>: one of {0}".format(list(problem_map.keys())))
        exit()
    
    if sys.argv[1] not in list(problem_map.keys()):
        print(  "WRONG ARGUMENTS:\n"
            "USAGE: python -m src <problem>\n"
            "<problem>: one of {0}".format(list(problem_map.keys())))
        exit() 

    problem_id = sys.argv[1]
    test_input_path = "./src/{0}/test/input".format(problem_id)
    test_output_path = "./src/{0}/test/output".format(problem_id)


# Saves the result in a file
def save_result(num: str, result: str):
    f = open("{0}/output{1}.txt".format(test_output_path, num), "w")
    f.write(result)


def generate_file_output(f, problem_class: Solution, id: str):
    lines = f.readlines()
    args = problem_class.get_arguments(lines)
    result = problem_class.solve(*args)
    result_string = problem_class.format_result(result)
    save_result(id, result_string)

# Generates the output for the given problem
def generate_output():
    try:
        input_files = [f for f in os.listdir(test_input_path)]
        input_files.sort()
        problem_class = problem_map[problem_id]
        input_files.sort()
        for filename in input_files:
            id = filename.replace("input", "").replace(".txt", "")
            f = open("{0}/{1}".format(test_input_path, filename), 'r')
            generate_file_output(f, problem_class, id)

    except Exception as e:
        print(e)
        print("Not possible to generate solution!")
        exit()


# RESOLUTION OF ARGUMENTS
if __name__ == '__main__':
    check_args()
    generate_output()
    