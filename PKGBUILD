# Author: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>
# Maintainer: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>

pkgname=julius-actions
pkgver=1.0.1
pkgrel=1
pkgdesc="julius action daemon"
arch=('x86_64')
url="https://github.com/arcan1s/julius-actions"
license=("GPL")
depends=('bash' 'julius' 'python2')
source=(https://github.com/arcan1s/julius-actions/releases/download/V.${pkgver}/${pkgname}-${pkgver}.tar.xz)
md5sums=('c8a6889ebb6b019580973ef13ddc8d18')
backup=('etc/conf.d/julius-actions.conf')

package()
{
  install -D -m755 ${srcdir}/usr/bin/julius-actions \
                   ${pkgdir}/usr/bin/julius-actions || return 1
  install -D -m755 ${srcdir}/usr/bin/julius-actions.py \
                   ${pkgdir}/usr/bin/julius-actions.py || return 1
  
  install -D -m755 ${srcdir}/etc/conf.d/julius-actions.conf \
                   ${pkgdir}/etc/conf.d/julius-actions.conf || return 1
}
