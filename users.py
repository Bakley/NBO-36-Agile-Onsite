import datetime
import json
import click

comments = []


class Users():
	"""users class"""
	@staticmethod
	def main(role):
		"""main app initialisation"""
		if role == "normal":
			click.echo("Hello normal! Logged in at {}".format(datetime.datetime.now()))
			option = int(input("Enter 1 for adding comment and 2 for editing"))
			if option == 1:
				"option 1 clicked. call comment implementation here"
				post_comment(role)
			if option == 2:
				"option 2 clicked. call edit implementation here"
				edit_comment(role)
		elif role == "mod":
			click.echo("Hello mod! Logged in at {}".format(datetime.datetime.now()))
			option = int(input("Enter 1 for comment and 2 for edit and 3 for delete"))
			if option == 1:
				"option 1 clicked. call comment implementation here"
			if option == 2:
				"option 2 clicked. call edit implementation here"
			if option == 3:
				"option 3 clicked. call delete implementation here"
		elif role == "admin":
			click.echo("Hello admin! Logged in at {}".format(datetime.datetime.now()))
			option = int(input("Enter 1 for comment and 2 for edit any and 3 for delete"))
			if option == 1:
				"option 1 clicked. call comment implementation here"
			if option == 2:
				"option 2 clicked. call edit any implementation here"
			if option == 3:
				"option 3 clicked. call delete implementation here"

def post_comment(role):
	'''A user can post a comment'''
	user_comment = str(input("Add a new comment: "))
	secret_key = str(input("Enter a secret key to identify your comment: "))

	if comments is not None:
		for comment in comments:
			if comment["secret_key"] == secret_key:
				secret_key = str(input("secret key already in use, enter a different key: "))

	comment_data = {
	"comment_posted": user_comment,
	"author": role,
	"time_posted": datetime.datetime.now(),
	"comment_id": len(comments)+1,
	"secret_key": secret_key
	}

	comments.append(comment_data)

	click.echo(comments)
	from main import getUsers
	getUsers()

def edit_comment(role):
	'''A user can edit an existing comment'''

	secret_key = str(input("Enter a secret key: "))

	if comments is not None:
		for comment in comments:
			if comment["secret_key"] == secret_key:

				old_comment = comment["comment_posted"]

				click.echo(old_comment)

				new_comment = str(input("Input changes: "))


				new_comment_data = {
						"comment_posted": new_comment,
						"author": role,
						"time_posted": datetime.datetime.now(),
						"comment_id": len(comments)+1,
						"secret_key": secret_key
				}

				#comments.remove(old_comment)
				comments.append(new_comment_data)
				click.echo("Edited comment {}".format(comments))
			click.echo("Error: no comment for that key")
	click.echo("No comments in database")

