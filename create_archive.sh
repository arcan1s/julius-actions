#!/bin/bash

if [ -d julius-actions ]; then
  rm -rf julius-actions
fi
mkdir julius-actions

mkdir -p julius-actions/usr/{bin,lib}
mkdir -p julius-actions/usr/lib/systemd/system
mkdir -p julius-actions/etc/conf.d

cp sources/julius-actions.service julius-actions/usr/lib/systemd/system/
cp sources/julius-actions.conf julius-actions/etc/conf.d/
cp sources/julius-actions julius-actions/usr/bin/
cp sources/julius-actions.py julius-actions/usr/bin/

cd julius-actions
tar -cf - * | xz -9 -c - > ../julius-actions-1.0.1.tar.xz
cd ..
rm -r julius-actions
