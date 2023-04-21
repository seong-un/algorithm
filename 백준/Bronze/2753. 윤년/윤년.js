const fs = require("fs")
const filePath = "/dev/stdin"
let year = Number(fs.readFileSync(filePath).toString())
if (year%400===0){
    console.log(1)
} else if (year%100===0){
    console.log(0)
} else if (year%4===0){
    console.log(1)
} else {
    console.log(0)
}