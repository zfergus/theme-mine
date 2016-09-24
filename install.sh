#!/bin/bash
# Install Theme-Mine by adding symbolic links in the neccessary folders.

# Install GTK-theme
ln -sf ./numix-mine/ /usr/share/themes/Numix-Mine

# Install Icon theme
ln -sf ./flattr-mine/ /usr/share/icons/flattr-mine

# Add Mimetypes not included by Ubuntu
cp ./mime-types/lisp.xml /usr/share/mime/packages/lisp.xml
update-mime-database /usr/share/mime/

