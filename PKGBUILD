# Author: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>
# Maintainer: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>

pkgname=julius-actions
pkgver=1.0.0
pkgrel=1
pkgdesc="julius action daemon"
arch=('x86_64')
url="https://github.com/arcan1s/julius-actions"
license=("GPL")
depends=('bash' 'julius' 'python2')
source=(https://github.com/arcan1s/julius-actions/releases/download/V.${pkgver}/${pkgname}-${pkgver}.tar.xz)
md5sums=('4e9676dfe75441db18a1c425b0fc4b2f')
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
