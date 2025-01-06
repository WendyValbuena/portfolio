<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nested Complex HTML Document</title>
</head>
<body>
    <header>
        <h1 id="mainTitle">Welcome to Our Company</h1>
        <nav>
            <ul>
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About Us</a></li>
                <li>
                    <a href="#services" class="nav-link">Services</a>
                    <ul class="dropdown">
                        <li><a href="#webdev">Web Development</a></li>
                        <li><a href="#graphicdesign">Graphic Design</a></li>
                        <li><a href="#seo">SEO Services</a></li>
                    </ul>
                </li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2 class="sectionTitle">About Us</h2>
            <div class="content">
                <p>We are a leading company in the industry.</p>
                <div class="team">
                    <h3>Our Team</h3>
                    <ul>
                        <li>
                            <h4>John Doe</h4>
                            <p>CEO</p>
                        </li>
                        <li>
                            <h4>Jane Smith</h4>
                            <p>CTO</p>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        <section id="services">
            <h2 class="sectionTitle">Our Services</h2>
            <div class="service-list">
                <div class="service-item">
                    <h3>Web Development</h3>
                    <p>Creating stunning websites.</p>
                </div>
                <div class="service-item">
                    <h3>Graphic Design</h3>
                    <p>Designing visual content.</p>
                </div>
                <div class="service-item">
                    <h3>SEO Services</h3>
                    <p>Improving search engine rankings.</p>
                </div>
            </div>
        </section>
        <section id="contact">
            <h2 class="sectionTitle">Contact Us</h2>
            <form id="contactForm">
                <label for="name">Name:</label>
                <input type="text" id="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                <label for="message">Message:</label>
                <textarea id="message" placeholder="Your Message"></textarea>
                <input type="submit" value="Send Message">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Company Name. All rights reserved.</p>
    </footer>
</body>
</html>

### **Homework**

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

