const R = 200;
const D = 10;
const NUM_YEARS = 80;
const YEAR_LENGTH = 365.2422;

function polar_to_cartesian(r, theta, center=[1100, 1100]) {
  const x = center[0] + r * Math.cos(theta + Math.PI / 2);
  const y = center[1] - r * Math.sin(theta + Math.PI / 2);
  return [x, y];
}

function getMonthColor(month, dayOfWeek) {
  const seasons = ["#007FFF", "#00FFFF", "#00FF00", "#7FFF00", "#FFFF00", "#FF7F7F", "#FF0FBF", "#FF0000", "#BFBF00", "#FF3F00", "#7F1F00", "#FFFFFF"];
  let color = seasons[month];
  return dayOfWeek > 4 ? lightenColor(color, 50) : color;
}

function lightenColor(color, percent) {
  var num = parseInt(color.replace("#",""), 16);
  var amt = Math.round(2.55 * percent);
  var R = (num >> 16) + amt;
  var B = (num >> 8 & 0x00FF) + amt;
  var G = (num & 0x0000FF) + amt;
  return "#" + (0x1000000 + (R<255?R<1?0:R:255)*0x10000 + (B<255?B<1?0:B:255)*0x100 + (G<255?G<1?0:G:255)).toString(16).slice(1);
}

function getPolygons() {
  const startDay = new Date(1976, 11, 21);
  const polygons = [];
  const allDates = [];
  for (let day = 0; day < Math.round(YEAR_LENGTH * NUM_YEARS); day++) {
    const today = new Date(startDay.getTime() + day * 24 * 60 * 60 * 1000);
    const thetaOld = 2 * Math.PI * (day-1) / YEAR_LENGTH;
    const theta = 2 * Math.PI * day / YEAR_LENGTH;
    const r1Old = R + D * thetaOld / (2 * Math.PI);
    const r2Old = R + D + D * thetaOld / (2 * Math.PI);
    const r1 = R + D * theta / (2 * Math.PI);
    const r2 = R + D + D * theta / (2 * Math.PI);
    const [x1, y1] = polar_to_cartesian(r1Old, thetaOld);
    const [x2, y2] = polar_to_cartesian(r2Old, thetaOld);
    const [x3, y3] = polar_to_cartesian(r1, theta);
    const [x4, y4] = polar_to_cartesian(r2, theta);
    const polygon = new Path2D();
    polygon.moveTo(x1, y1);
    polygon.lineTo(x2, y2);
    polygon.lineTo(x4, y4);
    polygon.lineTo(x3, y3);
    polygon.closePath();
    // Fill the polygon with a color
    const color = getMonthColor(today.getMonth(), today.getDay());
    polygons.push([polygon, today, color]);
    allDates.push(today);
  }
  return [polygons, allDates];
}

let tooltip = null;

function showTooltip(date, index) {
  if (!tooltip) {
    tooltip = document.createElement('div');
    tooltip.style.position = 'fixed';
    tooltip.style.padding = '10px';
    tooltip.style.background = 'white';
    tooltip.style.border = '1px solid black';
    document.body.appendChild(tooltip);
  }
  tooltip.textContent = `Date: ${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
  tooltip.style.left = `${event.clientX}px`;
  tooltip.style.top = `${event.clientY}px`;
}

window.onload = () => {
  const canvas = document.getElementById('myCanvas');
  const ctx = canvas.getContext('2d');
  const [polygons, allDates] = getPolygons();
  // Draw polygons
  polygons.forEach(([polygon, date, color]) => {
    ctx.fillStyle = color;
    ctx.fill(polygon);
    // Draw a black border around the polygon
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'black';
    ctx.stroke(polygon);
  });
  // Listen to mouse move event to display tooltip
  var showingTooltip = false;
  canvas.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    polygons.forEach(([polygon, date], i) => {
      if (ctx.isPointInPath(polygon, x, y)) {
	showTooltip(date, i);
	showingTooltip = true;
      }
    });
    if (!showingTooltip) {
      if (tooltip) {
	tooltip.remove();
      }
    }
  });
  // Hide the tooltip when the mouse leaves the canvas
  /*
  canvas.addEventListener('mouseleave', () => {
    if (tooltip) {
      tooltip.remove();
      tooltip = null;
    }
  });
  */
}
