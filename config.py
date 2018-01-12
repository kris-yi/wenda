import json


def config(app, phone):
    if app == '芝士超人':
        if phone == 'iphone8':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 153,
                'pixels_right': 750,
                'pixels_bottom': 350
            }
    elif app == '冲顶大会':
        if phone == 'iphone8':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 240,
                'pixels_right': 750,
                'pixels_bottom': 525
            }
        elif phone == 'iphone6':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 203,
                'pixels_right': 639,
                'pixels_bottom': 445
            }
        elif phone == 'iphone7p':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 343,
                'pixels_right': 1080,
                'pixels_bottom': 756
            }
    elif app == '百万英雄':
        if phone == 'iphone8':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 163,
                'pixels_right': 750,
                'pixels_bottom': 420
            }
        elif phone == '华为mate9':
            data = {
                'phone_system': 'android',
                'pixels_left': 0,
                'pixels_top': 250,
                'pixels_right': 1080,
                'pixels_bottom': 600
            }
    elif app == '百万赢家':
        if phone == 'iphone8':
            data = {
                'phone_system': 'ios',
                'pixels_left': 0,
                'pixels_top': 160,
                'pixels_right': 750,
                'pixels_bottom': 405
            }
    return json.dumps(data)
