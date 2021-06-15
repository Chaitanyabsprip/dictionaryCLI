Note: This project is in alpha stage, bugs and breaking changes are too be expected.

# DictionaryCLI

A cross-platform command line dictionary that allows you to bookmark words and easily flip
through them.

## Features

- **Search Mode**: Get definitions of words or phrases that includes different
parts of speeach, synonyms, antonyms and more.
- **Flip Mode**: Bookmark words and access them in the Flip mode.
- Configurable commands and keybinds.
- Cross platform, support for Linux and Windows

## Usage

Launch the application: `dictcli`

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

![Screenshot:2021-06-15](https://user-images.githubusercontent.com/55058351/122082231-73f8f100-ce1d-11eb-824a-058d2c007270.png)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
  
Install all the required python packages

```bash
pip3 install -r requirements.txt
```

or

```bash
make setup
```

### Installing


1. Install dictcli with python

```bash 
python3 setup.py install
```

2. with pip

```bash
pip3 install .
```

3. with make (using pyinstaller)

```bash
sudo make install
```

Now you should be able to run `dictcli` as a command from anywhere on the command line.

## Configuration

The configuration file is `$HOME/.config/dictCLI/config.yml` if you're on
Linux and `%LOCALAPPDATA%\dictCLI\config.yml` if you're on Windows.

The default config is in the root of the repository and is copied to the
location mentioned above on the installation of the application.

### Defaults:

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
- [ ] Non interactive use-case
- [ ] Deployment with CI
- [ ] Keybinds
- [ ] Support for multiple APIs
  
## Contributing

Contributions are always welcome!

Please read [CONTRIBUTING.md](https://github.com/Chaitanyabsprip/dictionaryCLI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

Please adhere to the [CODE OF CONDUCT](https://github.com/Chaitanyabsprip/dictionaryCLI/blob/master/CODE_OF_CONDUCT.md)

## Authors

- [@gsiddhant159](https://www.github.com/gsiddhant159)
- [@Chaitanyabsprip](https://www.github.com/Chaitanyabsprip)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
