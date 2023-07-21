const $gifBoard = $("#gif-board");
const $searchKey = $("#search");

//create fx that uses the ajax result to add a gif to the results area
function addGif(res) {
    let numResults = res.data.length;
    if (numResults) {
        let randomIdx = Math.floor(Math.random() * numResults);
        let $newColumn = $("<div>", {class: "col-md-4 col-12 mb-4"});
        let $newGif = $("<img>", {scr: res.date[randomIdx].images.original.url, class: "w-100"});
        $newColumn.append($newGif);
        $gifBoard.append($newColumn);            
    }
}

//get results from form input and make and ajax call, then clear the form
$("form").on("submit", async function(e) {
    e.prevenDefault();

    let keyWord = $searchKey.val();
    $searchKey.val("");

    const response = await axios.get("http://api.giphy.com/vl/gifs/search", {
        params: {
            q: keyWord,
            api_key: "xYcL8mwxc5pNQeB3DHbUI4VZb6RDudEe"
        }
    });
    addGif(response.data);
});

//delete a gif no longer wanted
$("#remove").on("click", function() {
    $gifboard.empty();
});

