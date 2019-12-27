# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

default_btn = ['A', 'B']

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
                'buttons' : default_btn
	})

@csrf_exempt
def message(request):
	json_str = ((request.body).decode('utf-8'))
	received_json = json.loads(json_str)
	content_name = received_json['content']
	type_name = received_json['type']
	user_name = received_json['user_key']
	
	if content_name == 'A':
		return JsonResponse({
			'message':{
				'text': "A Selected" # Anything you want
			},
                        'keyboard':{
                                'type':'buttons',
                                'buttons':default_btn
                        }
		})
	elif content_name == 'B':
                return JsonResponse({
			'message':{
				'text': "B Selected" #Anything you want
			},
                        'keyboard':{
                                'type':'buttons',
                                'buttons':default_btn
                        }
		})
