# Sistema de login com CustomTkinter

Um aplicativo de login utilizando Python, CustomTkinter e Sqlite.

## Descrição

Este projeto é um sistema de login com as seguintes funcionalidades:
- **Registra um usuário com senha criptografada em um banco de dados SQLite**
- **Possibilita realizar o seu login com as credenciais cadastradas**
- **Faz a verificação de credenciais no banco de dados**
- **Permite salvar usuário e senha através do botão "Lembrar de mim"**

## Requisitos

- Python 3.7 ou superior

## Instalação

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/cadumrod/login_system_GUI
    cd login_system_GUI
    ```

2. **Crie e ative um ambiente virtual:**

    No Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    No macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Construa o executável com `cx_Freeze`**:

    ```bash
    python setup.py build
    ```

## Uso

1. Após a construção, o executável estará disponível no diretório `build`. Para executar o aplicativo, navegue até o diretório de saída (por exemplo, `build/exe.win-amd64-3.12` no Windows) e execute o arquivo gerado:

    No Windows:
    ```bash
    cd build/exe.win-amd64-3.12
    app.exe
    ```

    No macOS/Linux:
    ```bash
    cd build/exe.macosx-10.6-intel-3.12
    ./app
    ```


## Estrutura do Projeto

- `app.py`: Arquivo principal do aplicativo.
- `setup.py`: Script de instalação e configuração do projeto.
- `db.py`: Script do banco de dados que se encontra dentro da pasta "database" deste repositório.
- `python.ico`: Ícone utilizado para o app que se encontra dentro da pasta "assets/icons/" deste repositório.
- `app.exe`: Executável que se encontra dentro da pasta "Sistema de login" deste repositório.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de requisitos com as dependências do projeto.
- `LICENSE`: Licença MIT.


## Autor

**Carlos Rodrigues**

- [GitHub](https://github.com/cadumrod)
- [E-mail](mailto:carlosrod.dev@gmail.com)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.