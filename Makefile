format:
	autoflake --remove-unused-variables --remove-all-unused-imports -r -i authentication core tests feed media posts users
	black authentication core tests feed media posts users

check-format:
	black --check authentication core tests feed media posts users

lint:
	python -m flake8 authentication core tests feed media posts users --ignore=E501
