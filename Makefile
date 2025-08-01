format:
	autoflake --remove-unused-variables --remove-all-unused-imports -r -i authentication core tests feed media posts users
	black authentication core tests feed media posts users

check-format:
	black --check authentication core tests feed media posts users

lint:
	python -m flake8 authentication core tests feed media posts users --ignore=E501

check-duplicate-code:
	pylint --disable=all --enable=similarities authentication core tests feed media posts users

uml:
	mkdir -p diagrams
	pyreverse -o png -p backend users/models.py posts/models.py feed/models.py -d diagrams

check-code-smells:
	pylint --disable=C0114,C0115,C0116,R0903,C0301,C0103,E1101 --ignore=migrations authentication core tests feed media posts users

check-security:
	bandit -r authentication core feed media posts users
