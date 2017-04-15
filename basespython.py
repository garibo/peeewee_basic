import peewee
import datetime

database = peewee.MySQLDatabase('peewee_test', host='localhost', port=3306, user='root', password='')

class User(peewee.Model):
	username = peewee.CharField(unique=True)
	email = peewee.CharField(index=True)
	create_date = peewee.DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = database
		db_table = "users"

if __name__ == '__main__':

	if not User.table_exists():
		User.create_table()

	username = input("Ingrese un nombre: ")
	email = input("Ingrese un email: ")

	if not User.select().where( User.username == username).exists():
		new_user = User.create(username = username, email = email)
		new_user.save()
	else:
		print ("El usuario ya se encuentra registrado")
