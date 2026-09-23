from main_module.fuctions.basic import aboutinfo,notfound,add,sub,div,multiplication,power,person

from main_module.fuctions.aifuctionality import city_weather,news_genrator,interview_question_genrator,impromtu_topic_genrator,quiz_genrator,qr_genrator

#from main_module.email_genrator.email_gen import send_an_email
functionallty={
    "who develops you":aboutinfo,
    "city weather":city_weather,
    "add two number":add,
    "subtract two number":sub,
    "division two number":div,
    "multiplication of two number":multiplication,
    "power of number":power,
    "Who is komal":person,
    "genrate news":news_genrator,
    "Genrate interview questions":interview_question_genrator,
    "impromtu topic genrator":impromtu_topic_genrator,
    "quiz genrator":quiz_genrator,
    "qr genrator":qr_genrator,
   # "genrate email":send_an_email,
    "not found": notfound
}