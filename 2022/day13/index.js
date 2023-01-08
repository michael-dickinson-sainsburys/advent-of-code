import fs from 'fs'

const arrayify = (x) => { return typeof x === 'object' ? x : [x] }

const comparePairs = (left, right) => {
    if (typeof left === 'number' && typeof right === 'number') {
        // console.log(`Comparing ${left} to ${right}`)
        if (left < right) return 1
        if (left > right) return -1
        return 0
    }
    if (typeof left === 'object' && typeof right === 'object') {
        for (let i = 0; i < Math.min(left.length, right.length); i++) {
            const inOrder = comparePairs(left[i], right[i])
            // console.log({ inOrder })
            if (inOrder !== 0) return inOrder
        }
        if (left.length === right.length) return 0
        return left.length < right.length ? 1 : -1
    }
    if (typeof left === 'number' || typeof right === 'number') {
        return comparePairs(arrayify(left), arrayify(right))
    }
    console.log('You missed something :(')
}

const inCorrectOrder = (left, right) => {
    // console.log(JSON.stringify(left))
    // console.log(JSON.stringify(right))
    const correct = comparePairs(left, right)
    // console.log(correct)
    if (correct === 0) console.log(`Something went very wrong here...\n${JSON.stringify(left)}\n${JSON.stringify(right)}`)
    return correct
}

const packetPairs = fs.readFileSync('puzzle.txt')
    .toString().split('\n\n')
    .map(pair => pair.split('\n').map(packet => JSON.parse(packet)))
console.log(packetPairs.reduce((sum, packetPair, index) => {
    return inCorrectOrder(...packetPair) === 1 ? sum + index + 1 : sum
}, 0))

let packets = packetPairs.flat(1)
const dividers = [[[2]], [[6]]]
dividers.map(divider => packets.push(divider))
packets.sort((a, b) => inCorrectOrder(b, a))
console.log(dividers.reduce((sum, divider) => { return sum * (packets.findIndex(x => x === divider) + 1) }, 1))
