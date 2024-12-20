import utils

# TODO verify all directories in wconfig are relative,
#      independent, within the project, and valid directories
# TODO verify all directories in wextern are outside project
#      and valid (and not within each other?)
# TODO add ability to provide a project_dir_path instead of
#      using working directory
# TODO should we really refer to the test and main dirs as the src dir sometimes?
# TODO make consistent order of include_dir and src_dir in places

class Assembly:

    cpp_version: int
    shared: bool
    static: bool

    src_dir_path: str
    include_dir_paths: list

    lib_names: list
    lib_dir_paths: list

    build_dir_path: str
    target_path: str

    # TODO require that section equals src, main, or test
    # TODO find cleaner way to determine extensions for target
    def __init__(self, config: dict, extern: dict, section: str) -> None:
        self.cpp_version = config["settings"]["c++"]
        self.shared = section == "src"
        self.static = config["settings"]["static"][section]

        self.src_dir_path = config["directories"][section]
        self.include_dir_paths = [config["directories"]["include"]] + extern["includes"]["all"] + extern["includes"][section]

        self.lib_names = config["dependencies"]["all"] + config["dependencies"][section]
        self.lib_dir_paths = extern["libraries"]["all"] + extern["libraries"][section]

        if section != "src":
            self.lib_names.append(config["targets"]["src"])
            self.lib_dir_paths.append(config["directories"]["bin"])

        self.build_dir_path = utils.add_paths(config["directories"]["build"], config["directories"][section])

        self.target_path = utils.add_paths(config["directories"]["bin"], config["targets"][section])
        if section == "src":
            self.target_path += ".dll"
        else:
            self.target_path += ".exe"

class Project:

    src: Assembly
    main: Assembly
    test: Assembly

    def __init__(self) -> None:
        config_path = "wconfig.json"
        extern_path = "wextern.json"

        config = utils.read_json_dict(config_path)
        extern = utils.read_json_dict(extern_path)

        self.src = Assembly(config, extern, "src")
        self.main = Assembly(config, extern, "main")
        self.test = Assembly(config, extern, "test")
