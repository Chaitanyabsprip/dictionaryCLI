Note: This project is in alpha stage. Bugs and breaking changes are to be expected.
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

Install dictionaryCLI with python

```bash 
  python setup.py install
```
    
## Configuration

The configuration file is `$HOME/.config/dictCLI/config.yml` if you're on
Linux and `$LOCALAPPDATA\dictCLI\config.yml` if you're on Windows
The default config is in the root of the repository and is copied to the
location mentioned above on the installation of the application.

##### Defaults:
```yaml
source: "wiktionary"

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
## Running Tests

To run tests, run the following command

```bash
  python -m unittest
```

## TODO

- [x] Use config.yml
- [ ] Deployment with CI
- [ ] Keybinds
- [ ] Support for multiple APIs
  
## Authors

- [@gsiddhant159](https://www.github.com/gsiddhant159)
- [@Chaitanyabsprip](https://www.github.com/Chaitanyabsprip)

  
## Contributing

Contributions are always welcome!

If you find any bugs or want to see any feature added, issues and PRs are
welcome!
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
