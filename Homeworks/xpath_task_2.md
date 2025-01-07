Go the https://grocerymate.masterschool.com 

1. Write the XPath for the highlighted icon/button given in the image below.
![image](https://github.com/user-attachments/assets/00b6cf27-8e1a-44fc-85d6-81d150be0f44)

"//div[@class='headerIcon'][1]"

2. Now, open https://grocerymate.masterschool.com/auth.
![image](https://github.com/user-attachments/assets/33b35d1c-0b36-442b-bcdd-c09d13348598)

Write the XPath of all input fields, sign in button, Create a new account link, and Go to Home link

"//input[@placeholder='Email address']"

"//input[@placeholder='Password']"

"//button[text()='Sign In']"

"//a[text()='Create a new account']"

"//a[text()='Go to Home']"

3. Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:
![image](https://github.com/user-attachments/assets/cc63440c-0c33-4813-88d2-1cc3cee80084)

Write the XPath for all input fields, Sign Up button.

"//input[@placeholder='Full Name']"

"//input[@placeholder='Email address']"

"//input[@placeholder='Password']"

//button[text()='Sign Up']"

4. Go to https://grocerymate.masterschool.com/store, you will see the following UI:
![image](https://github.com/user-attachments/assets/8ea5742e-6ffd-46de-9bb5-c9cfffa94805)

Write the XPath of Confirm button which you can see in the Modal. 

"//button[text()='Confirm']"

5. Go to the Shop page, write the XPath for quantity input of Oranges, Add to cart button for Oranges, and add to wish list for Oranges

"//input[@class='quantity' and @name='quantity_66b3a57b3fd5048eacb4798f']"

"//div[@class='card-header']//p[contains(text(), 'Oranges')]/ancestor::div[contains(@class, 'card')]//button[contains(@class, 'btn-cart')]"

"//div[@class='card-header']//p[contains(text(), 'Oranges')]/ancestor::div[contains(@class, 'card')]//button[contains(@class, 'btn btn-outline-dark ')]"







