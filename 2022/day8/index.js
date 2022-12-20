import fs from 'fs'

const buildMap = (lines) => {
    return lines.map(line => line.split(''))
}

const findVisibleTrees = (treeMap) => {
    let numberOfVisibleTrees = 2 * (treeMap.length + treeMap[0].length - 2)
    let treeVisible = 0
    for (let row = 1; row < treeMap.length - 1; row++) {
        for (let column = 1; column < treeMap.length - 1; column++) {
            // console.log(`Checking tree at (${row}, ${column}), value=${map[row][column]}`)
            treeVisible = 0
            // Check trees to left of tree
            if (treeMap[row].slice(0, column).every((value) => treeMap[row][column] > value)) {
                treeVisible = 1
                // console.log(`Tree of height ${treeMap[row][column]} at (${row + 1}, ${column + 1}) is visible from the left`)
            }
            // Check trees to right of tree
            if (treeMap[row].slice(column + 1).every((value) => treeMap[row][column] > value)) {
                treeVisible = 1
                // console.log(`Tree of height ${treeMap[row][column]} at (${row + 1}, ${column + 1}) is visible from the right`)
            }
            // Check trees above the tree
            if (treeMap.map(value => value[column]).slice(0, row).every((value) => treeMap[row][column] > value)) {
                treeVisible = 1
                // console.log(`Tree of height ${treeMap[row][column]} at (${row + 1}, ${column + 1}) is visible from the top`)
            }
            // Check trees below the tree
            if (treeMap.map(value => value[column]).slice(row + 1).every((value) => treeMap[row][column] > value)) {
                treeVisible = 1
                // console.log(`Tree of height ${treeMap[row][column]} at (${row + 1}, ${column + 1}) is visible from the bottom`)
            }
            // if (!treeVisible) { console.log(`Tree of height ${treeMap[row][column]} at (${row + 1}, ${column + 1}) is not visible from the outside`) }
            numberOfVisibleTrees += treeVisible
        }
    }
    return numberOfVisibleTrees
}

const getViewingDistanceForTree = (treeHeight, treesToCheck) => {
    let viewingDistance = 0
    for (let tree of treesToCheck) {
        viewingDistance += 1
        if (tree >= treeHeight) break
    }
    return viewingDistance
}

const getScenicScore = (treeMap) => {
    let treesUp, treesLeft, treesDown, treesRight
    let maxScenicScore = 0
    for (let row = 0; row < treeMap.length; row++) {
        for (let column = 0; column < treeMap.length; column++) {
            treesUp = treesLeft = treesDown = treesRight = 0
            // Check trees above the tree
            treesUp = getViewingDistanceForTree(treeMap[row][column], treeMap.map(value => value[column]).slice(0, row).reverse())
            // Check trees left of the tree
            treesLeft = getViewingDistanceForTree(treeMap[row][column], treeMap[row].slice(0, column).reverse())
            // Check trees below the tree
            treesDown = getViewingDistanceForTree(treeMap[row][column], treeMap.map(value => value[column]).slice(row + 1))
            // Check trees right of the tree
            treesRight = getViewingDistanceForTree(treeMap[row][column], treeMap[row].slice(column + 1))
            maxScenicScore = Math.max(maxScenicScore, treesUp * treesLeft * treesDown * treesRight)
        }
    }
    return maxScenicScore
}

const inputFile = 'puzzle.txt'
const lines = fs.readFileSync(inputFile).toString().split('\n')
const map = buildMap(lines)

console.log(`Part one: ${findVisibleTrees(map)}`)
console.log(`Part two: ${getScenicScore(map)}`)