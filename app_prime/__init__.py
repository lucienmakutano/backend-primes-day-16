from flask import Flask
from flask_restful import Resource, Api
import helpers

app = Flask(__name__)
api = Api(app)


class Primes(Resource):
    def get(self):
        return {"first 20 prime numbers": helpers.get_prime_numbers()}, 200


class Home(Resource):
    def get(self):
        return 'welcome to my website, please goto /primes to see 20 first prime number', 200


api.add_resource(Primes, '/primes')
api.add_resource(Home, '/')
