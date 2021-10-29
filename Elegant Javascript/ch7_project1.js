/* Ch7 Robot
Write a new class PGroup like Group in ch6, which stores a set of values. Has methods add, delete, and has. 
add method returns a new PGroup instance with new item leaving the old one unchanged. 
delete method creates a new instance without the item.
Use an empty instance PGroup.empty as a starting balue. 
*/


// https://github.com/SuyashD95/eloquent-js-solutions/blob/master/Chapter%207%20-%20Project%20-%20A%20Robot/persistent_group.js

class PGroup{
    constructor(pg = new Set()){
        this.group = pg
    }

    add(item){
        return new PGroup(this.group.concat(item))
    }

    delete(item){
        return new PGroup(this.group.filter(grp => grp !== item))
    }

    has(item){
        return this.group.includes(item)
    }
}


PGroup.empty = new PGroup([])
let a = PGroup.empty.add("a")
let ab = a.add("b")
let b = ab.delete("a")

console.log(a,ab,b)
console.log(b.has("b"))  //true
console.log(a.has("b"))  //false
console.log(b.has("a"))  //false
