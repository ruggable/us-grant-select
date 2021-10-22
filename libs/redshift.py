import psycopg2

from dev_secrets.redshift_creds import database, username, password, host, port, schema

current_connection = None
current_client = None

# def close_connection():
# 	if current_connection:
# 		if not current_connection.closed:
# 			current_connection.commit()
# 			current_connection.close()

def create_connection(host:str, username:str, port:str, database:str, password:str, schema:str, current_connection=current_connection):
	"""
	:param host: str -> db host
	:param username: str -> db username
	:param port: str -> db port number
	:param database: str -> db name
	:param password: str -> db password
	:param schema: str -> db schema

	retries db connection if it fails

	"""
	if current_connection:
		if not current_connection.closed:
			return current_connection
	tries = 5
	while tries > 0:
		try:
			current_connection = psycopg2.connect(dbname=database, host=host, port=port, user=username, password=password)
			return current_connection
		except psycopg2.OperationalError as e:
			print("error! Retrying.", e)
			tries -= 1
	print("Sorry... that didnt work")

def handle_grant(user, table):
	try:
		con = create_connection(host, username, port, database, password, schema, current_connection=current_connection)

		schemaname = table.split('.')[0]
		with con.cursor() as cur:
			cur.execute(f"SELECT has_schema_privilege('{user}', '{schemaname}', 'USAGE');")
			if cur.fetchone():
				print(f'{user} has usage on {schemaname}...')
				cur.execute(f'GRANT SELECT ON {table} to {user};')
			else:
				return False
			con.commit()
		return True
	except Exception as e:
		print(e)
		return False