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

// const inputFile = 'test.txt'
const inputFile = 'puzzle.txt'
const data = fs.readFileSync(inputFile).toString()
const wronglyPackedItems = data.split('\n').map(rucksack => findDuplicatedItems(splitContentsInHalf(rucksack))).flat()
const scores = wronglyPackedItems.map(letter => convertToNumber(letter))
console.log(scores.reduce((runningTotal, value) => runningTotal + value))

const sortShortestFirst = (list) => {
    return list.sort((a, b) => a.length - b.length)
}

const findCommonItemInRucksacks = (rucksacks) => {
    const sortedRucksacks = sortShortestFirst(rucksacks)
    return [...new Set(sortedRucksacks[0].split('').filter(letter => sortedRucksacks[1].includes(letter) && sortedRucksacks[2].includes(letter)))]
}

const rucksacks = data.split('\n')
let badges = []
for (let i = 0; i < rucksacks.length - 2; i = i + 3) {
    badges.push(findCommonItemInRucksacks(rucksacks.slice(i, i + 3)))
}
const total = badges.flat().map(letter => convertToNumber(letter)).reduce((runningTotal, value) => runningTotal + value)
console.log(total)
