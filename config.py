import os
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or b'6\xe9\xda\xead\x81\xf7\x8d\xbbH\x87\xe8m\xdd3%'

	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'task.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False