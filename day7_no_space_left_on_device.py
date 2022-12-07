class Dir:
    def __init__(self) -> None:
        self.dirs: dict[str, Dir] = {}
        self.files: dict[str, File] = {}

    @property
    def size(self) -> int:
        return sum(x.size for x in list(self.dirs.values()) + list(self.files.values()))


class File:
    def __init__(self, size: int) -> None:
        self.size = size


def main(terminal: str) -> None:
    root: Dir | None = None
    cwd: Dir | None = None
    for line in terminal.splitlines():
        if line[0] == "$":
            cmd, *args = line[1:].split()
            if cmd == "cd":
                if root is None:
                    root = Dir()
                    cwd = root
                else:
                    # TODO: cd ..
                    cwd = cwd.dirs[args[0]]
        else:
            size, name = line.split()
            try:
                cwd.files[name] = File(int(size))
            except ValueError:
                cwd.dirs[name] = Dir()
    print("hello")


if __name__ == "__main__":
    INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    main(INPUT)
