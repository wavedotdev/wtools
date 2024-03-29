import os
import sys
import private.private as private
import wrun

def runtest():
    private.check_environment()

    config = private.read_config()

    if config["type"] == "library":
        os.chdir("test")
        wrun.run()
    elif config["type"] == "test":
        wrun.run()
    else:
        sys.exit("Can only run test in library or test environment.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.exit("Too many arguments.")

    runtest()