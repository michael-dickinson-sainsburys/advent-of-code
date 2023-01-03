import fs from 'fs'

class HeightMap {
    constructor(lines) {
        this.charMap = lines.map(line => line.split(''))
        this.width = this.charMap[0].length
        this.height = this.charMap.length
        this.numOfVertices = this.width * this.height
        this.startCoords = this.findFirstCoordinatesWithValue('S')
        this.startNodeId = this.getNodeId(this.startCoords[0], this.startCoords[1])
        this.replaceNodeInMap('S', 'a')
        this.endCoords = this.findFirstCoordinatesWithValue('E')
        this.endNodeId = this.getNodeId(this.endCoords[0], this.endCoords[1])
        this.replaceNodeInMap('E', 'z')
        this.numberMap = this.convertToCharsToInts()
        this.generateEdges()
        this.breadthFirstSearch(this.startNodeId, this.endNodeId)
    }

    addEdge(sourceNodeId, neighbourNodeId) {
        this.edges[sourceNodeId].push(neighbourNodeId)
    }

    breadthFirstSearch(startNodeId, destinationNodeId) {
        this.predecessors = new Array(this.numOfVertices).fill(-1)
        this.distances = new Array(this.numOfVertices).fill(Infinity)
        this.visited = new Array(this.numOfVertices).fill(false)
        this.connected = false
        let queue = new Array()
        this.visited[startNodeId] = true
        this.distances[startNodeId] = 0
        queue.push(startNodeId)
        while (queue.length > 0) {
            const nodeId = queue.shift()
            for (let i = 0; i < this.edges[nodeId].length; i++) {
                const neighbourNodeId = this.edges[nodeId][i]
                if (this.visited[neighbourNodeId] === false) {
                    this.visited[neighbourNodeId] = true
                    this.distances[neighbourNodeId] = this.distances[nodeId] + 1
                    this.predecessors[neighbourNodeId] = nodeId
                    queue.push(neighbourNodeId)
                    if (neighbourNodeId === destinationNodeId) {
                        this.connected = true
                        return
                    }
                }
            }
        }
    }

    convertToCharsToInts() {
        return this.charMap.map(row => row.map(char => char.charCodeAt(0)))
    }

    findFirstCoordinatesWithValue(indicator) {
        for (let i = 0; i < this.height; i++) {
            const index = this.charMap[i].findIndex(element => element === indicator)
            if (index !== -1) {
                return [index, i]
            }
        }
    }

    generateEdges() {
        this.edges = new Array(this.numOfVertices).fill(0).map(() => new Array())
        for (let [y, row] of this.numberMap.entries()) {
            for (let [x, vertexValue] of row.entries()) {
                const currentNodeId = this.getNodeId(x, y)
                if (x > 0 && this.numberMap[y][x - 1] - vertexValue <= 1) this.addEdge(currentNodeId, this.getNodeId(x - 1, y))
                if (x < (this.width - 1) && this.numberMap[y][x + 1] - vertexValue <= 1) this.addEdge(currentNodeId, this.getNodeId(x + 1, y))
                if (y > 0 && this.numberMap[y - 1][x] - vertexValue <= 1) this.addEdge(currentNodeId, this.getNodeId(x, y - 1))
                if (y < (this.height - 1) && this.numberMap[y + 1][x] - vertexValue <= 1) this.addEdge(currentNodeId, this.getNodeId(x, y + 1))
            }
        }
    }

    getNodeId(x, y) {
        return (y * this.width) + x
    }

    getShortestPath() {
        if (this.connected === false) return []
        let path = new Array()
        let crawl = this.endNodeId
        path.push(crawl)
        while (this.predecessors[crawl] !== -1) {
            path.push(this.predecessors[crawl])
            crawl = this.predecessors[crawl]
        }
        return path.length - 1
    }

    replaceNodeInMap(pattern, replacement) {
        this.charMap = this.charMap.map(row => row.map(element => element === pattern ? replacement : element))
    }

    findAllPotentialStartNodes(identifier) {
        this.allStartNodes = new Array()
        for (let y = 0; y < this.charMap.length; y++) {
            for (let x = 0; x < this.charMap[0].length; x++) {
                if (this.charMap[y][x] === identifier) this.allStartNodes.push(this.getNodeId(x, y))
            }
        }
    }
}

const lines = fs.readFileSync('puzzle.txt').toString().split('\n')
const heightMap = new HeightMap(lines)
console.log(`Part one: ${heightMap.getShortestPath()}`)

heightMap.findAllPotentialStartNodes('a')
let shortestPaths = new Array()
let path = new Array()
for (const startNode of heightMap.allStartNodes) {
    heightMap.breadthFirstSearch(startNode, heightMap.endNodeId)
    path = heightMap.getShortestPath()
    if (path.length !== 0) shortestPaths.push(path)
}
console.log(`Part two: ${Math.min(...shortestPaths)}`)