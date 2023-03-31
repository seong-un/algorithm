const fs = require('fs');

// let num = fs.readFileSync('input.txt').toString().split(' ');
let num = fs.readFileSync('/dev/stdin').toString().split(' ');

const a = parseInt(num[0]);
const b = parseInt(num[1]);

console.log(a / b)
