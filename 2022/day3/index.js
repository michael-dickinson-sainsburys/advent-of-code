import fs from 'fs';

const items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

const splitContentsInHalf = (contents) => {
    const length = contents.length
    return [contents.slice(0, length / 2).split(''), contents.slice(length / 2, length)]
}

const findDuplicatedItems = (items) => {
    const duplicates = items[0].filter(item => items[1].includes(item))
    return [... new Set(duplicates)];
}

const convertToNumber = (letter) => {
    return items.indexOf(letter) + 1
}

const inputFile = 'test.txt'
// const inputFile = 'puzzle.txt'
const data = fs.readFileSync(inputFile).toString()
const wronglyPackedItems = data.split('\n').map(rucksack => findDuplicatedItems(splitContentsInHalf(rucksack))).flat()
const scores = wronglyPackedItems.map(letter => convertToNumber(letter))
console.log(scores.reduce((runningTotal, value) => runningTotal + value))
