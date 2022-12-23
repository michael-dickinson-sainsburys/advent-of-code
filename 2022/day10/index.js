import fs from 'fs'

const generateRegister = (lines) => {
    let registerValue = 1
    let register = [registerValue]
    for (const line of lines) {
        register.push(registerValue)
        if (line.startsWith('addx')) {
            registerValue += parseInt(line.split(' ').slice(-1))
            register.push(registerValue)
        }
    }
    return register
}

const partOne = (register) => {
    const signalStrengths = register.map((value, index) => (index + 1) * value)
    const interestingSignalStrengths = signalStrengths.filter((_, index) => (index + 1 - 20) % 40 === 0)
    return interestingSignalStrengths.reduce((sum, value) => sum += value)
}

const partTwo = (register, displayWidth = 40, displayHeight = 6, litPixel = '#', darkPixel = '.') => {
    let display = new Array(displayHeight).fill(darkPixel).map(() => new Array(displayWidth).fill(darkPixel))
    for (let i = 0; i < register.length; i++) {
        const currentRow = Math.floor(i / displayWidth)
        const currentColumn = i % displayWidth
        if (currentColumn >= register[i] - 1 && currentColumn <= register[i] + 1) display[currentRow][currentColumn] = litPixel
    }
    return display.map(row => row.join('')).join('\n')
}

const inputFile = 'puzzle.txt'
const lines = fs.readFileSync(inputFile).toString().split('\n')
const register = generateRegister(lines)

console.log(partOne(register))
console.log(partTwo(register))