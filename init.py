import auto_db

autos = [
    dict(vendor='Tesla',
         model_name='Model S',
         year_issue=2019,
         color='Red'),

    dict(vendor='Tesla',
         model_name='Model X',
         year_issue=2020,
         color='Black'),

    dict(vendor='Mercedes',
         model_name='GLE',
         year_issue=2018,
         color='Green'),
]

for i in autos:
    auto_db.create_new(i)
