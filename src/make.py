from compile_and_link import *
from project import *
import sys

# TODO add commands for getting args and exiting command sequence early
#      possibly instead of raise?
# TODO clean up all raise statements to be written in consistent style
# TODO do something to correct paths in json files for the platform
# TODO find some way to move all this repetition into helpers
# TODO print something out when nothing is changed to say nothing needed to change
# TODO we need to trigger a complete rebuild if wconfig or wextern is changed
# TODO if target is static need to check if dlls are newer than target

def make_assembly(assembly: Assembly) -> None:
    compile_and_link( \
        assembly.cpp_version, assembly.shared, assembly.static, \
        assembly.src_dir_path, assembly.include_dir_paths, \
        assembly.lib_names, assembly.lib_dir_paths, \
        assembly.build_dir_path, assembly.target_path)

## Build src.
def make_src(project: Project) -> None:
    make_assembly(project.src)

## Build src and main.
def make_main(project: Project) -> None:
    make_src(project)
    make_assembly(project.main)

## Build src and test.
def make_test(project: Project) -> None:
    make_src(project)
    make_assembly(project.test)

## This is the behavior of wmake.
if __name__ == "__main__":
    target = sys.argv[1]

    project = Project()

    if target == "src":
        make_src(project)
    elif target == "main":
        make_main(project)
    elif target == "test":
        make_test(project)
    else:
        raise Exception("Invalid make target " + target)