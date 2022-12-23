import fs from 'fs'

const move = (direction, position) => {
    if (direction === 'R') position[0] += 1
    if (direction === 'L') position[0] -= 1
    if (direction === 'U') position[1] += 1
    if (direction === 'D') position[1] -= 1
    return position
}

const tailAdjacentToHead = (headPosition, tailPosition) => {
    return (Math.abs(headPosition[0] - tailPosition[0]) <= 1 && Math.abs(headPosition[1] - tailPosition[1]) <= 1)
}

const moveTailTowardsHead = (headPosition, tailPosition) => {
    if ((headPosition[0] - tailPosition[0]) >= 1) tailPosition = move('R', tailPosition)
    if ((tailPosition[0] - headPosition[0]) >= 1) tailPosition = move('L', tailPosition)
    if ((headPosition[1] - tailPosition[1]) >= 1) tailPosition = move('U', tailPosition)
    if ((tailPosition[1] - headPosition[1]) >= 1) tailPosition = move('D', tailPosition)
    return tailPosition
}


const moveTail = (headPosition, tailPosition) => {
    if (!tailAdjacentToHead(headPosition, tailPosition)) {
        tailPosition = moveTailTowardsHead(headPosition, tailPosition)
    }
    return tailPosition
}

const trackKnots = (lines, knotsToTrack) => {
    let vistedPositionsByTail = new Set()
    let head = [0, 0]
    let tails = new Array(knotsToTrack).fill(0).map(() => new Array(2).fill(0))
    let previousKnot
    vistedPositionsByTail.add([0, 0].toString())
    for (const line of lines) {
        const [direction, distance] = line.split(' ')
        for (let i = 0; i < distance; i++) {
            head = move(direction, head)
            previousKnot = head
            for (let tail of tails) {
                tail = moveTail(previousKnot, tail)
                previousKnot = tail
            }
            vistedPositionsByTail.add(tails.slice(-1).toString())
        }
    }
    return vistedPositionsByTail
}

const inputFile = 'puzzle.txt'
const lines = fs.readFileSync(inputFile).toString().split('\n')

const partOne = trackKnots(lines, 1)
console.log(partOne.size)

const partTwo = trackKnots(lines, 9)
console.log(partTwo.size)
