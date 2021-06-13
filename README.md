Note: This project is in alpha stage, bugs and breaking changes are too be expected.
# DictionaryCLI

A cross-platform command line dictionary that allows you to bookmark words and easily flip
through them.

## Features

- **Search Mode**: Get definitions of words or phrases that includes different
parts of speeach, synonyms, antonyms and more.
- **Flip Mode**: Bookmark words and access them in the Flip mode.
- Configurable commands and keybinds.
- Cross platform
## Usage

```bash
Modes:
    Search        ':search',  ':s'
    Flip          ':flip',    ':f'

Commands:
    Help          ':help',    ':h'
    Quit          ':quit',    ':q'
    Bookmark      '/b'

Flip Mode Commands:
    Next          '',  'n', 'j'
    Prev          '.', 'p', 'k'    
```

  
## Installation 


1. Install dictcli with python

```bash 
python setup.py install
```

2. with pip

```bash
pip install .
```

3. with make (uses pyinstaller)

```bash
sudo make install
```

## Configuration

The configuration file is `$HOME/.config/dictCLI/config.yml` if you're on
Linux and `$LOCALAPPDATA\dictCLI\config.yml` if you're on Windows.

The default config is in the root of the repository and is copied to the
location mentioned above on the installation of the application.

##### Defaults:
```yaml
commands:
  help: ["h", "help"]

  quit: ["q", "exit", "quit"]

  search: ["s", "search"]

  flip:
    cmds: ["f", "flip"]
    randomize: ["r", "random"]
    next: ["n", "j", ""]
    prev: ["p", "k", "."]
```
## TODO

- [x] Use config.yml
- [x] Colors support for print and prompt
- [ ] Deployment with CI
- [ ] Keybinds
- [ ] Support for multiple APIs
  
## Authors

- [@gsiddhant159](https://www.github.com/gsiddhant159)
- [@Chaitanyabsprip](https://www.github.com/Chaitanyabsprip)

  
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
