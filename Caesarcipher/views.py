from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .cipher import CaesarCipher
import json


def caesar_cipher_page(request):
    data = dict()
    data['rotations'] = range(26)
    return render(request, 'caesar_cipher/index.html', data)


@require_POST
def encrypt_text(request):

    incoming_json = request.body.decode('utf-8')
    json_dict = json.loads(incoming_json)
    text = CaesarCipher(json_dict['text_for_encrypt'])
    data = dict()
    data['ciphered_text'] = text.caesar_main(int(json_dict['rotation']))
    data['count_let'] = [i for i in text.count()]
    data['count_f'] = [text.count()[i] for i in text.count()]
    print(data['count_f'])
    print(data['count_let'])
    return JsonResponse(data)


@require_POST
def decrypt_text(request):
    incoming_json = request.body.decode('utf-8')
    json_dict = json.loads(incoming_json)
    text = CaesarCipher(json_dict['text_for_decrypt'])
    data = dict()
    data['ciphered_text'] = text.caesar_main(int(json_dict['rotation']), False)
    data['count_let'] = [i for i in text.count()]
    data['count_f'] = [text.count()[i] for i in text.count()]
    return JsonResponse(data)


@require_POST
def bruted(request):
    incoming_json = request.body.decode('utf-8')
    json_dict = json.loads(incoming_json)
    text = CaesarCipher(json_dict['brute_text'])
    data = dict()
    data['bruted'] = ['\n'+' Rotation is ' + str(i) + ' : '+text.brute_force()[i] for i in text.brute_force()]
    data['count_let'] = [i for i in text.count()]
    data['count_f'] = [text.count()[i] for i in text.count()]
    print(data['bruted'])
    return JsonResponse(data)


@require_POST
def detect_rot(request):
    incoming_json = request.body.decode('utf-8')
    json_dict = json.loads(incoming_json)
    text = CaesarCipher(json_dict['detected_num'])
    data = dict()
    data['detect_num'] = text.try_detect_rotation()
    return JsonResponse(data)
