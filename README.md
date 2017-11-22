# Simple server http in python3

### Instaçação

- Clone o repositorio [git](https://git-scm.com/download/linux)
- instale o  python>=3.5 e o [Pip](https://pypi.python.org/pypi/pip)
- instale [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- dentro da pasta simplePythonWebServer crie um virtualenv com os seguintes comandos 
    ```
    $ virtualenv env -p python3
    ```
- Caso use windows 
    ```
    $ env\Script\activate
    ```
- Caso use linux
    ```
    $ source env/bin/activate
    ```
- e instale as dependências
    ```
    $ pip install -r requeriments.txt
    ```
 - rode o servidor
    ```
    $ python run.py
    ```
- e [clique aqui!](http://127.0.0.1:8080)

## Opções
#### Mudar de Banco:
Por padrão o banco escolhido é o sqlite3, por ser um projeto pequeno, mas caso queira mudar, altere o arquivo app/settings/__init__.py
    
    DATA_BASE = 'mysql+pymysql://user:pass@host/database'
    

#### Mudar de IP e Porta:
Ao chamar o servidor passe a ip e a porta que queira

    $ python run.py 192.168.1.10:8000
    
