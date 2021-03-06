PYTHON	= python3
MODULE	= rhd
VERSION	= $(shell awk '{print $$3}' ${MODULE}/_version.py | tr -d "'")

.PHONY: clean
clean: clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name __pycache__ -delete


.PHONY: build
build:
	$(PYTHON) setup.py bdist

.PHONY: test
test:
	$(PYTHON) setup.py bdist

.PHONY: source
source:
	$(PYTHON) setup.py sdist

.PHONY: install
install:
	$(PYTHON) setup.py install

.PHONY: release
release:
	git tag -s $(VERSION) -m "$(VERSION)"
	$(PYTHON) setup.py check sdist
	git push origin master --tags

.PHONY: deploy
deploy:
	#twine upload dist/*
