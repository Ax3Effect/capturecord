# Discord plays Capture the Flag!
Built by @Ax3Effect and @JWWilks

## Inspiration
Some really cool projects we've seen before are the "Twitch plays" games, where an entire twitch chat controls a video game which is being live-streamed. Some examples include "Twitch plays pokemon" and "Twitch plays undertale". We wanted to re-work this idea to allow any number of users in a Discord chat to play Capture the Flag which will be rendered on a web-based platform.

## What it does
A Discord bot initially assigns everyone in the Discord server to a team, red or blue. Then, any directional command (WASD) sent in the discord chat is used to calculate the new board state, which is then sent via sockets to the web client, over at http://discordflag.com . This allows both teams to struggle to work together as they attempt to win a simple Capture the Flag game against their opponents.

## How we built it
Our initial idea was to make the bot work entirely in Discord; it a Discord message for the game's grid every message. However due to some of Discord's API call limitations, and because we really wanted to challenge ourselves, we decided to work with Flask, Vue, and Socket.IO to create a web-interface which could receive data from the Discord bot. Now, the new board state (as calculated by directional commands) is sent to our web server, which updates the visual board. This way, everyone playing the game can also visit the website and see the board update in real-time.

## Challenges we ran into
It turns out sending data from a Discord bot to a web server is quite tough, especially when it comes to data interpretation and presentation. Furthermore, applying the (potentially hundreds) of user commands to calculate the game state in an efficient manner was also pretty tough.

## Accomplishments that we're proud of
The transition of data from Discord commands to the web server in real time is really cool. Especially when it comes to how quickly we are able to update the state of the web client when someone sends a message.

## What's next for Discord Plays CTF
The most challenging part of our project was the implementation of the base mechanics - that is the sockets, the game state, and the web app. But now with those implemented, they are essentially boilerplate. With some tweaking, we could easily use the same mechanics to create any number of games playable in the same format - not just CTF. We could even make a minigame bot with lots of different games!
