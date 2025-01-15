
### Scenario 1: Product Rating 5 stars 

Verify that a user can submit a rating exactly at the boundary of 5 stars

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e' |        |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 5 stars | The 5 stars are highlighted and the rating is accepted  | OK | | 
| 11b  | Click on send | The rating is displayed on the screen | OK | 
| 12   | Refresh product page	 | 5-star rating is displayed for product | OK | 

### Scenario 2: Product Rating 3 stars 

Submit a rating of 3 stars as a valid mid-point rating

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    |  put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'  |                        |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 3 stars | The 3 stars are highlighted and the rating is accepted  | OK | | 
| 11b  | Click on send | The rating is displayed on the screen | OK | |
| 12   | Refresh product page	 | 3-star rating is displayed for product | OK | 

### Scenario 3: Verify behavior when rating is submitted without feedback

As a user I hope to be able to rate the product without adding comments. 

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    |  put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                          |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 1 stars | The 1 stars are highlighted and the rating is accepted  | OK | | 
| 11b  | No comment |  | OK | | 
| 11c  | Click on send | The rating is displayed on the screen without comments| OK | |
| 12   | Refresh product page	 | 1-star rating is displayed for product without comments | OK | 

### Scenario 4: Verify behavior when feedback contains prohibited language.

As a user I expect to comment offensive words.
error: Comments do not appear but if I edit and retype them they do appear. 

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |               |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 1 stars | The 1 stars are highlighted and the rating is accepted  | OK | | 
| 11b  | comment: It's bullshit |  | OK | | 
| 11c  | Click on send | The rating is displayed on the screen without comments| OK | |
| 12   | Refresh product page	 | 1-star rating is displayed for product without comments | OK | 

### Scenario 5: Verify that a user can edit an existing rating and/or comment.

As a user when I add comments and ratings I expect to be able to edit them. 

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'  |                          |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 5 stars | The 5 stars are highlighted, and the rating is accepted | OK | | 
| 11b  | Add a comment: "Great product" | The comment is accepted and displayed | OK | | 
| 11c  | Click on send | The rating is displayed on the screen with comments| OK | |
| 12   | Edit the rating to 4 stars	 | The system updates the rating to 4 stars| OK | 
| 13  | Edit the comment: "Good product"	 | The system updates the comment to the new text	| OK | |
| 14  | Refresh product page	 | The updated rating 4 stars and comment ("Good product") are displayed	| OK | |

### Scenario 6: Verify that a user can delete an existing rating and/or comment

Select the delete option for a specific product’s rating/comment.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                                               |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Add a product with Add to cart | The product will be added to your cart | OK |            |              |
| 6    | Go to shopping cart | Fill in the data | OK | https://grocerymate.masterschool.com/checkout | |
| 7a   | Add the address  |    | OK | | 
| 7b   | Add payment details |  | OK   |  |  
| 7c   |  Click on Buy now | You are directed to Homepage | OK |  |  
| 8    | Go to shop        |    You are directed to store |   OK     |    https://grocerymate.masterschool.com/store |             |
| 10   | Select the purchased product  | The selected product appears | OK | https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f | 
| 11a  | Rate the product with 1-star | The 1-star are highlighted and the rating is accepted  | OK | | 
| 11b  | Comment: It was in poor condition; I won’t be buying here again |  The comment is accepted and displayed	| OK | | 
| 11c  | Click on send | The rating is displayed on the screen with comments| OK | |
| 12   | Refresh product page	 | The 1-star rating and comment are displayed for the product	 | OK | 
| 13a  | Click on the three dots review | Click on delete | OK  | |
| 13b  | Select the delete option	 | Edit rating and comments | OK | |
| 13c  | Save changes | The rating and comment are successfully deleted	 | OK | |
| 14 | Refresh product page	 | No rating or comment is displayed for the product		 | OK | |


### Scenario 7: Verify access for users exactly at the minimum age of 18

Verify access to alcoholic products for users with Age = 18

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                       |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Fill the pop-up with "30/04/2006" and click on Confirm | Message appears: "You are of age. You can now view all products, even alcohol products." | OK | 

### Scenario 8: Verify access denial for users under 18

Verify access denial for users with Age = 17

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                                        |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Fill the pop-up with "30/04/2007" and click on Confirm | You are underage. You can still browse the site, but you will not be able to view alcohol products.| OK | 

### Scenario 9: Allow access for users over 18

Allow access to alcoholic products for users with Age = 19

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                              |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Fill the pop-up with "30/04/2004" and click on Confirm |  You are of age. You can now view all products, even alcohol products. | OK | 


### Scenario 10: Verify behavior when age input is left empty

As a user I check the behavior when the age field is left empty

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'     |                             |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Fill the pop-up with age field empty " " and click on Confirm  | You are underage. You can still browse the site, but you will not be able to view alcohol products.| OK | 


### Scenario 11: Verify behavior with invalid age format

As a user I check the behavior when an invalid age format is entered

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                                    |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Enter "3,12,2002" in the age field	and click on confirm | You are underage. You can still browse the site, but you will not be able to view alcohol products.| OK | 

### Scenario 12: Verify free shipping eligibility for orders at the minimum threshold

As a user when I make purchases equal to 20 euros or more I expect free shipping. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                                       |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart		| OK | https://grocerymate.masterschool.com/checkout#!
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order			| OK | 
| 7    | Ensure the total order is 20€		 | Free shipment if your purchase is 20€ or more.	| OK | 
| 8    | Proceed to checkout	| Shipping fee is shown along with the total amount		| OK |


### Scenario 13: Verify free shipping eligibility for orders at the minimum threshold

As a user I hope that when making purchases with a totoal of 19,99 euros the free shipping will not be applied. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                                 |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart		| OK | 
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order			| OK | https://grocerymate.masterschool.com/checkout#!
| 7    | Ensure the total order is 19,99€	| Shipping fee is added as the total is below the free shipping threshold	| OK |
| 8    | Proceed to checkout	| Shipping fee is shown along with the total amount		| OK |

### Scenario 14: Verify shipping charges for orders well below the threshold

As a user when I have a total of 10 euros in my cart I expect that I will not receive free shipping. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                               |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart		| OK | 
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order			| OK | https://grocerymate.masterschool.com/checkout#!
| 7    | Ensure the total order is 10€	| Shipping fee is added as the total is below the free shipping threshold	| OK |
| 8    | Proceed to checkout	| Shipping fee is shown, and the total order is updated to 15€	| OK |

### Scenario 15: Notify user about eligibility for free shipping

As a user when I make purchases equal to 50 euros or more I expect free shipping. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                         |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart		| OK | 
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order			| OK | https://grocerymate.masterschool.com/checkout#!
| 7    | Ensure the total order increases to 50€	| The order total reaches 50€, which qualifies for free shipping| OK |
| 8    | Proceed to checkout	| Shipping fee is shown, and the total order is updated to 50€ | OK |

### Scenario 16: Notify user about eligibility for free shipping

As a user when I make purchases equal to 100 euros or more I expect free shipping. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'      |                                   |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart		| OK | 
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order			| OK | https://grocerymate.masterschool.com/checkout#!
| 7    | Ensure the total order increases to 100€	| The order total reaches 10€, which qualifies for free shipping| OK |
| 8    | Proceed to checkout	| Shipping fee is shown, and the total order is updated to 10€ | OK |

### Scenario 17: Verify shipping fee updates correctly when items are removed from the cart

As a user I check that the shipping fee is applied again if I reduce my order total to less than 20 euros. (20 euros minimum order for free shipping)

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | Put credentials 'email: ramovalbuena@gmail.com', 'password: ecd912f4bbd84e'       |                                  |     |                    |    |
| 3    | Click on Sign in           | You are directed to Homepage  | OK     | https://grocerymate.masterschool.com/ |               |
| 4    | Go to Shop button        |    A pop-up for age verification appears |   OK     |    https://grocerymate.masterschool.com/store |             |
| 5    | Browse and add products to the cart | Products are added to your cart, with total above 20€			| OK | 
| 6    | Go to the shopping cart	 | The cart page appears with the total value of the order		| OK | https://grocerymate.masterschool.com/checkout#!
| 7    | Remove items from the cart	| The total value of the cart drops below 20€	| OK |
| 8    | Check the shipping fee	| The shipping fee is applied again, as the total is now below 20€	 | OK |
| 9    | Proceed to checkout		 | The shipping fee is reflected in the final total	| OK | https://grocerymate.masterschool.com/checkout#!
















