


# Spam-HAM Filtering

It uses machine learning models to predict whether the text is spam or ligitimate.
if legitimate then ham

it is just practise of a prediction using nlp and machine learning 

# create the virtual env and activate it 

you can follow this link for setup of venv according to your device

https://realpython.com/python-virtual-environments-a-primer/

## if you are using virtualenv then,
	
	 python3 -m venv <virtual env name>
	
	 activate  <virtual env name>

## If you are using conda enviroment then,

	 conda create --name <virtual env name> python=3.7

	 conda activate <virtual env name>	

# Then after activating, run following command for dependencies of app


	 pip install nltk pandas numpy 

	 python -m nltk.downloader stopwords

	 python -m nltk.downloader puntk


after completion of setup run 
		
		python app.py



