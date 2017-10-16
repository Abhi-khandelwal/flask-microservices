
class  BaseConfig:
	"""Base Configuration"""
	DEBUG= False
	TESTING = False

class DevelopmentConfig(BaseConfig):
	"""Development Configuration"""
	DEBUG = True

class TestingConfig(BaseConfig):
	"""Testing Configuration"""
	DEBUG = True
	Testing = True

class ProductionConfig(BaseConfig):
	"""Production COnfiguration"""
	DEBUG = False
