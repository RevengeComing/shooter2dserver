.PHONY: clean install

clean:
	rm -rf build/ dist/ shooter2d.egg-info/
	pip uninstall shooter2d

install: clean
	python setup.py install