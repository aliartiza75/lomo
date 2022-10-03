.PHONY: docs
init:
	pip install -r requirements-dev.txt
test:
	# This runs all of the tests on all supported Python versions.
	tox -p



