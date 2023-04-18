/*Refactor this function using the rest operator and an arrow function:
function filterOutOdds() {
    var nums = Array.prototype.slice.call(arguments);
    return nums.filter(function(num) {
        return num % 2 === 0
    });
}
*/

const filterOutOdds = (...args) =>args.filter(val => val % 2 === 0);

/*Write a function called findMin that accepts a variable number of arguments and returns the smallest argument. Make sure to do this using the rest and spread operator. */

const findMin = (...args) => Math.min(...args); 

/*Write a function called mergeObjets that accepts two objects and returns a new object which contains all the keys and values of the first object and second object. */

const mergeObjets = (obj1, obj2) => ({...obj1, ...obj2});

/* Write a function called doubleAndReturnArgs which accepts an array and a varialbe number of arguments. The function should return a new array with the original array values and all of the additional arguments doubled. */

const doubleAndReturnArgs = (arr, ...args) => [...arr, ...args.map(val => val * 2)];

//Write the following functions using rest, spread, and refactor these functions to be arrow functions

/* remove a random element in the items array and return a new array without that item. 
function removeRandom(items) {

} */
const removeRandom = items => {
    let idx = Math.floor(Math.random() * items.length);
    return [...items.slice(0, idx), ...items.slice(idx + 1)];
}

/* return a new array with every item in array1 and array2.
function extend(array1, array2) {

}*/

const extend = (arr1, arr2) => {
    return[...arr1, ...arr2];
}

/*return an new object with all the keys and values from obj and a new key/value pair
function addKeyVal(obj, key, val){

}*/

const addKeyVal = (obj, key, val) => {
    let newObj = {...obj};
    newObje[key] = val;
    return newObj:
}

/*return a new object with a key removed.
function removeKey(obj, key) {

}*/
 
const removeKey = (obj, key) => {
    let newObj = {...obj};
    delete newObj[key];
    return newObj;
}

/*combine two objects and return a new object.
function combine (obj1, obj2) {

}*/

const combine = (obj1, obj2 ) => {
    return {...obj1, ...obj2};
}

/*return a new object with a modified key and value.
function update(obj, key, val) {

}*/

const update = (obj, key, val) => {
    let newObj = {...obj};
    newObj[key] = val;
    return newObj;
}



