# Imports make the mentioned "modules" accessible to the code within
# this file, which is itself a "module".
import argparse
import os
import datetime

def main() -> None:
    parser = argparse.ArgumentParser(prog="pyls", description="A baby version of ls.")
    # We now add descriptions for the expected arguments for our program.
    parser.add_argument(
        "dirname",
        nargs="?",# Indicates that either 0 or one directory name can be given.
        default=".", # Gives the default value to use when this argument is not given.
         # '.' means "current directory".
        help="The name of the directory whose contents are to be listed.",
    )
    parser.add_argument(
        "-l", "--longform",
        action="store_true",# Indicates that the value is a boolean and no further
           # values need to be supplied on the command line.
        default=False,# This is not really needed as False is the default already
        # when -l is not given on the command line. Including it
        # for illustration.
        help="Prints details about each file: <timestamp> <filesize> <filename>",
    )
      # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    parser.add_argument(
        "-F", "--formatted",
        action="store_true",
        default=False,
        help="Adds / for directories, * for executables.",
    )

    args = parser.parse_args()
    
    # Call the actual logic function
    pyls(args.dirname, args.longform, args.formatted)


def pyls(dirname: str, longform: bool, formatted: bool) -> None:
    try:
        entries = os.listdir(dirname)
    except FileNotFoundError:
        print(f"Error: Directory '{dirname}' not found.")
        return
    except NotADirectoryError:
        print(f"Error: '{dirname}' is not a directory.")
        return

    for name in sorted(entries):
        full_path = os.path.join(dirname, name)
        display_name = name

        # Add / or * if formatted
        if formatted:
            if os.path.isdir(full_path):
                display_name += "/"
            elif os.access(full_path, os.X_OK):
                display_name += "*"

        # Print in long form
        if longform:
            try:
                stats = os.stat(full_path)
                size = stats.st_size
                timestamp = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                print(f"{timestamp} {size:>8} {display_name}")
            except Exception as e:
                print(f"Error reading file info: {e}")
        else:
            print(display_name)


if __name__ == "__main__":
    main()
