import fs from 'fs'

const parseInputLines = (lines) => {
    return {
        diagram: lines.filter(line => line.includes('[')),
        columns: lines.filter(line => line.startsWith(' 1')),
        instructions: lines.filter(line => line.startsWith('move')),
    }
}

const getNumberOfStacks = (columns) => {
    return Math.max(...columns[0].replace(/ +/g, ' ').split(' '))
}

const createEmptyStacks = (numberOfStacks) => {
    return Array.from(Array(numberOfStacks), () => Array())
}

const parseDiagram = (diagramRows, numberOfStacks) => {
    const stacks = createEmptyStacks(numberOfStacks)
    diagramRows.map(row => {
        for (let i = 0; i * 4 + 1 < row.length; i++) {
            stacks[i].unshift(row[i * 4 + 1])
        }
    })
    return stacks.map(stack => stack.filter(box => box !== ' '))
}

const parseInstructions = (rawInstructions) => {
    const moves = rawInstructions.map(instruction => instruction.split(/move ([0-9]+) from ([0-9]+) to ([0-9]+)/))
    return moves.map(move => {
        return {
            quantity: parseInt(move[1]),
            from: parseInt(move[2]),
            to: parseInt(move[3])
        }
    })
}

const moveCrate = (stacks, from, to) => {
    return stacks[to - 1].push(stacks[from - 1].pop())
}

const moveCrates = (stacks, quantity, from, to) => {
    const cratesToMove = stacks[from].splice(stacks[from].length - quantity, quantity)
    stacks[to].push(cratesToMove)
    stacks[to] = stacks[to].flat()
    return stacks
}

const inputFile = 'puzzle.txt'
const input = fs.readFileSync(inputFile).toString()
const lines = input.split('\n')
const { diagram, columns, instructions } = parseInputLines(lines)
// console.log(instructions)

const numberOfColumns = getNumberOfStacks(columns)
const stacks = parseDiagram(diagram, numberOfColumns)

const moves = parseInstructions(instructions)
for (let move of moves) {
    for (let i = 1; i <= move.quantity; i++) {
        moveCrate(stacks, move.from, move.to)
    }
}

// const answer = stacks.map(stack => stack[stack.length - 1])
const answer = stacks.map(stack => stack.slice(-1))
console.log(answer.join(''))

let stacks2 = parseDiagram(diagram, numberOfColumns)
console.log(stacks2)
for (let move of moves) {
    stacks2 = moveCrates(stacks2, move.quantity, move.from - 1, move.to - 1)
}
console.log(stacks2)
const answer2 = stacks2.map(stack => stack.slice(-1))
console.log(answer2.join(''))
