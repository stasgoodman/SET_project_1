import typer
from tasks.runtests import *

app = typer.Typer(add_completion=False)


@app.command()
def catapi_tests():
    """
    Zdarova
    """
    run_catapi_tests()


@app.command()
def blabla():
    pass


if __name__ == '__main__':
    app()
