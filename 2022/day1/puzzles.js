import fs from 'fs';

const find_most_calories = (input) => {
    const elfInventory = input.split("\n\n");
    const maxCalories = elfInventory.reduce((acc, inventory) => {
        let calories = inventory.split("\n").reduce((partialSum, value) => partialSum + parseInt(value), 0);
        if (calories > acc.calories) {
            acc.calories = calories;
            acc.inventory = inventory;
        }
        return acc;
    }, {calories: 0});
    return {calories: maxCalories.calories, elf: elfInventory.indexOf(maxCalories.inventory) + 1}
}

const find_elf_positions_and_calories = (input) => {
    const elfIventory = input.split("\n\n")
    return elfIventory.map((inventory, index) => {
        return inventory.split("\n").reduce((partialSum, value) => partialSum + parseInt(value), 0)
    })
}

const puzzleInput = fs.readFileSync('puzzle_input.txt').toString()
const maxCalories = find_most_calories(puzzleInput)
console.log(`Elf ${maxCalories.elf} is carrying ${maxCalories.calories} calories.`)
const thing = find_elf_positions_and_calories(puzzleInput).sort((a, b) => b - a)
console.dir(thing[0] + thing[1] + thing[2])