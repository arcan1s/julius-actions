#!/bin/bash

if [ -d julius-actions ]; then
  rm -rf julius-actions
fi
mkdir -p julius-actions/usr/bin

cp sources/* julius-actions/usr/bin/

cd julius-actions
tar -cf - * | xz -9 -c - > ../julius-actions-1.1.0.tar.xz
cd ..
rm -r julius-actions
