from make import *
import sys
import utils

# TODO consider the args in the command
def run_assembly(assembly: Assembly, args = []) -> None:
    utils.run_command(assembly.target_path)

## Build src and main then run main with 'args'.
def run_main(project: Project, args = []) -> None:
    make_main(project)
    run_assembly(project.main, args)

## Build src and test then run test with 'args'.
def run_test(project: Project, args = []) -> None:
    make_test(project)
    run_assembly(project.test, args)

## This is the behavior of wrun.
if __name__ == "__main__":
    target = sys.argv[1]
    args = sys.argv[2:]

    project = Project()

    if target == "main":
        run_main(project)
    elif target == "test":
        run_test(project)
    else:
        raise Exception("Invalid run target " + target)