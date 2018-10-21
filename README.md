# binja_r2dec

### What this is

This is a simple plugin that just invokes the radare2 plugin, `r2dec` (an awesome decompiler), in Binary Ninja. This unfortunately does not preserve any comments or names you've given to variables and functions. Maybe one day...

### Requirements

You must have radare2, r2dec, and r2pipe installed. Details on installing radare2 can be found [here](https://github.com/radare/radare2) and details on installing r2dec [here](https://github.com/wargio/r2dec-js).

Then to install r2pipe, run:

```
$ pip install r2pipe --user
```

Lastly, once radare2 is installed, you must make sure `radare2` is in Binary Ninja's `PATH`. I've commented out two lines in the `__init__.py` file that you can edit to fix this issue.
