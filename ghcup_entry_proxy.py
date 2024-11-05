#! /usr/bin/python3

import pathlib
import sys
import os

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


GHC_INSTALL_SH_FILE_URL = "https://raw.githubusercontent.com/haskell/ghcup-hs/master/scripts/hooks/stack/ghc-install.sh"

def launch():
    prog_name, remaining_args = parse_args()

    if prog_name in CMD_TO_PKG_TABLE:
        target_exec_path = (
            pathlib.Path("~").expanduser().joinpath(".ghcup", "bin", prog_name)
        )
        if not target_exec_path.is_file():
            pkg_name = CMD_TO_PKG_TABLE[prog_name]
            subprocess.run(
                [
                    "ghcup",
                    "install",
                    pkg_name,
                    "--set",
                    "recommended",
                ],
                shell=False,
                check=True,
            )
            if pkg_name == "stack":
                ghc_install_sh_filename = pathlib.Path("~").expanduser().joinpath(".stack", "hooks", "ghc-install.sh")
                ghc_install_sh_filename.parent.mkdir(exist_ok=True, parents=True)
                subprocess.run(["curl", GHC_INSTALL_SH_FILE_URL, "-o", ghc_install_sh_filename], shell=False, check=True)
                subprocess.run(["chmod", "u+x", ghc_install_sh_filename])
                subprocess.run(["stack", "config", "set", "system-ghc", "false", "--global"])
                
        subprocess.run([target_exec_path, *remaining_args], shell=False, check=True)


if __name__ == "__main__":
    launch()
