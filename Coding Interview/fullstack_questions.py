'''
1) Write a function to categorize a given temperature in Fahrenheit and return one of 
the strings: "Freezing", "Cold", "Mild", "Hot", "Scorching".
'''
def check_temp(temp):
    if type(temp) is int or type(temp) is float:
        if temp > 150:
            print("scorching")
        elif temp > 85:
            print("hot")
        elif temp > 65:
            print("mild")
        elif temp >= 34:
            print ("cold")
        elif temp < 34:
            print ("freezing")
    else:
        print ("Temp must be an integer")

check_temp(94.34)


'''
2) The value of the variable input is a string 1,2,3,4,5,6,7. 
How would you get the sum of the integers contained inside input?
'''

txt = "1,2,3,4,5,6,7"
def sum_text(txt):
    if txt.replace(",","").isdigit():
        txt = list(txt.split(","))
        answer = list(map(int,txt))
        print(sum(answer))
    else:
        print("text is not numeric, may contain an invalid character")
sum_text(txt)


'''
3) Write a small PHP Script that will POST an email address to itself and record the 
email address to a file.
'''

<?php
$to_email = 'email@gmail.com';
$subject = "Testing emails";
$message = "This mail is sent using php mail";
$headers = "From: test@gmail.com";
mail($to_email,$subject,$message,$headers);

file_put_contents('email.txt', $to_email);
?>

'''
4) What is wrong with the SQL query below?

SELECT UserId, AVG(Total) AS AvgOrderTotal
FROM Invoices
HAVING COUNT(OrderId) >= 1
'''

4. WHERE is used for row data not aggregated data(pre filter), HAVING needs to be used with aggregated data 
(post filter). WHERE can not be used with COUNT, have to use HAVING. 
HAVING is same as the WHERE clause but is applied on grouped records.
This is Missing the GROUP BY before HAVING
"""
SELECT UserId, AVG(Total) AS AvgOrderTotal
FROM Invoices
GROUP BY UserId
HAVING COUNT(OrderId) >= 1
"""
