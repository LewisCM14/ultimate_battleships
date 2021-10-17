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

*Initial development was to create a flow diagram using [LucidChart](https://www.lucidchart.com/pages/) so i could begin exploring how the requirements for my game and their dependencies would work together. I adhered to [LucidChart](https://www.lucidchart.com/pages/) symbol notation and color coded my chart based on the differnt phases of the game.*

![The Whole flow diagram](/assets/images/flowchart.jpeg)

*The first step is to display the welcome message and collect a valid name input. This name input is then used to create the players board's to be used before the computer's board's are created.*

![The First Stage of the flow diagram](/assets/images/flow1.png)

*The player can then begin adding their ships. Collision, fitment and input validation checks must be run for each ship, once done the computers ships are randomly added to their board.*

![The Second Stage of the flow diagram](/assets/images/flow2.png)

*Once the board's are populated game play can begin, for each turn input validation checks must be run as well as the relevant board's information updated.*

![The Third Stage of the flow diagram](/assets/images/flow3.png)

*For each valid turn, game end conditions must be checked and if reached, the turn sequence must be broken out of and the game end logic run.*

![The Fourth Stage of the flow diagram](/assets/images/flow4.png)

*Once my flow diagram was completed i drew up a basic wire frame using Balsamiq so i could explore how the game would be displayed within the terminal.*

![Wire frame](/assets/images/wireframe.png)

[Return to Table of Contents](#contents)

## Existing Features <a name='existingfeatures'></a>

- **The Welcome Message**

    * When a new game starts the welcome message is displayed.

    * Within this the different types of ship are listed, as well as the: board size, total number of lives and the different styles of marker.

    * The player is then prompted for name input, which adheres to the validation checks listed. Input is repeated until a valid name is entered. User feedback is then provided on the name they entered.

![The Welcome Message](/assets/images/deploy.png)

- **The Board**

    * Once name input is validated, it is then used to create the player's board, which is displayed to them in the terminal for reference when placing their ships. The user is prompted to place each ship in turn, the ship name and size is displayed to them.

    * Orientation, column and then row inputs are requested for the ship location, all having validation checks on them. Before fitment and collision checks are ran on the input location for the ship, which must be passed else the user is prompted for input again.

    * Once a valid series of inputs are entered the ship is placed on the players board, their board is then printed to them with the placed ship for reference when placing the next. Once all ships are placed the computers ships are randomly placed on their board, following the same series of validation checks.

![The Game Board](/assets/images/board.png)

- **The Guess Board**

    * Once the ships have been placed on each board the game play sequence begins.

    * The player always goes first, their guess board is printed out to them for reference when entering a column and row, which must pass validation checks. Once a valid input is entered the result of their attack is printed out to them before the guess board is updated and printed out to them again. Validation checks prevent the user repeat guessing or attacking each specific coordinate.

    * The sleep method of the time library and a line break are used here to emphasize the individual turns, a countdown of three seconds is used before the computer makes their attack and the terminal is updated.

![The Guess Board](/assets/images/guess.png)

- **Ship Display**

    * Ships that haven't been hit are displayed on the player's board as solid squares.

    * Letter notation is used for column display purposes and number notation for the rows, this allows for easy differentiation when inputting coordinates.

    * Dashes are used for empty or coordinates that haven't been guessed, i felt this coupled with the squares to represent ships and O for a miss and X for a hit created a good level of contrast whilst also accurate representation of the intention behind the marker.

![Ship Display](/assets/images/ships.png)

- **Game Play Display**

    * User feedback is provided constantly throughout the game, specific to each phase.

    * The turn sequence is broken down as well as the result of each players attack. The boards are updated appropriately as well as the life counter decremented when required.

    * A consistent use of the sleep method and line breaks is also used throughout.

![A Hit Ship](/assets/images/hit.png)

- **Play Again**

    * Once the game end conditions have been met, which is a player having no lives left, the turn sequence is broken out off, with a win or lose message being displayed.

    * The player is them prompted to play again, input validation is used here to ensure a Y or N is entered.

    * If yes the game runs again from the beginning, else the player is told goodbye and the program ends.

![Play Again Display](/assets/images/playagain.png)

[Return to Table of Contents](#contents)

## Features Left to Implement <a name ='toimplement'></a>

*There are no features left to implement from the initial scope of my project, however i have some features that i would like to add in the future.*

*  Allow the user to adjust their name if they are not happy with the initial input.

*  Allow: Orientation, Column and Row inputs to be placed on the same line.

* Print the Player Board and Guess Board side by side in the terminal, rather than on top of one another.

* Highlight the Win or Lose message to greater effect.

* Refine the Computer Attack AI logic. I feel, rather than breaking out of the loop and returning a random input at the points marked on the image below. Which i had to do to prevent the computer getting stuck in an infinite loop if there wasn't a valid input coordinate based on their last hit, a more elegant solution could be developed. 

    Possibly checking for the total number of attempts at producing a valid coordinate before returning a random input. Due to the code logic currently only one attempt is made per turn, when multiple attempts could be made to ensure all options have been explored per turn. 
    
    Whilst on the face of it this solution appears simple, due to me using random when the computer decides to go left or right and top or bottom based off their last hit coordinate several alterations to the code are required to implement this solution which didn't fit inside my project deadline. Having developed the code to allow for column and row inputs to be entered together from the start would perhaps have made these alterations easier.

![Code mentioned above](/assets/images/improve.png)

[Return to Table of Contents](#contents)

## Testing <a name ='testing'></a>  

-  Due to the nature of the project testing has been conducted throughout its entirety, mainly through the use of running the program in the terminal and ensuring i get the output intended. Evidence of this is clear within my commits, with various debugs recorded. 

-  Various sections of code where also developed in isolation and outputs checked before being inserted into the running order as the size of the project grew.  

-  Once at the finished point, limit testing has been conducted by myself and my peers on slack through the peer-code-review channel, there is currently no reported issues that cause the game to break.

- **Validator Testing**

    - HTML
        - Not within project scope.

    - CSS
        - Not within project scope.

    - JS
        - Not within project scope.

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**

    - Not within project scope.

[Return to Table of Contents](#contents)

## Unfixed Bugs <a name ='bugs'></a>

-  The only bug i was unable to fix, due to not being able to replicate it, was an issue with how the board display was printed out to the terminal. My only instance of this bug was just after i utilized my updated legend. Once the guess board was printed out again on the next turn the display discrepancy wasn't present.

![bug](/assets/images/glitch.png)

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
