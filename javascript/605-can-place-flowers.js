
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
function canPlaceFlowers(flowerbed, n) {
    let count = 0;
    for(i = 0; i < flowerbed.length; i++) {
        if (flowerbed[i] === 0) {
            let emptyLeft = (i === 0) || (flowerbed[i - 1] === 0);
            let emptyRight = (i === flowerbed.length - 1) || (flowerbed[i + 1] === 0);
            if (emptyLeft && emptyRight) {
                flowerbed[i] = 1; // Plant a flower here
                count++;
                if (count >= n)
                    return true; // Early exit if we've planted enough flowers
            }
        }
    }
    return false;
};


let input = [1,0,0,0,1];
let toPlant = 1;
console.log(canPlaceFlowers(input, toPlant)); // true
