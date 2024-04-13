# Звіт до роботи №2
## Тема: Знайомство з ООП
### Мета роботи: 
Ознайомитимь та навчитись працювати з основами роботи з ООП.

---
### Виконання роботи
1. Результати виконання завдання 1 - "Створюємо перший class":
    - Створили два python файли із назвами `lab_2.ipynb` та `lab_2.py`.
    - Скопіювали даний у завданні код у `lab_2.py`:

    ```python
    
    class MyName:
        """Опис класу / Документація
        """
        total_names = 0 #Class Variable

        def __init__(self, name=None) -> None:
            self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
            MyName.total_names += 1 #modify class variable
            self.my_id = self.total_names

        @property
        def whoami(self): 
            """Class property
            return: повертаємо імя 
            """
            return f"My name is {self.name}"
        
        @property
        def my_email(self) -> str:
            """Class property
            return: повертаємо емейл
            """
            return self.create_email()
        
        def create_email(self) -> str:
            """Instance method
            """
            return f"{self.name}@itcollege.lviv.ua"

        @classmethod
        def anonymous_user(cls):
            """Classs method
            """
            return cls("Anonymous")
        
        @staticmethod
        def say_hello(message="Hello to everyone!"):
            """Static method
            """
            return f"You say: {message}"


    print("Let's Start!")

    names = ("Bohdan", "Marta", None)
    all_names = {name: MyName(name) for name in names}

    for name, me in all_names.items():
        print(f"""{">*<"*20}
    This is object: {me} 
    This is object attribute: {me.name} / {me.my_id}
    This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
    This is {type(me.create_email)} call: {me.create_email()}
    This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
    This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
    {"<*>"*20}""")

    print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
    ```

    - Ця програма створена для автоматичного введення імен в систему та для генерування їхніх емейл-адрес. Ось результат:

    ```
    Let's Start!
    >*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <__main__.MyName object at 0x0000025BB54D08C0> 
    This is object attribute: Bohdan / 1
    This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua     
    This is <class 'method'> call: Bohdan@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone! 
    This is class variable <class 'int'>: from class 4 / from object 4
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
    >*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <__main__.MyName object at 0x0000025BB54D08F0> 
    This is object attribute: Marta / 2
    This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
    This is <class 'method'> call: Marta@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone!
    This is class variable <class 'int'>: from class 4 / from object 4
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
    >*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
    This is object: <__main__.MyName object at 0x0000025BB54D0920>
    This is object attribute: Anonymous / 4
    This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
    This is <class 'method'> call: Anonymous@itcollege.lviv.ua
    This is static <class 'function'> with defaults: You say: Hello to everyone!
    This is class variable <class 'int'>: from class 4 / from object 4
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
    We are done. We create 4 names! ??? Why 4?
    ```

    - Виконали приклади які розглядали на лекції, вставивши їх у `lab_2.ipynb` та протестувавши:

    ![ipynb](images/ipynb.png "ipynb")




    

    - Встановили бібліотеку requests за допомогою команди `pip install requests`:

    ![pip_install_requests](images/pip_install_requests.png "pip_install_requests")

    - Імпортували та протестували її за допомогою команд:

    ```python
    >>> import requests
    >>> r = requests.get('https://google.com')
    >>> r.status_code
    ```

    ![import_requests](images/import_requests.png "import_requests")

    - Зробили її загальнодоступною для цілої системи за допомогою наступних команд:

    ```python
    pip show requests
    pip install requests==2.1
    pip show requests
    pip uninstall requests
    ```
    
    ![requests21](images/requests21.png "requests21")  

1. Результати виконання завдання 2 - "Робота у віртуальному середовищі":
    - Створили `VENV` та активували його за допомогою команд:
    
    ```python
    python -m venv ./my_env
    source my_env/Scripts/activate
    pip install requests
    deactivate
    pip show requests
    ```

    - Після нашого запиту команда вивела на екран інформацію про бібліотеку `requests`:

    ![venv_requests](images/venv_requests.png "venv_requests")

1. Результати виконання завдання 3 - "Робота з Pipenv":
    - Завантажили `pipenv` та вивели всі можливості його використання за допомогою `--help`:

    ```
    Usage: pipenv [OPTIONS] COMMAND [ARGS]...

    Options:
    --where                         Output project home information.
    --venv                          Output virtualenv information.
    --py                            Output Python interpreter information.
    --envs                          Output Environment Variable options.
    --rm                            Remove the virtualenv.
    --bare                          Minimal output.
    --man                           Display manpage.
    --support                       Output diagnostic information for use in
                                    GitHub issues.
    --site-packages / --no-site-packages
                                    Enable site-packages for the virtualenv.
                                    [env var: PIPENV_SITE_PACKAGES]
    --python TEXT                   Specify which version of Python virtualenv
                                    should use.
    --clear                         Clears caches (pipenv, pip).  [env var:
                                    PIPENV_CLEAR]
    -q, --quiet                     Quiet mode.
    -v, --verbose                   Verbose mode.
    --pypi-mirror TEXT              Specify a PyPI mirror.
    --version                       Show the version and exit.
    -h, --help                      Show this message and exit.


    Usage Examples:
    Create a new project using Python 3.7, specifically:
    $ pipenv --python 3.7

    Remove project virtualenv (inferred from current directory):
    $ pipenv --rm

    Install all dependencies for a project (including dev):
    $ pipenv install --dev

    Create a lockfile containing pre-releases:
    $ pipenv lock --pre

    Show a graph of your installed dependencies:
    $ pipenv graph

    Check your installed dependencies for security vulnerabilities:
    $ pipenv check

    Install a local setup.py into your virtual environment/Pipfile:
    $ pipenv install -e .

    Use a lower-level pip command:
    $ pipenv run pip freeze

    Commands:
    check         Checks for PyUp Safety security vulnerabilities and against
                    PEP 508 markers provided in Pipfile.
    clean         Uninstalls all packages not specified in Pipfile.lock.
    graph         Displays currently-installed dependency graph information.
    install       Installs provided packages and adds them to Pipfile, or (if no
                    packages are given), installs all packages from Pipfile.
    lock          Generates Pipfile.lock.
    open          View a given module in your editor.
    requirements  Generate a requirements.txt from Pipfile.lock.
    run           Spawns a command installed into the virtualenv.
    scripts       Lists scripts in current environment config.
    shell         Spawns a shell within the virtualenv.
    sync          Installs all packages specified in Pipfile.lock.
    uninstall     Uninstalls a provided package and removes it from Pipfile.
    update        Runs lock, then sync.
    upgrade       Resolves provided packages and adds them to Pipfile, or (if no
                    packages are given), merges results to Pipfile.lock
    verify        Verify the hash in Pipfile.lock is up-to-date.
    ```

    - Створили нове середовище та інсталювали бібліотеку `requests` у ньому, а також переконались що наприкінці установки були створені файли `Pipfile` та `Pipfile.lock`. `Pipfile` та `Pipfile lock` - це два файли, які використовуються для керування залежностями Python за допомогою інструменту pip.

    - `Pipfile` містить декларацію залежностей власного проєкту. 
    `Pipfile.lock` - це файл, який генерується `pip` на основі `Pipfile`. Він містить список усіх пакетів, які були встановлені у нашому середовищі Python, а також їх версії та хеш-суми.

    - Створили пайтон файл під назвою `test.py` та записали в нього задану програму. Запустили його у Visual Studio Code:

    ![pyprogramm_vs](images/pyprogramm_vs.png "pyprogramm_vs")

    Запустили його у командній строці:

    ![pyprogramm_cmd](images/pyprogramm_cmd.png "pyprogramm_cmd")

    Запустили його у `pipenv shell`:

    ![pyprogramm_pipenv](images/pyprogramm_pipenv.png "pyprogramm_pipenv")

    - За нашим вибором встановимо бібліотеку `pandas` із списку бібліотек Pypi. Встановили бібліотеку за допомогою: `pip install pandas`.
    - Ознайомившись із її документацією затестимо її:

    ![pandas](images/pandas.png "pandas")    

    Ця команда створює DataFrame з двома стовпцями: Name та Age, а потім друкує його текстове представлення.

    - Змінили інтерпретатор Python віртуальний:

    ![interpretator](images/interpretator.png "interpretator")

    Запустили за допомогою нього програму:

    ![script](images/script.png "script")

1. Результати виконання завдання 4 - "Робота зі змінними середовища":
    - Створивши файл `.env` використаємо код для створення змінної в ньому;

    ![environ](images/environ.png "environ")

    - Використаємо .env змінну без активації віртуального середовища:

    ![without_env](images/without_env.png "withot_env")

1. Результати виконання завдання 5 - "Допомога ChatGPT":
    - ChatGPT надав мені наступний код для створення сайту:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Привіт світ, вітаю на моєму сайті.'

    if __name__ == '__main__':
        app.run(debug=True)

    ```
    - Сайт є доступним та виглядає наступним чином:

    ![GPT_website](images/GPT_website.png "GPT_website")


### Висновок: 
Я ознайомився із основами віртуальних середовищ та навчився працювати із ними.

---