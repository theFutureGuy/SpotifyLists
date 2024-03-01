# Makefile for COSC525-Project2
.ONESHELL:
SHELL=/bin/bash
PYTHON_VERSION=3.10
ENV_NAME=tune_craft

# Use venv
BASE=venv
BIN=$(BASE)/bin
CREATE_COMMAND="python$(PYTHON_VERSION) -m venv $(BASE)"
DELETE_COMMAND="rm -rf $(BASE)"
ACTIVATE_COMMAND="source $(BIN)/activate"
DEACTIVATE_COMMAND="deactivate"

# To load an env file, use env_file=<path to env file>
# e.g. make release env_file=.env
ifneq ($(env_file),)
	include $(env_file)
endif

all:
	$(MAKE) help

help:
	@echo
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "                                              DISPLAYING HELP                                              "
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "Use make <make recipe> [env_file=<path to env file>]"
	@echo
	@echo "make help"
	@echo "       Display this message"
	@echo "make install [env_file=<path to env file>]"
	@echo "       Call clean delete_env create_env setup tests"
	@echo "make clean [env_file=<path to env file>]"
	@echo "       Delete all './build ./dist ./*.pyc ./*.tgz ./*.egg-info' files"
	@echo "make create_env [env_file=<path to env file>]"
	@echo "       Create a new virtual environment for the specified python version"
	@echo "make delete_env [env_file=<path to env file>]"
	@echo "       Delete the current virtual environment"
	@echo "-----------------------------------------------------------------------------------------------------------"

install:
	$(MAKE) delete_env
	$(MAKE) create_env
	$(MAKE) clean
	$(MAKE) requirements
	@echo -e "\033[0;31m############################################"
	@echo
	@echo "Installation Successful!"
	@echo "To activate the virtual environment run:"
	@echo '    source venv/bin/activate'

requirements:
	pip install -r requirements.txt

create_env:
	@echo "Creating virtual environment.."
	@eval $(CREATE_COMMAND)

delete_env:
	@echo "Deleting virtual environment.."
	@eval $(DELETE_COMMAND)

clean:
	@echo "Cleaning up..."
	rm -rf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info

.PHONY: help install clean delete_env create_env requirements
