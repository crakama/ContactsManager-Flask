# from app import contactsapp
# from flask import current_app
# from app import create_app
# from app.main import main as main_blueprint
# import unittest


# class FlaskTestCase(unittest.TestCase):

# 	#Ensure that flask was set up correctly
# 	def test_login(self):
# 		tester = contactsapp.test_client(self)
# 		response = tester.get('/login', content_type="html/text")
# 		self.assertEqual(response.status_code,200)

# 	def test_correct_login(self):
# 		tester = contactsapp.test_client(self)
# 		response = tester.get('/login', 
# 			data=dict(username="username", password="password"),follow_redirects=True)

# 		self.assertEqual(b'Please login' in response.data)

# 	def test_incorrect_login(self):
# 		tester = contactsapp.test_client(self)
# 		response = tester.get('/login', 
# 			data=dict(username="wrongusername", password="wrongpassword"),follow_redirects=True)
		
# 		self.assertEqual(b'Please login' in response.data)

# 	def test_logout(self):
# 		#self.contactsapp = create_app('testing')
# 		tester = contactsapp.test_client(self)
# 		tester.post('/login', 
# 			data=dict(username="wrongusername", password="wrongpassword"),follow_redirects=True)
# 		response = tester.get('/logout', follow_redirects=True)
# 		self.assertEqual(b'Please login' in response.data)

# # if __name__ == '__main__':

# # 	unittest.main()