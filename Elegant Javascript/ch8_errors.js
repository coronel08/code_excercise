/* Ch8 Errors
Function primitiveMultiply that in 20% of cases multiplies two numbers and in the other 80% of cases raises an exception
of MultiplicatorUnitFailure. Write a function that wraps this function and keeps trying until a call succeeds, returns result.

class MultiplicatorUnitFailure extends Error {}

function primitiveMultiply(a, b) {
  if (Math.random() < 0.2) {
    return a * b;
  } else {
    throw new MultiplicatorUnitFailure("Klunk");
  }
}

function reliableMultiply(a, b) {
  // Your code here.
}

console.log(reliableMultiply(8, 8)); // → 64
*/


class MultiplicatorUnitFailure extends Error{}

function primitiveMultiply(a,b){
    if(Math.random() < 0.2){
        return a*b
    } else {
        throw new MultiplicatorUnitFailure("Klunk")
    }
}

function reliableMultiply(a,b){
    try {
        return primitiveMultiply(a,b)
    } catch(e){
        if(e instanceof MultiplicatorUnitFailure){
            return reliableMultiply(a,b) 
        } else {
            throw `Caught a problem ${e}`
        }
    }
}

console.log(reliableMultiply(8,8))




/*
Consider a box with lock, with an array inside, write a function withBoxUnlocked that takes a function value as argument
unlocks the box, runs the function, and then locks the box before returning
*/


const box = {
    locked: true,
    unlock(){this.locked = false},
    lock(){this.locked = true},
    _content: [],
    get_content(){
        if(this.locked) throw new Error("Locked")
        return this._content
    }
}

function withBoxUnlocked(body){
    if(box.locked) box.unlock()
    try {
        console.log(box.get_content())
        return body()
    } finally {
        box.lock()
    }
}

withBoxUnlocked(function(){
    box._content.push("gold piece")
});


try{
    withBoxUnlocked(function(){
        throw new Error("Pirates on the horizon! Abort!")
    })
} catch (e){
    console.log("Error Raised: " + e)
}

console.log(box.locked) // true
