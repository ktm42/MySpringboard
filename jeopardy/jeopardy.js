const apiUrl = "https://jservice.io/api/"
let categories;
let currCategories = [];

async function startGame() {
  categories = 'undefined';
  currCategories = [];
  
  document.querySelector('#jeopardy tbody').replaceChildren();
  document.querySelector('#jeopardy thead').replaceChildren();
  
  await getCategories();
  
  const start = document.querySelector('#start')
};

async function getCategories() {
  let resp = await axios.get(`${apiUrl}categories?count=100`)
  categories = resp.data;
  randomCategories();
}

function randomCategories() {
  for (let i = 0; i < 6; i++) {
    let n = Math.floor(Math.random() * 100);  
    currCategories.push(categories[n]);
  }
  getClues();
}
   
async function getClues() {
  for (let i = 0; i < currCategories.length; i++) {
    let resp = await axios.get(`${apiUrl}category?id=${currCategories[i].id}`)
    currCategories[i].clues = resp.data;
  }
  addHeaders();
}

function addHeaders() {
  currCategories.forEach(category => {
    const title = document.createElement("th");
    title.classList.add("title");
    title.textContent = `${category.title}`;
    document.querySelector(`#jeopardy thead`).appendChild(title);
  });
  addTiles();
}
  
function addTiles() {
  for (let i=0; i < 5; i++) {
    let row = document.createElement("tr")
    currCategories.forEach(category => {
      const tile = document.createElement("td");
      tile.classList.add("tile", 'unflipped');
      tile.textContent = "?";
      row.appendChild(tile);
      
      const clue = category.clues.clues[i];
      tile.onclick = () => {
        if (tile.classList.contains('unflipped')){
          tile.classList.remove('unflipped');
          tile.textContent = clue.question;
          tile.classList.add('question');
        }
        else if(tile.classList.contains('question')) {
          tile.classList.remove('question');
          tile.textContent = clue.answer;
          tile.classList.add('answer');
        }
      }
    });
    document.querySelector('#jeopardy tbody').appendChild(row);
  }
}

const startBtn = document.querySelector("#start");
startBtn.addEventListener('click', () => {
  startBtn.textContent = 'Restart';
  startGame();
});