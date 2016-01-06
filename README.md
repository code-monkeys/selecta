# selecta
## Interactively select an entry from your history.

This is a python clone of François Fleuret's brilliant [selector](http://www.idiap.ch/~fleuret/software.html#selector)

```
$ selecta <(history)
```

# Installation

create a symlink:

```
$ sudo ln -s selecta.py /usr/bin/selecta
```

Add this to your .bashrc to bind the command to [ALT]+e:

```
bind '"\C-[e":"\C-a\C-kselecta <(history)\C-m"'
```
