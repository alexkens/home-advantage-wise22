# Home Advantage in Football

The term **Home Advantage** describes the benefit the hosting team has over the visiting team. Multiple reasons for an alledged advantage for teams playing on home ground have led to the introduction of the Away Goals Rule. The rule got introduced by the Union of European Football Associations (UEFA) in the year 1965 and has been active ever since. However, in the year 2021, the Away Goals Rule got abolished.  
This project serves for measuring and analyzing statistics in football that can be interpreted to find an answer to the question whether Home Advantage exists in professional european football or not. We have approached this matter from two perspectives and concluded that Home Advantage is

- based on the number of **home** wins in relation to **away** wins, and [1]

- based on the number of **home** goals in relation to **away** goals. [2]

# Table of Content

**Analysis**  
This directory contains all scripts that either

- perform an analysis and create plots, such as  
    - barplot_one_league.py [1]
    - barplot_all_leagues.py [1]
    - graph_line_all_leagues.py [1]
    - plot_goals.py [2]
    - plot_difference_goals.py [2]  
- are necessary for analyzing our data, such as
    - allFixtures.csv
        - csv file that contains all data we received
    - create_csv.py
        - script that creats allFixtures.csv from JSON data
    - AnalysisUtil.py
        - utility class with helpful functions for analysis
    - all_enums.py
        - contains useful enum class

**Requests**   
This directory contains all scripts that request data from our [API](https://www.api-football.com/).  
Every league that is considered during this project has its own request directory.

**Resources**  
This directory contains all received data in JSON format.  
Every league that is considered during this project has its own resources directory.

**Visualization**  
This directory contains all plots that have been shown in the presentations and research paper.

# How to run our code

**PLEASE MAKE SURE YOU HAVE PYTHON VERSION >3 INSTALLED**  
To check your version run this command in a terminal:  
(`python --version`)

There are several ways on how to run our code, but we recommend one of the two following.

**1. Terminal**  

In order for you to run our project locally in your terminal you have to follow the steps below.  

1. clone this repository by executing this command in a terminal:  
`git clone https://git.tu-berlin.de/six.six6/data-science-project-wise22.git`
2. install all dependencies by navigating to main/ and running this command:  
(`cd data-science-project-wise22`  
`cd main`)  
`pip install -r requirements.txt`  
3. you can run one of our python scripts with the following command:  
`python python_script.py` 

**2. IDEA**

For this section, the IDEA of our choice was PyCharm.  
You can download PyCharm right [here](https://www.jetbrains.com/pycharm/download/).  
If you choose another IDEA, please follow the IDEAs instructions on how to clone and run a git repository.

In order for you to run our project with PyCharm you have to follow the steps below.

1. When starting PyCharm, choose option 'Get from Version Control' enter the following url and press the 'Clone' button  
`https://git.tu-berlin.de/six.six6/data-science-project-wise22.git`  
2. in terminal (can be found in the bottom left) navigate to main/ and install all dependencies like this:  
`cd main`  
`pip install -r requirements.txt`  
3. you can run one of our python scripts by  
    - opening the script, 
    - right clicking on the code and 
    - pressing on Run 'python_script.py'
