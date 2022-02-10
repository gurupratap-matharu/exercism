// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  var timeInMinutes;

  switch (name) {
    case "Pure Strawberry Joy":
      timeInMinutes = 0.5;
      break;

    case "Energizer":
      timeInMinutes = 1.5;
      break;

    case "Green Garden":
      timeInMinutes = 1.5;
      break;

    case "Tropical Island":
      timeInMinutes = 3;
      break;

    case "All or Nothing":
      timeInMinutes = 5;
      break;

    default:
      timeInMinutes = 2.5;
  }

  return timeInMinutes;
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {}
/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  const juiceTimeMap = new Map();
  juiceTimeMap.set("Pure Strawberry Joy", 0.5);
  juiceTimeMap.set("Energizer", 1.5);
  juiceTimeMap.set("Green Garden", 1.5);
  juiceTimeMap.set("Tropical Island", 3);
  juiceTimeMap.set("All or Nothing", 5);

  while (orders.length && timeLeft >= 0) {
    var order = orders.shift();
    var time = juiceTimeMap.has(order) ? juiceTimeMap.get(order) : 0;
    timeLeft -= time;
  }
  return orders;
}
