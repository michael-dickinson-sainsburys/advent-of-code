import fs from 'fs'

const findMarker = (datastream, markerLength) => {
    for (let i = 0; i + markerLength <= datastream.length; i++) {
        if ([...new Set(datastream.slice(i, i + markerLength))].length === markerLength) {
            return i + markerLength
        }
    }
}

const inputFile = 'puzzle.txt'
const input = fs.readFileSync(inputFile).toString()
const lines = input.split('\n')

const startOfPacketMarkerLength = 4
lines.map(line => console.log(findMarker(line, startOfPacketMarkerLength)))

const startOfMessageMarkerLength = 14
lines.map(line => console.log(findMarker(line, startOfMessageMarkerLength)))
