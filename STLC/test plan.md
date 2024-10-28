# **Test Plan for Webshop**

## **1. Analyze the Product**

### **Objective**

The main objective of the product is to enhance the existing webshop by adding key new features, such as a product rating system, age verification for alcoholic products, and changes to shipping costs. Additionally, it aims to ensure the correct functioning of current features, such as the checkout process, user registration, product search, and cart management, thereby optimizing the user experience while complying with legal and privacy requirements.

### **User Base**

The product will be used by existing and new users of the webshop, including individuals over 18 years old who can purchase alcoholic products. Additionally, it will offer a free shipping option for users who make purchases above a certain amount. They will also be able to rate, comment on, and add all products to favorites.

### **Hardware and Software Specifications**

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops computers with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge
    - Dependencies: Backend services, payment gateways, age verification services, and shipping cost calculation services

### **Product Functionality**

The product allows users to:

- Register and log in
- Search for products and sort them by price or category
- Add products to favorites and to the shopping cart
- Process orders, choose a payment method, and calculate the total cost
- Rate products and leave reviews
- Verify their age to access alcoholic products
- Enjoy free shipping on orders that meet the minimum amount

## **2. Design the Test Strategy**

### **Scope of Testing**

- **In Scope:**
    - Register and login functionality
    - Find products and sort them by price and categories
    - Review and rate products
    - Add products to favorites and shopping cart
    - Age restriction for purchasing alcohol
    - Checkout process: payment method selection and cost calculation
    - Add free shipping for purchases that meet the minimum amount
- **Out of Scope:**
    - Backend database operations not affecting the user interface
    - Third-party ad services integration (unless directly related to ad removal for subscribed users)
    - Third-party payment gateways

### **Type of Testing**

- Functional Testing
- Regression Testing
- Performance Testing
- Security Testing
- Usability Testing
- Integration Testing
- System Testing

### **Risks and Issues**
- **Delays in development**
    - Mitigation: Add a buffer period to the schedule to account for potential delays.
- **Product Data Inaccuracy**
    - Mitigation: Implement a data validation process to ensure product descriptions, prices, and stock levels are accurate.
- **Payment Gateway Downtime**
    - Mitigation: Have backup payment options and monitor gateway status to switch if needed.
- **Shipping Cost Calculation Errors**
    - Mitigation: Run extensive tests on the shipping cost calculation logic to ensure accuracy, especially for orders that qualify for free shipping.

### **Test Logistics**

- **Jane Smith** - Test Manager
- **John Doe** - QA Engineer (Functional and Regression Testing)
- **Alice Johnson** - QA Engineer (Performance and Security Testing)
- **Robert Brown** - QA Engineer (Usability Testing)
- **Maria Garcia** - End User for UAT

## **3. Define Test Objectives**

### **Objectives**

- **Functionality:** Ensure new features and existing functionalities work as intended.
- **GUI:** Verify the graphical user interface for usability and consistency.
- **Performance:** Confirm the system's performance under expected load conditions.
- **Security:** Identify and mitigate potential security vulnerabilities.
- **Usability:** Assess the user-friendliness of the platform.

### **Expected Outcomes**

- **Functionality:** All features perform correctly according to specifications.
- **GUI:** The interface is intuitive, responsive, and free of defects.
- **Performance:** The platform meets performance benchmarks under load.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can navigate and use the platform easily.

## **4. Define Test Criteria**

### **Suspension Criteria**

- Testing will be suspended if critical defects are found that block the continuity of testing, if necessary resources are missing, if there are failures in service integrations (such as payment gateways), or if there are failures in the test environment.

### **Exit Criteria**

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed, with no open severity 1 or 2 defects.
- The platform meets the defined performance standards, with no excessive load times.
- No significant vulnerabilities are detected, and data handling practices comply with privacy standards.
- User acceptance tests have been completed and approval has been obtained.

## **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools, performance testing tools

## **6. Plan Test Environment**

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

## **7. Schedule and Estimation**

| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 16/10/2024 | 21/10/2024 | All | Test Manager | 15 hours |
| Test Case Design | 16/10/2024 | 21/10/2024 | All | QA Team | 30 hours |
| Unit Testing | 22/10/2024 | 27/10/2024 | DEV | Development Team | 40 hours |
| Integration Testing | 28/10/2024 | 02/11/2024 | TEST | QA Team | 25 hours |
| System Testing | 03/11/2024 | 10/11/2024 | TEST | QA Team | 50 hours |
| Regression Testing | 11/11/2024 | 15/11/2024 | TEST | QA Team | 30 hours |
| Performance Testing | 16/11/2024 | 18/11/2024 | TEST | QA Team | 20 hours |
| Security Testing | 19/11/2024 | 21/11/2024 | TEST | QA Team | 20 hours |
| UAT | 22/11/2024 | 28/11/2024 | ACC | End Users | 40 hours |
| Production Release | 29/11/2024 | 29/11/2024 | PROD | DevOps Team | 10 hours |

## **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**
