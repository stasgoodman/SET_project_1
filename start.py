import typer
from tasks.runtests import *

app = typer.Typer(add_completion=False)


@app.command()
def catapi_tests():
    """
    Zdarova
    """
    run_catapi_tests()
    run_2_catapi_tests()
    run_3_catapi_tests()


if __name__ == '__main__':
    app()
