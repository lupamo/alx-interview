const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
    console.log('Not a correct movie Id');
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching the movie:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        process.exit(1);
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                process.exit(1);
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
