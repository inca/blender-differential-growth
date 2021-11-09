# Differential Growth

![](demo.png)

## Development

It can be painful to develop in Blender's text editor.

One good solution is to symlink the repo to the Blender's addon location, then develop using your favorite editor.

### Mac/Linux

Locate the addons directory, then replace `ADDONS_DIR` in `symlink.sh` and run it.

### Windows

Run `cmd.exe` as Administrator (Start menu, search 'cmd', right click).

Then run (correct the paths as necessary):

```
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Blender\2.93\scripts\addons\diffgrow" "C:\Users\boris\3d\blender\diffgrowth"
```
