#! /usr/bin/python3

import pathlib
import sys

import subprocess

CMD_TO_PKG_TABLE = {
    "ghc": "ghc",
    "ghci": "ghc",
    "ghc-pkg": "ghc",
    "haddock": "ghc",
    "hp2ps": "ghc",
    "hpc": "ghc",
    "hsc2hs": "ghc",
    "runghc": "ghc",
    "runhaskell": "ghc",
    "cabal": "cabal",
    "stack": "stack",
    "haskell-language-server-wrapper": "hls",
}


def parse_args() -> tuple[str, list[str]]:
    prog_filename = pathlib.Path(sys.argv[0])
    remaining_args = sys.argv[1:]
    return prog_filename.name, remaining_args


def launch():
    prog_name, remaining_args = parse_args()

    if prog_name in CMD_TO_PKG_TABLE:
        target_exec_path = (
            pathlib.Path("~").expanduser().joinpath(".ghcup", "bin", prog_name)
        )
        if not target_exec_path.is_file():
            subprocess.run(
                [
                    "ghcup",
                    "install",
                    CMD_TO_PKG_TABLE[prog_name],
                    "--set",
                    "recommended",
                ],
                shell=False,
                check=True,
            )
        subprocess.run([target_exec_path, *remaining_args], shell=False, check=True)


if __name__ == "__main__":
    launch()
