import datetime

import click


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
			if option == 2:
				"option 2 clicked. call edit implementation here"
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
