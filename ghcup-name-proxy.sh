#! /bin/sh

progname=$(basename "$0")

acceptable_proxy_array=("cabal" "ghc" "ghci" "ghc-pkg" "haddock" "haskell-language-server-wrapper" "hp2ps" "hpc" "hsc2hs" "runghc" "runhaskell" "stack")


_value="\<${progname}\>"

if [[ ${acceptable_proxy_array[@]} =~ ${_value} ]]
then
    "${HOME}/.ghcup/bin/${progname}" $@ || (ghcup install ${progname} recommended && "${HOME}/.ghcup/bin/${progname}" $@)
else
    echo "ghcup-name-proxy can neither be called directly nor called with an unknown proxy name."
fi 
