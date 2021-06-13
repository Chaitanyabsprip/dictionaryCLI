PYTHON = python3
CACHE_DIR = "${HOME}/.cache/dictCLI"
CONFIG_DIR = "${HOME}/.config/dictCLI"


.PHONY = help setup clean

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"

clean:
	rm -rf dictVenv

install:
	pip install pyinstaller
	sudo pyinstaller dictcli/main.py -n dictcli --onefile 

run: setup
	PYTHONPATH='.' ${PYTHON} dictcli/main.py

setup:
	@[ -d "dictVenv" ] || virtualenv dictVenv
	@pip install -r requirements.txt
	@[ -d ${CACHE_DIR} ] || (mkdir "${CACHE_DIR}" && mkdir "${CACHE_DIR}/word_cache")
	@[ -d ${CONFIG_DIR} ] || (mkdir "${CONFIG_DIR}" && cp config.yml "${CONFIG_DIR}/config.yml")

test: setup
	${PYTHON} -m unittest
