
### Scenario 1: Product Rating 5 stars 

Verify that a user can submit a rating exactly at the boundary of 5 stars

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put your credentials      |                                                            |     |                    |    |
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
| 2    | put your credentials      |                                                                |     |                    |    |
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

Submit rating without comments

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put your credentials      |                                                                |     |                    |    |
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

Submit feedback with offensive terms

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put your credentials      |                                                                |     |                    |    |
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

### Scenario 5: Verify behavior when feedback contains prohibited language.

Submit feedback with offensive terms

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put your credentials      |                                                                |     |                    |    |
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

### Scenario 6: Verify that a user can delete an existing rating and/or comment

Select the delete option for a specific product’s rating/comment.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1    | Go to login page MarketMate     | Login page appears | OK     | https://grocerymate.masterschool.com/auth |               |
| 2    | put your credentials      |                                                                |     |                    |    |
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
| 11b  | Comment: It was in poor condition; I won’t be buying here again |  | OK | | 
| 11c  | Click on send | The rating is displayed on the screen with comments| OK | |
| 12   | Refresh product page	 | 1-star rating is displayed for product without comments | OK | 
| 13a  | Click on the three dots | Click on Edit | OK  | |
| 13b  | Edit Review  | Edit rating and comments | OK | |
| 13c  | Save changes | You have already reviewed this product | OK | |






