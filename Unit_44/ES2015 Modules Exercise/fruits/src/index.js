import fruits from './fruits';
import {choice, remove} from './helpers';

let fruit = choice(fruits);

console.log(`Can I have a ${fruit}, please`);
console.log(`Sure! Here you go: ${fruit}`);
console.log(`Yum, may I have another?`);

let remaining = remove(fruit, fruits);

console.log(`Sorry, we're out. We have ${remaining.length} left.`);