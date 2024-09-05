#!/usr/bin/node
/** A script that displays prints the title of a
 * Star Wars **/

const request = require('request');


const movieId = process.argv[2];

if (!movieId) {
    console.log('Not a correct movie Id');
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

async function getCharacters() {
    try {
        const response = await requestPromise(url);
        const data = JSON.parse(response.body);
        const characters = data.characters;

        for (const characterUrl of characters) {
            const characterResponse = await requestPromise(characterUrl);
            const characterData = JSON.parse(characterResponse.body);
            console.log(characterData.name);
        }
    } catch (error) {
        console.error('Error fetching data:', error.message);
        process.exit(1);
    }
}

getCharacters();