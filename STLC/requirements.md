## **The software**

Webshop, with the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

You can find the software here: https://grocerymate.masterschool.com/

## New features

### **1. Product Rating System**

**Requirement:** Users should be able to rate products with a 5-star system and have the option to add written feedback.

Questions:

1. How will ratings be displayed?
2. Can users update or delete their ratings?
3. Are there content restrictions on written feedback?

Detailed Requirement:

Users must be able to rate products using a 0 to 5-star system and add written reviews. They should also have the option to see the average rating and the total number of reviews. Users can update or delete their ratings and comments at any time, and the system must reflect these changes in real-time. Written reviews must be moderated to prevent inappropriate content, with automatic filters for offensive language.


### **2. Age Verification for Alcoholic Products**

**Requirement:** Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

Questions:

1. What happens if the user is under 18 or enters an invalid age?
2. Should age verification persist across sessions?
3. Are there legal or privacy requirements for age verification?

Detailed Requirement:

Alcoholic products require users to verify their age before accessing this category. A pop-up window will ask users to confirm they are 18 or older. If a user enters an invalid or underage response, they should be redirected to the homepage. If a user verifies their age during a session, the system should remember this information for future sessions unless they log out or clear cookies, in which case age verification will be required again. The system must comply with local laws on age verification and protect user privacy. Personal data should not be stored unnecessarily or shared with third parties unless required by law.


### **3. Shipping Cost Changes**

**Requirement:** Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

Questions:

1. What is the minimum order amount for free shipping?
2. How should the shipping fee be calculated for orders below the threshold?
3. How should the system notify users about shipping costs?

Detailed Requirement:

The system must offer free shipping for orders above a certain amount, while orders below this threshold will incur a shipping fee. The minimum amount for free shipping should be configurable by system administrators and visible to users at all times, preferably on the shopping cart summary page. For orders below the minimum, the system should automatically calculate the shipping fee based on a fixed rate or a tiered model, depending on weight or shipping distance. Users must be notified of the shipping costs or if they qualify for free shipping before completing the purchase, with clear notifications during the checkout process and no surprises in the final step.

