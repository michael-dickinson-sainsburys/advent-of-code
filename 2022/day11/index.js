import fs from "fs";

class Monkey {
    constructor(text, worryDivisor = 1) {
        const lines = text.split('\n')
        this.startingItems = lines[1].split(': ')[1].split(', ').map(item => parseInt(item))
        this.operation = lines[2].split('new = ')[1]
        this.divisibleBy = parseInt(lines[3].split(' ').at(-1))
        this.true = parseInt(lines[4].split(' ').at(-1))
        this.false = parseInt(lines[5].split(' ').at(-1))
        this.inspections = 0
        this.worryDivisor = worryDivisor
    }

    throwAllItems(monkeys, scaleDownFactor) {
        while (this.startingItems.length > 0) {
            const item = this.startingItems.shift()
            const worryLevel = this.doOperation(item)
            const test = worryLevel % this.divisibleBy === 0
            monkeys[this[test]].catchItem(this.worryDivisor > 1 ? worryLevel : worryLevel % scaleDownFactor)
            this.inspections += 1
        }
    }

    doOperation(old) {
        return Math.floor(eval(this.operation) / this.worryDivisor)
    }

    catchItem(item) {
        this.startingItems.push(item)
    }
}

const levelOfMonkeyBusiness = (monkeys, numOfRounds) => {
    const commonMultipleOfDivisors = monkeys.map(monkey => monkey.divisibleBy).reduce((a, b) => a * b)
    let inspections
    for (let i = 1; i <= numOfRounds; i++) {
        for (let monkey of monkeys) {
            monkey.throwAllItems(monkeys, commonMultipleOfDivisors)
        }
        if (i === 1 || i === 20 || i % 1000 === 0) {
            console.log(`Inspections after round ${i}: ${monkeys.map(monkey => monkey.inspections)}`)
        }
    }
    inspections = monkeys.map(monkey => monkey.inspections).sort((a, b) => b - a)
    return inspections[0] * inspections[1]
}

const input = fs.readFileSync('puzzle.txt').toString()
const monkeysP1 = input.split('\n\n').map(description => new Monkey(description, 3))
console.log(levelOfMonkeyBusiness(monkeysP1, 20))

const monkeysP2 = input.split('\n\n').map(description => new Monkey(description))
console.log(levelOfMonkeyBusiness(monkeysP2, 10000))
