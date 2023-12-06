let favNum = 7;
let baseURL = "http://numbersapi.com";

//1.
$.getJSON(`${baseURL}/${favNum}?json`, function(data) {
    console.log(data);
});

//2. 
let favNums = [7, 13, 42];
$.getJSON(`${baseURL}/${favNums}?json`, function(data) {
    console.log(data);
});

//3.
let facts = [];
$.getJSON(`${baseURL}/${favNum}?json`, function(data) {
    facts.push(data.text);
    $.getJSON(`${baseURL}/${favNum}?json`, function(data) {
        facts.push(data.text);
        $.getJSON(`${baseURL}/${favNum}?json`, function(datat) {
            facts.push(data.text);
            $.getJSON(`${baseURL}/${favNum}?json`, function(data) {
                facts.push(data.text);
                facts.forEach(fact => {
                    $('body').append(`<p>${fact}`);
                });
            });
        });
    });
});