all: test install clean

.PHONY: test install clean

test:
	python setup.py test

install:
	python setup.py install

clean:
	rm -rf solver/__pycache__/
	rm -rf android_bubble_sort_puzzle_solver.egg-info/
	rm -rf tests/__pycache__/
	rm -rf tests.egg-info/
	rm -rf build/
	rm -rf .coverage
	rm -rf dist/
	rm -rf .eggs/
	rm -rf .pytest_cache/
