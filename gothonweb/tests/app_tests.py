from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_404():
	resp = app.request("/void")
	assert_response(resp, status="404")
	
def test_200():
	resp = app.request("/hello")
	assert_response(resp)
	
def test_POST_wo_input():
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")
	
def test_POST():
	data = {'name': 'YG', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains="YG")