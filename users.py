import click

comment = [
    {
    "author": "Normal",
    "comment": "ifhgi"
},
{
    "author": "mod",
    "comment": "ifhgi"
},
{
    "author": "Normal",
    "comment": "ifhgi"
},
{
    "author": "Normal",
    "comment": "ifhgi"
}]


class Users():

    def main(self, role, id):
            self.mod_delete_a_comment(role, id)

    def mod_delete_a_comment(self, role, id):
        """Moderator can delete a comment"""
        global comment
        if role == "normal":
            click.echo("Normal user cannot delete an app")
        elif role == "mod":
            try:
                comment_value = [
                    new_comm for new_comm in comment if comment[0]['id'] == "id"]
                click.echo(comment_value)
                # del 
                comment.remove(comment_value)
                click.echo("Comment deleted")
            except Exception as e:
                print(e)

        elif role == "admin":
            click.echo("Hello admin!")
