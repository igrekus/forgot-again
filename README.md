## Python utilities

Growing collection of helper functions implementing those little snippets you always have to google for.

### Examples

Remove a file

```python
# Write
remove_if_exists('unneeded.file')

# Instead of

if isfile('unneeded.file'):
    os.remove('unneeded.file')

# or
try:
    os.remove('unneeded.file')
except FileNotFoundError:
    pass
```

Make dirs:

```python
# Write
make_dirs('dir')

# Instead of
if not isdir(path):
    makedirs(path)

# or
try:
    os.makedirs(path)
except FileExistsError:
    pass
```

TODO:

Priority:
* [ ] Make a package

Meh:

* [ ] Update readme 
* [ ] Add docstrings 
* [ ] Add more stuff

## Warning

API will change, a lot.
