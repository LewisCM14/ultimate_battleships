# ULTIMATE BATTLESHIPS

Ultimate Battleships is a pure python based mini game deployed to Heroku. Allowing the player to enter their own team name before placing their ships on the board. Collision and Fitment checks are run as well as input validation.

User feedback is provided throughout with basic AI used to determine the computers attacks during the game play, with a life counter being utilised to signal game end, the option to play again or quit is presented at this point.

![readme hero image](/assets/images/deploy.png)

# Table of Contents <a name='contents'></a>

* [User Experience (UX)](#userexperience)
* [Design](#design)
* [Development](#development)
* [Existing Features](#existingfeatures)
* [Features Left to Implement](#toimplement)
* [Testing](#testing)
* [Unfixed Bugs](#bugs)
* [Deployment](#deployment)
* [Technologies Used](#tech)
* [Credits](#credits)

## User Experience (UX) <a name='userexperience'></a>

- **User Stories**

    *The site works off the assumption the user is already aware of the classic game: Battleships.*

    + **First Time Visitor Goals**
    
        A. Welcome the User.

        B. Highlight to the user key aspects of the game play layout.

        C. Encouraged them to enter a team name and begin a game.

    + **Returning Visitor Goals**

        A. Begin testing the limits of the user input during game play.  

        B. Become familiar with the game layout.

        C. Attempt to beat the computer.

    + **Frequent Visitor Goals**

        A. Explore different styles of game play.

        B. Develop individual tactics for game play.

    - **Owners Story**

        *The main goal of the project is to create a robust python application that provides enjoyment to the user. This is done by allowing as much user based decision making as possible, with constant feedback provided. Basic AI is used to place the user in a challenging environment during game play, helping pull the application away from simply feeling like a data entry sequence.*

- **Research**

    *My research for the project consisted of browsing other developers battleship game based creations. With the intent of learning the common problems faced and the display choices they made.*

[Return to Table of Contents](#contents)

## Design <a name='design'></a>

- **Colour Scheme**

    *Not required for the scope of this project.*

- **Typography**

    *I chose to capitalize all text on the project to create consistency in size throughout.*

- **Imagery**

    *Special attention to the board display during game play was required to ensure for suitable contrast between the different markers. [The Ascii Code](https://theasciicode.com.ar/) website was used to explore my options regarding ASCII characters. I implemented the use of a functional legend late on in the project to allow for easy testing of this.*

    ![legend image](/assets/images/legend.png) 

- **Layout**

    *My goal with the layout of the project, when displayed within the terminal, was to ensure clear differentiation between the separate phases of the game. This is done through the use of a line break and the sleep method contained within the time library.*

[Return to Table of Contents](#contents)

## Development <a name='development'></a>

![Flowdiagram]()

![Wireframe]()

[Return to Table of Contents](#contents)

## Existing Features <a name='existingfeatures'></a>

![image of the index page]()

- **The Header**

    * 

    *

    *

[Return to Table of Contents](#contents)

## Features Left to Implement <a name ='toimplement'></a>

* 

*  

* 

[Return to Table of Contents](#contents)

## Testing <a name ='testing'></a>  

-  

-   

- 

- **Validator Testing**

    - HTML
        - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)

    - CSS
        - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

    - JS
        - No errors were found when passing through the [JS Quality tool](https://jshint.com/)

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**

![Lighthouse]()

- . 

- 

[Return to Table of Contents](#contents)

## Unfixed Bugs <a name ='bugs'></a>

-  

-

![Bug]()

[Return to Table of Contents](#contents)

## Deployment <a name ='deployment'></a>

- The site is deployed to GitHub pages. The steps to deploy are as follows: 

    1. In the GitHub repository, navigate to the Settings tab. 
    2. Navigate to the GitHub pages area and follow the link.
    3. Publish the site from the main branch in the root directory. Once complete a link to the site will be displayed. Indicating successful deployment. 

The live link can be found here - []()

- The site is deployed via Heroku. The steps to deploy are as follows:

    *Ensure the requirements for the project are added to the requirements.txt file prior to deployment*

    1. From the dashboard, select New and then Create new app.
    2. Enter an individual app name into the text box, select a region from the dropdown and then press Create app.
    3. A Heroku app has now been created and the Deploy tab is opened.
    4. Select the Settings tab.
    5. If required, click on the Reveal Config Vars button and add.
    6. In the Buildpacks section of the settings tab, click on Add Buildpack, select Python and then save changes.
    7. Click on Add Buildpack again, select node.js and then save changes.
        *When they are on the dashboard, ensure that python is above node.js on the list*
    8. Open the Deploy tab.
    9. In the deployment method section, select GitHub and confirm the connection.
    10. Enter the repo-name into the text box. When the correct repo appears, click Connect.
    11. If desired, in the Automatic deploys section, click Enable Automatic Deploys.
        *This then updates the deployment every time GitHub code is pushed.*
    12. To complete the process click on the Deploy Brach button in the Manual deploy section. 
        *This will take a few seconds to complete while Heroku builds the app.*
    13. A message will appear informing you that the app was successfully deployed and a View button will bring you to the live site.

The live link can be found here - []()

[Return to Table of Contents](#contents)

## Technologies Used <a name ='tech'></a>

- **Languages Used**

    * HTML5
    * CSS3
    * JS
    * PYTHON
    * MARKDOWN

- **Frameworks, Libraries & Programs Used**

    1. Balsamiq. 
        * Balsamiq was used to create the wireframes during the development process.
    
    2. [Lucidchart](https://lucid.co/).
        * Used to create flow-diagrams during development.

    3. [MyColor.Space](https://mycolor.space/).
        * Used to define my colour pallet 

    4. [Google Fonts](https://fonts.google.com/). 
        * Used to import the 

    5. [Font Awesome](https://fontawesome.com/).
        * Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

    6. Git.
        * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

    7. [GitHub](https://github.com/).
        * GitHub is used to store the projects code after being pushed from Git.

    8. [Am i Responsive](http://ami.responsivedesign.is/).
        * Used to create the hero image for readme.

    9. [Iconifier](https://iconifier.net/).
        * Used to create the favicon for the site.
    
    10. [Beautify](https://codebeautify.org/).
        * Used to beautify my: HTML, CSS and JS code.
    
    11. [Heroku](https://id.heroku.com/login).
        * Used to deploy my project.

[Return to Table of Contents](#contents)

## Credits <a name = 'credits'></a> 

* A special thank you to my mentor Can Sucullu. 

* Thanks to the Code Institute tutor support team, who helped me develop my understanding throughout this project.

* Finally thanks to my peers on Slack who responded to my questions.  

- **Content** 

    * I used the breakpoints listed on [FreeCodeCamp](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/) for my media queries.

    * 

    *  

    * 

    *  

    *     

- **Media**

    * 

    *

    *
    
    *

    *

[Return to Table of Contents](#contents)
