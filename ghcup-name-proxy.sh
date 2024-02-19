#! /bin/sh

progname=$(basename "$0")

acceptable_proxy_array=("ghc" "runhaskell" "runghc" "ghci" "haddock" "stack" "cabal" "haskell-language-server-wrapper")


_value="\<${progname}\>"

if [[ ${acceptable_proxy_array[@]} =~ ${_value} ]]
then
    ghcup run -- "$progname" $@
fi 
