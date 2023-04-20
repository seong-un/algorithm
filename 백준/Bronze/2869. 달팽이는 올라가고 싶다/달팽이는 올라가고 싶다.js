const fs = require("fs")
const filePath = "/dev/stdin"
let [A, B, V] = fs.readFileSync(filePath).toString().split(" ").map(string => {return Number(string)})
console.log(Math.floor((V - A) / (A - B))+((V - A) % (A - B) ? 2: 1))