# Cricket
Django Project - Cricket - Teams, playes, Matches Fixture, Points

# Administrator Credentials
  - admin/admin

# Models:
  - Team - Table
    - name - team name
    - logo_url - team image
    - club_state - text field
  
  - Player - Table
    - team - Foreginkey to Team table
    - firstname - player first name
    - lastname - player last name
    - image_url - player image (default image is exist)
    - player_jersey_no - Player jersey number
    - Country - player country
    - matches - player played match count
    - run - player total runs
    - highest_score - player high score
    - fifties - player total fifties
    - hundreds - player total hundreds
    
  - Matches - Table
    - left_team - Foreginkey to Team
    - right_team - Foreginkey to Team
    - winner_team - choice field (left_team, right_team, Not played, cancelled, both/draw)

# Urls:
  - / - list of teams
  - /teams/ - list of teams
  - /teams/&lt;int:pk&gt;/details - team details and list of players
  - /matches/ - list of match fixtures can generate and view.
  - /match/&lt;int:pk&gt;/update - update the match by choosing the winner team column. 
  - /points/  - see the points of each team (2 points for win, 1 points for both/draw)

# Prerequesties
  - Python3
  - Django2.2
  - Pillow

# Running the project
  - Download the repository.
  - Install the package.
    - `$ pip install <project_dir>/requiements.txt`
  - No need to do migrations.
  - Run the server
    ```$ python manage.py runserver```
  - Verify the project by navigating to your server address in your preferred browser.
    ```sh
    127.0.0.1:8000
    ```
    
    
