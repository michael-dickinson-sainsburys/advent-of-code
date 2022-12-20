import { captureRejectionSymbol } from 'events';
import fs from 'fs';

const calculateDirectorySizes = (lines) => {
    let path = []
    let sizes = {}
    for (const line of lines) {
        if (line.startsWith('$ cd ')) {
            let directoryName = line.slice(5)
            if (directoryName === '/') {
                path = []
                continue
            }
            if (directoryName === '..') {
                path.pop()
                continue
            }
            path.push(directoryName)
            continue
        }
        if (!line.startsWith('$') && !line.startsWith('dir')) {
            for (let i = 0; i < path.length + 1; i++) {
                let pathName = `/${path.slice(0, i).join("/")}`
                if (!(pathName in sizes)) {
                    sizes[pathName] = 0
                }
                sizes[pathName] += parseInt(line.split(' ')[0])
            }
        }
    }
    return sizes
}

const partTwo = (sizes, maxSpace = 70000000, spaceRequiredForUpdate = 30000000) => {
    const freeSpace = maxSpace - sizes['/']
    const spaceNeededToBeFreedUp = spaceRequiredForUpdate - freeSpace
    let deletionCandidates = Object.entries(sizes).filter((directory) => directory[1] > spaceNeededToBeFreedUp)
    deletionCandidates.sort((a, b) => a[1] - b[1])
    return deletionCandidates[0]
}

const inputFile = 'puzzle.txt'
const lines = fs.readFileSync(inputFile).toString().split('\n')
const sizes = calculateDirectorySizes(lines)
const partOne = Object.values(sizes).reduce((sum, size) => {
    if (size <= 100000) { return sum + size }
    else { return sum }
}, 0)
console.log(`Part one: ${partOne}`)
console.log(`Part two: ${partTwo(sizes)[1]}`)
