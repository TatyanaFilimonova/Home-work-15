# Home-work-15

Project structure

Sport_Spyders powered by Scrapy:

   - Tennis (https://www.wtatennis.com/news/)
   - Volleyball (https://en.volleyballworld.com/volleyball/competitions/vnl-2021/news/)
  
 Rest-API powered by Django + Django rest_framework + drf_yasg documentation
 
   - Rest_server
  
 Database models (powered by Postgres and mapped by Django ORM for all the packages - spyders and rest_api)
 
  - Sports
  
  - Article 

   To have an ability to import Django models into Scrapy, please change path in Scrapy settings.py  for ABSOLUTE path to you Django project:
   
      sys.path.insert(0,'/users/filim/goit/hw15/rest_api') 
   
    
To launch spyders: 

  - cd [sport_spyder]
  - scrapy crawl [spider]
  
To launch API on your localhost:8000:

  - cd [rest_api]
  - py manage.py runserver
   
To get DOC for API:

  - For UI DOC browse: localhost:8000/doc
  - For YAML DOC browse: localhost/doc?format=.yaml
  
  Please find a copy of .yaml file in project root.
  
Have a fun! (I had a lot of...)
