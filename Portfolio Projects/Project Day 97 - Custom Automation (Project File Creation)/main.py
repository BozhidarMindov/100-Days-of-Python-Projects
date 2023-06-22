import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create a Python project folder.")
    parser.add_argument("-p", "--project_path", help="Path where the project folder will be created")
    parser.add_argument("-f", "--functions", nargs="+", default=[], help="Function names to be created in main.py")
    parser.add_argument("-i", "--imports", nargs="+", default=[], help="Import statements to be added in main.py")

    return parser.parse_args()


def create_project_folder(project_path):
    if os.path.exists(project_path):
        raise FileExistsError(
            "Project folder already exists. Please provide a different path or delete the existing folder.")

    os.makedirs(project_path)
    os.chdir(project_path)


def add_shebang(main_file):
    main_file.write("#!/usr/bin/env python3\n\n")


def add_imports(main_file, import_names):
    for import_name in import_names:
        main_file.write(f"import {import_name}\n")
    main_file.write("\n")


def add_sample_functions(main_file, function_names):
    for function_name in function_names:
        main_file.write(f"\ndef {function_name}():\n    pass\n\n")


def create_main_file(function_names, import_names):
    with open(os.path.join("main.py"), "w") as main_file:
        add_shebang(main_file)
        add_imports(main_file, import_names)
        add_sample_functions(main_file, function_names)

        main_file.write("\ndef main():\n    pass\n\n")
        main_file.write('\nif __name__ == "__main__":\n    main()\n')


def create_requirements_file():
    with open(os.path.join("requirements.txt"), "w"):
        pass


def create_project(project_path, function_names, import_names):
    create_project_folder(project_path)
    create_main_file(function_names, import_names)
    create_requirements_file()


def main():
    args = parse_arguments()
    project_path = args.project_path
    function_names = args.functions
    import_names = args.imports

    create_project(project_path, function_names, import_names)


if __name__ == "__main__":
    main()
