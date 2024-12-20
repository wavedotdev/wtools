from project import *
import sys
import utils

def clean_assembly(assembly: Assembly) -> None:
    utils.delete_path(assembly.build_dir_path)
    utils.delete_path(assembly.target_path)

## Clean src and main and test.
def clean_all(project: Project) -> None:
    clean_assembly(project.src)
    clean_assembly(project.main)
    clean_assembly(project.test)
    print("Cleaned all.")

## Clean src.
def clean_src(project: Project) -> None:
    clean_assembly(project.src)
    print("Cleaned src.")

## Clean main.
def clean_main(project: Project) -> None:
    clean_assembly(project.main)
    print("Cleaned main.")

## Clean test.
def clean_test(project: Project) -> None:
    clean_assembly(project.test)
    print("Cleaned test.")

## This is the behavior of wclean.
if __name__ == "__main__":
    target = sys.argv[1]

    project = Project()

    if target == "all":
        clean_all(project)
    elif target == "src":
        clean_src(project)
    elif target == "main":
        clean_main(project)
    elif target == "test":
        clean_test(project)
    else:
        raise Exception("Invalid clean target " + target)