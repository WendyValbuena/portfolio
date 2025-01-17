Test Case Design for Online Grocery Webshop

### **1. Product Rating and Review System**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify that a user can submit a rating exactly at the boundary of 5 stars.
       - **Input:** Select 5 stars.
       - **Expected Outcome:** Rating is submitted successfully.
2. **Equivalence Partitioning:**
     - **Test Case:** Submit a rating of 3 stars as a valid mid-point rating.
       - **Input:** Select 3 stars.
       - **Expected Outcome:** Rating is submitted successfully.
3. **Error Guessing:**
     - **Test Case:** Verify behavior when rating is submitted without feedback.
       - **Input:** Submit rating without comments.
       - **Expected Outcome:** Rating is accepted, feedback optional.
4. **Error Guessing:**
     - **Test Case:** Verify behavior when feedback contains prohibited language.
       - **Input:** Submit feedback with offensive terms.
       - **Expected Outcome:** Error message: "Inappropriate language detected."
5. **Boundary Value Analysis**
     - **Test Case:** Verify that a user can edit an existing rating and/or comment by changing the rating or modifying the comment.
       - **Input:** Select 5 stars, edit the comment.
       - **Expected Outcome:** The system successfully updates the rating and comment, and the new values are displayed on the product page.
6. **Use Case Testing**
     - **Test Case:** Verify that a user can delete an existing rating and/or comment.
       - **Input:** Select the delete option for a specific product’s rating/comment.
       - **Expect:** The system successfully deletes the rating and/or comment, and no rating or comment is shown on the product page.
       
### **2. Age Verification for Alcoholic Products**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing.

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify access for users exactly at the minimum age of 18.
       - **Input:** Age Verification = '12-04-2006'
       - **Expected Outcome:** Access to alcoholic products is granted.
2. **Boundary Value Analysis:**
     - **Test Case:** Verify access denial for users under 18.
       - **Input:** Age Verification = '05-08-2007'
       - **Expected Outcome:** Error message: "Access denied. You must be at least 18 years old."
3. **Equivalence Partitioning:**
     - **Test Case:** Allow access for users over 18.
       - **Input:** Age Verification = '03-12-2005'
       - **Expected Outcome:** Access granted to alcoholic products.
4. **Error Guessing:**
     - **Test Case:** Verify behavior when age input is left empty.
       - **Input:** Age field empty.
       - **Expected Outcome:** Error message: "Age is required."
5. **Error Guessing:**
     - **Test Case:** Verify behavior with invalid age format.
       - **Input:** Age = '3,12,2002'
       - **Expected Outcome:** Error message: "Invalid age format."

### **3. Shipping Cost Calculation** (20 euros minimum order for free shipping)
**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify free shipping eligibility for orders at the minimum threshold. 
       - **Input:** Order total = 20€.
       - **Expected Outcome:** Free shipping applied 0€.
2. **Boundary Value Analysis:**
     - **Test Case:** Verify shipping cost for orders just below free shipping threshold.
       - **Input:** Order total = 19,99€.
       - **Expected Outcome:** Shipping fee added.
3. **Equivalence Partitioning:**
     - **Test Case:** Verify shipping charges for orders well below the threshold.
       - **Input:** Order total = 10€.
       - **Expected Outcome:** Order total = 15€.
4. **Use Case Testing:**
     - **Test Case:** Notify user about eligibility for free shipping.
       - **Input:** Order total increases to 50€ during checkout.
       - **Expected Outcome:** Message: "You qualify for free shipping!"
5. **Use Case Testing:**
     - **Test Case:** Notify user about eligibility for free shipping.
       - **Input:** Order total increases to $100 during checkout.
       - **Expected Outcome:** Message: "You qualify for free shipping!"
6. **Use Case Testing:**
     - **Test Case:** Verify shipping fee updates correctly when items are removed from the cart.
       - **Input:** Remove items to bring total below 20€.
       - **Expected Outcome:** Shipping fee re-applied.
