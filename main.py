import click
from users import Users


@click.command()
@click.option('--role', '-r', type=click.Choice(['normal', 'mod', 'admin']))
def getUsers(role):
    """get user according to role specified from Users class"""
    user = Users()
    user.main(role)


if __name__ == '__main__':
    getUsers()
