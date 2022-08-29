import os
import sys 
from .p2 import P2
from .p5 import P5
from .Solution import Solution

problem_map = {
    "p1": None,
    "p2": P2,
    "p3": None,
    "p4": None,
    "p5": P5, 
    "p6": None
}

problem_id = "p2"
test_input_path = "./src/{0}/test/input".format(problem_id)
test_output_path = "./src/{0}/test/output".format(problem_id)

def check_args():
    global problem_id
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


# Saves the result in a file
def save_result(num: int, result: str):
    f = open("{0}/o{1}".format(test_output_path, num), "w")
    f.write(result)


def generate_file_output(f, problem_class: Solution, id: int):
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
        for id, filename in enumerate(input_files):
            f = open("{0}/{1}".format(test_input_path, filename), 'r')
            generate_file_output(f, problem_class, id+1)

    except Exception as e:
        print(e)
        print("Not possible to generate solution!")
        exit()


# RESOLUTION OF ARGUMENTS
if __name__ == '__main__':
    check_args()
    generate_output()
