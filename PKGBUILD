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
md5sums=('58e861050a52fa055e78b3dfd2e478c1')
backup=('etc/conf.d/julius-actions.conf')

package()
{
  install -D -m755 ${srcdir}/usr/bin/julius-actions \
                   ${pkgdir}/usr/bin/julius-actions || return 1
  install -D -m755 ${srcdir}/usr/bin/julius-actions.py \
                   ${pkgdir}/usr/bin/julius-actions.py || return 1
  
  install -D -m755 ${srcdir}/etc/conf.d/julius-actions.conf \
                   ${pkgdir}/etc/conf.d/julius-actions.conf || return 1
  install -D -m755 ${srcdir}/usr/lib/systemd/system/julius-actions.service \
                   ${pkgdir}/usr/lib/systemd/system/julius-actions.service || return 1
}
