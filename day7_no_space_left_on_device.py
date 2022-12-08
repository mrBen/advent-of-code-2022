#!/usr/bin/env python3

from typing import Optional


class Dir:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.dirs: dict[str, Dir] = {}
        self.files: dict[str, File] = {}

    @property
    def size(self) -> int:
        return sum(x.size for x in list(self.dirs.values()) + list(self.files.values()))


class File:
    def __init__(self, size: int, parent: Dir) -> None:
        self.size = size
        self.parent = parent


def main(terminal: str) -> None:
    root: Optional[Dir] = None
    cwd: Optional[Dir] = None
    dirs: list[Dir] = []
    for line in terminal.splitlines():
        if line[0] == "$":
            cmd, *args = line[1:].split()
            if cmd == "cd":
                if root is None:
                    root = Dir(None)
                    dirs.append(root)
                    cwd = root
                else:
                    if args[0] == "..":
                        cwd = cwd.parent
                    else:
                        cwd = cwd.dirs[args[0]]
        else:
            size, name = line.split()
            try:
                cwd.files[name] = File(int(size), cwd)
            except ValueError:
                dir = Dir(cwd)
                dirs.append(dir)
                cwd.dirs[name] = dir

    print("Part One:")
    print(sum(dir.size for dir in dirs if dir.size <= 100_000))

    print("Part Two:")
    print(min(dir.size for dir in dirs if root.size - dir.size <= 40_000_000))


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
