# Author: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>
# Maintainer: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>

pkgname=julius-actions
pkgver=1.1.0
pkgrel=1
pkgdesc="julius action daemon"
arch=('x86_64')
url="https://github.com/arcan1s/julius-actions"
license=("GPL")
depends=('bash' 'julius' 'python2')
source=(https://github.com/arcan1s/julius-actions/releases/download/V.${pkgver}/${pkgname}-${pkgver}.tar.xz)
md5sums=('00f1ed4d6be4ef0516daa007f1bb969f')

package()
{
  install -D -m755 ${srcdir}/usr/bin/julius-actions \
                   ${pkgdir}/usr/bin/julius-actions || return 1
  install -D -m755 ${srcdir}/usr/bin/julius-actions.py \
                   ${pkgdir}/usr/bin/julius-actions.py || return 1
  install -D -m755 ${srcdir}/usr/bin/ja-edit.py \
                   ${pkgdir}/usr/bin/ja-edit.py || return 1
}
