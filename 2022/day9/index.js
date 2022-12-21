import fs from 'fs'

const moveHead = (direction, position) => {
    if (direction === 'R') position[0] += 1
    if (direction === 'L') position[0] -= 1
    if (direction === 'U') position[1] += 1
    if (direction === 'D') position[1] -= 1
    return position
}

const moveTail = (headPosition, tailPosition) => {
    if (!(Math.abs(headPosition[0] - tailPosition[0]) <= 1 && Math.abs(headPosition[1] - tailPosition[1]) <= 1)) {
        if ((headPosition[0] - tailPosition[0]) >= 1) tailPosition[0] += 1
        else if ((tailPosition[0] - headPosition[0]) >= 1) tailPosition[0] -= 1
        if ((headPosition[1] - tailPosition[1]) >= 1) tailPosition[1] += 1
        else if ((tailPosition[1] - headPosition[1]) >= 1) tailPosition[1] -= 1
    }
    return tailPosition
}
const partOne = (lines) => {
    let vistedPositionsByTail = new Set()
    let head = [0, 0]
    let tail = [0, 0]
    vistedPositionsByTail.add(tail.toString())
    for (const line of lines) {
        const [direction, distance] = line.split(' ')
        for (let i = 0; i < distance; i++) {
            head = moveHead(direction, head)
            tail = moveTail(head, tail)
            vistedPositionsByTail.add(tail.toString())
        }
    }
    return vistedPositionsByTail.size
}

const partTwo = (lines) => {
    let vistedPositionsByTail = new Set()
    let head = [0, 0]
    let tails = new Array(9).fill(0).map(() => new Array(2).fill(0))
    let previousKnot
    vistedPositionsByTail.add([0, 0].toString())
    for (const line of lines) {
        const [direction, distance] = line.split(' ')
        for (let i = 0; i < distance; i++) {
            head = moveHead(direction, head)
            previousKnot = head
            for (let tail of tails) {
                tail = moveTail(previousKnot, tail)
                previousKnot = tail
            }
            vistedPositionsByTail.add(tails.slice(-1).toString())
        }
    }
    return vistedPositionsByTail.size
}

const inputFile = 'puzzle.txt'
const lines = fs.readFileSync(inputFile).toString().split('\n')

console.log(partOne(lines))
console.log(partTwo(lines))
