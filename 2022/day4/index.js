import fs from 'fs'

const getSectionAssignments = (assignments) => {
    return assignments.split(',')
}

const getStartAndEndSections = (section) => {
    return section.split('-')
}

const startOverlaps = (a, b) => {
    return parseInt(a) <= parseInt(b)
}

const endOverlaps = (a, b) => {
    return parseInt(a) >= parseInt(b)
}

const assignmentCoveredByOtherAssignment = (assignments) => {
    if (startOverlaps(assignments[0][0], assignments[1][0]) && endOverlaps(assignments[0][1], assignments[1][1])) {
        return true
    }
    if (startOverlaps(assignments[1][0], assignments[0][0]) && endOverlaps(assignments[1][1], assignments[0][1])) {
        return true
    }
    return false
}

const assignmentsOverlap = (assignments) => {
    if (startOverlaps(assignments[0][0], assignments[1][0]) && endOverlaps(assignments[0][1], assignments[1][0])) {
        return true
    }
    if (startOverlaps(assignments[1][0], assignments[0][0]) && endOverlaps(assignments[1][1], assignments[0][0])) {
        return true
    }
    return false
}

// const inputFile = 'test.txt'
const inputFile = 'puzzle.txt'
const input = fs.readFileSync(inputFile).toString().split('\n')
const sectionAssignments = input.map(assignmentPair => getSectionAssignments(assignmentPair).map(section => getStartAndEndSections(section)))
console.log(sectionAssignments.filter(assignments => assignmentCoveredByOtherAssignment(assignments)).length)

console.log(sectionAssignments.filter(assignments => assignmentsOverlap(assignments)).length)

