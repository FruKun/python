#Напишите декоратор retry: 

#декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции. 
#При сбое декоратор должен подождать и повторить попытку выполнения функции. 
#При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой. 
#Если у декоратора заканчиваются попытки, он сдается и возвращает исключение