# Password Pandemonium
challeng discription:
>You're looking to book a flight to Florida with the totally-legit new budget airline, Oceanic Airlines! All you need to do is create an account! Should be pretty easy, right?
...right?
>https://pandemonium.web.2020.sunshinectf.org
>Author: Jeffrey D.
>

![](https://github.com/majidgourkani/ctf-writeup/blob/master/WEB/2020/sunshineCTF/12.PNG)

for choosing password of account we got some password policies as mentioned in below and we pass them:
1) Error! Password is too short.(123)
2) Error! Password must include more than two special characters.(qaz!!!)
3) Error! Password must include a prime amount of numbers.(qaz!!!11)
4) Error! Password must include an emoji.(qaz!!!11☺)
5) Error! Password's MD5 hash must start with a number.
6) Error! Password is too long.
7) Error! Password must have equal amount of uppercase and lowercase characters.

in this step my password was something like this:  `MEST@@@test11☺`


the last condithion was:


>**Error! Password must be valid JavaScript that evaluates to True.**


so i must choose a password that pass a true statment in JavaScript (something like 1=1), so after a while i found this
and got the flag:


password: `'☺1tM'!=!'Mt1☺'`


here is flag: `sun{Pal1ndr0m1c_EcMaScRiPt}`
![](https://github.com/majidgourkani/ctf-writeup/blob/master/WEB/2020/sunshineCTF/13.PNG)
