import pytest
from api_interview.app import create_app


@pytest.fixture(scope="module")
def app():
	"""Intance of Main Flask app API"""
	return create_app()
