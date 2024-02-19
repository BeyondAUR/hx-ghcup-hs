# Maintainer: Evan Greenup <evan_greenup@protonmail.com>
pkgname=ghcup-hs
pkgver=0.1.20.0
pkgrel=1
license=("LGPL-3.0-only")
arch=('x86_64')
url="https://github.com/haskell/ghcup-hs"
depends=(curl)
makedepends=(stack)
provides=("ghc" "stack" "cabal-install" "haskell-language-server")
conflicts=("ghc" "stack" "cabal-install" "haskell-language-server" "ghcup-hs-bin")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/haskell/ghcup-hs/archive/refs/tags/v${pkgver}.tar.gz"
        "ghcup-name-proxy.sh")
sha256sums=('9de3f367f298e9efecf9e9c2d50b828cec3af8cfd391e3b235057822b75d8fad'
            'ea10c877feb9f2d5f48bd5fa69d35537db66e18029650414b567d755029ac6d2')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  stack build ghcup:exe:ghcup
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  stack test
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -m755 -p "${pkgdir}/usr/bin/"
  install -m755 "$(stack path --local-install-root)/bin/ghcup" "${pkgdir}/usr/bin/ghcup"
  chmod 755 "${pkgdir}/usr/bin/ghcup"
  install -m755 "${srcdir}/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/ghcup-name-proxy.sh"
  mkdir -m755 -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/cabal"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/ghc"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/ghci"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/ghc-pkg"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/haddock"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/haskell-language-server-wrapper"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/hp2ps"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/hpc"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/hsc2hs"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/runghc"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/runhaskell"
  ln -s "/usr/bin/ghcup-name-proxy.sh" "${pkgdir}/usr/bin/stack"


  _install_completion_script bash bash-completion/completions/ghcup
  _install_completion_script zsh zsh/site-functions/_ghcup
  _install_completion_script fish fish/vendor_completions.d/ghcup.fish
}


_install_completion_script() {
  install -Dm644 <("$pkgdir/usr/bin/ghcup" --$1-completion-script "/usr/bin/ghcup") "$pkgdir/usr/share/$2"
}
