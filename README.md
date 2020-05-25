FlaskSeguro
==========
Exemplo do python-pagseguro utilizando Flask.

Integrantes Grupo
==========
- Anderson Taborga - RA:1801922
- Anna Veloso - RA: 1801230
- Gabriel Bezerra - RA:1801171
- Hellen Barbosa - RA: 1801219
- Jefferson Ximenes - RA: 1801158
- João Nunes - RA: 1801142

Instalação
==========

```bash
virtualenv env
source env/bin/activate
git clone https://github.com/rochacbruno/python-pagseguro.git
cd python-pagseguro/examples/flask/
pip install -r requirements.txt
./run.py
```

Configuração
==========
Altere o settings.cfg, ele possui as seguintes configurações por padrão:
```
EXTRA_AMOUNT = 12.12
REDIRECT_URL = "http://meusite.com/obrigado"
NOTIFICATION_URL = "http://meusite.com/notification"
EMAIL = "seuemail@dominio.com"
TOKEN = "ABCDEFGHIJKLMNO"
SECRET_KEY = "s3cr3t"
```


Testes
==========

```bash
./tests.py
```

Telas
==========
![](https://raw.githubusercontent.com/shyba/python-pagseguro/master/examples/flask/screenshots/screen1.png)
![](https://raw.githubusercontent.com/shyba/python-pagseguro/master/examples/flask/screenshots/screen2.png)
![](https://raw.githubusercontent.com/shyba/python-pagseguro/master/examples/flask/screenshots/screen3.png)
