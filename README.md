* What This Project Does



Opens a help documentation website



Reads the content (headings and text)



Identifies:



Main topics as Modules



Sub-topics as Submodules



Saves the extracted information into a JSON file



🛠️ Technologies Used



Python



Requests (to fetch website content)



BeautifulSoup (to parse HTML)



JSON (for structured output)



&nbsp;How to Run the Project

Step 1: Install dependencies

pip install requests beautifulsoup4



Step 2: Run the program

python module\_extractor.py



Output



The extracted modules and submodules are saved in:



output.json



Example Output Structure

{

&nbsp; "module": "Account Settings",

&nbsp; "Description": "Includes options to manage account preferences",

&nbsp; "Submodules": {

&nbsp;   "Change Password": "Allows users to update password",

&nbsp;   "Deactivate Account": "Temporarily disable the account"

&nbsp; }

}



&nbsp;Supported Websites (Tested)



https://help.instagram.com/



https://wordpress.org/documentation/



https://help.zluri.com/

