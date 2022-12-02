import fs from 'fs';

const scores = {X: 1, Y: 2, Z: 3}
const winningCombos = ['AY', 'BZ', 'CX']
const drawCombos = ['AX', 'BY', 'CZ']
const win = 6
const draw = 3
const lose = 0
const outcomes = {A: {win: 'Y', draw: 'X', lose: 'Z'}, B: {win: 'Z', draw: 'Y', lose: 'X'}, C: {win: 'X', draw: 'Z', lose: 'Y'}}

const scoreRound = (shapes) => {
    const opponent = shapes[0]
    const you = shapes[1]
    if (drawCombos.includes(`${opponent}${you}`)) {
        return draw + scores[you]
    }
    if (winningCombos.includes(`${opponent}${you}`)) {
        return win + scores[you]
    }
    return lose + scores[you]
}

const game = (rounds) => {
    const scores = rounds.map(round => scoreRound(round.split(" ")))
    return scores.reduce((runningTotal, value) => runningTotal + value, 0)
}

const puzzleInput = fs.readFileSync('puzzle_input.txt').toString()
const score = game(puzzleInput.split('\n'))
console.log(`Puzzle 1: ${score}`)

const scoreRound2 = (symbols) => {
    const opponent = symbols[0]
    const outcome = symbols[1]
    if (outcome === 'X') {
        return lose + scores[outcomes[opponent].lose]
    }
    if (outcome === 'Y') {
        return draw + scores[outcomes[opponent].draw]
    }
    return win + scores[outcomes[opponent].win]
}

const game2 = (rounds) => {
    const scores = rounds.map(round => scoreRound2(round.split(" ")))
    return scores.reduce((runningTotal, value) => runningTotal + value, 0)
}

const score2 = game2(puzzleInput.split('\n'))
console.log(`Puzzle 2: ${score2}`)