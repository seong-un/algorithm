const fs = require("fs")
const filePath = "/dev/stdin"
let [H, M]=fs.readFileSync(filePath).toString().split(" ").map(string => {return Number(string)})

M-=45
if (M<0){
    M+=60
    H-=1
}

if (H<0){
    H=23
}

console.log(H, M)