# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3
CACHE_DIR = "${HOME}/.cache/dictCLI"
CONFIG_DIR = "${HOME}/.config/dictCLI"


# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help setup clean

# Defining an array variable
FILES = input output

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To clean the project type make clean"
	@echo "------------------------------------"

# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
setup:
	[ -d "dictVenv" ] || virtualenv dictVenv
	[ -d ${CACHE_DIR} ] || (mkdir "${CACHE_DIR}" && mkdir "${CACHE_DIR}/word_cache")
	[ -d ${CONFIG_DIR} ] || (mkdir "${CONFIG_DIR}" && cp config.yml "${CONFIG_DIR}/config.yml")

# The ${} notation is specific to the make syntax and is very similar to bash's $() 
# This function uses pytest to test our source files
test: setup
	${PYTHON} -m unittest
	
run: setup
	PYTHONPATH='.' ${PYTHON} dictcli/main.py

# In this context, the *.project pattern means "anything that has the .project extension"
clean:
	rm -rf dictVenv
