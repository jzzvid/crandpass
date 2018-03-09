#!/bin/sh
# A simple install script

#FUNCTIONS
z_install() {
  echo "copying files..."
  cp ./src/crandpass /usr/bin
  echo "setting permissions..."
  chown root:root /usr/bin/crandpass
  chmod 755 /usr/bin/crandpass
  echo "done!"
}

z_remove() {
  echo "removing files..."
  rm -f /usr/bin/crandpass
  echo "done!"
}

z_help() {
  echo "crandpass installation script:"
  echo "To install crandpass run: install.sh"
  echo "To remove crandpass run: install.sh -r"
}

if [[ $EUID -ne 0 ]]; then
  z_help
  echo "ROOT REQUIRED!!"
  exit
fi

while getopts ":hr" opt; do
  case $opt in
   (h)
      z_help
      exit ;;
   (r)
      z_remove
      exit ;;
   (*)
      z_help
      exit ;;
   esac
done

z_install
exit