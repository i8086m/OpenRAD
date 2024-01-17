

function readInput() {
	let result = {
		headAngle: 0,
		reach: 0,
		stack: 0,
		setback: 0,
		rise: 0,
		stemLength: 0,
		stemAngle: 0,
		halfStack: 0,
	};

	result.headAngle = bikeHeadAngle.valueAsNumber;
	result.reach = bikeReach.valueAsNumber;
	result.stack = bikeStack.valueAsNumber;
	result.setback = bikeSetback.valueAsNumber;
	result.rise = bikeRise.valueAsNumber;
	result.stemLength = bikeStemLength.valueAsNumber;
	result.stemAngle = bikeStemAngle.valueAsNumber;
	result.halfStack = bikeHalfStack.valueAsNumber;
	
	return result
}


function getRAD(bike) {
	let result = {
		RAD: 0,
		RAAD: 0,
		eReach: 0,
		eStack: 0,
	};
	
	inverseStemAngle = 90 - bike.stemAngle
	inverseHeadAngle = 90 - bike.headAngle
	inverseTotalAngle = inverseHeadAngle + bike.stemAngle


	headAngleSin = Math.sin(inverseHeadAngle * Math.PI / 180)
	headAngleCos = Math.cos(inverseHeadAngle * Math.PI / 180)

	totalAngleSin = Math.sin(inverseTotalAngle * Math.PI / 180)
	totalAngleCos = Math.cos(inverseTotalAngle * Math.PI / 180)


	stemFrameOffset = -headAngleSin * bike.halfStack
	stemAngleOffset = totalAngleCos * bike.stemLength


	effectiveBarHeightSmallTriangle = headAngleCos * bike.halfStack
	effectiveBarHeightBigTriangle = totalAngleSin * bike.stemLength
	
	effectiveBarHeight = effectiveBarHeightSmallTriangle + effectiveBarHeightBigTriangle + bike.rise
   
	effectiveBarLength = stemFrameOffset + stemAngleOffset - bike.setback

	effectiveReach = effectiveBarLength + bike.reach
	effectiveStack = effectiveBarHeight + bike.stack

	totalRad = Math.sqrt(effectiveReach**2 + effectiveStack**2)

	totalRadAngle = Math.atan2(effectiveStack, effectiveReach) * (180 / Math.PI)


	
	result.RAD = totalRad;
	result.RAAD = totalRadAngle;
	result.eReach = effectiveReach;
	result.eStack = effectiveStack;
	
	return result

}

function getSHO(bike) {
	stemLevelAngle = (90 - bike.headAngle + bike.stemAngle) * Math.PI / 180
	stemVerticalAngle = (bike.headAngle - bike.stemAngle) * Math.PI / 180

	fullAngle = stemLevelAngle + stemVerticalAngle

	effectiveStemHeight = bike.stemLength * Math.sin(stemLevelAngle)
	effectiveStemLength = bike.stemLength * Math.sin(stemVerticalAngle)

	barHeight = effectiveStemHeight + bike.rise
	barDistance = effectiveStemLength - bike.setback

	second = Math.tan((90 - bike.headAngle) * Math.PI / 180) * barHeight

	return second + barDistance
}


function calculateTotal() {
	bike = readInput();
	
	let result = getRAD(bike);
	let sho = getSHO(bike);

	bikeRAD.value = result.RAD.toFixed(1);
	bikeRAAD.value = result.RAAD.toFixed(1);
	bikeSHO.value = sho.toFixed(1);
	bikeEffReach.value = result.eReach.toFixed(1);
	bikeEffStack.value = result.eStack.toFixed(1);

}

$(function() {
$(".qty").on("change keyup", calculateTotal)
})
