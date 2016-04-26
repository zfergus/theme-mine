# Theme-Mine

This is my theme for Ubunut/Unity. It utilizes the Numix-gtk theme and a custom set of 
Flattr icons.

## Contents

TODO: Breifly describe the four folder structure

## Installation

### Theme
To install Numix open a terminal and type the following:

```bash
sudo add-apt-repository ppa:numix/ppa
sudo apt-get update
sudo apt-get install numix-gtk-theme
```

This will install the Numix theme. To select the theme for use, open 
Unity-Tweak-Tool and select the numix theme from the themes menu.

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

After copying or linking the icon use `unity-tweak-tool` to select the icons.

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

This command requires that you executed command one above to backup the original 
launcher icons.

### Wallpaper
Select an image in `path/to/theme-mine/wallpapers` or a desired image. 
Right click and select `Set as Wallpaper`.

## License

TODO: Describe the licence

## Credits

TODO: Give credit to original creators

