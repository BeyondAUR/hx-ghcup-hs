#! /bin/sh

progname=$(basename "$0")

contains() {
    [[ $1 =~ (^|[[:space:]])$2($|[[:space:]]) ]] && exit(0) || exit(1)
}

contains ("ghc" "runhaskell" "runghc" "ghci" "haddock" "stack" "cabal" "haskell-language-server-wrapper") || exit

ghcup run -- "$progname" $@