const fs = require("fs")
const filePath = "/dev/stdin"
let input = fs.readFileSync(filePath).toString().split("\n")
for (string of input){
    if (string==='.'){
        break
    }
    let parenthesis = []
    let open_parenthesis = new Array('(', '[')
    for (i of string){
        if (open_parenthesis.includes(i)){
            parenthesis.push(i)
        } else if (i === ')'){
            try {
                if (parenthesis.pop() === '('){
                    continue
                } else {
                    console.log("no")
                    break
                }
            } catch {
                console.log("no")
                break
            }
        } else if (i === ']'){
            try {
                if (parenthesis.pop() === '['){
                    continue
                } else {
                    console.log("no")
                    break
                }
            } catch {
                console.log("no")
                break
            }
        } else if (i === '.'){
            if (parenthesis.length != 0){
                console.log("no")
            } else {
                console.log("yes")
            }
        }
    }
}