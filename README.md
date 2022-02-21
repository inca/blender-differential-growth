# Differential Growth for Blender

![](https://boris.okunskiy.name/posts/lichen1-transparent.png)

_Please see [the orginal blog post](https://boris.okunskiy.name/posts/blender-differential-growth) for a formal introduction_.

Differential growth is a generative algorithm inspired by the growth occurring in living organisms such as lichens, algae, poriferas and other kinds of organic forms.

## Installation

1. Download a zip file from [Releases](https://github.com/inca/blender-differential-growth/releases/latest)
2. Install the addon in Blender by going to Edit > Preferences > Addons > Install

### Important notes

- The algorithm is "destructive" (i.e. it will modify the mesh in-place). It is recommended to set the Undo Steps to maximum (Preferences > System > Undo Steps) to be able to revert to previous results.

- Some combination of parameters may result in [combinatorial explosion](https://en.wikipedia.org/wiki/Combinatorial_explosion) causing Blender to hang. It is recommended to save often.

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

## Credits

This work is heavily inspired by the work of others. Here's a non-exhaustive list of resources used in creation of this addon:

- [Anders Hoff · inconvergent.net](https://inconvergent.net/)
- [Floraform by Nervous System](https://n-e-r-v-o-u-s.com/projects/sets/floraform/)
- [Kaspar Ravel Blog](https://www.kaspar.wtf/code-poems/differential-growth)
- [Jason Webb 2D differential growth](https://medium.com/@jason.webb/2d-differential-growth-in-js-1843fd51b0ce)
- [Sheltron's amazing collection of math art](https://nshelton.github.io/about/)

## License

Differential Growth Addon uses [Blender License](https://www.blender.org/about/license/).

Free to Use. Free to Change. Free to Share. Free to Sell Your Work.
