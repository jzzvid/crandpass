#!/bin/sh

# RPM package script
# This script will create an RPM file for installation on Red Hat and SUSE
# based systems.  It requires rpmbuild.

# Variables
VERSION=6

# Functions
z_package () { 
   echo "creating purified source..."
   mkdir ./crandpass-$VERSION
   cp -r ./doc ./crandpass-$VERSION
   cp -r ./src ./crandpass-$VERSION
   tar -czf crandpass-$VERSION.tar.gz ./crandpass-$VERSION
   rm -rf ./crandpass-$VERSION
   
   echo "build package..."
   cp ./crandpass-$VERSION.tar.gz ~/rpmbuild/SOURCES
   rpmbuild -bb crandpass.spec
   
   echo "cleaning up..."
   rm -f ./crandpass-$VERSION.tar.gz
   }
   
z_package
exit
