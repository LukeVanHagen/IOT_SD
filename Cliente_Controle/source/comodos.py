class SalaEstar():
    _name = 'Sala de Estar'
    _image = 'images/sala_estar.jpeg'

    components = [
        {'pin': 0, 'status': 0, 'description': 'Lâmpada'}
    ]

class Cozinha():
    _name = 'Cozinha'
    _image = 'images/kitchen.jpg'

    components = [
        {'pin': 2, 'status': 0, 'description': 'Lâmpada'}
    ]

class Copa():
    _name = 'Copa'
    _image = 'images/copa.jpeg'

    components = [
        {'pin': 1, 'status': 0, 'description': 'Lâmpada'}
    ]

class Quarto():
    _name = 'Quarto'
    _image = 'images/quarto.jpg'

    components = [
        {'pin': 3, 'status': 0, 'description': 'Lâmpada'}
    ]

class Casa():
    _name = 'Casa'
    _image = 'images/house.jpeg'

    components = [
        {'pin': 'alarme', 'status': 0, 'description': 'Alarme'},
        {'pin': 'modo_automatico', 'status': 0, 'description': 'Modo Automático'}
    ]


# sala L0
# copa L1
# cozinha L2
# quarto L3
