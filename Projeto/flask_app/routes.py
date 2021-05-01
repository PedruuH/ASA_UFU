import database_utils
from flask import Blueprint, request, json, jsonify

urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/')
def index():
    return 'Backend Aplication.'

@urls_blueprint.route('/login', methods = ['GET','POST'])
def login():
    login_data = request.get_json()
    bd_data = database_utils.get_users()


    
@urls_blueprint.route('/logout', methods = ['GET','POST'])
def logout():
    

@urls_blueprint.route('/aeroportosearch', methods = ['GET'])
def get_aeroportos():
    
@urls_blueprint.route('/aeroportobyorigem', methods = ['GET'])
def get_aeroportos_por_origem():

@urls_blueprint.route('/voossearchcia', methods = ['GET'])
def pesquisa_voo_cia():


@urls_blueprint.route('/voossearch', methods = ['GET'])
def pesquisa_voo():

@urls_blueprint.route('/checkout', methods = ['POST'])
def compra()):
    
