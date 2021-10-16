# Home-work-15

Project structure

Sport_Spyders powered by Scrapy:

   - Tennis
   - Volleyball
  
 Rest-API powered by Django  
 
   - Rest_server
  
 Database models (powered by Postgres and mapped by Django ORM for all packages - spyders and rest_api)
 
  - Sports
  
  - Article 

   To have an ability to import Django models into Scrapy, please change path in Scrapy settings.py:
   
      sys.path.insert(0, '/users/filim/goit/rest_api')] 
   
   for ABSOLUTE path to you Django project.
  
To launch spyders: 

 - cd [sport_spyder]
  - scrapy crawl [spider]
  
To launch API on your localhost:8000:

  - cd [rest_api]
   - py manage.py runserver
   
To get DOC for API:

  - UI DOC localhost:8000/doc
  - YAML DOC localhost/doc?format=.yaml
  
  Please find a copy of .yaml file in project root.
  
