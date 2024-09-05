#!/usr/bin/node

/** A script that displays prints the title of a
 * Star Wars **/

function getRequest(url) {
    const request = require('request');
    return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
            if (error) {
                reject(error);  
            } else {
                resolve(JSON.parse(body));
            }
        });
    });
}

async function getCharacters() {
    const args = process.argv;

    if (args.length < 3) {
        console.log('Please provide a movie ID');
        return;
    }

    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

    try {
        const movie = await getRequest(movieUrl);

        if (movie.characters === undefined) {
            console.log('No characters found for this movie.');
            return;
        }

        for (const char of movie.characters) {
            const character = await getRequest(char);
            console.log(character.name);
        }
    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
}

getCharacters();