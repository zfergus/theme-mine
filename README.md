# Theme-Mine

This is my theme for Ubunut/Unity. It utilizes the Numix-gtk theme and a 
custom set of Flattr icons.

## Contents

TODO: Breifly describe the four folder structure

## Installation

### Theme
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
sudo cp -r /path/to/theme-mine/flattr-mine /usr/share/icons/
```

**To create a live update via a symbolic link:**
```bash
sudo ln -s /path/to/theme-mine/flattr-mine /usr/share/icons/flattr-mine
```

After copying or linking the icons use `unity-tweak-tool` to select 
`flattr-mine` from the icons menu.

### Launcher
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
original launcher icons.

### Wallpaper
Select an image in `path/to/theme-mine/wallpapers` or a desired image. 
Right click and select `Set as Wallpaper`.

## License

TODO: Describe the licence

## Credits

TODO: Give credit to original creators

