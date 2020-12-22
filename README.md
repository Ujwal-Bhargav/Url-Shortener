# Url_Shortener
Url shortner using Flask web framework in python

1. Install flask:

	    pip install flask
2. For using global variables:

	    pip install python-dotenv(to use flask_env file)
3. For storing data:

      	    pip install sqlalchemy

Instructions:

1. Create a virtual environment(Preferably python3.6 and above) 
2. Install packages specified in requirements.txt
3. Create database


     a) Install sqlite2 with the following command: 
     
     	   sudo apt install sqlite3
     
     
     b)from terminal at folder location open python run the following commands to create a table:
     
     	    from urlshortener import create_app
            from urlshortener.extensions import db
	    from urlshortener.models import Link
            db.create_all(app=create_app)
            exit()
	   
	   
     c)if created you will see db.sqlite3 file created.
     
     
     d)To verify table is created or not(from terminal at the folder location)
           
	   > sqlite3 urlshortener/db.sqlite3
 	
	d1)this open sqlite3, to see tables created give following command.
        
	    sqlite3> .tables
         
	d2)shows tables created
        
		link

