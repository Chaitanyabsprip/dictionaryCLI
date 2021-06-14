PYTHON = python3
CACHE_DIR = "${HOME}/.cache/dictCLI"
CONFIG_DIR = "${HOME}/.config/dictCLI"


.PHONY = help setup clean test

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"

clean:
	@rm -rf dictVenv

install: setup
	@/usr/bin/env pip3 install pyinstaller
	@pyinstaller dictcli/main.py -n dictcli --onefile && cp dist/dictcli /usr/local/bin/dictcli || rm -rf build dist dictcli.spec
	@echo "cleaning up"
	@/usr/bin/env pip3 uninstall pyinstaller
	@rm -rf build dictcli.spec

run: setup
	PYTHONPATH='.' ${PYTHON} dictcli/main.py

setup:
	@[ -d "dictVenv" ] || virtualenv dictVenv
	@/usr/bin/env pip3 install -r requirements.txt
	@[ -d ${CACHE_DIR} ] || (mkdir "${CACHE_DIR}" && mkdir "${CACHE_DIR}/word_cache")
	@[ -d ${CONFIG_DIR} ] || (mkdir "${CONFIG_DIR}" && cp config.yml "${CONFIG_DIR}/config.yml")

test: setup
	@${PYTHON} -m unittest

uninstall:
	@rm -rf /usr/local/bin/dictcli build dist dictcli.spec
