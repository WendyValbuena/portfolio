Test Case Design for Online Grocery Webshop

### **1. Product Rating and Review System**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify that a user can submit a rating exactly at the boundary of 5 stars.
       - **Input:** Select 5 stars.
       - **Expected Outcome:** Rating is submitted successfully.
2. **Boundary Value Analysis:**
     - **Test Case:** Verify that the system prevents ratings above 5 stars.
       - **Input:** Attempt to submit 6 stars.
       - **Expected Outcome:** Error message: "Invalid rating."
3. **Equivalence Partitioning:**
     - **Test Case:** Submit a rating of 3 stars as a valid mid-point rating.
       - **Input:** Select 3 stars.
       - **Expected Outcome:** Rating is submitted successfully.
4. **Error Guessing:**
     - **Test Case:** Verify behavior when rating is submitted without feedback.
       - **Input:** Submit rating without comments.
       - **Expected Outcome:** Rating is accepted, feedback optional.
5. **Error Guessing:**
     - **Test Case:** Verify behavior when feedback contains prohibited language.
       - **Input:** Submit feedback with offensive terms.
       - **Expected Outcome:** Error message: "Inappropriate language detected."

### **2. Age Verification for Alcoholic Products**
**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing.

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify access for users exactly at the minimum age of 18.
       - **Input:** Age = 18.
       - **Expected Outcome:** Access to alcoholic products is granted.
2. **Boundary Value Analysis:**
     - **Test Case:** Verify access denial for users under 18.
       - **Input:** Age = 17.
       - **Expected Outcome:** Error message: "Access denied. You must be at least 18 years old."
3. **Equivalence Partitioning:**
     - **Test Case:** Allow access for users over 18.
       - **Input:** Age = 19.
       - **Expected Outcome:** Access granted to alcoholic products.
4. **Error Guessing:**
     - **Test Case:** Verify behavior when age input is left empty.
       - **Input:** Age field empty.
       - **Expected Outcome:** Error message: "Age is required."
5. **Error Guessing:**
     - **Test Case:** Verify behavior with invalid age format.
       - **Input:** Age = "abc".
       - **Expected Outcome:** Error message: "Invalid age format."

### **3. Shipping Cost Calculation**
**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

### Test Cases:
1. **Boundary Value Analysis:**
     - **Test Case:** Verify free shipping eligibility for orders at the minimum threshold.
       - **Input:** Order total = $100 (assuming $100 is the free shipping threshold).
       - **Expected Outcome:** Free shipping applied.
2. **Boundary Value Analysis:**
     - **Test Case:** Verify shipping cost for orders just below free shipping threshold.
       - **Input:** Order total = $99.99.
       - **Expected Outcome:** Shipping fee added.
3. **Equivalence Partitioning:**
     - **Test Case:** Verify shipping charges for orders well below the threshold.
       - **Input:** Order total = $50.
       - **Expected Outcome:** Order total = $20.
4. **Use Case Testing:**
     - **Test Case:** Notify user about eligibility for free shipping.
       - **Input:** Order total increases to $100 during checkout.
       - **Expected Outcome:** Message: "You qualify for free shipping!"
5. **Use Case Testing:**
     - **Test Case:** Notify user about eligibility for free shipping.
       - **Input:** Order total increases to $100 during checkout.
       - **Expected Outcome:** Message: "You qualify for free shipping!"
6. **Use Case Testing:**
     - **Test Case:** Verify shipping fee updates correctly when items are removed from the cart.
       - **Input:** Remove items to bring total below $100.
       - **Expected Outcome:** Shipping fee re-applied.

### **4. Checkout Process and Payment Method Selection**
**Test Design Techniques:** Use Case Testing, Error Guessing

### Test Cases:

1. **Use Case Testing:**
     - **Test Case:** Verify payment method selection at checkout.
       - **Input:** Select "Credit Card" as payment method.
       - **Expected Outcome:** User can proceed to enter credit card details.
2. **Use Case Testing:**
     - **Test Case:** Verify order summary displays total cost after item selection.
       - **Input:** Add multiple items to cart.
       - **Expected Outcome:** Order summary shows total item cost plus shipping if applicable.
3. **Error Guessing:**
     - **Test Case:** Verify behavior when payment details are left blank.
     - **Input:** Proceed without entering payment information.
     - **Expected Outcome:** Error message: "Payment information required."
4. **Error Guessing:**
     - **Test Case:** Verify system response when an expired credit card is used.
       - **Input:** Enter expired credit card.
       - **Expected Outcome:** Error message: "Invalid or expired card."
