# Theme-Mine

<img src="./flattr-mine/flattr-mine.png" width="600px">

This is my theme for Ubunutu/Unity. It utilizes the
[Numix-GTK](https://github.com/numixproject/numix-gtk-theme) theme and a
custom version of the
[Flattr](https://github.com/KaOSx/flattr-icons-kde)/
[Lüv](https://github.com/NitruxSA/luv-icon-theme) icon theme.

## Contents

Theme-Mine consists of multiple components, an icon theme, GTK theme, and a set
of wallpapers.

### Flattr-Mine
Flattr-Mine is a customized version of the Flattr/Lüv icon theme. It includes
icons from different versions of the original theme as well as some additional
self-created icons.

### Numix-Mine
Numix-Mine is a stable backup of the Numix-GTK theme. This theme has been
unedited and is included as a stable version. Feel free to use a
newer version. See [here](https://github.com/numixproject/numix-gtk-theme)
for more information.

## Installation

Use the bash script `install.sh` to install Theme-Mine, or install manually:

### GTK Theme
To install the theme you can either copy it, requiring a copy for every
update, or create a symbolic link, requiring no future copying.

**To copy the theme:**
```bash
sudo cp -r /path/to/theme-mine/numix-mine/ /usr/share/themes/
```

**To create a live update via a symbolic link:**
```bash
sudo ln -s /path/to/theme-mine/numix-mine/ /usr/share/themes/Numix-Mine
```

After copying or linking the theme use `unity-tweak-tool` to select the
`Numix-Mine` from the `Themes` menu.

### Icons
To install the icons you can either copy them requiring a copy for every
update or create a symbolic link requiring no future copying.

**To copy icons:**
```bash
sudo cp -r /path/to/theme-mine/flattr-mine/ /usr/share/icons/
```

**To create a live update via a symbolic link:**
```bash
sudo ln -s /path/to/theme-mine/flattr-mine/ /usr/share/icons/flattr-mine
```

After copying or linking the icons use `unity-tweak-tool` to select
`flattr-mine` from the icons menu.

<!-- ### Launcher
To remove the bubble around the launcher icons:

```bash
sudo cp /usr/share/unity/icons/* path/to/theme-mine/launcher/Backup_Icons/
sudo cp /path/to/theme-mine/launcher/New_Icons/* /usr/share/unity/icons/
```

The first command is to make a backup of the originals in case something goes
wrong or you want the originals back. The second command then replaces the
default launcher icons with the new ones.

#### To Restore Original Launcher Icons

```bash
sudo cp path/to/theme-mine/launcher/Backup_Icons/* /usr/share/unity/icons/
```

This command requires that you executed command one above to backup the
original launcher icons. -->

### Wallpaper
Select an image in `path/to/theme-mine/wallpapers` or a desired image.
Right click and select `Set as Wallpaper`.

## License

Flattr-Mine is licensed under the Creative Commons License (CC BY-NC-SA 4.0).
See `flattr-mine/LICENSE.txt` for more information.

Numix-Mine is licensed under GNU General Public License (GPL-3.0+).
See `numix-mine/LICENSE` for more information.

## Credits

Flattr-Mine is based of the following Flattr/Luv icons with some original additions:
* [github.com/NitruxSA/luv-icon-theme](https://github.com/NitruxSA/luv-icon-theme)
* [github.com/MishkaRogachev/flattr-icons-kde](https://github.com/MishkaRogachev/flattr-icons-kde)
* [github.com/KaOSx/flattr-icons-kde](https://github.com/KaOSx/flattr-icons-kde)

Numix-Mine based on a stable version of:
* [github.com/numixproject/numix-gtk-theme](https://github.com/numixproject/numix-gtk-theme)

Wallpaper:
* [Ciri vs. Imlerith by Mo Xuan Zhang](./wallpapers/ciri.png)
* [The Saddest Khajiit by DarrenGeers](./wallpapers/khajiit.png)
* [Totem by Justin Maller](./wallpaper/wall.png)
