#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.co/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`An error occurred: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie data. Response code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((character) => {
    request(character, (error, response, body) => {
      if (error) {
        console.error(`An error occurred: ${error}`);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to retrieve character data. Response code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

