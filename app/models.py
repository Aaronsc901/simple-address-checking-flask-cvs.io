from werkzeug.utils import secure_filename
import requests
import pandas as pd
import os 

class Post():
	def one(self):
		#Carga de Archivos
		filename = secure_filename(self.filename)
		self.save(os.path.join('media',filename))
		fullfile = os.path.join('media',filename)
		#Lectura del CSV
		csv = pd.read_csv(os.path.join('media/', filename))
		#Carga de los datos (nombres)
		pg = csv['nombres'].values 
		#Diccionarios con los datos
		d1 = dict()
		d2 = dict()
		#Variables de for
		num = 0
		URL = ""
		
		for x in pg:
			#Tomando los nombres, o en su defecto las urls
			d1[int(num)] = str(x)
			num = num + 1
			#Consultas con requests
			try:
				URL = str(x)
				req = requests.get(URL, timeout = 0.9)
				status_code = req.status_code
				if status_code == 200:
					d2[int(num)] = str(status_code)
				else: 
					d2[int(num)] = str(status_code)	

			except requests.exceptions.ConnectionError: 
				d2[int(num)] = "Error de conexion."

			except requests.exceptions.Timeout: 
				d2[int(num)] = "Tiempo de espera excedido."	

		return d1, d2			
