install:
	@pip install requests pycurl mock coveralls pylint pycodestyle

tests:
	@python -m unittest discover -s test -p '*Test.py'

coverage:
	@coverage run -m unittest discover -s test -p '*Test.py'
