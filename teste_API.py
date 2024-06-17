import unittest
import requests

class TestAPI(unittest.TestCase):

   def test_get_request(self):
        response = requests.get('https://api-trainersquad.onrender.com/api/personal/2')
        
        if response.status_code == 404:
            self.assertEqual(response.status_code, 404)
            self.assertIn('Nome não encontrado', response.json().get('message', ''))
            print("Nada encontrado")
            return
            
        self.assertEqual(response.status_code, 200)

        data = response.json()
        print(data)
        self.assertIn('nome', data)
        self.assertIn('senha', data)
        self.assertEqual(data['id'], 2)


if __name__ == '__main__':
    unittest.main()
