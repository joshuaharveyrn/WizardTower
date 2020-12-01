import gpt_2_simple as gpt2
import os
import requests
import sys
import time
import flask
from flask import request
from flask import jsonify


model_name = "124M"

sess = gpt2.start_tf_sess()

gpt2.load_gpt2(sess, model_name=model_name)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""
conversation = ""

while True:
	input_text = input()

	conversation = conversation + input_text

	#gpt2.generate(sess, model_name=model_name)
	single_text = gpt2.generate(sess, return_as_list=True, prefix=conversation, length=50, temperature=0.7, truncate="<|endoftext|>", include_prefix=False)[0]

	print(single_text)
	time.sleep(1)
"""

@app.route('/response', methods=['POST'])
def get_gpt_response():
	conversation = request.form['conversation']
	print(conversation)
	print(str(conversation))
	single_text = gpt2.generate(sess, return_as_list=True, prefix=str(conversation), length=50, temperature=0.7, truncate="<|endoftext|>", include_prefix=False)[0]
	return jsonify(single_text)

app.run()
