// Ch 6.1 Exercise Notes https://gist.github.com/jonurry?page=4
/*
A class named Vec, takes x and y parameters that save to properties of the same name.
has 2 methods, plus and minus that take another vector as a parameter and return a new vector that has sum or diff between values
Add a getter property named length, that does Pythagoras' Theorem(multiply x,y to 2nd power and square root the sum) 
*/

class Vec{
    constructor(x,y){
        this.x = x,
        this.y = y
    }

    plus(vector){
        return new Vec(this.x + vector.x, this.y + vector.y)
    }

    minus(vector){
        return new Vec(this.x - vector.x, this.y - vector.y)
    }
    
    // used getter so it could be called .length instead of .length()     
    get length(){
        return Math.sqrt(Math.pow(this.x,2) + Math.pow(this.y,2))
    }
}

console.log(new Vec(1,2).plus(new Vec(2,3))) //Vec(x:3, y:5)
console.log(new Vec(1, 2).minus(new Vec(2, 3))) // → Vec{x: -1, y: -1}
console.log(new Vec(3, 4).length) // → 5



// Ch 6.2 Exercise Groups
/*
Create a class Groups that has methods named add, delete, and has. constructor creates an empty group
Method adds will add a value to the group if it isnt aalready there. Method delete removes from group.
Method has returns a boolean value indicating whether argument is in group. 
Method from will be static and iterate objects and creates a group that contains all values
*/

class Group{
    constructor(){
        this.group = []
    }

    add(item){
        if(!this.group.includes(item)){
            this.group.push(item)
        }
    }

    delete(item){
        let index = this.group.indexOf(item)
        if (index >= 0){
            this.group.splice(index, 1)
        }

        // Using filter isntead 
        // return this.group.filter(i => i !== item)
    }

    has(item){
        return this.group.includes(item)
    }

    static from(items){
        let grp = new Group()
        for(let item of items){
            grp.add(item)
        }
        return grp
    }
}

let group = Group.from([10,20,30,40,50])
console.log(group.has(10))
group.add(3)
group.delete(10)
console.log(group.has(10))
console.log(group)


/* Non Static Version of from, 
    from(items){
        for(let item of items){
            this.add(item)
        }
    }
    
let group = new Group();
group.from([12, 8 ,32, 10, 20, 3])
*/






/* Ch: 6.3 Exercise Iterable groups
Make the group class iterable, avoid using Symbol.iterator on the array

*/


class GroupIterator{
    constructor(obj){
        this.count = 0,
        this.group = obj.group
    }
    
    next(){
        if (this.count == this.group.length){
            return {done: true}
        }

        let value = this.group[this.count]
        this.count ++

        return {value, done:false}
    }
}

// Could also add this into the Group class as following below in the comments:
// [Symbol.iterator](){return new GroupIterator(this}
Group.prototype[Symbol.iterator] = function(){
    return new GroupIterator(this)
}

for(let value of Group.from(["a", "b", "c"])){
    console.log(value)
}






/* Ch 6.4 Exercise Borrowing a method
Earlier in the chapter, I mentioned that an object’s hasOwnProperty can be used as a more robust alternative to the in 
operator when you want to ignore the prototype’s properties. But what if your map needs to include the word "hasOwnProperty"? 
You won’t be able to call that method anymore because the object’s own property hides the method value.

Can you think of a way to call hasOwnProperty on an object that has its own property by that name?
*/


let map = {one: true, two: true, hasOwnProperty: true};

// Fix this call
// console.log(map.hasOwnProperty("one")); // → true

console.log(hasOwnProperty.call(map,"one"))
