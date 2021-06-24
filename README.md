# Battle of Teams

- Multiplayer Role-Playing Strategy Game, built in Python played on terminal. 

- This game was written for a one-week project during our training at HTU's National ICT Upskilling Program.

- Built by Hamza Radaideh, Hisham Marie, Reema Eilouti and our Mentor George Khoury.



## Set Up

- Clone the repo on your machine using: `git clone https://github.com/reema-eilouti/battle_of_teams_game`

- Install dependencies using: `pip3 install termcolor` for displaying colours on terminal.

- run the `battlefield.py` file using: `python3 battlefield.py`



## Game Instructions

- Two teams: A and B, each have three characters; A Warrior, a Medic and an Explorer.

- You win the game by killing the other team's characters.


### Characters Description:

- **Attributes:**
    - Each character has:
        - **Health**: Starts at 100%
        - **Strength**: Starts at 100%

    - **Warrior**'s extra attributes:
        - Popularity Points.

    - **Medic**'s extra attributes:
        - Nanobots.
        - Nanobots Accuracy Level.
        - Magic Level.

    - **Explorer**'s extra attributes:
        - Gold Pouch.
        - Foresight; 1, 2 or 3.
        - *Sectumsempra* Possession; Yes or No.

- The **Warrior** can:
    - **Attack**: Decreases the health of the opponent by a factor of **1/5 * warrior strength**. The strength of the warrior who launched the attack decreases by **5%**.
    - **Buy an Armor**: Adds a shield/armor for any team member, in exchange for one piece of gold. Reduces the strength of the warrior by **2%** and increases their popularity level by **1**.
    - **Share Intelligence**: Adds **1** to the explorer's foresight for every **3** popularity points.

- The **Medic** can:
    - **Heal**: Increases the health of the team member chosen by a factor of **number of nanobots * their accuracy level**. Decreases the medic strength by **5%**.
    - **Cast a Spell**: Casts two types of spell on the opponent either '*Sectumsempra'* or *'Confringo'*. If the explorer has gone to the forbidden library **Sectumsempra** is chosen and it is more powerful *(cuts health in half)*. **Confringo** decreases opponents health by **Magic Level * (Strength / 10)**. Decrease the strength of the medic by **10%**.
    - **Go Back to The Future**: Increases the number of nanobots by a **random factor** and increases their level of accuracy by **1**.

- The **Explorer** can:
    - **Go on a Quest**: Puts the explorer on a random map to collect gold based on the foresight level. Decreases the explorer's strength by a factor of **gold coins * 2**.
    - **Go to The Forbidden Library**: Raises the flag of the *Sectumsempra* Possession which makes the following 'Cast Spell' extra powerful. Decreases the explorer's strength by a **random factor** (10% - 50%).

