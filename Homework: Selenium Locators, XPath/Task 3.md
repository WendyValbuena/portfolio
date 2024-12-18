1. Write the XPath to locate the main **h1** element.

//h1[@id="mainTitle"] 

2. Write the XPath to select the **About Us** navigational link.

//a[@class="nav-link" and text()="About Us"]

3. Write the XPath to select the **Graphic Design** dropdown link.

//ul[@class="dropdown"]//a[text()="Graphic Design"]

4. Write the XPath to select the team member’s name **Jane Smith**.

//div[@class="team"]//h4[text()="Jane Smith"]

5. Write the XPath to select the description (which is inside the paragraph) of **SEO Services**. 

//p[text()="Improving search engine rankings."]

6. Write an XPath expression to select all service items in the "**Our Services**" section.

//div[@class="service-item"]/h3

7. What is the XPath to select the **email input field** in the contact form?

//input[@id="email"]

8. How would you write an XPath to select the **entire contact form**?

//form[@id="contactForm"]

9. Provide the XPath to select the **footer paragraph element**.

//footer[text()]

10. What is the XPath to select the **first team member**'s (`<h4>`) name?

//div[@class="team"]//h4[text()="John Doe"]

//div[@class="team"]/ul/li[1]/h4

11. How can you select the description of the **second service** item using XPath?

//ul[@class="dropdown"]/li[2]

12. What is the XPath to select the "Contact Us" section header (`<h2>` element)?

//h2[@class="sectionTitle" and text()="Contact Us"]

13. Write an XPath expression to select all links within the dropdown under the "Services" navigation item.

//li[a[text()="Services"]]/ul[@class="dropdown"]//a

14. What is the XPath to select the first `<li>` under the "Our Team" section?

//div[@class="team"]//ul/li[1]

15. Provide the XPath to locate the "Send Message" button in the contact form.

//input[@type="submit" and @value="Send Message"]
