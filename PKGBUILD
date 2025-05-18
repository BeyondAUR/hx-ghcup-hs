# Maintainer: Evan Greenup <evan_greenup@protonmail.com>
_name=ghcup-hs
pkgname=hx-${_name}
pkgver=0.1.50.2
pkgrel=1
license=("LGPL-3.0-only")
arch=('x86_64')
url="https://github.com/haskell/ghcup-hs"
depends=(curl python gcc gmp make ncurses libyaml)
makedepends=(stack cabal-install git)
provides=("ghc" "stack" "cabal-install" "haskell-language-server")
conflicts=("ghc" "stack" "cabal-install" "haskell-language-server" "ghcup-hs-bin")
replaces=("ghcup-hs")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/haskell/ghcup-hs/archive/refs/tags/v${pkgver}.tar.gz"
        "ghcup_entry_proxy.py")
sha256sums=('ba2a2ef799fa7810970e09b19a7fdd7b2360ddd64d8e9b0624ab640cca627b89'
            '9e440ce518a46d9d1b42617dd45fd8fc557e66a64fd49929694fdf7336a78263')
_resolver="lts-23.1"
prepare() {
  stack update --resolver=$_resolver
}

build() {
  cd "${srcdir}/${_name}-${pkgver}"

  stack build --resolver=$_resolver ghcup:exe:ghcup
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  mkdir -m755 -p "${pkgdir}/usr/bin/"
  install -m755 "$(stack path --resolver=${_resolver} --local-install-root)/bin/ghcup" "${pkgdir}/usr/bin/ghcup"
  chmod 755 "${pkgdir}/usr/bin/ghcup"
  mkdir -m755 -p "${pkgdir}/usr/share/ghcup/script"
  install -m755 "${srcdir}/ghcup_entry_proxy.py" "${pkgdir}/usr/share/ghcup/script/ghcup_entry_proxy.py"
  mkdir -m755 -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/cabal"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/ghc"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/ghci"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/ghc-pkg"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/haddock"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/haskell-language-server-wrapper"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/hp2ps"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/hpc"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/hsc2hs"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/runghc"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py""${pkgdir}/usr/bin/runhaskell"
  ln -s "/usr/share/ghcup/script/ghcup_entry_proxy.py" "${pkgdir}/usr/bin/stack"


  _install_completion_script bash bash-completion/completions/ghcup
  _install_completion_script zsh zsh/site-functions/_ghcup
  _install_completion_script fish fish/vendor_completions.d/ghcup.fish
}


_install_completion_script() {
  install -Dm644 <("$pkgdir/usr/bin/ghcup" --$1-completion-script "/usr/bin/ghcup") "$pkgdir/usr/share/$2"
}
