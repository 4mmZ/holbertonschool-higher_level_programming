fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    console.log(`Character Name: ${characterName}`);
  })
  .catch(error => console.error('Error:', error));